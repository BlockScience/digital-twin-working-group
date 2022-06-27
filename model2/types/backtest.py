from dataclasses import dataclass
from .prices import prices_table_processed, returns_table_processed, Prices
from .actions import trade_table_processed, Trades
from pandas import DataFrame
from typing import TypedDict

historical_data = DataFrame
input_data = DataFrame
output_data = DataFrame

historical_data_model = DataFrame
input_data_model = DataFrame
output_data_model = DataFrame

model_starting_state = TypedDict('model_starting_state', prices=Prices, trades=Trades)


@dataclass
class BacktestData():
    pure_returns: returns_table_processed
    prices_data: prices_table_processed
    trades_data: trade_table_processed
    
@dataclass
class InputData():
    starting_state: prices_table_processed
    historical_data: historical_data
    input_data: input_data
    output_data: output_data
    ending_state: prices_table_processed
    
@dataclass
class InputDataModel():
    starting_state: model_starting_state
    ending_state: model_starting_state
    historical_data: historical_data_model
    input_data: input_data_model
    output_data: output_data_model