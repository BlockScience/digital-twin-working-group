import sqlite3
from sqlite3 import Connection
import pandas as pd
from .types import (prices_table_raw, prices_table_processed,
                   returns_table_raw, returns_table_processed,
                   trade_table_raw, trade_table_processed,
                   BacktestData, InputData)

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


def process_pure_returns(pure_returns_data: returns_table_raw) -> returns_table_processed:
    """
    Function to convert raw returns table to processed

    Parameters
    ----------
    pure_returns_data : returns_table_raw
        Raw version

    Returns
    -------
    returns_table_processed
        Processed version

    """
    
    #Set and sort time index
    pure_returns_data = pure_returns_data.set_index('t')
    pure_returns_data = pure_returns_data.sort_index()
    
    return pure_returns_data

def process_prices(prices_data: prices_table_raw) -> prices_table_processed:
    """
    Function to convert raw prices table to processed

    Parameters
    ----------
    prices_data : prices_table_raw
        Raw version

    Returns
    -------
    prices_table_processed
        Processed version

    """
    
    #Set and sort index
    prices_data = prices_data.set_index('t')
    prices_data = prices_data.sort_index()
    
    return prices_data

def process_trades(trades_data: trade_table_raw) -> trade_table_processed:
    """
    Function to convert raw trades table to processed

    Parameters
    ----------
    trades_data : trade_table_raw
        Raw version

    Returns
    -------
    trade_table_processed
        Processed version

    """
    
    trades_data = trades_data.rename(columns = {"time": "t"})
    
    #Pivot to t x trade x had_trade
    trades_data["had_trade"] = True
    trades_data = trades_data.pivot("t", "trade", "had_trade")
    trades_data = trades_data.fillna(False)
    
    return trades_data

def pull_backtest_data() -> BacktestData:
    """
    Does the aggregate data pull for pulling backtest data

    Returns
    -------
    BacktestData
        The data used for backtesting the model

    """
    
    #Connect to database
    con = create_connection()
    
    #Raw data pulls
    pure_returns_data = pull_pure_returns(con)
    prices_data = pull_prices(con)
    trades_data = pull_trades(con)
    
    #Data processing
    pure_returns_data = process_pure_returns(pure_returns_data)
    prices_data = process_prices(prices_data)
    trades_data = process_trades(trades_data)
    
    #Create backtest data object
    data = BacktestData(pure_returns = pure_returns_data, 
                        prices_data = prices_data,
                        trades_data = trades_data)
    
    return data

def create_input_data(backtest_data: BacktestData) -> InputData:
    """
    Take backtest data and turn it into input data

    Parameters
    ----------
    backtest_data : BacktestData
        Backtest data

    Returns
    -------
    InputData
        Input data for use in the model

    """
    
    #Grab the relevant data
    pure_returns_data = backtest_data.pure_returns.copy()
    prices_data = backtest_data.prices_data.copy()
    trades_data = backtest_data.trades_data.copy()
    
    #Grab the starting state
    starting_state = prices_data.iloc[0]
    
    #Push ahead prices data
    prices_data = prices_data.iloc[1:]
    prices_data.index = prices_data.index - 1
    
    #Combine data
    historical_data = pd.concat([pure_returns_data, prices_data, trades_data], axis=1)
    historical_data[["Arbitrage", "Momentum Buy", "Momentum Sell"]] = historical_data[["Arbitrage", "Momentum Buy", "Momentum Sell"]].fillna(False)
    
    #Build input and output data
    input_data = historical_data[["index_return", "basket_return"]]
    output_data = historical_data[["index_price", "basket_price", "Arbitrage", "Momentum Buy", "Momentum Sell"]]
    
    out = InputData(starting_state = starting_state,
                    historical_data = historical_data,
                    input_data = input_data,
                    output_data = output_data)
    
    return out