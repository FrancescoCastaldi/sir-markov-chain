# src/ — Core Library

## Responsibility

**Service Layer** del progetto: implementa il modello probabilistico SIR come catena di Markov,
la simulazione Monte Carlo, le funzioni di analisi statistica e il rendering grafico.
Espone una API pubblica pulita tramite `__init__.py`.

---

## Design Patterns

- **Module Separation (SRP)**: ogni modulo ha una sola responsabilità — il nucleo matematico
  (`model.py`) non dipende da nessun altro modulo interno.
- **Default Parameters Pattern**: tutte le costanti globali (`N`, `BETA`, `GAMMA`, `I0`,
  `T_MAX`, `M`, `SEED`) sono definite in `model.py` e importate dagli altri moduli;
  ogni funzione accetta parametri opzionali con default che puntano a queste costanti.
- **Pad-to-NaN Pattern** (`plotting.pad_results`): le traiettorie MC hanno lunghezze diverse
  (l'epidemia si estingue in tempi diversi); l'allineamento avviene riempiendo con `NaN`
  per poter usare `np.nanmean` / `np.nanstd` senza distorcere le medie.
- **CLI Entry Point Pattern**: `simulation.py` e `sensitivity.py` usano il guard
  `if __name__ == "__main__"` con `argparse` per essere eseguibili sia come script
  che importabili come moduli nei test.

---

## Moduli

### `model.py` — Nucleo Markoviano

**Funzioni pubbliche**:

| Funzione | Firma | Descrizione |
|---|---|---|
| `next_state` | `(s,i,r,n,β,γ) → (s',i',r')` | Un passo della catena: campiona `Bin(s, β·i/N)` e `Bin(i, γ)` |
| `transition_matrix` | `(n,β,γ) → (P, states)` | Costruisce P esplicitamente (usabile solo per N≤6) |

**Dettaglio `next_state`**:
- Guard immediato se `i=0` (stato assorbente — ritorna senza campionare).
- `p_si = β · i / n` è il parametro della Binomiale di contagio.
- I due campionamenti (`new_infections`, `recoveries`) sono indipendenti.

**Dettaglio `transition_matrix`**:
- Genera tutti gli stati `(s,i,r)` con `s+i+r=n` via `itertools.product`.
- Per ogni stato transitorio (`i>0`): somma su tutti i possibili `(c, g)` i prodotti
  `Bin.pmf(c; s, β·i/n) × Bin.pmf(g; i, γ)` e li accumula nella cella `P[idx, jdx]`.
- Usa `scipy.stats.binom.pmf` per la distribuzione binomiale esatta.

---

### `simulation.py` — Simulatore Monte Carlo

**Funzioni pubbliche**:

| Funzione | Firma | Descrizione |
|---|---|---|
| `run_single` | `(n,i0,t_max,β,γ) → ndarray(t+1,3)` | Singola traiettoria, si ferma a estinzione |
| `run_montecarlo` | `(m,n,i0,t_max,β,γ) → list[ndarray]` | M simulazioni indipendenti |
| `parse_args` | `(argv?) → Namespace` | Parser argparse per CLI |

**Flow CLI**:
1. `parse_args()` → seed opzionale, parametri modello.
2. `run_single()` → singola traiettoria per il grafico.
3. `run_montecarlo()` → M replicazioni.
4. `plot_*()` → salvataggio figure in `img/`.
5. `compute_stats()` → stampa statistiche aggregate.

---

### `analysis.py` — Statistiche e ODE

**Funzioni pubbliche**:

| Funzione | Firma | Descrizione |
|---|---|---|
| `extinction_time` | `(traj) → int` | Primo `t` con `I_t = 0`; fallback: `len(traj)-1` |
| `compute_stats` | `(results) → dict[str, float]` | Media/std di picco, τ, R∞ |
| `solve_ode_sir` | `(n,β,γ,i0,t_max,dt) → (t,s,i,r)` | ODE SIR con Euler esplicito |
| `get_mc_mean_std` | `(results) → dict` | Media/std allineate via pad_results |

**ODE Solver**: Eulero esplicito con `dt=1.0` (default). Clip a `max(x, 0)` ad ogni passo
per evitare valori negativi da errori floating point.

---

### `plotting.py` — Visualizzazione

**Funzioni pubbliche**:

| Funzione | Output | Descrizione |
|---|---|---|
| `plot_single_trajectory` | `img/single_trajectory.png` | S, I, R vs t per una traiettoria |
| `plot_mean_trajectory` | `img/mean_trajectory.png` | Media ± std su M simulazioni |
| `plot_tau_histogram` | `img/tau_histogram.png` | Istogramma di τ con media evidenziata |
| `plot_sensitivity_comparison` | `img/sensitivity_comparison.png` | Confronto I_mean per 5 scenari |
| `plot_ode_comparison` | `img/ode_comparison.png` | MC vs ODE per gli infetti |
| `plot_transition_heatmap` | `img/transition_heatmap.png` | Heatmap P per N piccolo |
| `pad_results` | `(S_mat, I_mat, R_mat, max_len)` | Helper: allinea traiettorie con NaN |

Tutte le funzioni accettano `save_path: Optional[str]` con default in `IMG_DIR = ../img/`.
Usano `plt.close()` dopo ogni save per evitare memory leak con matplotlib.

---

### `sensitivity.py` — Analisi di Sensibilità

**Costante globale**:
```python
SCENARI: list[tuple[str, float, float, str]] = [
    ("beta=0.15, gamma=0.1", 0.15, 0.1, "steelblue"),
    ("beta=0.20, gamma=0.1", 0.20, 0.1, "firebrick"),   # baseline
    ("beta=0.25, gamma=0.1", 0.25, 0.1, "seagreen"),
    ("beta=0.20, gamma=0.05", 0.20, 0.05, "darkorange"), # R0=4
    ("beta=0.20, gamma=0.15", 0.20, 0.15, "purple"),     # R0=1.33
]
```

**Funzioni**:
- `run_sensitivity()`: itera sugli scenari, tabella a terminale + sensitivity_comparison.png.
- `run_ode_comparison()`: MC baseline + ODE → ode_comparison.png + stampa comparativa.

---

### `__init__.py` — API Pubblica

Re-esporta tutti i simboli pubblici dei 5 moduli. Permette importazioni come:
```python
from src import next_state, run_montecarlo, compute_stats
```
Definisce `__all__` esplicito (17 simboli).

---

## Integration Points

- **Consumed by**: `tests/test_model.py` (importa `model`, `simulation`)
- **Consumed by**: `notebooks/` (importa tramite sys.path o pacchetto installato)
- **Produces**: figure PNG in `img/` (consumate da `report/relazione.tex`)
- **Depends on**: `numpy`, `matplotlib`, `scipy.stats.binom`
