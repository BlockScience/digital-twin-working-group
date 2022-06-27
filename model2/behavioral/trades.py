def arbitrage_decision(basket_price, index_price, theta1):
    return abs(basket_price - index_price) > theta1