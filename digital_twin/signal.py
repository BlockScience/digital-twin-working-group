from abc import ABC, abstractmethod

class SignalExtrapolation(ABC):
    
    @abstractmethod
    def extrapolate_signals(self, stochastic_params, t, n):
        pass
