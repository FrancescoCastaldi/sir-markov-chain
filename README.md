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
│   ├── model.py          # Nucleo SIR: next_state(), costanti
│   ├── simulation.py     # Simulazione Monte Carlo + plotting
│   └── analysis.py       # Statistiche: picco, τ, R∞
├── notebooks/
│   └── exploration.ipynb # Analisi esplorativa interattiva
├── img/                  # Output immagini per la relazione
├── plots/                # Output grafici (generati a runtime)
├── report/
│   └── relazione.md      # Relazione accademica
└── tests/
    ├── __init__.py
    └── test_model.py     # Unit test sulla catena SIR
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
python src/simulation.py
```

I grafici per la relazione vengono salvati in `img/`.

## Utilizzo

```bash
# Eseguire simulazione completa (3 plot + statistiche)
python src/simulation.py

# Eseguire analisi statistica
python src/analysis.py

# Eseguire test
python -m pytest tests/ -v

# Notebook interattivo
jupyter notebook notebooks/exploration.ipynb
```

## Riferimenti

- Dispensa del corso (*Fullesame.pdf*), Capitolo 7 — Catene di Markov
- Norris, J.R. — *Markov Chains*, Cambridge University Press
