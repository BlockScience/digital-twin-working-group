from model2.types import Prices

def price_impact_arbitrage(basket_price, index_price) -> Prices:
    index_price = basket_price
    return Prices(index_price = index_price,
                  basket_price = basket_price)