import pandas as pd
from .psub import partial_state_update_block
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment



def load_config(monte_carlo_runs: int, timesteps: int,
                params: dict, initial_state):
    sim_config = config_sim({
        'N': monte_carlo_runs,  # number of monte carlo runs
        'T': range(timesteps),  # number of timesteps
        'M': params             # simulation parameters
    })
    
    exp = Experiment()
    exp.append_configs(
        sim_configs=sim_config,
        initial_state=initial_state,
        partial_state_update_blocks=partial_state_update_block
    )
    return exp
    
    
def run(exp) -> pd.DataFrame:
    """
    Run simulation

    """
    # execute in local mode
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
    print(configs)

    sim = Executor(exec_context=local_mode_ctx, configs=exp.configs)
    raw_system_events, tensor_field, sessions = sim.execute()
    df = pd.DataFrame(raw_system_events)
    return df


def postprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: Refine and extract metrics from the simulation

    Args:
        df (pd.DataFrame): simulation dataframe

    Returns:
        pd.DataFrame: postprocessing result
    """
    return df
