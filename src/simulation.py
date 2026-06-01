import numpy as np
import matplotlib.pyplot as plt
import os
from model import next_state, N, BETA, GAMMA

I0 = 5
T = 100
M = 1000

def run_single(n=N, i0=I0, t=T, beta=BETA, gamma=GAMMA):
    s, i, r = n - i0, i0, 0
    trajectory = [(s, i, r)]
    for _ in range(t):
        s, i, r = next_state(s, i, r, n, beta, gamma)
        trajectory.append((s, i, r))
        if i == 0:
            break
    return np.array(trajectory)

def run_montecarlo(m=M, n=N, i0=I0, t=T, beta=BETA, gamma=GAMMA):
    results = []
    for _ in range(m):
        traj = run_single(n, i0, t, beta, gamma)
        results.append(traj)
    return results

def plot_single_trajectory(traj, save_path="../plots/single_trajectory.png"):
    steps = range(len(traj))
    plt.figure(figsize=(10, 5))
    plt.plot(steps, traj[:, 0], label="S (Suscettibili)", color="steelblue")
    plt.plot(steps, traj[:, 1], label="I (Infetti)", color="firebrick")
    plt.plot(steps, traj[:, 2], label="R (Rimossi)", color="seagreen")
    plt.xlabel("Passo temporale t")
    plt.ylabel("Numero di individui")
    plt.title("Evoluzione SIR — singola traiettoria")
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150)
    plt.close()

def plot_mean_trajectories(results, save_path="../plots/mean_trajectories.png"):
    max_len = max(len(r) for r in results)
    s_mat = np.full((len(results), max_len), np.nan)
    i_mat = np.full((len(results), max_len), np.nan)
    r_mat = np.full((len(results), max_len), np.nan)
    for k, traj in enumerate(results):
        l = len(traj)
        s_mat[k, :l] = traj[:, 0]
        i_mat[k, :l] = traj[:, 1]
        r_mat[k, :l] = traj[:, 2]
    s_mean = np.nanmean(s_mat, axis=0)
    i_mean = np.nanmean(i_mat, axis=0)
    r_mean = np.nanmean(r_mat, axis=0)
    steps = range(max_len)
    plt.figure(figsize=(10, 5))
    plt.plot(steps, s_mean, label="E[S]", color="steelblue")
    plt.plot(steps, i_mean, label="E[I]", color="firebrick")
    plt.plot(steps, r_mean, label="E[R]", color="seagreen")
    plt.xlabel("Passo temporale t")
    plt.ylabel("Numero medio di individui")
    plt.title(f"Traiettorie medie — {len(results)} simulazioni MC")
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150)
    plt.close()

if __name__ == "__main__":
    traj = run_single()
    plot_single_trajectory(traj)
    results = run_montecarlo()
    plot_mean_trajectories(results)
    print("Grafici salvati in plots/")
