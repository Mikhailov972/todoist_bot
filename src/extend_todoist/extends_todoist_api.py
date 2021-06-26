from todoist.api import TodoistAPI, DEFAULT_API_VERSION

from src.extend_todoist.extends_labels_manager import ExtendsLabelsManager


class ExtendsTodoistAPI(TodoistAPI):
    def __init__(
            self,
            token="",
            api_endpoint="https://api.todoist.com",
            api_version=DEFAULT_API_VERSION,
            session=None,
            cache="~/.todoist-sync/",
    ):
        TodoistAPI.__init__(self, token, api_endpoint, api_version, session, cache)
        self.labels = ExtendsLabelsManager(self)
