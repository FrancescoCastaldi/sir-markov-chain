import numpy as np

N = 100
BETA = 0.3
GAMMA = 0.1

def transition_probs(s, i, n=N, beta=BETA, gamma=GAMMA):
    p_new_infection = beta * i / n
    p_si = min(p_new_infection * s, s) / s if s > 0 else 0
    p_ir = gamma
    return p_si, p_ir

def next_state(s, i, r, n=N, beta=BETA, gamma=GAMMA):
    if i == 0:
        return s, 0, r
    p_si, p_ir = transition_probs(s, i, n, beta, gamma)
    new_infections = np.random.binomial(s, p_si)
    recoveries = np.random.binomial(i, p_ir)
    s_new = s - new_infections
    i_new = i + new_infections - recoveries
    r_new = r + recoveries
    return s_new, i_new, r_new
