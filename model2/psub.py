from .mechanism.pure_returns import p_decode_return_input_backtest, s_pure_return


price_update_block_backtest = {
        'policies': {
            'returns': p_decode_return_input_backtest
        },
        'variables': {
            'prices': s_pure_return
        }
}

backtest_psub = [price_update_block_backtest]