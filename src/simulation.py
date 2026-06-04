import numpy as np
import matplotlib.pyplot as plt
import os
from model import next_state, N, BETA, GAMMA, I0, T_MAX, M

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img")

def run_single(n=N, i0=I0, t_max=T_MAX, beta=BETA, gamma=GAMMA):
    s, i, r = n - i0, i0, 0
    traj = [(s, i, r)]
    for _ in range(t_max):
        s, i, r = next_state(s, i, r, n, beta, gamma)
        traj.append((s, i, r))
        if i == 0:
            break
    return np.array(traj)

def run_montecarlo(m=M, n=N, i0=I0, t_max=T_MAX, beta=BETA, gamma=GAMMA):
    return [run_single(n, i0, t_max, beta, gamma) for _ in range(m)]

def _pad(results):
    max_len = max(len(r) for r in results)
    def pad_col(col):
        mat = np.full((len(results), max_len), np.nan)
        for k, traj in enumerate(results):
            mat[k, :len(traj)] = traj[:, col]
        return mat
    return pad_col(0), pad_col(1), pad_col(2), max_len

def plot_single_trajectory(traj):
    os.makedirs(IMG_DIR, exist_ok=True)
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
    plt.savefig(os.path.join(IMG_DIR, "single_trajectory.png"), dpi=150)
    plt.close()

def plot_mean_trajectory(results):
    os.makedirs(IMG_DIR, exist_ok=True)
    s_mat, i_mat, r_mat, max_len = _pad(results)
    steps = range(max_len)
    for mat, color, label in [
        (s_mat, "steelblue", "S"),
        (i_mat, "firebrick", "I"),
        (r_mat, "seagreen", "R"),
    ]:
        mean = np.nanmean(mat, axis=0)
        std  = np.nanstd(mat, axis=0)
        plt.plot(steps, mean, color=color, label=f"E[{label}]")
        plt.fill_between(steps, mean - std, mean + std, color=color, alpha=0.15)
    plt.xlabel("Passo temporale $t$")
    plt.ylabel("Individui")
    plt.title(f"Traiettorie medie ± 1 std — {len(results)} simulazioni MC")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "mean_trajectory.png"), dpi=150)
    plt.close()

def plot_tau_histogram(results):
    os.makedirs(IMG_DIR, exist_ok=True)
    taus = []
    for traj in results:
        ext = np.where(traj[:, 1] == 0)[0]
        taus.append(int(ext[0]) if len(ext) > 0 else len(traj) - 1)
    plt.figure(figsize=(8, 4))
    plt.hist(taus, bins=30, color="slateblue", edgecolor="white")
    plt.xlabel("Tempo di estinzione $\\tau$")
    plt.ylabel("Frequenza")
    plt.title("Distribuzione empirica del tempo di estinzione")
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "tau_histogram.png"), dpi=150)
    plt.close()
    return taus

if __name__ == "__main__":
    traj = run_single()
    plot_single_trajectory(traj)
    print("[1/3] single_trajectory.png salvato")

    results = run_montecarlo()
    plot_mean_trajectory(results)
    print("[2/3] mean_trajectory.png salvato")

    taus = plot_tau_histogram(results)
    print("[3/3] tau_histogram.png salvato")

    print(f"\n=== Statistiche su {M} simulazioni ===")
    peak = [np.max(r[:, 1]) for r in results]
    r_inf = [r[-1, 2] for r in results]
    print(f"Picco infetti I_max:       media={np.mean(peak):.1f}  std={np.std(peak):.1f}  min={np.min(peak):.0f}  max={np.max(peak):.0f}")
    print(f"Tempo estinzione tau:      media={np.mean(taus):.1f}  std={np.std(taus):.1f}  min={np.min(taus):.0f}  max={np.max(taus):.0f}")
    print(f"Rimossi finali R_inf:      media={np.mean(r_inf):.1f}  std={np.std(r_inf):.1f}  min={np.min(r_inf):.0f}  max={np.max(r_inf):.0f}")
