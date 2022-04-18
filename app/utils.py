from pymongo import MongoClient
import os


def get_db():
    port = os.environ.get('DB_PORT')
    client = MongoClient(
        host=os.environ.get('DB_HOST'),
        port=int(port),
        username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'),
        password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'),
    )
    db = client['google_db']
    # for a simpler deployment
    db.trends.create_index([('keyword', 'text')])
    db.trends.create_index([('keyword', 1), ('date', 1)], unique=True)
    return db
