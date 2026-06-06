"""
Analisi di sensibilità: varia β e γ, mostra l'impatto su picco, τ e R∞.

Esecuzione:
  python src/sensitivity.py
  python src/sensitivity.py --sims 200 --seed 42

Genera:
  - Tabella riassuntiva a terminale
  - Grafico comparativo in img/sensitivity_comparison.png
  - Confronto ODE vs MC in img/ode_comparison.png
"""

import argparse
import numpy as np
from model import BETA, GAMMA, N, I0, T_MAX, M, SEED
from simulation import run_montecarlo, parse_args as sim_parse_args
from analysis import compute_stats, solve_ode_sir, get_mc_mean_std
from plotting import plot_sensitivity_comparison, plot_ode_comparison


# Scenari da confrontare: (label, beta, gamma, color)
SCENARI = [
    ("β=0.15, γ=0.1", 0.15, 0.1, "steelblue"),
    ("β=0.20, γ=0.1", 0.20, 0.1, "firebrick"),
    ("β=0.25, γ=0.1", 0.25, 0.1, "seagreen"),
    ("β=0.20, γ=0.05", 0.20, 0.05, "darkorange"),
    ("β=0.20, γ=0.15", 0.20, 0.15, "purple"),
]


def run_sensitivity(n=N, i0=I0, t_max=T_MAX, sims=M, seed=None):
    """Esegue analisi di sensibilità su tutti gli scenari."""
    if seed is not None:
        np.random.seed(seed)

    print(f"{'Scenario':<22} {'R₀':>5} {'Picco I':>8} {'τ medio':>8} "
          f"{'R∞ medio':>9} {'R∞ std':>7}")
    print("-" * 62)

    scenario_curves = []

    for label, beta, gamma, color in SCENARI:
        r0 = beta / gamma
        results = run_montecarlo(sims, n, i0, t_max, beta, gamma)
        stats = compute_stats(results)
        mc = get_mc_mean_std(results)

        print(f"{label:<22} {r0:>5.2f} {stats['mean_peak_infected']:>8.1f} "
              f"{stats['mean_extinction_time']:>8.1f} "
              f"{stats['mean_r_inf']:>9.1f} {stats['std_r_inf']:>7.1f}")

        scenario_curves.append((label, mc["i_mean"], color))

    # Grafico comparativo
    plot_sensitivity_comparison(scenario_curves)
    print("\n[grafico] sensitivity_comparison.png salvato")


def run_ode_comparison(beta=BETA, gamma=GAMMA, n=N, i0=I0, t_max=T_MAX, sims=M, seed=None):
    """Confronta la media Monte Carlo con la soluzione ODE deterministica."""
    if seed is not None:
        np.random.seed(seed)

    print(f"\n=== Confronto ODE vs MC (β={beta}, γ={gamma}) ===")

    # MC
    results = run_montecarlo(sims, n, i0, t_max, beta, gamma)
    mc = get_mc_mean_std(results)

    # ODE
    t_ode, s_ode, i_ode, r_ode = solve_ode_sir(n, beta, gamma, i0, t_max)

    # Grafico
    plot_ode_comparison(mc["t"], mc["i_mean"], mc["i_std"],
                        t_ode, i_ode)
    print("[grafico] ode_comparison.png salvato")

    # Statistiche ODE a t_max
    r0 = beta / gamma
    print(f"  R₀ = {r0:.2f}")
    print(f"  ODE — picco I: {np.max(i_ode):.1f}")
    print(f"  ODE — R∞:      {r_ode[-1]:.1f}")
    print(f"  MC  — picco I: {mc['i_mean'].max():.1f} ± {mc['i_std'].max():.1f}")
    print(f"  MC  — R∞:      {mc['r_mean'][-1]:.1f} ± {mc['r_std'][-1]:.1f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analisi sensibilità SIR")
    parser.add_argument("--sims", type=int, default=500,
                        help="Simulazioni per scenario (default: 500)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Seed per riproducibilità")
    args = parser.parse_args()

    run_sensitivity(sims=args.sims, seed=args.seed)
    run_ode_comparison(sims=args.sims, seed=args.seed)
