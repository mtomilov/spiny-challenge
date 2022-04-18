import logging
import os

import pandas as pd
from flask import Flask, jsonify

from utils import get_db

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)


@app.route('/ping')
def ping_server():
    return 'hello world'


@app.route('/apis/search_interest/<string:keyword>')
def get_search_interest(keyword: str):
    db = get_db()
    trends = db.trends.find({'keyword': keyword})
    df = pd.DataFrame(list(trends))
    if df.empty:
        return {}

    df['interest'] = (
        (df['interest'] - df['interest'].min())
        / (df['interest'].max() - df['interest'].min())
        * 100
    )
    df['date'] = df['date'].astype('str')
    interest = {row['date']: row['interest'] for row in df.to_dict(orient='records')}
    return jsonify(interest)


if __name__ == '__main__':
    debug = bool(os.environ.get('DEBUG'))
    app.run(host='0.0.0.0', port=5000, debug=debug)
