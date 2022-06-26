from abc import ABC, abstractmethod

class StochasticFit(ABC):
    
    def __init__(self, params):
        self.params = params
        
    def fit_data(self, input_data, historical_data):
        # Go through each param and get the stochastic fit
        for param in self.params:
            self.fit_param(param, input_data, historical_data)
        
    @abstractmethod
    def fit_param(self, param, input_data, historical_data):
        pass
