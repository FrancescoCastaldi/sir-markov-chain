from __future__ import annotations

import numpy as np
from itertools import product
from typing import Optional
from scipy.stats import binom

# ── Costanti globali ──────────────────────────────────────────────
N: int = 100
BETA: float = 0.2
GAMMA: float = 0.1
I0: int = 5
T_MAX: int = 200
M: int = 1000
SEED: Optional[int] = None  # Se impostato, garantisce riproducibilità

# ── Funzioni di simulazione ──────────────────────────────────────

def next_state(
    s: int,
    i: int,
    r: int,
    n: int = N,
    beta: float = BETA,
    gamma: float = GAMMA,
) -> tuple[int, int, int]:
    """
    Un passo della catena: contagio ~ Binomial(s, β·i/N), guarigione ~ Binomial(i, γ).

    Parametri:
        s: suscettibili correnti
        i: infetti correnti
        r: rimossi correnti
        n: popolazione totale (default: N)
        beta: tasso di trasmissione (default: BETA)
        gamma: tasso di guarigione (default: GAMMA)

    Restituisce:
        (s', i', r') — nuovo stato dopo un passo temporale.
    """
    if i == 0:
        return s, 0, r
    p_si: float = beta * i / n
    new_infections: int = int(np.random.binomial(s, p_si))
    recoveries: int = int(np.random.binomial(i, gamma))
    return s - new_infections, i + new_infections - recoveries, r + recoveries


def transition_matrix(
    n: int,
    beta: float,
    gamma: float,
) -> tuple[np.ndarray, list[tuple[int, int, int]]]:
    """
    Calcola la matrice di transizione P per popolazione N piccola (N ≤ 6).

    Restituisce (P, states) dove P[i,j] = Prob(stato_i → stato_j)
    e states è la lista delle triple (s, i, r).

    Parametri:
        n: popolazione totale
        beta: tasso di trasmissione
        gamma: tasso di guarigione

    Restituisce:
        P: matrice di transizione (n_stati × n_stati)
        states: lista di tuple (s, i, r) che indicizza le righe/colonne
    """
    # Genera tutti gli stati (s,i,r) con s+i+r = n
    states: list[tuple[int, int, int]] = []
    for s, i in product(range(n + 1), repeat=2):
        r = n - s - i
        if r >= 0:
            states.append((s, i, r))

    n_states: int = len(states)
    P: np.ndarray = np.zeros((n_states, n_states))
    state_index: dict[tuple[int, int, int], int] = {
        st: idx for idx, st in enumerate(states)
    }

    for idx, (s, i, r) in enumerate(states):
        if i == 0:
            # Stato assorbente
            P[idx, idx] = 1.0
            continue

        p_si: float = beta * i / n
        for c in range(s + 1):
            p_c: float = binom.pmf(c, s, p_si)
            if p_c == 0:
                continue
            for g in range(i + 1):
                p_g: float = binom.pmf(g, i, gamma)
                if p_g == 0:
                    continue
                sn: int = s - c
                i_n: int = i + c - g
                r_n: int = r + g
                if i_n >= 0 and sn >= 0:
                    jdx: int = state_index[(sn, i_n, r_n)]
                    P[idx, jdx] += p_c * p_g

    return P, states
