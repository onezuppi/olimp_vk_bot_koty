import json

class name():
    def __init__(self):
        with open('json/name.json', 'r', encoding='utf-8') as fh:
            self.data = json.load(fh)

    def name(self):
        return self.data["name"]

    def version(self):
        return self.data["version"]

    def url(self):
        return self.data["url"]

    def info(self):
        return self.data["info"]

    def code_name(self):
        return self.data["code_name"]

    def bot_img(self):
        return self.data["bot_img"]

    def egg(self):
        return self.data["egg"]
