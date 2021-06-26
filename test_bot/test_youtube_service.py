import unittest
from unittest.mock import patch

from mock.mock_youtube_service import *
from src.youtube_service import *


class TestYouTubeService(unittest.TestCase):
    def test_get_video_id(self):
        share_video_url = 'https://youtu.be/lKo-F3gSl7I'
        self.assertEqual('lKo-F3gSl7I', get_video_id(share_video_url))

    def test_get_playlist_id(self):
        share_playlist_url = 'https://youtube.com/playlist?list=PL6yLoZ_3Y0HKGL3F7vv2SNSrA3TkbXtBX'
        self.assertEqual('PL6yLoZ_3Y0HKGL3F7vv2SNSrA3TkbXtBX', get_playlist_id(share_playlist_url))

    @patch('src.youtube_service.send_request_get_title_playlist', side_effect=mock_send_request_title_playlist)
    def test_get_title_playlist(self, mock_send_request_title_playlist):
        share_playlist_url = 'https://youtube.com/playlist?list=PL6yLoZ_3Y0HKGL3F7vv2SNSrA3TkbXtBX'
        self.assertEqual(get_title_playlist(share_playlist_url), 'Spring course for beginner')

    @patch('src.youtube_service.send_request_get_title_video', side_effect=mock_send_request_title_video)
    def test_get_title_video(self, mock_send_request_title_video):
        share_video_url = 'https://youtu.be/ClAdw7ZJf5E'
        self.assertEqual(get_title_video(share_video_url), 'How To Mock Patch A Function')

    def test_parse_pages(self):
        expected = {'first_video_id': 'first_video', 'second_video_id': 'second_video'}
        self.assertEqual(parse_pages(mock_pages()), expected)

    @patch('src.youtube_service.send_request_get_playlist', side_effect=mock_pages())
    def test_get_all_pages_playlist_recursively(self, mock_send_request_playlist):
        actual = get_all_pages_playlist_recursively('anyId')
        self.assertEqual(actual, mock_pages())
        self.assertEqual(mock_send_request_playlist.call_count, 2)
