def mock_send_request_title_playlist(self):
    return {
        "items": [
            {
                "snippet": {
                    "localized": {
                        "title": "Spring course for beginner"
                    }
                }
            }
        ]
    }


def mock_send_request_title_video(self):
    return {
        "items": [
            {
                "snippet": {
                    "title": "How To Mock Patch A Function"
                }
            }
        ]
    }


def mock_send_request_playlist_first_page(self):
    return {
        "items": [
            {
                "snippet": {
                    "title": "How To Mock Patch A Function"
                }
            }
        ]
    }


def mock_pages():
    first_page = {
        "nextPageToken": "second",
        "items": [
            {
                "snippet": {
                    "title": "first_video",
                    "resourceId": {
                        "videoId": "first_video_id"
                    }
                }
            }
        ]
    }

    second_page = {
        "items": [
            {
                "snippet": {
                    "title": "second_video",
                    "resourceId": {
                        "videoId": "second_video_id"
                    }
                }
            }
        ]
    }

    return [first_page, second_page]
