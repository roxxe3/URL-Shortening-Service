from datetime import datetime

import json


class Short_url:
    def __init__(self ,id , url):
        self.id = id
        self.url = url
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.updatedAt = datetime.now().strftime('%Y-%m-%d %H:%M')

    def create_dict(self):
        urls_dict = {}
        urls_dict["id"] = self.id
        urls_dict["url"] = self.url
        urls_dict["createdAt"] = self.createdAt
        urls_dict["updatedAt"] = self.updatedAt
        urls_dict["accessCount"] = 0
        return urls_dict

    def save_file(self, new_url_dict):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(new_url_dict)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)