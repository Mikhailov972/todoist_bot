import unittest

from src.todoist_service import get_task_url, format_to_hypertext


class TestTodoistService(unittest.TestCase):
    def test_format_to_hypertext(self):
        self.assertEqual(format_to_hypertext('Google', 'https://www.google.ru/'), '[Google](https://www.google.ru/)')

    def test_get_task_url(self):
        self.assertEqual(get_task_url('project_id', 'task_id'), 'todoist.com/app/project/project_id/task/task_id')
