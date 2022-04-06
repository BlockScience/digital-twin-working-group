
from numpy import s_

#from model.parts.assets.asset import s_basket_asset, s_index_asset
#from model.parts.traders.momentum import p_momentum_trade, s_momentum_trade
#from .parts.traders.arbitrage import p_arb_trade, s_arb_trade
#from .parts.assets.asset import s_basket_asset, s_index_asset

"""
Partial state update blocks:

1. Rates are randomly drawn to generate prices
2. The arbitraguer decides whether to trade or not
3. The momentum trader decides whether to buy or sell
"""

partial_state_update_block = [
{
        'policies': {
            'test': lambda a,b,c,d: {"A": None}
        },
        'variables': {
            'trades': lambda a,b,c,d,e: ("trades", None)
        }
}
]