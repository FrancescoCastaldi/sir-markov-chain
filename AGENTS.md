# AGENTS.md — Progetto SIR Markov Chain

> **Scopo**: Questo file è un *living document* per AI agent (OpenCode) che lavorano
> sul progetto. Contiene l'architettura, le convenzioni, lo stato dei lavori e
> le task da completare incrementalmente.
>
> **Ogni AI agente deve LEGGERE QUESTO FILE prima di iniziare qualsiasi task**.

---

## 1. Panoramica del Progetto

```
sir-markov-chain/
├── .opencode/          ← Configurazione agenti OpenCode
├── AGENTS.md           ← QUESTO FILE — knowledge base per AI
├── README.md           ← Documentazione utente
├── requirements.txt    ← Dipendenze Python
├── pyproject.toml      ← Config moderna del progetto
├── src/
│   ├── __init__.py     ← Pacchetto con export pulito
│   ├── model.py        ← Logica SIR: next_state, transition_matrix, costanti
│   ├── simulation.py   ← Monte Carlo + CLI con argparse + seed
│   ├── plotting.py     ← Funzioni di plotting separate
│   ├── analysis.py     ← Statistiche + ODE deterministica
│   └── sensitivity.py  ← Analisi di sensibilità parametri
├── notebooks/
│   └── exploration.ipynb ← Notebook esplorativo interattivo
├── img/                ← Output immagini per la relazione
├── plots/              ← Output grafici (runtime)
├── report/
│   ├── relazione.md    ← Relazione accademica (COMPLETA)
│   └── presentazione.md ← Presentazione orale con Q&A, checklist, lavagna
└── tests/
    ├── __init__.py      ← Per pytest
    └── test_model.py   ← Test unitari (11 test)
```

### 1.1 Descrizione

Modello SIR (Suscettibili–Infetti–Rimossi) come **catena di Markov a tempo discreto**.
Progetto accademico per il corso **Modelli Probabilistici** — Università di Bologna,
A.A. 2025/2026, Prof. Salvatore Federico.

**Obiettivo**: Applicare il formalismo delle catene di Markov (matrice di transizione,
classificazione stati, assorbimento) usando simulazione Monte Carlo.

### 1.2 Tecnologie

| Tool        | Versione | Ruolo                        |
|-------------|----------|------------------------------|
| Python      | ≥ 3.10   | Linguaggio principale        |
| numpy       | ≥ 1.24   | Calcolo vettoriale / casuale |
| matplotlib  | ≥ 3.7    | Grafici e figure             |
| pytest      | ≥ 7.0    | Test (dev dependency)        |
| jupyter     | ≥ 1.0    | Notebook esplorativo         |

---

## 2. Architettura del Codice

### 2.1 Dependency Graph

```
model.py  ←──  simulation.py  ←──  analysis.py  ←──  sensitivity.py
    ↑                ↑                ↑                   ↑
    └── costanti     └── run_montecarlo └── solve_ode_sir └── run_sensitivity()
    └── next_state()     └── next_state()                    └── run_ode_comparison()
    └── transition_matrix()

plotting.py  ←──  simulation.py
         ↑         analysis.py
         └──      sensitivity.py
```

### 2.2 Moduli

#### `src/model.py` — Nucleo matematico
- **Costanti globali**: `N=100`, `BETA=0.2`, `GAMMA=0.1`, `I0=5`, `T_MAX=200`, `M=1000`, `SEED=None`
- **Funzione chiave**: `next_state(s, i, r, n, beta, gamma) → (s', i', r')`
  - Contagio: `Binomial(s, β·i/N)` • Guarigione: `Binomial(i, γ)`
  - Se `i==0` → stato assorbente, ritorna invariato
- **Pattern**: funzione pura con parametri espliciti, no side effects
- **Nuovo**: `transition_matrix(n, beta, gamma)` → calcola matrice P esplicita per N≤5

#### `src/simulation.py` — Esecuzione esperimenti
- `run_single()` → traiettoria `np.array` (shape: `[t+1, 3]`)
- `run_montecarlo(m=1000)` → lista di traiettorie
- `parse_args()` → CLI con `--N`, `--beta`, `--gamma`, `--sims`, `--seed`, `--no-plot`
- `__main__`: seed → singola traiettoria → MC → 3 plot → statistiche via analysis

#### `src/plotting.py` — Funzioni di plotting separate
- `pad_results()`, `plot_single_trajectory()`, `plot_mean_trajectory()`, `plot_tau_histogram()`
- **Nuovo**: `plot_sensitivity_comparison()`, `plot_ode_comparison()`
- Salva PNG in `img/` con `dpi=150`

#### `src/analysis.py` — Statistiche + ODE
- `extinction_time(traj)` → primo indice dove I=0
- `compute_stats(results)` → dict con mean/std di peak, τ, R∞
- **Nuovo**: `solve_ode_sir()` → soluzione ODE con Eulero
- **Nuovo**: `get_mc_mean_std()` → media e std da risultati MC allineati

