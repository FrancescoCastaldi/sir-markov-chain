"""
Simulazione Monte Carlo del modello SIR.
Supporta parametri da riga di comando e seed per riproducibilità.

Esempi:
  python src/simulation.py
  python src/simulation.py --beta 0.3 --gamma 0.2 --sims 500
  python src/simulation.py --seed 42 --N 200
"""

import argparse
import numpy as np
from model import next_state, N, BETA, GAMMA, I0, T_MAX, M, SEED
from plotting import plot_single_trajectory, plot_mean_trajectory, plot_tau_histogram


def run_single(n=N, i0=I0, t_max=T_MAX, beta=BETA, gamma=GAMMA):
    """Singola traiettoria SIR. Restituisce array shape (t+1, 3)."""
    s, i, r = n - i0, i0, 0
    traj = [(s, i, r)]
    for _ in range(t_max):
        s, i, r = next_state(s, i, r, n, beta, gamma)
        traj.append((s, i, r))
        if i == 0:
            break
    return np.array(traj)


def run_montecarlo(m=M, n=N, i0=I0, t_max=T_MAX, beta=BETA, gamma=GAMMA):
    """Lancia M simulazioni Monte Carlo. Restituisce lista di traiettorie."""
    return [run_single(n, i0, t_max, beta, gamma) for _ in range(m)]


# ── CLI ──────────────────────────────────────────────────────────

def parse_args(argv=None):
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
    args = parse_args()

    # Seed per riproducibilità
    if args.seed is not None:
        np.random.seed(args.seed)
        print(f"[setup] Seed fissato a {args.seed}")

    print(f"[setup] N={args.N}, β={args.beta}, γ={args.gamma}, "
          f"I₀={args.i0}, T_MAX={args.t_max}, M={args.sims}")

    # Singola traiettoria
    traj = run_single(args.N, args.i0, args.t_max, args.beta, args.gamma)
    if not args.no_plot:
        plot_single_trajectory(traj)
        print("[1/4] single_trajectory.png salvato")

    # Monte Carlo
    results = run_montecarlo(args.sims, args.N, args.i0,
                             args.t_max, args.beta, args.gamma)

    if not args.no_plot:
        plot_mean_trajectory(results)
        print("[2/4] mean_trajectory.png salvato")

        taus = plot_tau_histogram(results)
        print("[3/4] tau_histogram.png salvato")

    # Statistiche
    from analysis import compute_stats
    stats = compute_stats(results)
    print(f"\n=== Statistiche su {args.sims} simulazioni ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.2f}")

    R0 = args.beta / args.gamma
    print(f"\n  R₀ = β/γ = {R0:.2f}")
