# # from reportlab.lib import colors
# # from reportlab.lib.pagesizes import letter
# # from reportlab.platypus import (
# #     SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
# # )
# # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # from reportlab.lib.units import inch
# # import os
# # from config import config


# # def generate_pdf(student_name, test_info, subjects, chapters, feedback, chart_paths, output_path):
# #     pdf_path = os.path.join(config.OUTPUT_REPORTS_DIR, output_path)
# #     doc = SimpleDocTemplate(pdf_path, pagesize=letter)
# #     styles = getSampleStyleSheet()
# #     story = []

# #     # Custom styles
# #     title_style = styles['Heading1']
# #     subtitle_style = styles['Heading2']
# #     body_style = ParagraphStyle(name='Body', fontName='Helvetica', fontSize=11, leading=16)
# #     bold_style = ParagraphStyle(name='Bold', fontName='Helvetica-Bold', fontSize=12)
# #     section_number = 1

# #     logo_path = os.path.join("output", "logo.png")

# #     # Cover Page
# #     if os.path.exists(logo_path):
# #         story.append(Image(logo_path, width=2.5 * inch, height=2.5 * inch))
# #         story.append(Spacer(1, 0.3 * inch))
    
# #     story.append(Paragraph("Academic Performance Feedback Report", title_style))
# #     story.append(Spacer(1, 0.1 * inch))
# #     story.append(Paragraph(f"Student Name: <b>{student_name}</b>", bold_style))
# #     story.append(Paragraph("Examination: QPT 1", body_style))
# #     story.append(Paragraph("Date: 11 May 2025", body_style))
# #     story.append(PageBreak())

# #     # Section 1: Personalized Intro
# #     story.append(Paragraph(f"{section_number}. Personalized Intro", subtitle_style))
# #     section_number += 1

# #     summary = f"""
# #     <b>Total Time:</b> {test_info['totalTime']} min<br/>
# #     <b>Questions:</b> {test_info['totalQuestions']}<br/>
# #     <b>Total Marks:</b> {test_info['totalMarks']}<br/>
# #     <b>Time Taken:</b> {test_info['totalTimeTaken']} sec<br/>
# #     <b>Marks Scored:</b> {test_info['totalMarkScored']}<br/>
# #     <b>Attempted:</b> {test_info['totalAttempted']}<br/>
# #     <b>Correct:</b> {test_info['totalCorrect']}<br/>
# #     <b>Accuracy:</b> {test_info['accuracy']}%
# #     """
# #     story.append(Paragraph(summary, body_style))
# #     story.append(Spacer(1, 0.3 * inch))

# #     # Insert overall subject-wise accuracy chart here
# #     for chart_path in chart_paths:
# #         if "subject_accuracy" in chart_path and os.path.exists(chart_path):
# #             story.append(Paragraph("Subject-Wise Accuracy Overview", body_style))
# #             story.append(Image(chart_path, width=6 * inch, height=4 * inch))
# #             story.append(Spacer(1, 0.2 * inch))

# #     story.append(PageBreak())

# #     # Section 2: Detailed Performance Breakdown
# #     story.append(Paragraph(f"{section_number}. Detailed Performance Breakdown", subtitle_style))
# #     section_number += 1

# #     table_data = [["Chapter (Subject)", "Attempted", "Correct", "Accuracy (%)", "Avg Time (sec)", "Difficulty"]]
# #     for chap, stats in chapters.items():
# #         difficulty_str = ', '.join([f"{k} ({v})" for k, v in stats['difficulty'].items()])
# #         table_data.append([
# #             f"{chap} ({stats['subject']})", stats['attempted'], stats['correct'],
# #             stats['accuracy'], stats['avg_time'], difficulty_str
# #         ])
# #     table = Table(table_data, hAlign='LEFT')
# #     table.setStyle(TableStyle([
# #         ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
# #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
# #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
# #         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
# #         ('FONTSIZE', (0, 0), (-1, 0), 11),
# #         ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
# #         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
# #     ]))
# #     story.append(table)
# #     story.append(Spacer(1, 0.3 * inch))