#### `src/sensitivity.py` — Analisi di sensibilità
- `run_sensitivity()` → varia β, γ su scenari predefiniti, stampa tabella
- `run_ode_comparison()` → confronta ODE con media MC, genera grafico
- `__main__`: esegue entrambe le analisi

#### `tests/test_model.py` — Test (11 test totali)
- `test_conservation()` → S+I+R == N sempre
- `test_absorbing_state()` → se I=0 resta I=0
- `test_non_negative()` → nessun compartimento negativo
- `test_transition_matrix_stochastic()` → righe P sommano a 1
- `test_transition_matrix_absorbing()` → stati I=0 hanno P[i,i]=1
- `test_run_single_shape()` → array shape corretto
- `test_run_single_zero_beta()` → β=0 estingue l'infezione
- `test_run_single_gamma_one()` → γ=1 azzera I subito

### 2.3 Convenzioni di Codice

| Aspetto           | Regola                                              |
|-------------------|-----------------------------------------------------|
| Lingua            | Nomi variabili/funzioni in **inglese**              |
| Commenti/docstring| **Italiano** (contesto accademico)                  |
| Type hints        | **Non usati** — DA AGGIUNGERE gradualmente          |
| Testing           | pytest, test in `tests/test_*.py`                   |
| Naming            | `snake_case` per funzioni/variabili                 |
| Constants         | `UPPER_CASE` per costanti globali                   |
| Import style      | `from module import func` (non `import module`)     |
| Max line length   | 100 caratteri                                       |

---

## 3. Task Registrate

Ogni task ha: **ID**, **stato**, **difficoltà**, **dipendenze**, **criteri di accettazione**.

Stati: `🔴 TODO` | `🟡 IN PROGRESS` | `🟢 DONE` | `⭕ CANCELLED`

<!--
AGGIORNAMENTO: Quando un AI completa un task, deve:
1. Cambiare lo stato da 🔴 a 🟢
2. Aggiungere una nota in "Progress Log"
3. Commitare con messaggio "agents: task TASK_ID — descrizione"
-->

### Task Prioritari (devono essere risolti prima)

| ID          | Stato | Difficoltà | Task | Dipendenze |
|-------------|-------|------------|------|------------|
| **T-001** | 🟢 | Facile | **Fix import `transition_probs` in test_model.py** — Rimosso l'import inesistente. | nessuna |
| **T-002** | 🟢 | Facile | **Fix import relativo in analysis.py** — Usato `from src.simulation import ...` | T-001 |
| **T-003** | 🟢 | Facile | **Sync README parametri** — β=0.2, T_MAX=200, allineati al codice. | nessuna |
| **T-004** | 🟢 | Media | **Eliminare duplicazione stats** — simulation.py chiama `compute_stats()` da analysis.py via import locale (evita circolarità). | T-002 |

### Task di Struttura

| ID          | Stato | Difficoltà | Task | Dipendenze |
|-------------|-------|------------|------|------------|
| **T-005** | 🟢 | Facile | **Creare `tests/__init__.py`** — Permette a pytest di scoprire i test. | nessuna |
| **T-006** | 🟢 | Facile | **Popolare `src/__init__.py`** — Export pulito: `from .model import next_state, N, BETA, GAMMA` | nessuna |
| **T-007** | 🟢 | Media | **Creare `pyproject.toml`** — `[project]` con dipendenze, `[tool.pytest.ini_options]`, comandi. | T-005, T-006 |
| **T-008** | 🟢 | Media | **Configurare `.opencode/opencode.jsonc`** — Regole per agenti: linguaggio, convenzioni, cartelle. | nessuna |

### Task di Funzionalità

| ID          | Stato | Difficoltà | Task | Dipendenze |
|-------------|-------|------------|------|------------|
| **T-009** | 🟢 | Media | **Aggiungere CLI argparser** — `--N`, `--beta`, `--gamma`, `--sims`, `--seed`, `--no-plot` da riga comando. | T-007 |
| **T-010** | 🟢 | Media | **Seed riproducibile** — `np.random.seed(seed)` globale, salvato nei metadati. | T-009 |
| **T-011** | 🟢 | Media | **Creare notebook esplorativo** — `notebooks/exploration.ipynb` con analisi interattiva. | nessuna |
| **T-012** | 🟢 | Media | **Matrice di transizione esplicita per N piccolo** — Funzione `transition_matrix()` in model.py, verifica stocastica. | T-006 |

### Task di Qualità

| ID          | Stato | Difficoltà | Task | Dipendenze |
|-------------|-------|------------|------|------------|
| **T-013** | 🟢 | Media | **Aggiungere type hints** — Tutte le funzioni pubbliche con annotazioni. | nessuna |
| **T-014** | 🟢 | Media | **Aggiungere docstring** — Tutte le funzioni pubbliche con parametri, returns, esempi. | T-013 |
| **T-015** | 🟢 | Media | **Aumentare copertura test** — Test per `run_single()`, per `transition_matrix()`, per casi edge (N=1, β=0, γ=1). 11 test totali. | T-005 |
| **T-016** | ⭕ | Facile | **Aggiungere `requirements-dev.txt`** — Coperto da pyproject.toml `[project.optional-dependencies] dev`. | T-007 |
| **T-017** | 🟢 | Media | **Refactor: separare plotting da simulation.py** — Creato `src/plotting.py` con tutte le funzioni di plot. | nessuna |

