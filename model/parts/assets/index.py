import numpy as np
from .asset import Asset, Price, Rate


def index_rate(r_b: float, lambda1: float, mu: float, sigma: float) -> Rate:
    """
    Calculate r_i = lambda1 * r_b + (1-lambda1)*Normal(mu, sigma^2)

    Args:
        lambda1 (float): Weight of basket's effect on index price
        mu (float): Mean of Normal distribution from which the rate is sampled
        sigma (float): Standard deviation of Normal distribution from which the rate is sampled.

    Returns:
        Rate: Basket rate of return
    """
    return lambda1 * r_b + (1 - lambda1) * np.random.normal(mu, sigma)


def s_index_asset(params, substep, state_history, prev_state, policy_input) -> tuple[str, Asset]:
    """
    State update function for index asset

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
    # generate next period rate
    # TODO: how to access state from substep?
    basket: Asset = state_history[substep - 1]['basket']
    r: Rate = index_rate(
        basket.r, params['lambda_index'], params['mu_index'], params['sigma_index'])
    # calculate next period price
    p: Price = prev_state['index'].p * (1 + r)
    return (y, Asset(p, r))
