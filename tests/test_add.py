import unittest
from task_manager import TaskManager


class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        manager = TaskManager()

        task = manager.add_task("Study Python")

        self.assertEqual(len(manager.tasks), 1)
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Study Python")
        self.assertFalse(task["completed"])


if __name__ == "__main__":
    unittest.main()