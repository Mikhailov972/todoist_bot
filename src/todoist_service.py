from src.config_util import ConfigUtil
from src.extend_todoist.extends_todoist_api import ExtendsTodoistAPI

tokens = ConfigUtil()
token = tokens.todoist_token

api = ExtendsTodoistAPI(token)


def add_youtube_playlist(playlist_with_title):
    main_task_name = format_to_hypertext(playlist_with_title['name'], playlist_with_title['url'])
    main_task = api.items.add(main_task_name, labels=[api.labels.get_by_name('YouTube')])

    for num, (id_video, name) in enumerate(playlist_with_title['playlist'].items(), start=1):
        share_youtube_url = 'https://youtu.be/{}'.format(id_video)
        api.items.add('{}) {}'.format(num, format_to_hypertext(name, share_youtube_url)), parent_id=main_task['id'])
    api.commit()

    return get_task_url(main_task.data['project_id'], main_task.data['id'])


def add_task(title, url, label_name):
    inbox_id = 2267224752
    main_task_name = format_to_hypertext(title, url)
    main_task = api.items.add(main_task_name, labels=[api.labels.get_by_name(label_name)], project_id=inbox_id)
    api.commit()

    return get_task_url(main_task.data['project_id'], main_task.data['id'])


def format_to_hypertext(name, url):
    return '[{}]({})'.format(name, url)


def get_task_url(project_id, task_id):
    return 'todoist.com/app/project/{}/task/{}'.format(project_id, task_id)
