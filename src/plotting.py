"""
Funzioni di plotting per il modello SIR.
Separate da simulation.py per modularità.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Costante: cartella di output per le figure della relazione
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img")


# ── Helper ───────────────────────────────────────────────────────

def pad_results(results):
    """Allinea traiettorie di lunghezza diversa riempiendo con NaN."""
    max_len = max(len(r) for r in results)

    def pad_col(col):
        mat = np.full((len(results), max_len), np.nan)
        for k, traj in enumerate(results):
            mat[k, :len(traj)] = traj[:, col]
        return mat

    return pad_col(0), pad_col(1), pad_col(2), max_len


# ── Plot principali ──────────────────────────────────────────────

def plot_single_trajectory(traj, save_path=None):
    """Singola traiettoria SIR (S, I, R nel tempo)."""
    if save_path is None:
        save_path = os.path.join(IMG_DIR, "single_trajectory.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    steps = range(len(traj))
    plt.figure(figsize=(9, 4))
    plt.plot(steps, traj[:, 0], label="S (Suscettibili)", color="steelblue")
    plt.plot(steps, traj[:, 1], label="I (Infetti)", color="firebrick")
    plt.plot(steps, traj[:, 2], label="R (Rimossi)", color="seagreen")
    plt.xlabel("Passo temporale $t$")
    plt.ylabel("Individui")
    plt.title("Evoluzione SIR — singola traiettoria")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()


def plot_mean_trajectory(results, save_path=None):
    """Traiettoria media ± 1 deviazione standard su M simulazioni."""
    if save_path is None:
        save_path = os.path.join(IMG_DIR, "mean_trajectory.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    s_mat, i_mat, r_mat, max_len = pad_results(results)
    steps = range(max_len)

    plt.figure(figsize=(9, 4))
    for mat, color, label in [
        (s_mat, "steelblue", "S"),
        (i_mat, "firebrick", "I"),
        (r_mat, "seagreen", "R"),
    ]:
        mean = np.nanmean(mat, axis=0)
        std = np.nanstd(mat, axis=0)
        plt.plot(steps, mean, color=color, label=f"E[{label}]")
        plt.fill_between(steps, mean - std, mean + std, color=color, alpha=0.15)

    plt.xlabel("Passo temporale $t$")
    plt.ylabel("Individui")
    plt.title(f"Traiettorie medie ± 1 std — {len(results)} simulazioni MC")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()


def plot_tau_histogram(results, save_path=None):
    """Istogramma del tempo di estinzione τ."""
    if save_path is None:
        save_path = os.path.join(IMG_DIR, "tau_histogram.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Calcola i tempi di estinzione
    from analysis import extinction_time
    taus = [extinction_time(r) for r in results]

    plt.figure(figsize=(8, 4))
    plt.hist(taus, bins=30, color="slateblue", edgecolor="white")
    plt.axvline(np.mean(taus), color="darkred", linestyle="--",
                label=f"Media τ = {np.mean(taus):.1f}")
    plt.xlabel("Tempo di estinzione $\\tau$")
    plt.ylabel("Frequenza")
    plt.title("Distribuzione empirica del tempo di estinzione")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    return taus


# ── Plot aggiuntivi ──────────────────────────────────────────────

def plot_sensitivity_comparison(scenario_results, save_path=None):
    """
    Confronto di scenari: β e γ diversi.
    scenario_results = [(label, mean_I_array, color), ...]
    """
    if save_path is None:
        save_path = os.path.join(IMG_DIR, "sensitivity_comparison.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.figure(figsize=(10, 4))
    for label, mean_i, color in scenario_results:
        plt.plot(range(len(mean_i)), mean_i, color=color, label=label, alpha=0.8)

    plt.xlabel("Passo temporale $t$")
    plt.ylabel("Infetti medi E[I]")
    plt.title("Confronto scenari: effetto di β e γ")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()


def plot_ode_comparison(t_mc, mean_i_mc, std_i_mc, t_ode, i_ode, save_path=None):
    """Confronto tra media Monte Carlo e soluzione ODE per gli infetti."""
    if save_path is None:
        save_path = os.path.join(IMG_DIR, "ode_comparison.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.figure(figsize=(9, 4))
    plt.plot(t_mc, mean_i_mc, color="firebrick", label="MC media E[I]")
    plt.fill_between(t_mc,
                     np.maximum(mean_i_mc - std_i_mc, 0),
                     mean_i_mc + std_i_mc,
                     color="firebrick", alpha=0.12, label="MC ± 1 std")
    plt.plot(t_ode, i_ode, color="black", linestyle="--", linewidth=2,
             label="ODE deterministica")
    plt.xlabel("Passo temporale $t$")
    plt.ylabel("Infetti I")
    plt.title("Confronto: simulazione stocastica vs ODE deterministica")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
