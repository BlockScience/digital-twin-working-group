import pandas as pd
from .psub import backtest_psub
from .types import model_starting_state
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment



def load_config_backtest(monte_carlo_runs: int, timesteps: int,
                params: dict, initial_state: model_starting_state) -> Experiment:
    """
    Loads the configuration for a backtest

    Parameters
    ----------
    monte_carlo_runs : int
        The number of monte carlo runs to run
    timesteps : int
        The number of timesteps to run
    params : dict
        The parameters of the backtest
    initial_state : starting_state
        The initial state

    Returns
    -------
    Experiment
        A cadCAD experiment

    """
    
    #Load simulation config
    sim_config = config_sim({
        'N': monte_carlo_runs,  # number of monte carlo runs
        'T': range(timesteps),  # number of timesteps
        'M': params             # simulation parameters
    })
    
    #Create experiment
    exp = Experiment()
    exp.append_configs(
        sim_configs=sim_config,
        initial_state=initial_state,
        partial_state_update_blocks=backtest_psub
    )
    
    return exp
    

