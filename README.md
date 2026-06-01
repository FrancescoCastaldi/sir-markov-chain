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
├── README.md
├── requirements.txt
├── src/
│   ├── model.py          # Matrice di transizione e logica SIR
│   ├── simulation.py     # Simulazione Monte Carlo
│   └── analysis.py       # Statistiche: media infetti, tempo estinzione
├── notebooks/
│   └── exploration.ipynb # Analisi esplorativa interattiva
├── plots/
│   └── .gitkeep          # Output grafici (generati a runtime)
├── report/
│   └── relazione.md      # Relazione accademica
└── tests/
    └── test_model.py     # Unit test sulla matrice di transizione
```

## Parametri del Modello

| Parametro | Simbolo | Valore default |
|-----------|---------|----------------|
| Popolazione | N | 100 |
| Prob. contagio | β | 0.3 |
| Prob. guarigione | γ | 0.1 |
| Infetti iniziali | I₀ | 5 |
| Passi temporali | T | 100 |
| Simulazioni MC | M | 1000 |

## Installazione

```bash
pip install -r requirements.txt
```

## Esecuzione

```bash
python src/simulation.py
```

I grafici vengono salvati in `plots/`.

## Riferimenti

- Dispensa del corso (*Fullesame.pdf*), Capitolo 7 — Catene di Markov
- Norris, J.R. — *Markov Chains*, Cambridge University Press
