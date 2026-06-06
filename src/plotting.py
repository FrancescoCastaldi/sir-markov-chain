"""
Funzioni di plotting per il modello SIR.
Separate da simulation.py per modularità.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import os
from typing import Optional, Any

# Costante: cartella di output per le figure della relazione
IMG_DIR: str = os.path.join(os.path.dirname(__file__), "..", "img")


# ── Helper ───────────────────────────────────────────────────────

def pad_results(
    results: list[np.ndarray],
) -> tuple[np.ndarray, np.ndarray, np.ndarray, int]:
    """
    Allinea traiettorie di lunghezza diversa riempiendo con NaN.

    Parametri:
        results: lista di array, ciascuno di shape (t_k+1, 3)

    Restituisce:
        (matrice_S, matrice_I, matrice_R, max_len):
        ciascuna matrice ha shape (M, max_len) con NaN dove mancano dati.
    """
    max_len: int = max(len(r) for r in results)

    def pad_col(col: int) -> np.ndarray:
        mat: np.ndarray = np.full((len(results), max_len), np.nan)
        for k, traj in enumerate(results):
            mat[k, :len(traj)] = traj[:, col]
        return mat

    return pad_col(0), pad_col(1), pad_col(2), max_len


# ── Plot principali ──────────────────────────────────────────────

def plot_single_trajectory(
    traj: np.ndarray,
    save_path: Optional[str] = None,
) -> None:
    """
    Singola traiettoria SIR (S, I, R nel tempo).

    Parametri:
        traj: array di shape (t+1, 3) con colonne [S, I, R]
        save_path: percorso file di output (default: img/single_trajectory.png)
    """
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


def plot_mean_trajectory(
    results: list[np.ndarray],
    save_path: Optional[str] = None,
) -> None:
    """
    Traiettoria media ± 1 deviazione standard su M simulazioni.

    Parametri:
        results: lista di array, ciascuno di shape (t_k+1, 3)
        save_path: percorso file di output (default: img/mean_trajectory.png)
    """
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
        mean: np.ndarray = np.nanmean(mat, axis=0)
        std: np.ndarray = np.nanstd(mat, axis=0)
        plt.plot(steps, mean, color=color, label=f"E[{label}]")
        plt.fill_between(steps, mean - std, mean + std, color=color, alpha=0.15)

    plt.xlabel("Passo temporale $t$")
    plt.ylabel("Individui")
    plt.title(f"Traiettorie medie ± 1 std — {len(results)} simulazioni MC")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()


def plot_tau_histogram(
    results: list[np.ndarray],
    save_path: Optional[str] = None,
) -> list[int]:
    """
    Istogramma del tempo di estinzione τ.

    Parametri:
        results: lista di array, ciascuno di shape (t_k+1, 3)
        save_path: percorso file di output (default: img/tau_histogram.png)

    Restituisce:
        Lista dei tempi di estinzione per ogni simulazione.
    """
    if save_path is None:
        save_path = os.path.join(IMG_DIR, "tau_histogram.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Calcola i tempi di estinzione
    from analysis import extinction_time
    taus: list[int] = [extinction_time(r) for r in results]

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

def plot_sensitivity_comparison(
    scenario_results: list[tuple[str, np.ndarray, str]],
    save_path: Optional[str] = None,
) -> None:
    """
    Confronto di scenari: β e γ diversi.

    Parametri:
        scenario_results: lista di tuple (label, mean_I_array, color)
        save_path: percorso file di output (default: img/sensitivity_comparison.png)
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


def plot_ode_comparison(
    t_mc: np.ndarray,
    mean_i_mc: np.ndarray,
    std_i_mc: np.ndarray,
    t_ode: np.ndarray,
    i_ode: np.ndarray,
    save_path: Optional[str] = None,
) -> None:
    """
    Confronto tra media Monte Carlo e soluzione ODE per gli infetti.

    Parametri:
        t_mc: asse temporale MC
        mean_i_mc: media MC degli infetti
        std_i_mc: deviazione standard MC degli infetti
        t_ode: asse temporale ODE
        i_ode: infetti ODE
        save_path: percorso file di output (default: img/ode_comparison.png)
    """
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


def plot_transition_heatmap(
    n: int = 4,
    beta: float = 0.5,
    gamma: float = 0.3,
    save_path: Optional[str] = None,
    annot: bool = True,
) -> None:
    """
    Heatmap della matrice di transizione P per N piccola.

    Mostra visivamente la struttura della matrice: le righe sono stati di partenza,
    le colonne stati di arrivo. Le righe con I=0 appaiono come delta su se stesse
    (stati assorbenti, probabilit� 1 sulla diagonale).

    Parametri:
        n: dimensione della popolazione (default: 4, consigliato ≤5)
        beta: tasso di trasmissione
        gamma: tasso di guarigione
        save_path: percorso file di output (default: img/transition_heatmap.png)
        annot: se True, annota le celle con i valori di probabilit� (default: True)
    """
    from model import transition_matrix

    if save_path is None:
        save_path = os.path.join(IMG_DIR, "transition_heatmap.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    P, states = transition_matrix(n, beta, gamma)
    n_states: int = len(states)

    # Crea etichette per gli stati: (s,i,r)
    state_labels: list[str] = [f"({s},{i},{r})" for (s, i, r) in states]

    # Determina dimensione figura in base a n
    figsize: tuple[float, float] = (max(6, n_states * 0.55),
                                    max(5, n_states * 0.5))

    plt.figure(figsize=figsize)
    plt.imshow(P, cmap="YlOrRd", vmin=0, vmax=1, aspect="equal")

    # Annotazioni numeriche
    if annot:
        for i in range(n_states):
            for j in range(n_states):
                val: float = P[i, j]
                if val > 0.005:  # Mostra solo probabilit� significative
                    plt.text(j, i, f"{val:.2f}",
                             ha="center", va="center",
                             fontsize=7,
                             color="white" if val > 0.6 else "black")

    plt.xticks(range(n_states), state_labels, rotation=90, fontsize=7)
    plt.yticks(range(n_states), state_labels, fontsize=7)
    plt.xlabel("Stato di arrivo")
    plt.ylabel("Stato di partenza")
    plt.title(f"Matrice di transizione P — N={n}, beta={beta}, gamma={gamma}")

    # Barra dei colori
    cbar: Any = plt.colorbar(shrink=0.8)
    cbar.set_label("Probabilita di transizione")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
