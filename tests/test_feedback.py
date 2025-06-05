import unittest
from src import data_processing, ai_feedback

class TestFeedback(unittest.TestCase):
    def test_generate_feedback(self):
        file_path = "data/submission1.json"
        try:
            test_info, syllabus, subjects, chapters, llm_context = data_processing.process_single_json(file_path, "John Doe")
            feedback = ai_feedback.generate_feedback("John Doe", test_info, subjects, chapters, llm_context)
            self.assertIsInstance(feedback, str)
            self.assertGreater(len(feedback), 0)
            self.assertNotIn("Error generating feedback", feedback)
        except Exception as e:
            self.fail(f"generate_feedback failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()