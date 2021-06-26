import requests
from todoist.managers.labels import LabelsManager


class ExtendsLabelsManager(LabelsManager):
    def get_by_name(self, name):
        for label in self.get_all():
            if label['name'] == name:
                return label['id']

    def get_all(self):
        return requests.get("https://api.todoist.com/rest/v1/labels",
                            headers={
                                "Authorization": "Bearer %s" % self.token
                            }).json()
