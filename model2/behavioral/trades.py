def arbitrage_decision(basket_price, index_price, theta1):
    return abs(basket_price - index_price) > theta1

def momentum_buy_decision(period_return, theta2):
    return period_return > theta2

def momentum_sell_decision(period_return, theta2):
    return period_return < -theta2