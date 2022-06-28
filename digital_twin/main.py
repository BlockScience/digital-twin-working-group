from abc import ABC, abstractmethod
from copy import deepcopy

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
    
    def run_backtest(self, monte_carlo_runs: int, params: dict):
        input_data = self.input_data.input_data
        timesteps = len(input_data)
        params = deepcopy(params)
        params["input_data"] =  [input_data]
        initial_state = self.input_data.starting_state
        
        exp = self.backtest_model.load_config(monte_carlo_runs, timesteps,
                                              params, initial_state)
        backtest_data = self.backtest_model.run_model(exp)
        backtest_data = self.backtest_model.post_processing(backtest_data)
        self.backtest_data = backtest_data
    
    def fit_stochastic_fit(self):
        self.stochastic_fit_params = self.stochastic_fit.fit_data(self.input_data,
                                                                  self.historical_data)

    def process_signals(self, params, signals_raw):
        signals = []
        for p, s in zip(params, signals_raw):
            signals.extend(self.signal_extrapolation.process_signal(p, s))
        return signals
    
    def extrapolate_signals(self):
        self.signals_raw = self.signal_extrapolation.extrapolate_signals(self.stochastic_fit_params, self.extrapolation_epochs)
        self.signals = self.process_signals(self.stochastic_fit_params, self.signals_raw)
    
    def run_extrapolation(self, monte_carlo_runs: int, params: dict):
        initial_state = self.input_data.ending_state
        timesteps = self.extrapolation_epochs
        params = deepcopy(params)
        params["input_data"] =  self.signals
        
        exp = self.extrapolation_model.load_config(monte_carlo_runs, timesteps,
                                              params, initial_state)
        extrapolation_data = self.extrapolation_model.run_model(exp)
        extrapolation_data = self.extrapolation_model.post_processing(extrapolation_data)
        self.extrapolation_data = extrapolation_data

    def graph_backtest_difference(self):
        self.reporting_module.graph_backtest_difference(self.historical_data,
                                                        self.backtest_data)

    def mse_backtest_difference(self):
        return self.reporting_module.mse_backtest_difference(self.historical_data,
                                                        self.backtest_data)

    def save_backtest(self):
        self.reporting_module.save_backtest(self.backtest_data)

    def create_backtest_reports(self, backtest_template):
        self.save_backtest()
        self.reporting_module.create_backtest_report(backtest_template)