# #     story.append(PageBreak())

# #     # Section 3: Time vs. Accuracy Insights
# #     story.append(Paragraph(f"{section_number}. Time vs. Accuracy Insights", subtitle_style))
# #     section_number += 1

# #     for chart_path in chart_paths:
# #         if "accuracy_over_time" in chart_path and os.path.exists(chart_path):
# #             story.append(Paragraph("Cumulative Accuracy Over Time", body_style))
# #             story.append(Image(chart_path, width=6 * inch, height=4 * inch))
# #             story.append(Spacer(1, 0.2 * inch))

# #     story.append(PageBreak())

# #     # Section 4: Actionable Suggestions for Improvement
# #     story.append(Paragraph(f"{section_number}. Actionable Suggestions for Improvement", subtitle_style))
# #     section_number += 1

# #     feedback_sections = feedback.split('\n\n')
# #     for section in feedback_sections:
# #         story.append(Paragraph(section.strip(), body_style))
# #         story.append(Spacer(1, 0.1 * inch))

# #     # Footer Branding (optional)
# #     story.append(PageBreak())
# #     story.append(Paragraph("Powered by AI-Powered Feedback System", styles['Normal']))
# #     if os.path.exists(logo_path):
# #         story.append(Image(logo_path, width=1.5 * inch, height=1.5 * inch))

# #     doc.build(story)
# #     return pdf_path











# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import (
#     SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
# )
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch
# import os
# from config import config

# def generate_pdf(student_name, test_info, subjects, chapters, feedback, chart_paths, output_path):
#     pdf_path = os.path.join(config.OUTPUT_REPORTS_DIR, output_path)
#     doc = SimpleDocTemplate(pdf_path, pagesize=letter)
#     styles = getSampleStyleSheet()
#     story = []

#     # Custom styles
#     title_style = styles['Heading1']
#     subtitle_style = styles['Heading2']
#     body_style = ParagraphStyle(name='Body', fontName='Helvetica', fontSize=11, leading=16)
#     bold_style = ParagraphStyle(name='Bold', fontName='Helvetica-Bold', fontSize=12)
#     section_number = 1

#     logo_path = os.path.join("output", "logo.png")

#     # Cover Page
#     if os.path.exists(logo_path):
#         story.append(Image(logo_path, width=2.5 * inch, height=2.5 * inch))
#         story.append(Spacer(1, 0.3 * inch))

#     story.append(Paragraph("Academic Performance Feedback Report", title_style))
#     story.append(Spacer(1, 0.1 * inch))
#     story.append(Paragraph(f"Student Name: <b>{student_name}</b>", bold_style))
#     story.append(Paragraph("Examination: QPT 1", body_style))
#     story.append(Paragraph("Date: 11 May 2025", body_style))
#     story.append(PageBreak())

#     # Section 1: Personalized Introduction
#     story.append(Paragraph(f"{section_number}. Personalized Introduction", subtitle_style))
#     section_number += 1

#     intro_text = """
#     Hi John, great job on completing QPT 1! It's fantastic that you're actively working to improve
#     your skills. Your results show a good foundation, and with a few focused adjustments, you can
#     really unlock your potential! Let's dive into your performance to identify areas where you excel
#     and where we can make some strategic improvements
#     """
#     story.append(Paragraph(intro_text.strip(), body_style))
#     story.append(Spacer(1, 0.2 * inch))

#     summary = """
#     <b>Total Time:</b> 180 min<br/>
#     <b>Questions:</b> 75<br/>
#     <b>Total Marks:</b> 300
#     """
#     story.append(Paragraph(summary, body_style))
#     story.append(Spacer(1, 0.2 * inch))

#     # Performance Metrics Table
#     table_data = [
#         ["Metric", "Value"],
#         ["Time Taken", "4998 sec"],
#         ["Marks Scored", "133"],
#         ["Attempted", "47"],
#         ["Correct", "36"],
#         ["Accuracy", "76.6%"]
#     ]
#     table = Table(table_data, hAlign='LEFT')
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 11),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#     ]))
#     story.append(table)
#     story.append(Spacer(1, 0.3 * inch))