### Task di Report / Analisi

| ID          | Stato | Difficoltà | Task | Dipendenze |
|-------------|-------|------------|------|------------|
| **T-018** | 🟢 | Media | **Analisi sensibilità parametri** — `src/sensitivity.py` varia β, γ e mostra impatto su τ, R∞, picco. Genera tabella + grafico comparativo. | T-009, T-010 |
| **T-019** | 🟢 | Difficile | **Confronto con ODE deterministica** — Soluzione ODE SIR con Eulero in `analysis.py`, confronto grafico con media MC. | T-017 |
| **T-020** | 🟢 | Media | **Heatmap probabilità di transizione** — Per N piccolo, visualizzare matrice P come heatmap. | T-012 |

---

## 4. Pattern e Linee Guida per AI Agent

### 4.1 Come eseguire un task

1. **Leggi AGENTS.md** — contesto completo del progetto
2. **Leggi i file coinvolti** — capisci il codice esistente
3. **Esegui i test** — `pytest tests/` prima di modificare
4. **Modifica** — segui le convenzioni del progetto
5. **Verifica** — test passano? output atteso?
6. **Aggiorna AGENTS.md** — cambia stato task da 🔴 a 🟢
7. **Commit** — messaggio nel formato `agents: T-XXX — descrizione breve`

### 4.2 Pattern di codice validati

```python
# PATTERN: next_state — funzione pura, side-effect free
def next_state(s: int, i: int, r: int, n: int = N,
               beta: float = BETA, gamma: float = GAMMA) -> tuple[int, int, int]:
    if i == 0:
        return s, 0, r
    p_si = beta * i / n
    new_infections = np.random.binomial(s, p_si)
    recoveries = np.random.binomial(i, gamma)
    return s - new_infections, i + new_infections - recoveries, r + recoveries
```

```python
# PATTERN: run_single — loop temporale con break su assorbimento
def run_single(...) -> np.ndarray:
    traj = [(s, i, r)]
    for _ in range(t_max):
        s, i, r = next_state(s, i, r, ...)
        traj.append((s, i, r))
        if i == 0:
            break
    return np.array(traj)
```

```python
# PATTERN: plot — save to IMG_DIR, tight_layout, dpi=150
def plot_*(...):
    os.makedirs(IMG_DIR, exist_ok=True)
    plt.figure(figsize=(9, 4))
    # ... plotting code ...
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "name.png"), dpi=150)
    plt.close()
```

### 4.3 Anti-pattern da evitare

| ❌ Da evitare | ✅ Alternativa |
|---|---|
| `from simulation import ...` (import relativo) | `from src.simulation import ...` |
| Test importa funzioni inesistenti | Sync import con `model.py` |
| Statistiche duplicate in più file | Centralizza in `analysis.py` |
| Parametri hard-coded sparsi | Costanti in `model.py` + CLI args |
| `plots/` vs `img/` ambigui | `img/` per output relazione, `plots/` per analisi |

### 4.4 Linguaggio

| Contesto | Lingua |
|----------|--------|
| Codice (nomi, funzioni) | **Inglese** |
| Docstring / commenti | **Italiano** |
| AGENTS.md | **Italiano** |
| README.md | **Italiano** |
| Messaggi commit | **Inglese** |
| Nome variabili | **Inglese** |

---

## 5. Progress Log

> **Ogni AI che completa un task aggiunge qui una riga.**

| Data | Task | Autore | Note |
|------|------|--------|------|
| 2026-06-06 | T-001 → T-008, T-011 | OpenCode | Fix import rotto, import relativo, parametri README, duplicazione stats, init pacchetto/tests, pyproject.toml, opencode.jsonc, notebook esplorativo. |
| 2026-06-06 | T-009, T-010, T-012, T-015, T-017, T-018, T-019 | OpenCode | CLI argparser, seed riproducibile, matrice transizione, test (3→11), refactor plotting, sensitivity.py, ODE comparison. |
| 2026-06-06 | Presentazione orale | OpenCode | report/presentazione.md: 21 slide, testo orale, Q&A, checklist, lavagna. |
| 2026-06-06 | T-013, T-014 | OpenCode | Type hints + docstring su tutti i moduli src/. Fix bug np.random.binomial.pmf → scipy.stats.binom.pmf. Risolto import circolare analysis.py. Unicode fix per Windows terminal. |
| 2026-06-06 | T-020 | OpenCode | Heatmap matrice di transizione in plotting.py + badge classici GitHub su README.

---

## 6. Comandi Utili

```bash
# Eseguire simulazione completa
python src/simulation.py

# Eseguire analisi statistica
python src/analysis.py

# Eseguire test
python -m pytest tests/ -v

# Eseguire test con coverage
python -m pytest tests/ --cov=src -v

# Installare dipendenze
pip install -r requirements.txt

# Lanciare notebook
jupyter notebook notebooks/exploration.ipynb
```
