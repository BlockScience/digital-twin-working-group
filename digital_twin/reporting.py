from abc import ABC, abstractmethod
import os
from pathlib import Path
import papermill as pm

class ReportingModule(ABC):
    
    @abstractmethod
    def graph_backtest_difference(self, historical_data, backtest_data):
        pass
    
    @abstractmethod
    def mse_backtest_difference(self, historical_data, backtest_data):
        pass

    @abstractmethod
    def save_backtest(self, backtest_data):
        pass
    
    def create_backtest_report(self, backtest_template):
        runtime = "TEST"
        working_path = Path(".")
        path = "."
        input_nb_path = (
            working_path / backtest_template).expanduser()
        output_nb_path = (
            working_path / f'reports/{runtime}-Backtest.ipynb').expanduser()
        output_html_path = (
            working_path / f'reports/{runtime}-Backtest.html').expanduser()
        pm.execute_notebook(
            input_nb_path,
            output_nb_path,
            parameters=dict(base_path=path))
        export_cmd = f"jupyter nbconvert --to html '{output_nb_path}'"
        os.system(export_cmd)
        os.system(f"rm '{output_nb_path}'")
