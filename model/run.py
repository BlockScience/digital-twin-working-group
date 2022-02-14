import pandas as pd
from model import config
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs


def run() -> pd.DataFrame:
    """
    Run simulation

    """
    # execute in local mode
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    sim = Executor(exec_context=local_mode_ctx, configs=configs)
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
