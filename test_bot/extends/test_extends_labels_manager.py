import unittest
from unittest.mock import patch

from src.extend_todoist.extends_todoist_api import ExtendsTodoistAPI
from test_bot.mock.mock_extends_labels_manager import get_mock_labels


class TestExtendsLabelsManager(unittest.TestCase):

    @patch('src.extend_todoist.extends_labels_manager.ExtendsLabelsManager.get_all', side_effect=get_mock_labels)
    def test_find_label_by_name(self, mock_labels):
        api = ExtendsTodoistAPI('token')
        self.assertEqual(api.labels.get_by_name('Second_Label'), 2)
