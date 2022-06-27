from model2.types import Prices

def price_impact_arbitrage(basket_price, index_price) -> Prices:
    index_price = basket_price
    return Prices(index_price = index_price,
                  basket_price = basket_price)


def compute_period_return(current_index_price, past_index_price,
                          lookback):
    mu1 = .01
    period_return = current_index_price / past_index_price  - 1 - mu1 * lookback
    return period_return

def price_impact_momentum(basket_price, index_price, momentum_buy, momentum_sell) -> Prices:
    if momentum_buy:
        index_price = index_price * 1.025
    elif momentum_sell:
        index_price = index_price * (1-.025)
    return Prices(index_price = index_price,
                  basket_price = basket_price)