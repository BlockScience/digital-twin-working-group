from abc import ABC, abstractmethod

class ReportingModule(ABC):
    
    @abstractmethod
    def graph_backtest_difference(self, historical_data, backtest_data):
        pass
    
    @abstractmethod
    def mse_backtest_difference(self, historical_data, backtest_data):
        pass
    
    def create_backtest_report(self, historical_data, backtest_data):
        pass
