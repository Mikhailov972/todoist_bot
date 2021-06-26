import logging

import telegram
from telegram.ext import Updater

from src import handlers
from src.config_util import ConfigUtil

tokens = ConfigUtil()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    bot = telegram.Bot(token=tokens.telegram_token)
    updater = Updater(token=tokens.telegram_token)
    dispatcher = updater.dispatcher
    handlers.init_handlers(dispatcher)
    updater.start_polling()
    logger.info('App START!')
