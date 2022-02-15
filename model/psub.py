from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE

from numpy import s_

from model.parts.assets.asset import s_basket_asset, s_index_asset
from model.parts.traders.momentum import p_momentum_trade, s_momentum_trade
from .parts.traders.arbitrage import p_arb_trade, s_arb_trade
from .parts.assets.asset import s_basket_asset, s_index_asset

"""
Partial state update blocks

The PSUBs are configured here by assigning the policies and state variables
to be calculated and updated in each block.
"""

partial_state_update_block = [
    {
        'policies': {
        },
        'variables': {
            # TODO: should these be separate?
            'basket': s_basket_asset,
            'index': s_index_asset
        }
    },
    {
        'policies': {
            'arb_trade': p_arb_trade
        },
        'variables': {
            'index': s_arb_trade
        }
    },
    {
        'policies': {
            'momentum_trade': p_momentum_trade
        },
        'variables': {
            'index': s_momentum_trade
        }
    }
]

]
