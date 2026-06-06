[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![CLI](https://img.shields.io/badge/CLI-argparse-black?logo=gnubash&logoColor=white)](src/simulation.py)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/francceco-/sir-markov-chain?logo=git)](https://github.com/francceco-/sir-markov-chain)
[![Repo size](https://img.shields.io/github/repo-size/francceco-/sir-markov-chain?logo=github)](https://github.com/francceco-/sir-markov-chain)
[![Tests](https://img.shields.io/badge/tests-12%2F12-brightgreen?logo=pytest)](tests/)
[![DOI](https://img.shields.io/badge/status-completo-success)](https://github.com/francceco-/sir-markov-chain)

# Simulazione SIR come Catena di Markov

**Corso**: Modelli Probabilistici — Università di Bologna  
**Docente**: Prof. Salvatore Federico  
**Studente**: Francesco Castaldi

---

## Descrizione

Modellazione di una epidemia su popolazione piccola (N=100) tramite catena di Markov a tempo discreto con stati **S** (Suscettibili), **I** (Infetti), **R** (Rimossi).

L'obiettivo è applicare il formalismo delle catene di Markov — non fare epidemiologia — usando una matrice di transizione stocastica e simulazione Monte Carlo.

## Struttura del Progetto

```
sir-markov-chain/
├── .opencode/            # Configurazione agenti OpenCode
├── AGENTS.md             # Knowledge base per AI agent
├── README.md
├── requirements.txt
├── pyproject.toml        # Config moderna del progetto
├── src/
│   ├── __init__.py       # Export del pacchetto
│   ├── model.py          # Nucleo SIR: next_state, transition_matrix, costanti
│   ├── simulation.py     # Simulazione Monte Carlo + CLI con argparse + seed
│   ├── plotting.py       # Funzioni di plotting separate
│   ├── analysis.py       # Statistiche + ODE deterministica
│   └── sensitivity.py    # Analisi di sensibilità parametri
├── notebooks/
│   └── exploration.ipynb # Analisi esplorativa interattiva
├── img/                  # Output immagini per la relazione
├── plots/                # Output grafici (runtime)
├── report/
│   ├── relazione.md      # Relazione accademica
│   └── presentazione.md  # Presentazione orale con Q&A, checklist, lavagna
└── tests/
    ├── __init__.py
    └── test_model.py     # Unit test (11 test: catena SIR, matrice P, edge case)
```

## Parametri del Modello

| Parametro | Simbolo | Valore default |
|-----------|---------|----------------|
| Popolazione | N | 100 |
| Prob. contagio | β | 0.2 |
| Prob. guarigione | γ | 0.1 |
| Infetti iniziali | I₀ | 5 |
| Passi temporali | T_MAX | 200 |
| Simulazioni MC | M | 1000 |

## Installazione

```bash
pip install -r requirements.txt
```

## Esecuzione

```bash
# Simulazione completa con parametri default
python src/simulation.py

# Simulazione con parametri custom e seed per riproducibilità
python src/simulation.py --beta 0.3 --gamma 0.2 --sims 500 --seed 42

# Solo simulazione senza plot
python src/simulation.py --no-plot

# Analisi di sensibilità (5 scenari + confronto con ODE)
python src/sensitivity.py

# Analisi statistica
python src/analysis.py

# Eseguire test
python -m pytest tests/ -v

# Notebook interattivo
jupyter notebook notebooks/exploration.ipynb
```

I grafici per la relazione vengono salvati in `img/` con dpi=150.
I risultati della simulazione (picco medio, tempo di estinzione, rimossi finali)
vengono stampati a terminale.

## Riferimenti

- Dispensa del corso (*Fullesame.pdf*), Capitolo 7 — Catene di Markov
- Norris, J.R. — *Markov Chains*, Cambridge University Press
