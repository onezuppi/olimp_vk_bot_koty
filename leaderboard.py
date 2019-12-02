import json

class leaderboard():
    def __init__(self):
        with open('json/leaderboard.json', 'r', encoding='utf-8') as fh:
            self.data = json.load(fh)

    def keys(self):
        return self.data.keys()

    def add(self,id,value):
        self.data[str(id)] = value
        self.save()

    def save(self):
        with open('json/leaderboard.json', 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(self.data,indent=2,ensure_ascii=False))

    def get(self,id):
        return self.data.get(str(id))

    def set(self,id):
        self.data[str(id)] += 1
        self.save()

    def raw_data(self):
        return self.data
