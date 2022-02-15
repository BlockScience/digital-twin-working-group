from dataclasses import dataclass

"""
Price type alias for float
"""
Price = float


"""
Rate type alias for float
"""
Rate = float


@dataclass
class Asset():
    p: Price
    r: Rate

    def __init__(self, p: Price, r: Rate) -> None:
        """
        Construct an Asset from a Price and Rate

        Args:
            p (Price): Current price of the asset
            r (Rate): Rate of asset's growth
        """
        self.p = p
        self.r = r
