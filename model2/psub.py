from .mechanism.pure_returns import p_decode_return_input_backtest, p_decode_return_input_extrapolation,  s_pure_return


price_update_block_backtest = {
        'policies': {
            'returns': p_decode_return_input_backtest
        },
        'variables': {
            'prices': s_pure_return
        }
}

price_update_block_extrapolation = {
    'policies': {
            'returns': p_decode_return_input_extrapolation
        },
        'variables': {
            'prices': s_pure_return
        }
}

backtest_psub = [price_update_block_backtest]
extrapolation_psub = [price_update_block_extrapolation]