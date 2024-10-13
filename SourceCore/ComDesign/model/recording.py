from templates.config import db


def recording(username, data):
    collection = db[username]
    collection.insert_one(data)
