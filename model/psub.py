from model.parts.mechanism.pure_returns import p_decode_return_input, s_pure_return
"""
Partial state update blocks:

1. Rates are randomly drawn to generate prices
2. The arbitraguer decides whether to trade or not
3. The momentum trader decides whether to buy or sell
"""

partial_state_update_block = [
{
        'policies': {
            'returns': p_decode_return_input
        },
        'variables': {
            'prices': s_pure_return
        }
}
]