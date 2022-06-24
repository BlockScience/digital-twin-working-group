from dataclasses import dataclass

trade_action = bool

@dataclass
class Trades():
    arbitrage: trade_action
    momentum_buy: trade_action
    momentum_sell: trade_action
