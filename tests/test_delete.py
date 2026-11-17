import unittest
from task_manager import TaskManager


class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
        manager = TaskManager()
        first = manager.add_task("Task to delete")
        second = manager.add_task("Task to keep")

        manager.delete_task(first["id"])

        self.assertEqual(len(manager.tasks), 1)
        self.assertEqual(manager.tasks[0]["id"], second["id"])

        with self.assertRaises(ValueError):
            manager.delete_task(999)


if __name__ == "__main__":
    unittest.main()