#     # Insert overall subject-wise accuracy chart
#     for chart_path in chart_paths:
#         if "subject_accuracy" in chart_path and os.path.exists(chart_path):
#             story.append(Paragraph("Subject-Wise Accuracy Overview", body_style))
#             story.append(Image(chart_path, width=6 * inch, height=4 * inch))
#             story.append(Spacer(1, 0.2 * inch))

#     story.append(PageBreak())

#     # Section 2: Detailed Performance Breakdown
#     story.append(Paragraph(f"{section_number}. Detailed Performance Breakdown", subtitle_style))
#     section_number += 1

#     # Overall Performance
#     story.append(Paragraph("<b>Overall:</b>", bold_style))
#     overall_table_data = [
#         ["Metric", "Value"],
#         ["Marks Scored", "133/300 (44.3%)"],
#         ["Attempted", "47/75 (62.7%)"],
#         ["Correct", "36/47 (76.6%)"],
#         ["Accuracy", "76.6%"]
#     ]
#     overall_table = Table(overall_table_data, hAlign='LEFT')
#     overall_table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 11),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#     ]))
#     story.append(overall_table)
#     story.append(Spacer(1, 0.2 * inch))
#     story.append(Paragraph("You completed the test well within the time limit of 180 minutes, which is excellent!", body_style))
#     story.append(Spacer(1, 0.2 * inch))

#     # Subject-wise Performance
#     story.append(Paragraph("<b>Subject-wise:</b>", bold_style))
#     subject_table_data = [
#         ["Subject", "Marks", "Attempted", "Correct", "Accuracy", "Avg Time/Question"],
#         ["Physics", "44/100", "16", "12", "75%", "186.5 sec"],
#         ["Chemistry", "60/100", "20", "16", "80%", "69.8 sec"],
#         ["Maths", "29/100", "11", "8", "72.73%", "56.1 sec"]
#     ]
#     subject_table = Table(subject_table_data, hAlign='LEFT')
#     subject_table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 11),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#     ]))
#     story.append(subject_table)
#     story.append(Spacer(1, 0.2 * inch))

#     # Subject-wise comments
#     subject_comments = """
#     <b>Physics:</b> This is the longest average time per question, indicating potential time management issues within Physics.<br/>
#     <b>Chemistry:</b> Excellent performance! You are doing well in Chemistry.<br/>
#     <b>Maths:</b> While the accuracy is good (72.73%), your performance in functions and sets and relations needs improvement.
#     """
#     story.append(Paragraph(subject_comments, body_style))
#     story.append(Spacer(1, 0.2 * inch))

#     # Chapter-wise Performance
#     story.append(Paragraph("<b>Chapter-wise:</b>", bold_style))
#     chapter_table_data = [
#         ["Chapter (Subject)", "Attempted", "Correct", "Accuracy", "Avg Time"],
#         ["Capacitance (Physics)", "10", "6", "60.0%", "50.0 sec"],
#         ["Electrostatics (Physics)", "15", "10", "66.67%", "59.8 sec"],
#         ["Solutions (Chemistry)", "12", "7", "58.33%", "41.2 sec"],
#         ["Electrochemistry (Chemistry)", "10", "1", "10.0%", "7.3 sec"],
#         ["Functions (Maths)", "17", "7", "41.18%", "98.5 sec"],
#         ["Sets and Relations (Maths)", "7", "5", "71.43%", "173.3 sec"]
#     ]
#     chapter_table = Table(chapter_table_data, hAlign='LEFT')
#     chapter_table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 11),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#     ]))
#     story.append(chapter_table)
#     story.append(Spacer(1, 0.2 * inch))

#     # Chapter-wise comments
#     chapter_comments = """
#     <b>Electrochemistry (Chemistry):</b> This is a clear area for improvement.<br/>
#     <b>Functions (Maths):</b> Significantly longer average time per question in Functions.
#     """
#     story.append(Paragraph(chapter_comments, body_style))
#     story.append(Spacer(1, 0.3 * inch))

#     story.append(PageBreak())

