from dataclasses import dataclass
from pandas import DataFrame

share_price = float
percentage_return = float
prices_table_raw = DataFrame
prices_table_processed = DataFrame
returns_table_raw = DataFrame
returns_table_processed = DataFrame

@dataclass
class Prices():
    index_price: share_price
    basket_price: share_price
        
@dataclass
class Returns():
    index_return: percentage_return
    basket_return: percentage_return
