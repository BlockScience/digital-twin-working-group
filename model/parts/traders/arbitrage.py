import dataclasses
from re import I
from ..assets import Asset


@dataclasses
class Arbitraguer:
    """ dataclass representing the arbitrage trader """
    theta: float

    def __init__(self, theta: float) -> None:
        """
        Constructor for arbitrage trader

        Args:
            theta (float): Threshold for arbitrage
        """
        self.theta = theta


def arb_check(arb: Arbitraguer, basket: Asset, index: Asset) -> bool:
    """
    Check if the arbitrage trader should make a trade

    Args:
        arb (arb_trader): The arbitrage trader

    Returns:
        bool: Whether the trader should make a trade
    """
    return abs(basket.p - index.p) > arb.theta


def arb_trade(trade: bool, basket: Asset, index: Asset) -> Asset:
    """
    The arbitraguer trade action

    Args:
        trade (bool): _description_
        basket (Asset): _description_
        index (Asset): _description_

    Returns:
        Asset: _description_
    """
    return basket if trade else index


def p_arb_trade(params, substep, state_history, prev_state, policy_input) -> dict[str, bool]:
    """
    Policy function for whether the arbitraguer trades

    Args:
        params (_type_): _description_
        substep (_type_): _description_
        state_history (_type_): _description_
        prev_state (_type_): _description_
        policy_input (_type_): _description_

    Returns:
        dict[str, bool]: _description_
    """
    y = 'arb_trade'
    return {y: arb_check(params['arb'], prev_state['basket'], prev_state['index'])}


def s_arb_trade(params, substep, state_history, prev_state, policy_input) -> tuple[str, Asset]:
    """
    State update function for arbitraguer price action

    Args:
        params (_type_): _description_
        substep (_type_): _description_
        state_history (_type_): _description_
        prev_state (_type_): _description_
        policy_input (_type_): _description_

    Returns:
        tuple[str, Asset]: _description_
    """
    y = 'index'
    x = arb_trade(policy_input['arb_trade'],
                  prev_state['basket'], prev_state['index'])
    return (y, x)
