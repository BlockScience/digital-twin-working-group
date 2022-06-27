from .mechanism.pure_returns import p_decode_return_input_backtest, p_decode_return_input_extrapolation,  s_pure_return
from .mechanism.trades import p_arbitrage_trade, s_update_prices, s_arbitrage_trade, p_momentum_trade, s_momentum_trade

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

arbitrage_trade_block = {    'policies': {
            'arbitrage_trade': p_arbitrage_trade
        },
        'variables': {
            'prices': s_update_prices,
            'trades': s_arbitrage_trade
        }}

momentum_trade_block = {    'policies': {
            'arbitrage_trade': p_momentum_trade
        },
        'variables': {
            'prices': s_update_prices,
            'trades': s_momentum_trade
        }}

trading_blocks = [arbitrage_trade_block, momentum_trade_block]

backtest_psub = [price_update_block_backtest] + trading_blocks
extrapolation_psub = [price_update_block_extrapolation] + trading_blocks