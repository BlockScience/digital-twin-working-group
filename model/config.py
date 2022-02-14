from mimetypes import init
from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from .statevars import initial_state
from .sysparams import params
from .psub import psub

MONTE_CARLO_RUNS = 1
TIMESTEPS = 100

sim_config = config_sim({
    'N': MONTE_CARLO_RUNS,  # number of monte carlo runs
    'T': range(TIMESTEPS),  # number of timesteps
    'M': params             # simulation parameters
})

exp = Experiment()
exp.append_configs(
    sim_configs=sim_config,
    initial_state=initial_state,
    partial_state_update_blocks=psub
)
