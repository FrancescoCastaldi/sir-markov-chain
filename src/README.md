# 🧠 Core Engine (`src/`)

<p align="center">
  <em>Il cuore matematico, statistico e visuale del simulatore SIR stocastico.</em>
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Architettura e Struttura dei File](#-architettura-e-struttura-dei-file)
- [💻 Analisi dei Componenti Core](#-analisi-dei-componenti-core)
- [🔗 Dipendenze e Flusso Dati](#-dipendenze-e-flusso-dati)
- [⚙️ Usage](#-usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- **Markov Core**: Calcolo probabilistico rigoroso delle transizioni (infezione e guarigione).
- **Runners**: Motori per simulazioni singole e Monte Carlo parallelo.
- **Analytics**: Risoluzione numerica deterministica (Kermack-McKendrick) e aggregazione statistica dei tensori stocastici.
- **Plotting**: Visualizzazione scientifica modulare indipendente dalla logica di dominio.

## 🏗️ Architettura e Struttura dei File

```text
src/
├── model.py        # Logica pura di transizione Markoviana
├── simulation.py   # CLI e runner Monte Carlo
├── analysis.py     # Aggregazione statistica e solver ODE
├── sensitivity.py  # Script per l'analisi R_0 parametrizzata
├── plotting.py     # Gestione rendering via Matplotlib
└── __init__.py     # Re-export dell'API pubblica
```

L'architettura separa rigorosamente il dominio puramente matematico (`model.py`), dalle operazioni stateful e I/O come le simulazioni (`simulation.py`), l'analisi (`analysis.py`), e il rendering visivo (`plotting.py`).

## 💻 Analisi dei Componenti Core

### `model.py`
Questo modulo contiene la logica **pura** (stateless) della Catena di Markov. Calcola le probabilità di transizione per il singolo passo basandosi sulle equazioni del processo Binomiale.
```python
def next_state(s, i, r, beta, gamma):
    """
    Determina il prossimo stato (S, I, R) usando la probabilità stocastica.
    C_t ~ Bin(S_t, beta * I_t / N)
    G_t ~ Bin(I_t, gamma)
    """
    n = s + i + r
    p_inf = beta * i / n if n > 0 else 0
    new_inf = np.random.binomial(s, p_inf)
    new_rec = np.random.binomial(i, gamma)
    return s - new_inf, i + new_inf - new_rec, r + new_rec
```

### `analysis.py`
Fornisce funzioni per convertire le distribuzioni empiriche generate in statistiche aggregabili e integra il sistema ODE equivalente.
```python
def solve_ode_sir(n, i0, t_max, beta, gamma):
    """Risolve il sistema ODE SIR (Kermack-McKendrick) tramite Eulero Esplicito."""
    s_out = [n - i0]
    i_out = [i0]
    r_out = [0]
    # [...]
```

## 🔗 Dipendenze e Flusso Dati
- **Input**: `simulation.py` accetta argomenti CLI dall'utente e chiama `model.py` iterativamente per generare le traiettorie.
- **Flusso intermedio**: I tensori generati passano a `analysis.py` per le medie e l'allineamento (padding) tramite NumPy.
- **Output**: I dati processati fluiscono a `plotting.py` che genera le immagini PNG esportandole in `/img/`.

## ⚙️ Usage
La directory è disegnata per essere eseguita dal root del progetto usando la sintassi modulo di Python.

```bash
# Esegui il ciclo principale
python src/simulation.py --n 100 --i0 5 --beta 0.2 --gamma 0.1 --sims 1000
```

## ⚠️ Developer Notes

> [!WARNING]  
> Tutte le funzioni di aggregazione di traiettorie stocastiche devono gestire lunghezze di array variabili! L'epidemia termina quando `I=0`, che avviene a tempi di assorbimento $\tau$ differenti. Utilizzare sempre `pad_results()` da `analysis.py` prima di calcolare medie e standard deviation.

> [!NOTE]
> `model.py` non dipende e non deve **mai** dipendere dagli altri file in `src/`. Questa invariante assicura che il modello matematico sia testabile singolarmente e importabile senza dipendenze circolari.