#     # Section 3: Time vs. Accuracy Insights
#     story.append(Paragraph(f"{section_number}. Time vs. Accuracy Insights", subtitle_style))
#     section_number += 1

#     insights_text = """
#     Generally, your accuracy is quite good (76.6%) overall. However, there are some concerning things to note:<br/>
#     <b>Physics:</b> You spent the most time per question in Physics (186.5 seconds) while maintaining a 75% accuracy. This suggests you may need to work on time management while answering Physics questions.<br/>
#     <b>Chemistry:</b> You were very efficient in Chemistry, achieving a high accuracy (80%) with a relatively short time per question (69.8 seconds).<br/>
#     <b>Maths:</b> While the accuracy is good (72.73%), your performance in functions and sets and relations needs improvement. This suggests that you may need to focus on the core concepts of these two topics.
#     """
#     story.append(Paragraph(insights_text.strip(), body_style))
#     story.append(Spacer(1, 0.2 * inch))

#     # Insert individual subject charts
#     for subject in ["Physics", "Chemistry", "Maths"]:
#         for chart_path in chart_paths:
#             if subject.lower() in chart_path.lower() and os.path.exists(chart_path):
#                 story.append(Paragraph(f"{subject} Performance Chart", body_style))
#                 story.append(Image(chart_path, width=6 * inch, height=4 * inch))
#                 story.append(Spacer(1, 0.2 * inch))

#     story.append(PageBreak())

#     # Section 4: Actionable Suggestions for Improvement
#     story.append(Paragraph(f"{section_number}. Actionable Suggestions for Improvement", subtitle_style))
#     section_number += 1

#     suggestions = [
#         "<b>1. Prioritize Time Management in Physics:</b><br/>"
#         "Your average time per question in Physics is significantly higher than in other subjects. To improve, try these strategies:<br/>"
#         "<b>Practice with Timed Sets:</b> Dedicate specific blocks of time to solving physics problems. Start with a generous time limit and gradually reduce it.<br/>"
#         "<b>Identify Time-Consuming Topics:</b> Review the concepts within Physics that you are struggling with to solve quickly.<br/>"
#         "<b>Strategic Skipping:</b> Learn to identify questions you can answer quickly and those that will take longer. Don't be afraid to skip a question if it's taking too much time, and come back to it later if you have time.<br/><br/>",

#         "<b>2. Focus on Core Concepts, Especially in Electrochemistry and Functions:</b><br/>"
#         "<b>Electrochemistry:</b> Your performance in Electrochemistry (10% accuracy) needs immediate attention. Review the fundamentals of the Nernst equation, Electrode potential, and Faraday's laws. Practice with a variety of problems.<br/>"
#         "<b>Functions:</b> Focus on strengthening your understanding of the core concepts of Functions.<br/><br/>",

#         "<b>3. Review and Practice Weak Areas:</b><br/>"
#         "Identify the specific concepts within each chapter where you struggled. Review the relevant theory, work through example problems, and then attempt practice questions on those areas. For example, if you struggled with “Energy stored in capacitor,” focus on those concepts."
#     ]

#     for para in suggestions:
#         story.append(Paragraph(para.strip(), body_style))
#         story.append(Spacer(1, 0.15 * inch))

#     story.append(PageBreak())

#     # Section 5: Final Encouragement
#     story.append(Paragraph(f"{section_number}. Final Encouragement", subtitle_style))
#     section_number += 1

#     encouragement = """
#     John, you're demonstrating a solid understanding, and I'm confident that by focusing on these areas, you'll see a significant improvement in your scores! Keep up the hard work, and remember that consistent effort is the key to success. Feel free to ask if you have any more questions or want to discuss these points in more detail.
#     """
#     story.append(Paragraph(encouragement.strip(), body_style))
#     story.append(Spacer(1, 0.15 * inch))

#     if os.path.exists(logo_path):
#         story.append(Image(logo_path, width=1.5 * inch, height=1.5 * inch))

#     doc.build(story)
#     return pdf_path


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
import re
from config import config

