import time
from pathlib import Path

import pandas as pd
from pymongo.database import Database
from pytrends.request import TrendReq
from utils import get_db

PULL_TIMEOUT = 1


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
    db.trends.insert_many(df.to_dict(orient='records'), ordered=False)


if __name__ == '__main__':
    path = Path(__file__).with_name('top-search-keywords.csv')
    with open(path) as f:
        keywords = f.read().strip().splitlines()

    db = get_db()
    for keyword in keywords[:1]:
        df = pull_trend(keyword)
        save_trend(db, df)
        time.sleep(PULL_TIMEOUT)
