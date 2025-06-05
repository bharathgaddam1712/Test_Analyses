import unittest
from src import data_processing

class TestDataProcessing(unittest.TestCase):
    def test_process_json(self):
        file_path = "data/submission1.json"
        try:
            test_info, syllabus, subjects, chapters, llm_context = data_processing.process_json(file_path, "John Doe")
            self.assertIsInstance(test_info, dict)
            self.assertIsInstance(syllabus, dict)
            self.assertIsInstance(subjects, dict)
            self.assertIsInstance(chapters, dict)
            self.assertIsInstance(llm_context, str)
            self.assertIn("Physics", subjects)
            self.assertGreater(len(chapters), 0)
        except Exception as e:
            self.fail(f"process_json failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()