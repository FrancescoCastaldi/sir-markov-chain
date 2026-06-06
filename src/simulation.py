"""
Simulazione Monte Carlo del modello SIR.
Supporta parametri da riga di comando e seed per riproducibilità.

Esempi:
  python src/simulation.py
  python src/simulation.py --beta 0.3 --gamma 0.2 --sims 500
  python src/simulation.py --seed 42 --N 200
"""

from __future__ import annotations

import argparse
import numpy as np
from typing import Optional
from model import next_state, N, BETA, GAMMA, I0, T_MAX, M, SEED
from plotting import plot_single_trajectory, plot_mean_trajectory, plot_tau_histogram


def run_single(
    n: int = N,
    i0: int = I0,
    t_max: int = T_MAX,
    beta: float = BETA,
    gamma: float = GAMMA,
) -> np.ndarray:
    """
    Genera una singola traiettoria SIR.

    Parametri:
        n: popolazione totale
        i0: infetti iniziali
        t_max: orizzonte temporale massimo
        beta: tasso di trasmissione
        gamma: tasso di guarigione

    Restituisce:
        Array di shape (t+1, 3) con colonne [S, I, R] fino all'estinzione o t_max.
    """
    s: int = n - i0
    i: int = i0
    r: int = 0
    traj: list[tuple[int, int, int]] = [(s, i, r)]
    for _ in range(t_max):
        s, i, r = next_state(s, i, r, n, beta, gamma)
        traj.append((s, i, r))
        if i == 0:
            break
    return np.array(traj)


def run_montecarlo(
    m: int = M,
    n: int = N,
    i0: int = I0,
    t_max: int = T_MAX,
    beta: float = BETA,
    gamma: float = GAMMA,
) -> list[np.ndarray]:
    """
    Lancia M simulazioni Monte Carlo.

    Parametri:
        m: numero di simulazioni
        n: popolazione totale
        i0: infetti iniziali
        t_max: orizzonte temporale massimo
        beta: tasso di trasmissione
        gamma: tasso di guarigione

    Restituisce:
        Lista di M array, ciascuno di shape (t_k+1, 3).
    """
    return [run_single(n, i0, t_max, beta, gamma) for _ in range(m)]


# ── CLI ──────────────────────────────────────────────────────────

def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    """
    Analizza gli argomenti da riga di comando.

    Parametri:
        argv: lista di stringhe (default: sys.argv[1:])

    Restituisce:
        Namespace con attributi: N, beta, gamma, i0, t_max, sims, seed, no_plot.
    """
    parser = argparse.ArgumentParser(
        description="Simulazione SIR come Catena di Markov"
    )
    parser.add_argument("--N", type=int, default=N,
                        help=f"Dimensione popolazione (default: {N})")
    parser.add_argument("--beta", type=float, default=BETA,
                        help=f"Tasso di trasmissione β (default: {BETA})")
    parser.add_argument("--gamma", type=float, default=GAMMA,
                        help=f"Tasso di guarigione γ (default: {GAMMA})")
    parser.add_argument("--i0", type=int, default=I0,
                        help=f"Infetti iniziali (default: {I0})")
    parser.add_argument("--t-max", type=int, default=T_MAX,
                        help=f"Orizzonte temporale (default: {T_MAX})")
    parser.add_argument("--sims", type=int, default=M,
                        help=f"Numero simulazioni MC (default: {M})")
    parser.add_argument("--seed", type=int, default=SEED,
                        help="Seed per generatore casuale (default: nessuno)")
    parser.add_argument("--no-plot", action="store_true",
                        help="Esegue solo la simulazione senza generare plot")
    return parser.parse_args(argv)


# ── Entry point ──────────────────────────────────────────────────

if __name__ == "__main__":
    args: argparse.Namespace = parse_args()

    # Seed per riproducibilità
    if args.seed is not None:
        np.random.seed(args.seed)
        print(f"[setup] Seed fissato a {args.seed}")

    print(f"[setup] N={args.N}, beta={args.beta}, gamma={args.gamma}, "
          f"I0={args.i0}, T_MAX={args.t_max}, M={args.sims}")

    # Singola traiettoria
    traj: np.ndarray = run_single(args.N, args.i0, args.t_max, args.beta, args.gamma)
    if not args.no_plot:
        plot_single_trajectory(traj)
        print("[1/4] single_trajectory.png salvato")

    # Monte Carlo
    results: list[np.ndarray] = run_montecarlo(args.sims, args.N, args.i0,
                                                args.t_max, args.beta, args.gamma)

    if not args.no_plot:
        plot_mean_trajectory(results)
        print("[2/4] mean_trajectory.png salvato")

        taus = plot_tau_histogram(results)
        print("[3/4] tau_histogram.png salvato")

    # Statistiche
    from analysis import compute_stats
    stats: dict[str, float] = compute_stats(results)
    print(f"\n=== Statistiche su {args.sims} simulazioni ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.2f}")

    R0 = args.beta / args.gamma
    print(f"\n  R0 = beta/gamma = {R0:.2f}")
