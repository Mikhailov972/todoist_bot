import logging

from telegram import ParseMode
from telegram.ext import MessageHandler, Filters, CommandHandler

from src import todoist_service
from src.article_service import parse_title
from src.youtube_service import get_playlist, get_title_playlist, get_title_video

logger = logging.getLogger(__name__)


def init_handlers(dispatcher):
    article_regex = r'^http[s]?://(?!.*youtube\.com)(?!.*youtu\.be).+'
    youtube_playlist_regex = r'^https://youtube\.com/playlist\?list=.{18,34}$'
    youtube_regex = r'^https://youtu\.be/.{11}$'

    dispatcher.add_handler(MessageHandler(Filters.regex(article_regex), article_handler))
    dispatcher.add_handler(MessageHandler(Filters.regex(youtube_playlist_regex), youtube_playlist_handler))
    dispatcher.add_handler(MessageHandler(Filters.regex(youtube_regex), youtube_video_handler))
    dispatcher.add_handler(CommandHandler('start', start_handler))


def youtube_playlist_handler(update, context):
    if not check_username(update, context):
        return

    url = update.message.text
    logger.info('Start get data playlist: %s', url)
    title_playlist = get_title_playlist(url)
    playlist = get_playlist(url)

    playlist_with_title = {'name': title_playlist, 'url': url, 'playlist': playlist}

    logger.info('Success build playlist: %s', playlist_with_title['name'])

    task_url = todoist_service.add_youtube_playlist(playlist_with_title)
    logger.info('Created task: %s', task_url)
    send_msg_complete_task(create_message(title_playlist, task_url), update, context)


def youtube_video_handler(update, context):
    if not check_username(update, context):
        return

    url = update.message.text
    logger.info('Start get video data: %s', url)

    title = get_title_video(url)
    logger.info('Success build playlist: %s', title)

    task_url = todoist_service.add_task(title, url, 'YouTube')
    logger.info('Created task: %s', task_url)
    send_msg_complete_task(create_message(title, task_url), update, context)


def article_handler(update, context):
    if not check_username(update, context):
        return

    url = update.message.text
    logger.info('Start parse site: %s', url)

    title = parse_title(url)
    logger.info('Success parse site title: %s', title)
    task_url = todoist_service.add_task(title, url, 'Статьи')
    logger.info('Created task: %s', task_url)
    send_msg_complete_task(create_message(title, task_url), update, context)


def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Praise the sun!")


def check_username(update, context):
    msg_for_stranger = '<a href=\'{}\'>{}</a>'.format('https://youtu.be/fBGWtVOKTkM',
                                                      'Hehe hehe... You have no power here...')
    username = update.message.from_user.username
    logger.info('User %s send message', username)
    if username != 'Mikhailov972':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=msg_for_stranger,
                                 parse_mode=ParseMode.HTML)
        return False
    return True


def send_msg_complete_task(message, update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)


def create_message(title, task_url):
    return 'Task <a href=\'{}\'>{}</a> completed!'.format(task_url, title)
