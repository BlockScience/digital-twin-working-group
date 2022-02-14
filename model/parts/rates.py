def basket_rate(mu: float, sigma: float) -> float:
    """
    Calculate r_b = N(mu, sigma^2)

    Args:
        mu (float): Mean of Normal distribution from which the rate is sampled
        sigma (float): Standard deviation of Normal distribution from which the rate is sampled.

    Returns:
        float: Basket rate of return
    """
    return np.random.normal(mu, sigma)


def index_rate(r_b: float, lambda1: float, mu: float, sigma: float) -> float:
    """
    Calculate r_i = lambda1 * r_b + (1-lambda1)*Normal(mu, sigma^2)

    Args:
        lambda1 (float): Weight of basket's effect on index price
        mu (float): Mean of Normal distribution from which the rate is sampled
        sigma (float): Standard deviation of Normal distribution from which the rate is sampled.

    Returns:
        float: Basket rate of return
    """
    return lambda1 * r_b + (1 - lambda1) * np.random.normal(mu, sigma)
