from abc import ABC, abstractmethod

class SignalExtrapolation(ABC):
    
    @abstractmethod
    def extrapolate_signals(self, stochastic_params, t, n):
        pass

    @abstractmethod
    def process_signal(self, param, signal_raw):
        pass
