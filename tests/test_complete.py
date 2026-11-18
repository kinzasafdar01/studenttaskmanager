import unittest
from task_manager import TaskManager


class TestCompleteTask(unittest.TestCase):
    def test_complete_task(self):
        manager = TaskManager()
        task = manager.add_task("Revise DevOps")

        manager.complete_task(task["id"])

        self.assertTrue(manager.tasks[0]["completed"])

        with self.assertRaises(ValueError):
            manager.complete_task(999)


if __name__ == "__main__":
    unittest.main()