def generate_pdf(student_name, test_info, subjects, chapters, feedback, chart_paths, output_path):
    pdf_path = os.path.join(config.OUTPUT_REPORTS_DIR, output_path)
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    title_style = styles['Heading1']
    subtitle_style = styles['Heading2']
    body_style = ParagraphStyle(name='Body', fontName='Helvetica', fontSize=11, leading=16)
    bold_style = ParagraphStyle(name='Bold', fontName='Helvetica-Bold', fontSize=12)
    section_number = 1

    logo_path = os.path.join("output", "logo.png")

    # Parse test syllabus to extract exam name and date
    syllabus = test_info.get('syllabus', '')
    exam_name = "QPT 1"  # Default fallback
    exam_date = "11 May 2025"  # Default fallback
    if syllabus:
        # Extract exam name and date from <h1> tag (e.g., "<h1>QPT-1 Syllabus - 11-12-2025</h1>")
        match = re.search(r'<h1>(.*?)\s*Syllabus\s*-\s*(.*?)</h1>', syllabus)
        if match:
            exam_name = match.group(1).replace(" Syllabus", "").strip()
            exam_date = match.group(2).strip()

    # Cover Page
    if os.path.exists(logo_path):
        story.append(Image(logo_path, width=2.5 * inch, height=2.5 * inch))
        story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph("Academic Performance Feedback Report", title_style))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(f"Student Name: <b>{student_name}</b>", body_style))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(f"Examination: {exam_name}", body_style))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(f"Date: {exam_date}", body_style))
    story.append(PageBreak())

    # Section 1: Personalized Introduction
    story.append(Paragraph(f"{section_number}. Personalized Introduction", subtitle_style))
    section_number += 1
    story.append(Spacer(1, 0.3 * inch))

    intro_text = f"""
    Hi {student_name}, great job on completing {exam_name}! It's fantastic that you're actively working to improve
    your skills. Your results show a good foundation, and with a few focused adjustments, you can
    really unlock your potential! Let's dive into your performance to identify areas where you excel
    and where we can make some strategic improvements
    """
    story.append(Paragraph(intro_text.strip(), body_style))
    story.append(Spacer(1, 0.2 * inch))

    summary = f"""
    <b>Total Time:</b> {test_info.get('totalTime', 'N/A')} min<br/>
    <b>Questions:</b> {test_info.get('totalQuestions', 'N/A')}<br/>
    <b>Total Marks:</b> {test_info.get('totalMarks', 'N/A')}
    """
    story.append(Paragraph(summary, body_style))
    story.append(Spacer(1, 0.2 * inch))

    # Performance Metrics Table
    table_data = [
        ["Metric", "Value"],
        ["Time Taken", f"{test_info.get('totalTimeTaken', 'N/A')} sec"],
        ["Marks Scored", f"{test_info.get('totalMarkScored', 'N/A')}"],
        ["Attempted", f"{test_info.get('totalAttempted', 'N/A')}"],
        ["Correct", f"{test_info.get('totalCorrect', 'N/A')}"],
        ["Accuracy", f"{test_info.get('accuracy', 'N/A')}%"]
    ]
    table = Table(table_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.3 * inch))

    # Insert overall subject-wise accuracy chart
    for chart_path in chart_paths:
        if "subject_accuracy" in chart_path and os.path.exists(chart_path):
            story.append(Paragraph("Subject-Wise Accuracy Overview", body_style))
            story.append(Image(chart_path, width=6 * inch, height=4 * inch))
            story.append(Spacer(1, 0.2 * inch))

    story.append(PageBreak())

    # Section 2: Detailed Performance Breakdown
    story.append(Paragraph(f"{section_number}. Detailed Performance Breakdown", subtitle_style))
    section_number += 1
    story.append(Spacer(1, 0.3 * inch))

    # Overall Performance
    story.append(Paragraph("<b>Overall:</b>", bold_style))
    story.append(Spacer(1, 0.2 * inch))
    overall_table_data = [
        ["Metric", "Value"],
        ["Marks Scored", f"{test_info.get('totalMarkScored', 'N/A')}/{test_info.get('totalMarks', 'N/A')} ({round(test_info.get('totalMarkScored', 0)/test_info.get('totalMarks', 1)*100, 1)}%)"],
        ["Attempted", f"{test_info.get('totalAttempted', 'N/A')}/{test_info.get('totalQuestions', 'N/A')} ({round(test_info.get('totalAttempted', 0)/test_info.get('totalQuestions', 1)*100, 1)}%)"],
        ["Correct", f"{test_info.get('totalCorrect', 'N/A')}/{test_info.get('totalAttempted', 'N/A')} ({round(test_info.get('totalCorrect', 0)/test_info.get('totalAttempted', 1)*100, 1)}%)"],
        ["Accuracy", f"{test_info.get('accuracy', 'N/A')}%"]
    ]
    overall_table = Table(overall_table_data, hAlign='LEFT')
    overall_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(overall_table)
    story.append(Spacer(1, 0.2 * inch))
    time_taken_min = round(test_info.get('totalTimeTaken', 0) / 60, 1) if test_info.get('totalTimeTaken') else 'N/A'
    story.append(Paragraph(f"You completed the test well within the time limit of {test_info.get('totalTime', 'N/A')} minutes, which is excellent!", body_style))
    story.append(Spacer(1, 0.2 * inch))

    # Subject-wise Performance
    story.append(Paragraph("<b>Subject-wise:</b>", bold_style))
    story.append(Spacer(1, 0.2 * inch))
    subject_table_data = [["Subject", "Marks", "Attempted", "Correct", "Accuracy", "Avg Time/Question"]]
    for subject, stats in subjects.items():
        subject_table_data.append([
            subject,
            f"{stats.get('marks', 'N/A')}/{stats.get('total_marks', 'N/A')}",
            stats.get('attempted', 'N/A'),
            stats.get('correct', 'N/A'),
            f"{stats.get('accuracy', 'N/A')}%",
            f"{stats.get('avg_time', 'N/A')} sec"
        ])
    subject_table = Table(subject_table_data, hAlign='LEFT')
    subject_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(subject_table)
    story.append(Spacer(1, 0.2 * inch))

    # Subject-wise comments
    subject_comments = []
    for subject, stats in subjects.items():
        accuracy = stats.get('accuracy', 0)
        avg_time = stats.get('avg_time', 0)
        if accuracy < 50:
            comment = f"<b>{subject}:</b> Your performance needs improvement. Focus on core concepts and practice more questions."
        elif avg_time > 100:
            comment = f"<b>{subject}:</b> High time per question ({avg_time} sec) indicates potential time management issues."
        else:
            comment = f"<b>{subject}:</b> Good performance with {accuracy}% accuracy. Keep practicing to maintain or improve."
        subject_comments.append(comment)
    story.append(Paragraph("<br/>".join(subject_comments), body_style))
    story.append(Spacer(1, 0.2 * inch))

    # Chapter-wise Performance
    story.append(Paragraph("<b>Chapter-wise:</b>", bold_style))
    story.append(Spacer(1, 0.2 * inch))
    chapter_table_data = [["Chapter (Subject)", "Attempted", "Correct", "Accuracy", "Avg Time"]]
    for chapter, stats in chapters.items():
        chapter_table_data.append([
            f"{chapter} ({stats.get('subject', 'N/A')})",
            stats.get('attempted', 'N/A'),
            stats.get('correct', 'N/A'),
            f"{stats.get('accuracy', 'N/A')}%",
            f"{stats.get('avg_time', 'N/A')} sec"
        ])
    chapter_table = Table(chapter_table_data, hAlign='LEFT')
    chapter_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(chapter_table)
    story.append(Spacer(1, 0.2 * inch))

    # Chapter-wise comments
    chapter_comments = []
    for chapter, stats in chapters.items():
        accuracy = stats.get('accuracy', 0)
        avg_time = stats.get('avg_time', 0)
        if accuracy < 50:
            chapter_comments.append(f"<b>{chapter} ({stats.get('subject', 'N/A')}):</b> This is a clear area for improvement.")
        elif avg_time > 100:
            chapter_comments.append(f"<b>{chapter} ({stats.get('subject', 'N/A')}):</b> Significantly longer average time per question ({avg_time} sec).")
    if chapter_comments:
        story.append(Paragraph("<br/>".join(chapter_comments), body_style))
    story.append(Spacer(1, 0.3 * inch))

    story.append(PageBreak())

    # Section 3: Time vs. Accuracy Insights
    story.append(Paragraph(f"{section_number}. Time vs. Accuracy Insights", subtitle_style))
    section_number += 1
    story.append(Spacer(1, 0.3 * inch))

    insights_text = f"""
    Generally, your accuracy is quite good ({test_info.get('accuracy', 'N/A')}%) overall. However, there are some areas to note:<br/>
    """
    for subject, stats in subjects.items():
        insights_text += f"<b>{subject}:</b> You spent an average of {stats.get('avg_time', 'N/A')} seconds per question with {stats.get('accuracy', 'N/A')}% accuracy. "
        if stats.get('avg_time', 0) > 100:
            insights_text += "Consider improving time management for this subject.<br/>"
        elif stats.get('accuracy', 0) < 50:
            insights_text += "Focus on strengthening core concepts to improve accuracy.<br/>"
        else:
            insights_text += "Good performance, keep practicing to maintain or improve.<br/>"
    story.append(Paragraph(insights_text.strip(), body_style))
    story.append(Spacer(1, 0.3 * inch))

    # Insert individual subject charts
    story.append(Paragraph("Subject-Wise Performance Chart", subtitle_style))
    story.append(Spacer(1, 0.2 * inch))
    for subject in subjects.keys():
        for chart_path in chart_paths:
            if subject.lower() in str(chart_path).lower() and os.path.exists(chart_path):
                story.append(Image(chart_path, width=6 * inch, height=4 * inch))
                story.append(Spacer(1, 0.3 * inch))

    story.append(PageBreak())

    # Section 4: Actionable Suggestions for Improvement
    story.append(Paragraph(f"{section_number}. Actionable Suggestions for Improvement", subtitle_style))
    section_number += 1
    story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph(f"Hey {student_name}, let's take your performance to the next level with these tailored strategies:", body_style))
    story.append(Spacer(1, 0.2 * inch))

    suggestions = feedback.get('suggestions', [])
    if suggestions and isinstance(suggestions, list):
        for suggestion in suggestions:
            if not suggestion.strip():
                continue
            # Split suggestion into main title and sub-bullets
            parts = suggestion.split('*')
            main_suggestion = parts[0].strip()
            sub_points = [p.strip() for p in parts[1:] if p.strip()]

            # Format suggestion with bold main title and bold sub-headings
            formatted_text = f"<b>{main_suggestion}</b><br/>"
            if sub_points:
                formatted_sub_points = []
                for sp in sub_points:
                    # Split sub-point into heading and description (assuming heading ends with colon)
                    sub_parts = sp.split(':', 1)
                    if len(sub_parts) == 2:
                        heading, description = sub_parts
                        formatted_sub_points.append(f"• <b>{heading.strip()}</b>: {description.strip()}")
                    else:
                        formatted_sub_points.append(f"• {sp}")
                formatted_text += "<br/>".join(formatted_sub_points)
            story.append(Paragraph(formatted_text.strip(), body_style))
            story.append(Spacer(1, 0.5 * inch))
    else:
        # Fallback suggestions if feedback is empty or invalid
        suggestions_list = []
        high_time_subjects = [s for s, stats in subjects.items() if stats.get('avg_time', 0) > 100]
        if high_time_subjects:
            sub_points = [
                f"<b>Practice with a timer</b>: Set a timer to mimic exam pressure and get faster at solving questions in {', '.join(high_time_subjects)}.",
                "<b>Focus on quick wins</b>: Tackle easier questions first to build momentum.",
                f"<b>Review slow topics</b>: Dive into what’s holding you up in {', '.join(high_time_subjects)}.",
                "<b>Stay calm</b>: Take a deep breath if you feel rushed during practice."
            ]
            suggestions_list.append(
                f"<b>1. Boost Your Time Management:</b><br/>"
                f"You’re spending a bit longer on questions in {', '.join(high_time_subjects)}. Let’s speed things up with these tips:<br/>"
                f"{'<br/>'.join(sub_points)}"
            )
        low_accuracy_chapters = [(c, stats) for c, stats in chapters.items() if stats.get('accuracy', 0) < 50]
        if low_accuracy_chapters:
            chapter_list = ', '.join([f"{c} ({stats.get('subject', 'N/A')} - {stats.get('accuracy', 'N/A')}%)" for c, stats in low_accuracy_chapters])
            sub_points = [
                f"<b>Revisit core concepts</b>: Brush up on key topics in {chapter_list}.",
                "<b>Solve varied problems</b>: Try different question types to build confidence.",
                "<b>Use visual aids</b>: Watch tutorials or draw diagrams for tough concepts.",
                "<b>Ask for help</b>: Reach out to a teacher or friend if you’re stuck!"
            ]
            suggestions_list.append(
                f"<b>2. Dive Into Weak Areas:</b><br/>"
                f"Your performance in {chapter_list} could use some love. Here’s how to tackle it:<br/>"
                f"{'<br/>'.join(sub_points)}"
            )
        suggestions_list.append(
            f"<b>3. Master Your Practice Routine:</b><br/>"
            f"Let’s make your study sessions super effective, {student_name}!<br/>"
            f"<b>Set clear goals</b>: Decide what you want to achieve each session.<br/>"
            f"<b>Mix it up</b>: Combine theory review, problem-solving, and past papers.<br/>"
            f"<b>Take breaks</b>: Study for 25 minutes, then rest for 5 to stay fresh.<br/>"
            f"<b>Track progress</b>: Note what’s improving to stay motivated!"
        )
        suggestions_list.append(
            f"<b>4. Analyze Your Mistakes:</b><br/>"
            f"Mistakes are your best teachers, {student_name}! Let’s learn from them:<br/>"
            f"<b>Review wrong answers</b>: Check what went wrong on each question.<br/>"
            f"<b>Spot patterns</b>: Are you making careless errors or missing concepts?<br/>"
            f"<b>Redo problems</b>: Try similar questions to lock in the learning.<br/>"
            f"<b>Stay positive</b>: Every mistake brings you closer to mastery!"
        )
        suggestions_list.append(
            f"<b>5. Build a Growth Mindset:</b><br/>"
            f"You’ve got the potential to shine, {student_name}! Here’s how to keep growing:<br/>"
            f"<b>Celebrate small wins</b>: Every step forward counts, so pat yourself on the back!<br/>"
            f"<b>Embrace challenges</b>: Tough topics are chances to get stronger.<br/>"
            f"<b>Stay consistent</b>: Keep studying a little every day to build habits.<br/>"
            f"<b>Believe in yourself</b>: You’re capable of amazing things!"
        )
        for suggestion in suggestions_list:
            story.append(Paragraph(suggestion.strip(), body_style))
            story.append(Spacer(1, 0.5 * inch))

    story.append(PageBreak())

    # Section 5: Final Encouragement
    story.append(Paragraph(f"{section_number}. Final Encouragement", subtitle_style))
    section_number += 1
    story.append(Spacer(1, 0.3 * inch))

    closing = feedback.get('closing', '')
    if closing.strip():
        encouragement = closing
    else:
        encouragement = f"""
        Hey {student_name}, you’re doing fantastic just by putting in the effort—that’s huge! Your hard work on {exam_name} shows you’ve got a solid base to build on. Keep diving into those practice sessions, stay curious, and don’t be afraid to tackle the tough stuff. I’m totally cheering for you, and I know you’re going to crush it in your next test. Let’s keep that momentum going!
        """
    story.append(Paragraph(encouragement.strip(), body_style))
    story.append(Spacer(1, 0.2 * inch))

    if os.path.exists(logo_path):
        story.append(Image(logo_path, width=1.5 * inch, height=1.5 * inch))

    doc.build(story)
    return pdf_path