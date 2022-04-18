import time
from pathlib import Path

import pandas as pd
from pymongo.database import Database
from pymongo.errors import BulkWriteError
from pytrends.request import TrendReq
import logging

from utils import get_db

PULL_TIMEOUT = 1

logger = logging.getLogger(__name__)


def pull_trend(keyword: str, timeframe: str = 'now 4-H') -> pd.DataFrame:
    """
    Pulls Google Trends data for a given keyword and timeframe.

    Args:
        keyword (str): The keyword to pull data for.
        timeframe (str): The timeframe to pull data for.

    Returns:
        pd.DataFrame: A dataframe containing the data.
    """
    pytrend = TrendReq(hl='en-US')
    pytrend.build_payload([keyword], timeframe=timeframe)
    return pytrend.interest_over_time()


def save_trend(db: Database, df: pd.DataFrame) -> None:
    keyword = df.columns[0]
    df.reset_index(inplace=True)
    df.rename(columns={keyword: 'interest', 'isPartial': 'is_partial'}, inplace=True)
    df['keyword'] = keyword
    try:
        # with ordered=False all document inserts will be attempted
        db.trends.insert_many(df.to_dict(orient='records'), ordered=False)
    except BulkWriteError as e:
        # filter out duplicate key errors
        filtered_write_errors = [
            err for err in e.details['writeErrors'] if err['code'] != 11000
        ]
        if filtered_write_errors:
            e.details['writeErrors'] = filtered_write_errors
            raise e


if __name__ == '__main__':
    path = Path(__file__).with_name('top-search-keywords.csv')
    with open(path) as f:
        keywords = f.read().strip().splitlines()

    db = get_db()
    for keyword in keywords:
        df = pull_trend(keyword)
        save_trend(db, df)
        time.sleep(PULL_TIMEOUT)
        logger.info('pulled the trends for {}'.format(keyword))
