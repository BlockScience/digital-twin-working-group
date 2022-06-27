from model2.types import Trades, trade_action

def p_arbitrage_trade(_params, substep, sH, s):
    #Current prices
    prices = s["prices"]
    arbitrage_trade = False
    
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