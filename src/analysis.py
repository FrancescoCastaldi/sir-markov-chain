import numpy as np
from simulation import run_montecarlo, N, I0, T, BETA, GAMMA

def extinction_time(traj):
    for t, state in enumerate(traj):
        if state[1] == 0:
            return t
    return len(traj) - 1

def compute_stats(results):
    peak_infects = []
    ext_times = []
    for traj in results:
        peak_infects.append(np.max(traj[:, 1]))
        ext_times.append(extinction_time(traj))
    stats = {
        "mean_peak_infected": np.mean(peak_infects),
        "std_peak_infected": np.std(peak_infects),
        "mean_extinction_time": np.mean(ext_times),
        "std_extinction_time": np.std(ext_times),
        "max_extinction_time": np.max(ext_times),
    }
    return stats

if __name__ == "__main__":
    results = run_montecarlo()
    stats = compute_stats(results)
    print("=== Statistiche Simulazione SIR ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.2f}")
