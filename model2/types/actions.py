from dataclasses import dataclass
from pandas import DataFrame

trade_action = bool
trade_table_raw = DataFrame
trade_table_processed = DataFrame

@dataclass
class Trades():
    arbitrage: trade_action
    momentum_buy: trade_action
    momentum_sell: trade_action
