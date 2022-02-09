from abc import ABC, abstractmethod

class DataPipeline(ABC):
    @abstractmethod
    def pull_historical_data(self):
        pass
    
    @abstractmethod
    def compute_input_data(self, data):
        pass
    
    @abstractmethod
    def format_input_data(self, data):
        pass