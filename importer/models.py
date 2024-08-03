from pymongo import MongoClient
from django.conf import settings

def get_db():
    client = MongoClient(settings.MONGO_URL)
    db = client['new_db']
    return db
