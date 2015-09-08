import unittest
from app.painter import Painter

class TestPainter(unittest.TestCase):
    def setUp(self):
        self.painter = Painter()

    def test_job_class_name(self):
        self.assertEqual(self.painter.job_class_name, "Apprentice")

    def test_working_job(self):
        self.assertEqual(self.painter.working_job, False)

if __name__ == '__main__':
    unittest.main()
