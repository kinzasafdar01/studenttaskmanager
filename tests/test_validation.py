import unittest
from task_manager import TaskManager


class TestTaskValidation(unittest.TestCase):
    def test_reject_empty_titles(self):
        manager = TaskManager()

        for title in ["", "   "]:
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    manager.add_task(title)

        self.assertEqual(manager.tasks, [])


if __name__ == "__main__":
    unittest.main()