import json

class data():
    def __init__(self):
        with open('json/data.json', 'r', encoding='utf-8') as fh:
            self.datp = json.load(fh)
        with open('json/future.json', 'r', encoding='utf-8') as fh:
            self.fut_dat = json.load(fh)

    def data(self):
        return self.datp

    def future(self):
        return self.fut_dat
