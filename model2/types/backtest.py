from dataclasses import dataclass
from .prices import prices_table_processed, returns_table_processed
from .actions import trade_table_processed
from pandas import DataFrame

historical_data = DataFrame
input_data = DataFrame
output_data = DataFrame

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