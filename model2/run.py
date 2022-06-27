import pandas as pd
from .psub import backtest_psub, extrapolation_psub
from .types import model_starting_state, raw_results, processed_results
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from pandas import DataFrame


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

def load_config_extrapolation(monte_carlo_runs: int, timesteps: int,
                params: dict, initial_state: model_starting_state) -> Experiment:
    """
    Loads the configuration for extrapolation

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
        partial_state_update_blocks=extrapolation_psub
    )
    
    return exp

def run(exp: Experiment) -> raw_results:
    """
    Run a cadCAD simulation

    Parameters
    ----------
    exp : Experiment
        The experiment to run

    Returns
    -------
    DataFrame
        The results dataframe

    """
    
    # execute in local mode
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
    
    #Run the simulation and convert to DataFrame
    sim = Executor(exec_context=local_mode_ctx, configs=exp.configs)
    raw_system_events, tensor_field, sessions = sim.execute()
    df = pd.DataFrame(raw_system_events)
    
    return df

def post_processing(df: raw_results) -> processed_results:
    """
    Post processes the results for cadCAD runs

    Parameters
    ----------
    df : raw_results
        Raw results from cadCAD run

    Returns
    -------
    processed_results
        Processed results

    """
    
    return df
