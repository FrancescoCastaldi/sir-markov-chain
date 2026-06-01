import numpy as np
from simulation import run_montecarlo, M

def extinction_time(traj):
    ext = np.where(traj[:, 1] == 0)[0]
    return int(ext[0]) if len(ext) > 0 else len(traj) - 1

def compute_stats(results):
    peak   = [np.max(r[:, 1]) for r in results]
    taus   = [extinction_time(r) for r in results]
    r_inf  = [r[-1, 2] for r in results]
    return {
        "mean_peak_infected":    np.mean(peak),
        "std_peak_infected":     np.std(peak),
        "mean_extinction_time":  np.mean(taus),
        "std_extinction_time":   np.std(taus),
        "max_extinction_time":   np.max(taus),
        "mean_r_inf":            np.mean(r_inf),
        "std_r_inf":             np.std(r_inf),
    }

if __name__ == "__main__":
    results = run_montecarlo()
    stats = compute_stats(results)
    print(f"=== Statistiche su {M} simulazioni ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.2f}")
