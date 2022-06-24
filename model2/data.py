import sqlite3
from sqlite3 import Connection
import pandas as pd
from types import (prices_table_raw, prices_table_processed,
                   returns_table_raw, returns_table_processed,
                   trade_table_raw, trade_table_processed)

def create_connection() -> Connection:
    """
    Builds the connection to the database

    Returns
    -------
    Connection
        A sqlite3 connection

    """
    return sqlite3.connect('arb.db')

def pull_pure_returns(con: Connection) -> returns_table_raw:
    """
    Pulls the pure returns table

    Parameters
    ----------
    con : Connection
        A sqlite3 connection

    Returns
    -------
    returns_table_raw
        Pure returns table

    """
    return pd.read_sql("SELECT * FROM pure_returns", con)

def pull_prices(con: Connection) -> prices_table_raw:
    """
    Pulls the prices table

    Parameters
    ----------
    con : Connection
        A sqlite3 connection

    Returns
    -------
    prices_table_raw
        Prices table

    """
    return pd.read_sql("SELECT * FROM prices", con)

def pull_trades(con: Connection) -> trade_table_raw:
    """
    Pulls the trades table

    Parameters
    ----------
    con : Connection
        A sqlite3 connection

    Returns
    -------
    trade_table_raw
        Trades table

    """
    return pd.read_sql("SELECT * FROM trades", con)