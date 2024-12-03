from pymongo import MongoClient
from datetime import datetime
import json

# Connect to the local MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create or access a database
db = client['mydatabase']

# Create or access a collection (similar to a table in SQL)
collection = db['urls']

print("Connected to MongoDB locally!")

class Short_url:
    def __init__(self ,id , url):
        self.id = id
        self.url = url
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.updatedAt = datetime.now().strftime('%Y-%m-%d %H:%M')

    def create_dict(self):
        urls_dict = {}
        urls_dict["_id"] = self.id
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
    
    def save_to_db(self, new_url_dict):
        result = collection.insert_one(new_url_dict)
        print("Inserted task with ID:", result.inserted_id)
    @classmethod
    def find_url(cls, shortcode):
        url_dict = collection.find_one({"_id": shortcode})
        if url_dict is None:
            raise ValueError("Shortcode not found")
        collection.update_one({"_id": shortcode}, {"$inc": {"accessCount": 1}})
        return url_dict
    @classmethod
    def update_url(cls, shortcode, new_url):
        data =collection.update_one({"_id": shortcode}, {"$set": {
            "url": new_url,
            "updatedAt": datetime.now().strftime('%Y-%m-%d %H:%M'),
            "accessCount": 0}
            })
        return data
    
    @classmethod
    def delete_url(cls, shortcode):
        collection.delete_one({"_id": shortcode})
        return True