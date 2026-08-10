# Repository Atlas: `sir-markov-chain`

> **Generato**: 2026-08-04 | **Versione**: 1.0.0 | **Linguaggio**: Python 3.10+

---

## Project Responsibility

Libreria e applicazione per la **simulazione stocastica di un'epidemia SIR** modellata come
**catena di Markov a tempo discreto** su popolazione finita `N=100`.  
Scopo primario: applicazione didattica dei fondamenti delle catene di Markov (proprietà di
Markov, matrice di transizione stocastica, stati assorbenti/transitori, assorbimento quasi certo)
su un caso concreto e numericamente trattabile.  
Contiene anche confronto con la soluzione deterministica ODE (Kermack–McKendrick) e analisi
di sensibilità su `R₀ = β/γ`.

---

## System Entry Points

| File | Ruolo |
|------|-------|
| [`src/simulation.py`](src/simulation.py) | **Entrypoint CLI principale** — lancia simulazioni Monte Carlo con argparse |
| [`src/sensitivity.py`](src/sensitivity.py) | **Entrypoint analisi di sensibilità** — varia β,γ su 5 scenari |
| [`src/analysis.py`](src/analysis.py) | **Entrypoint statistico** — compute_stats, ODE solver |
| [`pyproject.toml`](pyproject.toml) | Configurazione pacchetto Python (setuptools, dipendenze, pytest) |
| [`requirements.txt`](requirements.txt) | Dipendenze runtime: numpy, matplotlib, scipy |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | Pipeline CI GitHub Actions (Python 3.10–3.13, pytest + smoke tests) |

---

## Data & Control Flow (Flusso Principale)

```
CLI args (argparse)
    │
    ▼
simulation.py::parse_args()
    │
    ├─► run_single(n, i0, t_max, β, γ)
    │       │
    │       └─► model.py::next_state(s, i, r)  ← CORE MARKOV STEP
    │               ├── C_t ~ Bin(s, β·i/N)   [contagio]
    │               └── G_t ~ Bin(i, γ)        [guarigione]
    │
    ├─► run_montecarlo(M, ...) → list[ndarray shape (t+1, 3)]
    │
    ├─► plotting.py::plot_single_trajectory()  → img/single_trajectory.png
    ├─► plotting.py::plot_mean_trajectory()    → img/mean_trajectory.png
    ├─► plotting.py::plot_tau_histogram()      → img/tau_histogram.png
    │
    └─► analysis.py::compute_stats()          → dict statistiche
```

**Flusso secondario (sensitivity.py):**
```
sensitivity.py::run_sensitivity()
    │  per ogni scenario (β, γ):
    ├─► simulation.py::run_montecarlo()
    ├─► analysis.py::compute_stats() + get_mc_mean_std()
    └─► plotting.py::plot_sensitivity_comparison() → img/sensitivity_comparison.png

sensitivity.py::run_ode_comparison()
    ├─► simulation.py::run_montecarlo()
    ├─► analysis.py::solve_ode_sir()           [Euler esplicito]
    └─► plotting.py::plot_ode_comparison()     → img/ode_comparison.png
```

---

## Directory Map (Aggregated)

| Directory | Responsabilità | Mappa dettagliata |
|-----------|---------------|-------------------|
| [`src/`](src/) | Core library: modello Markov, simulatore MC, plotting, analisi statistica | [View Map](src/codemap.md) |
| [`tests/`](tests/) | Suite pytest (16 test): next_state, transition_matrix, run_single | [View Map](tests/codemap.md) |
| [`report/`](report/) | Deliverable accademici: relazione LaTeX, presentazione Beamer, dispense | [View Map](report/codemap.md) |
| [`references/`](references/) | Materiali di riferimento: dispense per l'orale, progetti d'esempio | [View Map](references/codemap.md) |
| [`notebooks/`](notebooks/) | Analisi esplorativa interattiva Jupyter (exploration + pipeline completa) | [View Map](notebooks/codemap.md) |
| [`img/`](img/) | Output figure PNG ad alta risoluzione per relazione (dpi=150) | — |
| [`plots/`](plots/) | Output runtime temporanei (ignorati da git) | — |
| [`.github/workflows/`](.github/workflows/) | CI GitHub Actions: test matrice Python 3.10–3.13 | — |
| [`.agents/skills/`](.agents/skills/) | Skills AI personalizzate (university-project-architect, codemap, …) | — |

