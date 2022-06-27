from model2.types import Trades
from model2.behavioral.trades import arbitrage_decision, momentum_buy_decision, momentum_sell_decision
from model2.policy.trades import price_impact_arbitrage, compute_period_return, price_impact_momentum

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

def p_momentum_trade(_params, substep, sH, s):
    #Current prices
    prices = s["prices"]
    basket_price = prices.basket_price
    index_price = prices.index_price
    t = s["timestep"]
    lookback = _params["lookback"]
    lookback_i = max(t - lookback, 0)

    past_index_price = sH[lookback_i][-1]["prices"].index_price
    theta2 = _params["theta2"]
    
    period_return = compute_period_return(index_price, past_index_price,
                          lookback)
    
    momentum_buy = momentum_buy_decision(period_return, theta2)
    momentum_sell = momentum_sell_decision(period_return, theta2)
    prices = price_impact_momentum(basket_price, index_price, momentum_buy, momentum_sell)
    return {"new_prices": prices,
            "momentum_buy": momentum_buy,
            "momentum_sell": momentum_sell}

def s_update_prices(_params, substep, sH, s, _input):
    new_prices = _input["new_prices"]
    
    return ("prices", new_prices)

def s_arbitrage_trade(_params, substep, sH, s, _input):
    trades = Trades(arbitrage = _input["arbitrage_trade"],
                    momentum_buy = None,
                    momentum_sell = None)
    return ("trades", trades)

def s_momentum_trade(_params, substep, sH, s, _input):
    trades = s["trades"]
    trades.momentum_buy = _input["momentum_buy"]
    trades.momentum_sell = _input["momentum_sell"]
    return ("trades", trades)
    
    