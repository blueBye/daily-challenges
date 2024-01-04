import unittest
from tasks import Task, CompositeTask


def normalize_string(s):
    return ' '.join(s.lower().split())


class TestTask(unittest.TestCase):
    def assertEqualNormalized(self, a, b):
        self.assertEqual(normalize_string(a), normalize_string(b))

    def test_task_initialization(self):
        task = Task("Test Task")
        self.assertEqualNormalized(task.name, "test task")
        self.assertFalse(task.completed)

    def test_composite_task_initialization(self):
        composite_task = CompositeTask("Composite Task")
        self.assertEqualNormalized(composite_task.name, "composite task")
        self.assertFalse(composite_task.completed)

    def test_complex_composite_task_initialization(self):
        composite_task = CompositeTask("Composite Task")
        subtask1 = Task("task1")
        subtask2 = Task("task2")
        composite_task.add_subtask(subtask1)
        composite_task.add_subtask(subtask2)
        composite_task.mark_complete()
        print(composite_task.get_detail())
        self.assertTrue(composite_task.completed)

        