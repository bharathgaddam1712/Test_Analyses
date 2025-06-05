# import os
# from src import data_processing, ai_feedback, visualization, pdf_generator
# from config import config

# def main():
#     # Configuration
#     student_name = "John Doe"
#     file_path = os.path.join(config.DATA_DIR, "submission2.json")
#     chart1_base_path = "accuracy_over_time"
#     chart2_path = "subject_accuracy.png"
#     pdf_path = f"{student_name}_performance_report.pdf"
    
#     try:
#         # Ensure output directories exist
#         os.makedirs(config.OUTPUT_CHARTS_DIR, exist_ok=True)
#         os.makedirs(config.OUTPUT_REPORTS_DIR, exist_ok=True)
        
#         # Process JSON for detailed analysis
#         test_info, syllabus, subjects, chapters, llm_context = data_processing.process_single_json(file_path, student_name)
        
#         # Compute cumulative accuracy over time for individual subjects
#         subjects_accuracy_over_time = data_processing.compute_accuracy_over_time(file_path)
        
#         # Generate visualizations
#         subject_charts = visualization.plot_cumulative_accuracy_over_time(subjects_accuracy_over_time, chart1_base_path)
#         subject_accuracy_chart = visualization.plot_subject_accuracy(subjects, chart2_path)
#         chapter_table = visualization.create_chapter_table(chapters)
        
#         # Generate AI feedback
#         feedback = ai_feedback.generate_feedback(student_name, test_info, subjects, chapters, llm_context)
        
#         # Generate PDF report
#         charts = subject_charts + [subject_accuracy_chart]
#         pdf_file = pdf_generator.generate_pdf(student_name, test_info, subjects, chapters, feedback, charts, pdf_path)
        
#         # Print results
#         print("Test Info:", test_info)
#         print("Syllabus:", syllabus)
#         print("Subjects:", subjects)
#         print("Chapters:", chapters)
#         print("Chapter Table:")
#         print(chapter_table)
#         print("Subject-wise Cumulative Accuracy Over Time Data:")
#         for subj, df in subjects_accuracy_over_time.items():
#             print(f"\n{subj}:\n{df}")
#         print("LLM Context:")
#         print(llm_context)
#         print("Feedback:")
#         print(feedback)
#         print(f"PDF Report Generated: {pdf_file}")
        
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         raise  # Re-raise to get the full traceback

# if __name__ == "__main__":
#     main()











import os
from src import data_processing, ai_feedback, visualization, pdf_generator
from config import config

def main():
    # Configuration
    student_name = "John Doe"
    file_path = os.path.join(config.DATA_DIR, "submission1.json")
    chart1_base_path = "accuracy_over_time"
    chart2_path = "subject_accuracy.png"
    pdf_path = f"{student_name}_performance_report.pdf"
    
    try:
        # Ensure output directories exist
        os.makedirs(config.OUTPUT_CHARTS_DIR, exist_ok=True)
        os.makedirs(config.OUTPUT_REPORTS_DIR, exist_ok=True)
        
        # Process JSON for detailed analysis
        test_info, syllabus, subjects, chapters, llm_context = data_processing.process_single_json(file_path, student_name)
        
        # Compute cumulative accuracy over time for individual subjects
        subjects_accuracy_over_time = data_processing.compute_accuracy_over_time(file_path)
        
        # Generate visualizations
        subject_charts = visualization.plot_cumulative_accuracy_over_time(subjects_accuracy_over_time, chart1_base_path)
        subject_accuracy_chart = visualization.plot_subject_accuracy(subjects, chart2_path)
        chapter_table = visualization.create_chapter_table(chapters)
        
        # Generate AI feedback
        feedback = ai_feedback.generate_feedback(student_name, test_info, subjects, chapters, llm_context)
        
        # Generate PDF report
        charts = subject_charts + [subject_accuracy_chart]
        pdf_file = pdf_generator.generate_pdf(student_name, test_info, subjects, chapters, feedback, charts, pdf_path)
        
        # Print results
        print("Test Info:", test_info)
        print("Syllabus:", syllabus)
        print("Subjects:", subjects)
        print("Chapters:", chapters)
        print("Chapter Table:")
        print(chapter_table)
        print("Subject-wise Cumulative Accuracy Over Time Data:")
        for subj, df in subjects_accuracy_over_time.items():
            print(f"\n{subj}:\n{df}")
        print("LLM Context:")
        print(llm_context)
        print("Feedback:")
        print(feedback)
        print(f"PDF Report Generated: {pdf_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise  # Re-raise to get the full traceback

if __name__ == "__main__":
    main()