import numpy as np
from itertools import product

# ── Costanti globali ──────────────────────────────────────────────
N = 100
BETA = 0.2
GAMMA = 0.1
I0 = 5
T_MAX = 200
M = 1000
SEED = None  # Se impostato, garantisce riproducibilità

# ── Funzioni di simulazione ──────────────────────────────────────

def next_state(s, i, r, n=N, beta=BETA, gamma=GAMMA):
    """Un passo della catena: contagio ~ Binomial(s, β·i/N), guarigione ~ Binomial(i, γ)."""
    if i == 0:
        return s, 0, r
    p_si = beta * i / n
    new_infections = np.random.binomial(s, p_si)
    recoveries = np.random.binomial(i, gamma)
    return s - new_infections, i + new_infections - recoveries, r + recoveries


def transition_matrix(n, beta, gamma):
    """
    Calcola la matrice di transizione P per popolazione N piccola (N ≤ 6).
    Restituisce (P, states) dove P[i,j] = prob(stato_i → stato_j)
    e states è la lista delle triple (s,i,r).
    """
    # Genera tutti gli stati (s,i,r) con s+i+r = n
    states = []
    for s, i in product(range(n + 1), repeat=2):
        r = n - s - i
        if r >= 0:
            states.append((s, i, r))

    n_states = len(states)
    P = np.zeros((n_states, n_states))
    state_index = {st: idx for idx, st in enumerate(states)}

    for idx, (s, i, r) in enumerate(states):
        if i == 0:
            # Stato assorbente
            P[idx, idx] = 1.0
            continue

        p_si = beta * i / n
        # Pre-calcola tutte le probabilità Binomiali
        max_c = min(s, n)  # massimi contagi possibili
        # Proba di avere c contagi
        for c in range(s + 1):
            p_c = np.random.binomial.pmf(c, s, p_si)
            if p_c == 0:
                continue
            # Proba di avere g guarigioni
            for g in range(i + 1):
                p_g = np.random.binomial.pmf(g, i, gamma)
                if p_g == 0:
                    continue
                sn = s - c
                i_n = i + c - g
                r_n = r + g
                if i_n >= 0 and sn >= 0:
                    jdx = state_index[(sn, i_n, r_n)]
                    P[idx, jdx] += p_c * p_g

    return P, states
