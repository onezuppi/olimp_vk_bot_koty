import json

class settings():
    def __init__(self):
        with open('json/settings.json', 'r', encoding='utf-8') as fh:
            self.data = json.load(fh)

    def api(self):
        return self.data["api"]

    def mes_api(self):
        return self.data["mes_api"]

    def use_dir(self):
        return self.data["use_dir"]

    def db(self):
        return self.data["db"]

    def owner_id(self):
        return self.data["owner_id"]
