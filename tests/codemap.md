# tests/ — Suite di Test

## Responsibility

**Verification Layer**: suite pytest per la verifica delle proprietà matematiche e
comportamentali del modello SIR. Garantisce che gli invarianti della catena di Markov
(conservazione, non-negatività, stocasticità della matrice P, assorbimento, markovianità, monotonicità) siano
soddisfatti dopo ogni modifica al codice.

---

## Design

- **Framework**: `pytest` (configurato in `pyproject.toml` con `testpaths = ["tests"]` e
  `pythonpath = ["src"]` — nessun `sys.path.insert` necessario nel codice di test).
- **Seed espliciti** per test stocastici: ogni test che dipende da campionamento usa
  `np.random.seed(42)` per garantire riproducibilità.
- **Pattern** usato per i test della matrice: loop su `n in range(1, 6)` — verifica le
  proprietà su popolazioni piccole dove la matrice è costruibile esattamente.
- **Import pattern**: `from model import …` e `from simulation import …` (import diretti
  senza package prefix, funzionano grazie a `pythonpath = ["src"]` in pyproject.toml).

---

## Test Inventory (16 test)

### `next_state` — 4 test

| Test | Cosa verifica | Metodo |
|---|---|---|
| `test_conservation` | `S+I+R=N` per ogni passo | 100 chiamate random |
| `test_absorbing_state` | Se `I=0`, rimane `I=0` | Caso singolo `(60,0,40)` |
| `test_non_negative` | `S,I,R ≥ 0` sempre | 100 chiamate random |
| `test_absorbing_all_seeds` | Stato assorbente invariante per qualsiasi S | 20 casi random con `I=0` |

### `transition_matrix` — 5 test

| Test | Cosa verifica | Metodo |
|---|---|---|
| `test_transition_matrix_stochastic` | Righe sommano a 1.0 (atol=1e-10) | N=1..5 |
| `test_transition_matrix_absorbing` | `P[i,i]=1` per tutti gli stati con `I=0` | N=1..5 |
| `test_transition_matrix_non_negative` | `P ≥ 0` ovunque | N=1..5 |
| `test_transition_matrix_shape` | `P.shape == (n_states, n_states)` | N=1..5 |
| `test_transition_matrix_row_stochasticity_strict` | Somma esatta righe e assenza NaN/Inf | N=1..4 |

### `run_single` — 4 test

| Test | Cosa verifica | Metodo |
|---|---|---|
| `test_run_single_shape` | Output `ndim=2`, `shape[1]=3`, `shape[0]≥2` | N=10, i0=2, t_max=50 |
| `test_run_single_stops_at_extinction` | `traj[-1, 1] == 0` (I=0 finale) | seed=42, γ=0.5 |
| `test_run_single_zero_beta` | Con β=0, S non cambia, I scende a 0 | seed=42, β=0.0, γ=0.5 |
| `test_run_single_gamma_one` | Con γ=1, estinzione rapida | seed=42, γ=1.0 |

### Invarianti Teorici Avanzati — 3 test

| Test | Cosa verifica | Metodo |
|---|---|---|
| `test_theoretical_absorbing_expected_time` | Assorbimento quasi certo $\tau < \infty$ | N=20, Monte Carlo |
| `test_markov_property_memoryless` | Assenza di memoria (Markov property) | Verifica transizioni condizionate |
| `test_monotonicity_of_removed` | Monotonicità debole $R_{t+1} \ge R_t$ | Traiettorie MC con seed fissato |

---

## Flow

```
pytest tests/ -v
    │
    └─► tests/test_model.py
            ├── import model (via pythonpath=["src"])
            │       └── next_state, transition_matrix
            └── import simulation
                    └── run_single
```

---

## Integration Points

- **Dipende da**: `src/model.py` (next_state, transition_matrix), `src/simulation.py` (run_single)
- **Eseguito da**: CI GitHub Actions su push/PR (matrice Python 3.10–3.13)
- **Eseguito localmente**: `python -m pytest tests/ -v`
