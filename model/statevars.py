import numpy as np
from typing import Annotated
from .sysparams import params
from .parts import rates

p_basket: float = 100
p_index: float = 100

r_basket: float = rates.basket_rate(
    params['mu_basket'], params['sigma_basket'])
r_index: float = rates.index_rate(
    r_basket, params['lambda_index'], params['mu_index'], params['sigma_index'])

"""
Genesis state for state variables
"""
initial_state = {
    'p_basket': p_basket,
    'p_index': p_index,
    'r_basket': r_basket,
    'r_index': r_index
}
