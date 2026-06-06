"""
Analisi statistica e confronto con ODE per il modello SIR.

Funzioni:
  - extinction_time()     : tempo di estinzione da una traiettoria
  - compute_stats()       : statistiche descrittive su M simulazioni
  - solve_ode_sir()       : soluzione ODE deterministica (Euler)
  - get_mc_mean_std()     : media e std da risultati MC allineati
"""

from __future__ import annotations

import numpy as np
from typing import Any
from model import M


# ── Statistiche Monte Carlo ──────────────────────────────────────

def extinction_time(traj: np.ndarray) -> int:
    """
    Primo istante t in cui I_t = 0.

    Parametri:
        traj: array di shape (t+1, 3) con colonne [S, I, R]

    Restituisce:
        Indice del primo passo con I=0, oppure len(traj)-1 se mai estinto.
    """
    ext: np.ndarray = np.where(traj[:, 1] == 0)[0]
    return int(ext[0]) if len(ext) > 0 else len(traj) - 1


def compute_stats(results: list[np.ndarray]) -> dict[str, float]:
    """
    Statistiche descrittive su una lista di traiettorie MC.

    Parametri:
        results: lista di array, ciascuno di shape (t_k+1, 3)

    Restituisce:
        Dizionario con media e std di: picco infetti, tempo estinzione, rimossi finali.
    """
    peak: list[float] = [float(np.max(r[:, 1])) for r in results]
    taus: list[int] = [extinction_time(r) for r in results]
    r_inf: list[float] = [float(r[-1, 2]) for r in results]
    return {
        "mean_peak_infected":   np.mean(peak),
        "std_peak_infected":    np.std(peak),
        "mean_extinction_time": np.mean(taus),
        "std_extinction_time":  np.std(taus),
        "max_extinction_time":  np.max(taus),
        "mean_r_inf":           np.mean(r_inf),
        "std_r_inf":            np.std(r_inf),
    }


# ── ODE deterministica (Euler esplicito) ─────────────────────────

def solve_ode_sir(
    n: int,
    beta: float,
    gamma: float,
    i0: int,
    t_max: int,
    dt: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Risolve le ODE del modello SIR con metodo di Eulero esplicito.

    Parametri:
        n: popolazione totale
        beta: tasso di trasmissione
        gamma: tasso di guarigione
        i0: infetti iniziali
        t_max: orizzonte temporale massimo
        dt: passo di integrazione (default: 1.0)

    Restituisce:
        (t_array, s_array, i_array, r_array) — array di shape (steps+1,).
    """
    steps: int = int(t_max / dt)
    s: float = float(n - i0)
    i: float = float(i0)
    r: float = 0.0

    t_vals: np.ndarray = np.zeros(steps + 1)
    s_vals: np.ndarray = np.zeros(steps + 1)
    i_vals: np.ndarray = np.zeros(steps + 1)
    r_vals: np.ndarray = np.zeros(steps + 1)

    t_vals[0], s_vals[0], i_vals[0], r_vals[0] = 0, s, i, r

    for k in range(1, steps + 1):
        ds: float = -beta * s * i / n
        di: float = beta * s * i / n - gamma * i
        dr: float = gamma * i
        s += ds * dt
        i += di * dt
        r += dr * dt
        # Previeni valori negativi per piccoli floating point
        s, i, r = max(s, 0), max(i, 0), max(r, 0)
        t_vals[k] = k * dt
        s_vals[k], i_vals[k], r_vals[k] = s, i, r

    return t_vals, s_vals, i_vals, r_vals


def get_mc_mean_std(
    results: list[np.ndarray],
) -> dict[str, Any]:
    """
    Media e std delle traiettorie MC allineate con padding NaN.

    Parametri:
        results: lista di array, ciascuno di shape (t_k+1, 3)

    Restituisce:
        Dizionario con t, s_mean, s_std, i_mean, i_std, r_mean, r_std.
    """
    from plotting import pad_results
    s_mat, i_mat, r_mat, max_len = pad_results(results)
    return {
        "t": np.arange(max_len),
        "s_mean": np.nanmean(s_mat, axis=0),
        "s_std":  np.nanstd(s_mat, axis=0),
        "i_mean": np.nanmean(i_mat, axis=0),
        "i_std":  np.nanstd(i_mat, axis=0),
        "r_mean": np.nanmean(r_mat, axis=0),
        "r_std":  np.nanstd(r_mat, axis=0),
    }


# ── Entry point ──────────────────────────────────────────────────

if __name__ == "__main__":
    from simulation import run_montecarlo
    results: list[np.ndarray] = run_montecarlo()
    stats: dict[str, float] = compute_stats(results)
    print(f"=== Statistiche su {M} simulazioni ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.2f}")
