from abc import ABC, abstractmethod

class Model(ABC):
    
    @abstractmethod
    def load_config(self, monte_carlo_runs, timesteps,
                    params, initial_state):
        pass
    
    @abstractmethod
    def run_model(self, exp):
        pass
    
    @abstractmethod
    def post_processing(self, backtest_data):
        pass