---

## Key Abstractions

### Spazio degli stati SIR

```
E = { (s, i, r) ∈ ℕ₀³ : s + i + r = N }
|E| = C(N+2, 2) = (N+1)(N+2)/2
```

Per `N=100`: **5151 stati**. La catena non è irriducibile. Classe chiusa: stati con `i=0` (assorbenti).

### Matrice di transizione `P`

Calcolabile esplicitamente solo per `N ≤ 6` (funzione `model.transition_matrix(n, β, γ)`).  
Per `N=100`: dimensione 5151×5151 — gestita via simulazione MC.

### Invarianti matematici garantiti dal codice

| Invariante | Verificato in |
|---|---|
| `S + I + R = N` per ogni passo | `test_conservation()` |
| `P[i,i] = 1` per stati con `I=0` | `test_transition_matrix_absorbing()` |
| `P ≥ 0` e righe sommano a 1 | `test_transition_matrix_stochastic()` |
| `S, I, R ≥ 0` per ogni passo | `test_non_negative()` |

---

## Dipendenze tra Moduli

```
model.py          ← nucleo (nessun import interno al progetto)
    ▲
    ├── simulation.py  (importa: model, plotting, analysis)
    ├── analysis.py    (importa: model; plotting via pad_results)
    ├── plotting.py    (importa: model via transition_matrix; analysis via extinction_time)
    └── sensitivity.py (importa: model, simulation, analysis, plotting)

src/__init__.py   ← re-export pubblico di tutti i simboli principali
```

**Nota**: Gli script usano import diretti (`from model import …`) invece di import relativi.
`pyproject.toml` aggiunge `src/` al `pythonpath` di pytest per risolvere gli import nei test.

---

## Parametri di Default (src/model.py)

| Costante | Valore | Descrizione |
|---|---|---|
| `N` | 100 | Dimensione popolazione |
| `BETA` | 0.2 | Tasso trasmissione |
| `GAMMA` | 0.1 | Tasso guarigione |
| `I0` | 5 | Infetti iniziali |
| `T_MAX` | 200 | Passi temporali massimi |
| `M` | 1000 | Simulazioni Monte Carlo |
| `SEED` | `None` | Seed RNG (None = non deterministico) |
| `R₀ = β/γ` | 2.0 | Calcolato |

---

## Output Prodotti

| File | Prodotto da | Contenuto |
|---|---|---|
| `img/single_trajectory.png` | `plot_single_trajectory()` | Traiettoria singola (S,I,R) |
| `img/mean_trajectory.png` | `plot_mean_trajectory()` | Media ± std su M simulazioni |
| `img/tau_histogram.png` | `plot_tau_histogram()` | Distribuzione empirica di τ |
| `img/ode_comparison.png` | `plot_ode_comparison()` | MC vs ODE Kermack–McKendrick |
| `img/sensitivity_comparison.png` | `plot_sensitivity_comparison()` | Confronto 5 scenari |
| `img/transition_heatmap.png` | `plot_transition_heatmap()` | Heatmap matrice P (N piccolo) |

---

## Comandi di Riferimento Rapido

```bash
# Simulazione completa riproducibile
python src/simulation.py --seed 42 --sims 1000

# Test suite completa
python -m pytest tests/ -v

# Analisi di sensibilità
python src/sensitivity.py --sims 500 --seed 42

# Matrice di transizione (N≤6)
python -c "from src.model import transition_matrix; P,s = transition_matrix(3,0.5,0.3); print(P.round(3))"
```
