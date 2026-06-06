"""
Analisi statistica e confronto con ODE per il modello SIR.

Funzioni:
  - extinction_time()     : tempo di estinzione da una traiettoria
  - compute_stats()       : statistiche descrittive su M simulazioni
  - solve_ode_sir()       : soluzione ODE deterministica (Euler)
  - get_mc_mean_std()     : media e std da risultati MC allineati
"""

import numpy as np
from src.simulation import run_montecarlo, M


# ── Statistiche Monte Carlo ──────────────────────────────────────

def extinction_time(traj):
    """Primo istante t in cui I_t = 0."""
    ext = np.where(traj[:, 1] == 0)[0]
    return int(ext[0]) if len(ext) > 0 else len(traj) - 1


def compute_stats(results):
    """Statistiche descrittive su una lista di traiettorie."""
    peak = [np.max(r[:, 1]) for r in results]
    taus = [extinction_time(r) for r in results]
    r_inf = [r[-1, 2] for r in results]
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

def solve_ode_sir(n, beta, gamma, i0, t_max, dt=1.0):
    """
    Risolve le ODE del modello SIR con metodo di Eulero esplicito.

    Parametri:
      n, beta, gamma, i0, t_max  — come per la simulazione MC
      dt                         — passo di integrazione (default: 1.0)

    Restituisce (t_array, s_array, i_array, r_array).
    """
    steps = int(t_max / dt)
    s = float(n - i0)
    i = float(i0)
    r = 0.0

    t_vals = np.zeros(steps + 1)
    s_vals = np.zeros(steps + 1)
    i_vals = np.zeros(steps + 1)
    r_vals = np.zeros(steps + 1)

    t_vals[0], s_vals[0], i_vals[0], r_vals[0] = 0, s, i, r

    for k in range(1, steps + 1):
        ds = -beta * s * i / n
        di = beta * s * i / n - gamma * i
        dr = gamma * i
        s += ds * dt
        i += di * dt
        r += dr * dt
        # Previeni valori negativi per piccoli floating point
        s, i, r = max(s, 0), max(i, 0), max(r, 0)
        t_vals[k] = k * dt
        s_vals[k], i_vals[k], r_vals[k] = s, i, r

    return t_vals, s_vals, i_vals, r_vals


def get_mc_mean_std(results):
    """Media e std delle traiettorie MC allineate con padding NaN."""
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
    results = run_montecarlo()
    stats = compute_stats(results)
    print(f"=== Statistiche su {M} simulazioni ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.2f}")
