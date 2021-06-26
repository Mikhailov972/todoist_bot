from src.config_util import ConfigUtil

config_util = ConfigUtil()
youtube = config_util.build_discovery_google(config_util)


def get_title_playlist(url):
    playlist_id = get_playlist_id(url)
    response = send_request_get_title_playlist(playlist_id)
    return response['items'][0]['snippet']['localized']['title']


def get_title_video(url):
    video_id = get_video_id(url)
    response = send_request_get_title_video(video_id)
    return response['items'][0]['snippet']['title']


def get_playlist(url):
    playlist_id = get_playlist_id(url)
    all_pages = get_all_pages_playlist_recursively(playlist_id)
    return parse_pages(all_pages)


def get_all_pages_playlist_recursively(playlist_id, page_token='', pages=None):
    response = send_request_get_playlist(playlist_id, page_token)

    try:
        if pages is None:
            pages = []
        pages.append(response)

        next_page_token = response['nextPageToken']
        return get_all_pages_playlist_recursively(playlist_id, next_page_token, pages)
    except KeyError:
        return pages


def parse_pages(pages):
    playlist = {}

    for page in pages:
        for items in page['items']:
            snippet = items['snippet']
            playlist.update({snippet['resourceId']['videoId']: snippet['title']})
    return playlist


def get_playlist_id(url):
    return url[34:68]


def get_video_id(url):
    return url[17:28]


def send_request_get_title_playlist(playlist_id):
    request = youtube.playlists().list(part='snippet', id=playlist_id, fields='items(snippet(localized(title)))')
    return request.execute()


def send_request_get_title_video(video_id):
    request = youtube.videos().list(part='snippet', id=video_id, fields='items(snippet(title))')
    return request.execute()


def send_request_get_playlist(playlist_id, page_token):
    request = youtube.playlistItems().list(part='snippet', playlistId=playlist_id, maxResults=50,
                                           fields='nextPageToken,items(snippet(title, resourceId(videoId)))',
                                           pageToken=page_token)
    return request.execute()
