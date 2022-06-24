from dataclasses import dataclass

share_price = float
percentage_return = float

@dataclass
class Prices():
    index_price: share_price
    basket_price: share_price
        
@dataclass
class Returns():
    index_return: percentage_return
    basket_return: percentage_return
