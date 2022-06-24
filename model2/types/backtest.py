from dataclasses import dataclass
from .prices import prices_table_processed, returns_table_processed
from .actions import trade_table_processed

@dataclass
class BacktestData():
    pure_returns: returns_table_processed
    prices_data: prices_table_processed
    trades_data: trade_table_processed
    