"""
Test unitari per il modello SIR.

Copertura:
  - next_state: conservazione, stato assorbente, non-negatività
  - transition_matrix: stocasticità, assorbimento, non-negatività, shape
  - run_single: shape, estinzione, β=0, γ=1
"""

from __future__ import annotations

import sys
sys.path.insert(0, "../src")
import numpy as np
from model import next_state, transition_matrix


# ── Test per next_state ──────────────────────────────────────────

def test_conservation() -> None:
    """S + I + R == N per ogni passo."""
    for _ in range(100):
        s, i = int(np.random.randint(1, 50)), int(np.random.randint(1, 20))
        r = 100 - s - i
        sn, in_, rn = next_state(s, i, r)
        assert sn + in_ + rn == 100, "Violazione conservazione N"


def test_absorbing_state() -> None:
    """Se I = 0, il sistema rimane in I = 0."""
    s, i, r = 60, 0, 40
    sn, in_, rn = next_state(s, i, r)
    assert in_ == 0, "I=0 non è assorbente"


def test_non_negative() -> None:
    """Nessun compartimento può diventare negativo."""
    for _ in range(100):
        s, i = int(np.random.randint(1, 50)), int(np.random.randint(1, 20))
        r = 100 - s - i
        sn, in_, rn = next_state(s, i, r)
        assert sn >= 0 and in_ >= 0 and rn >= 0, \
            f"Valori negativi: ({sn}, {in_}, {rn})"


def test_absorbing_all_seeds() -> None:
    """Se I=0, next_state ritorna sempre lo stesso stato."""
    for _ in range(20):
        s = int(np.random.randint(0, 100))
        r = 100 - s
        sn, in_, rn = next_state(s, 0, r)
        assert sn == s and in_ == 0 and rn == r


# ── Test per transition_matrix ──────────────────────────────────

def test_transition_matrix_stochastic() -> None:
    """Ogni riga di P deve sommare a 1 (matrice stocastica)."""
    for n in range(1, 6):
        P, states = transition_matrix(n, beta=0.5, gamma=0.3)
        row_sums: np.ndarray = P.sum(axis=1)
        assert np.allclose(row_sums, 1.0, atol=1e-10), \
            f"N={n}: righe non stocastiche, somma = {row_sums}"


def test_transition_matrix_absorbing() -> None:
    """Stati con I=0 devono avere P[i,i] = 1."""
    for n in range(1, 6):
        P, states = transition_matrix(n, beta=0.5, gamma=0.3)
        for idx, (s, i, r) in enumerate(states):
            if i == 0:
                assert P[idx, idx] == 1.0, \
                    f"Stato ({s},{i},{r}) non assorbente in N={n}"


def test_transition_matrix_non_negative() -> None:
    """Tutti gli elementi di P devono essere >= 0."""
    for n in range(1, 6):
        P, states = transition_matrix(n, beta=0.5, gamma=0.3)
        assert np.all(P >= 0), f"N={n}: elementi negativi in P"


def test_transition_matrix_shape() -> None:
    """P deve avere dimensione (n_states, n_states)."""
    for n in range(1, 6):
        P, states = transition_matrix(n, beta=0.5, gamma=0.3)
        n_states: int = len(states)
        assert P.shape == (n_states, n_states), \
            f"N={n}: shape {P.shape} != ({n_states}, {n_states})"


# ── Test per run_single (da simulation) ──────────────────────────

def test_run_single_shape() -> None:
    """run_single deve restituire array shape (t+1, 3) con t almeno 1."""
    from simulation import run_single
    traj: np.ndarray = run_single(n=10, i0=2, t_max=50, beta=0.5, gamma=0.3)
    assert traj.ndim == 2, "run_single non restituisce array 2D"
    assert traj.shape[1] == 3, "run_single non restituisce 3 colonne"
    assert traj.shape[0] >= 2, "run_single troppo corta"


def test_run_single_stops_at_extinction() -> None:
    """run_single deve fermarsi quando I=0."""
    from simulation import run_single
    np.random.seed(42)
    traj: np.ndarray = run_single(n=10, i0=1, t_max=200, beta=0.1, gamma=0.5)
    assert traj[-1, 1] == 0, "L'ultimo I deve essere 0 (estinzione)"


def test_run_single_zero_beta() -> None:
    """Con β=0, nessun contagio: I deve scendere a 0 per sole guarigioni."""
    from simulation import run_single
    np.random.seed(42)
    traj: np.ndarray = run_single(n=100, i0=10, t_max=50, beta=0.0, gamma=0.5)
    assert traj[-1, 1] == 0, "Con β=0 l'infezione deve estinguersi"
    assert traj[-1, 0] == 100 - traj[-1, 2], "Tutti i guariti vengono dai primi infetti"


def test_run_single_gamma_one() -> None:
    """Con γ=1, l'infezione si estingue entro 2 passi (contagio prima di guarigione)."""
    from simulation import run_single
    np.random.seed(42)
    traj: np.ndarray = run_single(n=100, i0=5, t_max=50, beta=0.3, gamma=1.0)
    # Con γ=1, al passo 1: Binomial(i0, 1) = i0 guarigioni, ma ci possono essere nuovi contagi
    # La catena si estingue quando i nuovi contagi + guarigioni portano I a 0
    assert traj[-1, 1] == 0, "Con γ=1 la catena deve estinguersi"
    assert traj.shape[0] <= 3, f"Con γ=1 la catena deve estinguersi in ≤3 passi, ne ha {traj.shape[0]}"


# ── Esecuzione diretta ───────────────────────────────────────────

if __name__ == "__main__":
    np.random.seed(0)
    test_conservation()
    test_absorbing_state()
    test_non_negative()
    test_absorbing_all_seeds()
    test_transition_matrix_stochastic()
    test_transition_matrix_absorbing()
    test_transition_matrix_non_negative()
    test_transition_matrix_shape()
    test_run_single_shape()
    test_run_single_stops_at_extinction()
    test_run_single_zero_beta()
    test_run_single_gamma_one()
    print("Tutti i test passati.")
