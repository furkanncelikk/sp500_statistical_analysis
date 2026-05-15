"""
db_utils.py
-----------
Central database connection manager for the S&P 500 Quantitative Research project.

Data Source:
    - A private PostgreSQL data warehouse (`sp500_dw`) populated via a custom
      automated pipeline using the yfinance API.
    - Tables: `daily_prices` (OHLCV), `tickers` (metadata), `ticker_stats` (pre-computed stats).
    - The pipeline covers all current S&P 500 constituents with full historical daily data.

Usage:
    from db_utils import fetch_data
    df = fetch_data("SELECT * FROM tickers LIMIT 5")

Note:
    Connection credentials are stored in `config.py` which is excluded from
    version control via .gitignore. To replicate this project, create a
    config.py with your own DB_URL.
"""

import pandas as pd
from sqlalchemy import create_engine

# Import credentials from private config (not in GitHub)
try:
    from config import DB_URL
except ImportError:
    raise EnvironmentError(
        "config.py bulunamadı. Lütfen DB_URL değişkeninizle bir config.py dosyası oluşturun.\n"
        "Örnek: DB_URL = 'postgresql+psycopg2://user:password@host:port/dbname'"
    )

# Singleton engine — bağlantı bir kere kurulur, tekrar kullanılır
_engine = None

def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(DB_URL)
    return _engine


def fetch_data(query: str) -> pd.DataFrame:
    """
    Execute a SQL query against the sp500_dw database and return a DataFrame.

    Parameters
    ----------
    query : str
        Any valid PostgreSQL SELECT statement.

    Returns
    -------
    pd.DataFrame
    """
    return pd.read_sql(query, get_engine())
