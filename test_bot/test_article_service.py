import unittest
from unittest.mock import patch

from src.article_service import parse_title
from mock.mock_article_service import mock_html_page


class TestArticleService(unittest.TestCase):
    @patch('src.article_service.send_request_get_html_page', side_effect=mock_html_page)
    def test_parse_title(self, mock_send_request_get_html_page):
        self.assertEqual(parse_title('anyWebSite'), 'Title WEB Site!')
