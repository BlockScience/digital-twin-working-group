from model2.types import Trades
from model2.behavioral.trades import arbitrage_decision
from model2.policy.trades import price_impact_arbitrage

def p_arbitrage_trade(_params, substep, sH, s):
    #Current prices
    prices = s["prices"]
    basket_price = prices.basket_price
    index_price = prices.index_price
    theta1 = _params["theta1"]
    
    arbitrage_trade = arbitrage_decision(basket_price, index_price, theta1)
    
    if arbitrage_trade:
        prices = price_impact_arbitrage(basket_price, index_price)
    
    return {"new_prices": prices,
            "arbitrage_trade": arbitrage_trade}

def s_update_prices(_params, substep, sH, s, _input):
    new_prices = _input["new_prices"]
    
    return ("prices", new_prices)

def s_arbitrage_trade(_params, substep, sH, s, _input):
    trades = Trades(arbitrage = _input["arbitrage_trade"],
                    momentum_buy = None,
                    momentum_sell = None)
    return ("trades", trades)