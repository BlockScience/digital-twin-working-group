import numpy as np
from .asset import Asset, Price, Rate


def basket_rate(mu: float, sigma: float) -> Rate:
    """
    Calculate r_b = N(mu, sigma^2)

    Args:
        mu (float): Mean of Normal distribution from which the rate is sampled
        sigma (float): Standard deviation of Normal distribution from which the rate is sampled.

    Returns:
        Rate: Basket rate of return
    """
    return np.random.normal(mu, sigma)


def s_basket_asset(params, substep, state_history, prev_state, policy_input) -> tuple[str, Asset]:
    """
    State update function for basket asset

    Args:
        params (_type_): _description_
        substep (_type_): _description_
        state_history (_type_): _description_
        prev_state (_type_): _description_
        policy_input (_type_): _description_

    Returns:
        tuple[str, Asset]: _description_
    """
    y = 'basket'
    # generate next period rate
    r: Rate = basket_rate(params['mu_basket'], params['mu_sigma'])
    # calculate next period price
    p: Price = prev_state['basket'].p * (1 + r)
    return (y, Asset(p, r))
