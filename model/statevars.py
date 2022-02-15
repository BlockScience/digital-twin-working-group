from model.parts.traders import arbitrage
from .sysparams import params
from .parts.assets import rates, asset

p_basket: asset.Price = 100
p_index: asset.Price = 100

r_basket: asset.Rate = rates.basket_rate(
    params['mu_basket'], params['sigma_basket'])
r_index: asset.Rate = rates.index_rate(
    r_basket, params['lambda_index'], params['mu_index'], params['sigma_index'])

"""
Genesis state for state variables
"""
initial_state = {
    'basket': asset.Asset(p_basket, r_basket),
    'index': asset.Asset(p_index, r_index),
}
