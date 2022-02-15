""" mu param for basket Normal RV """
from model.parts.traders.arbitrage import Arbitrageur
from model.parts.traders.momentum import Momentum


mu_basket: float = .1
""" sigma param for basket Normal RV """
sigma_basket: float = .05
""" lambda param for index """
lambda_index: float = .9
""" mu param for index Normal RV """
mu_index: float = .0
""" sigma param for index Normal RV """
sigma_index: float = 1
""" theta param for arbitrage trader """
theta_arb: float = 10
""" lookback param for momentum trader """
lookback: int = 5
""" theta param for momentum trader """
theta_momentum: float = .1
""" price impact of momentum trader """
impact = .005

"""
Model paramaters
"""
params = {
    'mu_basket': mu_basket,
    'sigma_basket': sigma_basket,
    'lambda_index': lambda_index,
    'mu_index': mu_index,
    'sigma_index': sigma_index,
    'arb': Arbitrageur(theta_arb),
    'momentum': Momentum(lookback, mu_basket, theta_momentum, impact)
}
