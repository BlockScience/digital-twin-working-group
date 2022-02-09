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
    
    def compute_input_data(self):
        self.input_data_raw = self.data_pipeline.compute_input_data(self.historical_data)
        self.input_data = self.data_pipeline.format_input_data(self.input_data_raw)
    
    def run_backtest(self):
        backtest_data = self.backtest_model.run_model(self.input_data)
        backtest_data = self.backtest_model.post_processing(backtest_data)
        self.backtest_data = backtest_data
    
    def fit_stochastic_fit(self):
        self.stochastic_fit_params = self.stochastic_fit.fit_data(self.input_data)
    
    def extrapolate_signals(self):
        self.signals = self.signal_extrapolation.extrapolate_signals(self.stochastic_fit_params, self.extrapolation_epochs)
    
    def run_extrapolation(self):
        extrapolation_data = self.extrapolation_model.run_model(self.signals, self.historical_data)
        extrapolation_data = self.extrapolation_model.post_processing(extrapolation_data)
        self.extrapolation_data = extrapolation_data
    