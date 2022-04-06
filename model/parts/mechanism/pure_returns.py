from dataclasses import dataclass
share_price = float
@dataclass
class Prices():
    index_price: share_price
    basket_price: share_price
    
    
def p_decode_return_input(_params, substep, sH, s):
    t = s["timestep"]
    
    returns = _params["input_data"].loc[t,"returns"]

    return {"returns": returns}


def s_pure_return(_params, substep, sH, s, _input):
    # Grab current prices
    prices = s["prices"]

    returns = _input["returns"]
    
    new_prices = Prices(index_price = (1 + returns.index_return) * prices.index_price,
                        basket_price = (1 + returns.basket_return) * prices.basket_price)

    return ("prices", new_prices)