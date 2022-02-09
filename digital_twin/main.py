from abc import ABC, abstractmethod

class DigitalTwin(ABC):
    
    def __init__(self,
                 name = None,
                 data_pipeline = None,
                 backtest_model = None,
                 stochastic_fit = None,
                signal_extrapolation = None,
                extrapolation_model = None,
                reporting_module = None,
                extrapolation_epochs = 7):
        self.name = name
        self.extrapolation_epochs = extrapolation_epochs
        
        self.data_pipeline = data_pipeline
        self.backtest_model = backtest_model
        self.stochastic_fit = stochastic_fit
        self.signal_extrapolation = signal_extrapolation
        self.extrapolation_model = extrapolation_model
        self.reporting_module = reporting_module
        
        self.historical_data = None
        self.input_data = None
        self.backtest_data = None
        self.stochastic_fit_params = None
        self.signals = None
        self.extrapolation_data = None
        
    
    @abstractmethod
    def load_data_initial(self):
        pass
    
    @abstractmethod
    def load_data_prior(self):
        pass
    
    @abstractmethod
    def compute_input_data(self):
        pass
    
    @abstractmethod
    def run_backtest(self):
        pass
    
    @abstractmethod
    def fit_stochastic_fit(self):
        pass
    
    @abstractmethod
    def extrapolate_signals(self):
        pass
    
    @abstractmethod
    def run_extrapolation(self):
        pass
    
    @abstractmethod
    def graph_backtest_difference(self):
        pass