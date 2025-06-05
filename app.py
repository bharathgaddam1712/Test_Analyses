from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os
import json
import re
from src.data_processing import process_single_json, compute_accuracy_over_time
from src.ai_feedback import generate_feedback
from src.visualization import plot_subject_accuracy, plot_cumulative_accuracy_over_time
from src.pdf_generator import generate_pdf
from config import config

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        # Extract form data
        student_name = request.form['student_name']
        exam_title = request.form['exam_title']
        exam_date = request.form['exam_date']
        json_file = request.files['json_file']

        # Validate file extension
        if not json_file.filename.endswith('.json'):
            return jsonify({'error': 'File must be a JSON file'}), 400

        # Save JSON file temporarily
        json_path = os.path.join(config.OUTPUT_REPORTS_DIR, f'temp_{student_name}.json')
        json_file.save(json_path)

        # Process JSON
        test_info, syllabus, subjects, chapters, llm_context = process_single_json(json_path, student_name)
        test_info['syllabus'] = f"<h1>{exam_title} Syllabus - {exam_date} </h1>"

        # Generate feedback
        feedback = generate_feedback(student_name, test_info, subjects, chapters, llm_context)

        # Generate charts
        subject_accuracy_path = plot_subject_accuracy(subjects, f'subject_accuracy_{student_name}.png')
        subjects_data = compute_accuracy_over_time(json_path)
        subject_chart_paths = plot_cumulative_accuracy_over_time(subjects_data, f'accuracy_over_time_{student_name}')
        chart_paths = [subject_accuracy_path] + subject_chart_paths
        base_url = 'http://localhost:5000'
        chart_dict = {
            'subject_accuracy': f'{base_url}/{subject_accuracy_path}',
            'physics': f'{base_url}/{next((p for p in subject_chart_paths if "physics" in p.lower()), "")}',
            'chemistry': f'{base_url}/{next((p for p in subject_chart_paths if "chemistry" in p.lower()), "")}',
            'maths': f'{base_url}/{next((p for p in subject_chart_paths if "maths" in p.lower()), "")}'
        }

        # Generate subject and chapter comments
        subject_comments = []
        for subject, stats in subjects.items():
            accuracy = stats.get('accuracy', 0)
            avg_time = stats.get('avg_time_per_question', 0)
            if accuracy < 50:
                comment = f"<b>{subject}:</b> Your performance needs improvement. Focus on core concepts and practice more questions."
            elif avg_time > 100:
                comment = f"<b>{subject}:</b> High time per question ({avg_time} sec) indicates potential time management issues."
            else:
                comment = f"<b>{subject}:</b> Good performance with {accuracy}% accuracy. Keep practicing to maintain or improve."
            subject_comments.append(comment)
        subject_comments = "<br/>".join(subject_comments)

        chapter_comments = []
        for chapter, stats in chapters.items():
            accuracy = stats.get('accuracy', 0)
            avg_time = stats.get('avg_time', 0)
            if accuracy < 50:
                chapter_comments.append(f"<b>{chapter} ({stats.get('subject', 'N/A')}):</b> This is a clear area for improvement.")
            elif avg_time > 100:
                chapter_comments.append(f"<b>{chapter} ({stats.get('subject', 'N/A')}):</b> Significantly longer average time per question ({avg_time} sec).")
        chapter_comments = "<br/>".join(chapter_comments) if chapter_comments else ""

        # Generate insights
        insights = f"Generally, your accuracy is quite good ({test_info.get('accuracy', 'N/A')}%) overall. However, there are some areas to note:<br/>"
        for subject, stats in subjects.items():
            insights += f"<b>{subject}:</b> You spent an average of {stats.get('avg_time_per_question', 'N/A')} seconds per question with {stats.get('accuracy', 'N/A')}% accuracy. "
            if stats.get('avg_time_per_question', 0) > 100:
                insights += "Consider improving time management for this subject.<br/>"
            elif stats.get('accuracy', 0) < 50:
                insights += "Focus on strengthening core concepts to improve accuracy.<br/>"
            else:
                insights += "Good performance, keep practicing to maintain or improve.<br/>"

        # Generate PDF (server-side, for CLI or fallback)
        pdf_path = generate_pdf(student_name, test_info, subjects, chapters, feedback, chart_paths, f'Analysis_{student_name}.pdf')

        # Prepare response
        response_data = {
            'student_name': student_name,
            'exam_title': exam_title,
            'exam_date': exam_date,
            'test_info': test_info,
            'subjects': subjects,
            'chapters': chapters,
            'suggestions': feedback.get('suggestions', []),
            'closing': feedback.get('closing', ''),
            'subject_comments': subject_comments,
            'chapter_comments': chapter_comments,
            'insights': insights,
            'charts': chart_dict,
            'pdf_path': pdf_path
        }

        # Clean up temporary JSON file
        if os.path.exists(json_path):
            os.remove(json_path)

        return jsonify(response_data)
    except Exception as e:
        if os.path.exists(json_path):
            os.remove(json_path)
        return jsonify({'error': str(e)}), 500

@app.route('/api/download', methods=['POST'])
def download():
    try:
        data = request.json
        pdf_path = data['pdf_path']
        if not os.path.exists(pdf_path):
            return jsonify({'error': 'PDF not found'}), 404
        return send_file(pdf_path, as_attachment=True, download_name=os.path.basename(pdf_path))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/output/charts/<path:filename>')
def serve_chart(filename):
    return send_from_directory(config.OUTPUT_CHARTS_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)


