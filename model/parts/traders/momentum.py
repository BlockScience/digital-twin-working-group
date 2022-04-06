import numpy as np
from dataclasses import dataclass
from ..assets.asset import Asset


@dataclass
class Momentum:
    """ dataclass representing the momentum trader """
    lookback: int
    mu: float
    theta: float
    impact: float

    """ constructor """

    def __init__(self, lookback: int, mu: float, theta: float, impact: float) -> None:
        self.lookback = lookback
        self.mu = mu
        self.theta = theta
        self.impact = impact


def momentum_check(momentum: Momentum, historical: Asset) -> bool:
    """
    Check if the momentum trader should make a trade

    Args:
        momentum (Momentum): _description_
        historical (Asset): _description_

    Returns:
        bool: _description_
    """
    period_return = (momentum.index.p / historical.p) - \
        1 - (momentum.mu * momentum.lookback)
    return abs(period_return) > momentum.theta


def momentum_trade(buy: bool, momentum: Momentum, index: Asset) -> Asset:
    """
    Momentum trader trade action

    Args:
        buy (bool): _description_
        momentum (Momentum): _description_
        index (Asset): _description_

    Returns:
        Asset: _description_
    """
    return index.p * (1 + momentum.impact) if buy else index.p * (1 - momentum.impact)


def p_momentum_trade(params, substep, state_history, prev_state, policy_input) -> dict[str, bool]:
    """
    Policy function for whether the momentum trader trades

    Args:
        params (_type_): _description_
        substep (_type_): _description_
        state_history (_type_): _description_
        prev_state (_type_): _description_
        policy_input (_type_): _description_

    Returns:
        dict[str, bool]: _description_
    """
    policy = 'momentum_trade'
    # get current timestep
    curr_time: int = prev_state['timestep'] if substep != 1 else prev_state['timestep'] + 1
    # get historical price
    lookback: int = max(curr_time - params['momentum'].lookback + 1, 0)
    historical: Asset = state_history[lookback]['index']

    return {policy: momentum_check(params['momentum'], historical)}


def s_momentum_trade(params, substep, state_history, prev_state, policy_input) -> tuple[str, Asset]:
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
    x = momentum_trade(
        policy_input['momentum_trade'], params['momentum'], prev_state['index'])
    return (y, x)
