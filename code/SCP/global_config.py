import torch

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DTYPE = torch.float32


P_CAUSE_CAUSE = 0.3
SAMPLE_SIZE = 5000
N_CAUSE = 10
N_CONFOUNDER = 20
P_CONFOUNDER_CAUSE = 0.3
CAUSE_NOISE = 0.01
OUTCOME_NOISE = 0.01
OUTCOME_INTERACTION = True
P_OUTCOME_DOUBLE = 0.05
P_OUTCOME_SINGLE = 0.3
CONFOUNDING_LEVEL = 3