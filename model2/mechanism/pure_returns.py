from .types import Prices
    
def p_decode_return_input_backtest(_params, substep, sH, s):
    
    t = s["timestep"]
    returns = _params["input_data"].loc[t,"returns"]

    return {"returns": returns}

def p_decode_return_input_extrapolation(_params, substep, sH, s):
    pass


def s_pure_return(_params, substep, sH, s, _input):
    # Grab current prices
    prices = s["prices"]

    returns = _input["returns"]
    
    new_prices = Prices(index_price = (1 + returns.index_return) * prices.index_price,
                        basket_price = (1 + returns.basket_return) * prices.basket_price)

    return ("prices", new_prices)
