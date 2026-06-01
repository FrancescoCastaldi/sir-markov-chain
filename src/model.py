import numpy as np

N = 100
BETA = 0.2
GAMMA = 0.1
I0 = 5
T_MAX = 200
M = 1000

def next_state(s, i, r, n=N, beta=BETA, gamma=GAMMA):
    if i == 0:
        return s, 0, r
    p_si = beta * i / n
    new_infections = np.random.binomial(s, p_si)
    recoveries = np.random.binomial(i, gamma)
    return s - new_infections, i + new_infections - recoveries, r + recoveries
