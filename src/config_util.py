import json
import os

import yaml
from googleapiclient import discovery


class ConfigUtil:
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(self.ROOT_DIR, '../config.yaml'), 'r') as stream:
            config_yaml = yaml.safe_load(stream)
            self.telegram_token = config_yaml.get('tokens')['telegram']
            self.todoist_token = config_yaml.get('tokens')['todoist']
            self.youtube = config_yaml.get('tokens')['youtube']

    @staticmethod
    def build_discovery_google(self):
        config = ConfigUtil()
        token = config.youtube
        with open(os.path.join(self.ROOT_DIR, '../google_api_rest.json'), encoding='utf-8') as f:
            service = json.load(f)
        return discovery.build_from_document(service, developerKey=token)
