# 🧪 Test Suite (`tests/`)

<p align="center">
  <em>Batteria di unit test per la verifica rigorosa degli invarianti matematici e dell'esattezza del simulatore.</em>
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Architettura e Struttura dei File](#-architettura-e-struttura-dei-file)
- [💻 Analisi dei Componenti Core](#-analisi-dei-componenti-core)
- [🔗 Dipendenze e Flusso Dati](#-dipendenze-e-flusso-dati)
- [⚙️ Usage](#-usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- **Conservation Checking**: Assicura che la popolazione resti costante (`S + I + R = N`) per *qualsiasi* iterazione di Markov.
- **Stochastic Matrix Validation**: Verifica che la matrice di transizione esatta `P` sia non-negativa e che le sue righe sommino a 1.
- **Absorbing States Tests**: Certifica che tutti gli stati con `I=0` abbiano probabilità di transizione $P(i,i) = 1$.
- **Integration Tests**: Valida le pipeline run-to-completion dei file CLI senza causare side-effect o crash.

## 🏗️ Architettura e Struttura dei File

```text
tests/
├── test_model.py       # Unit test per le funzioni matematiche pure in src/model.py
├── test_simulation.py  # Test di integrazione per i runner Monte Carlo
└── conftest.py         # (Opzionale) Fixtures condivise per la suite
```

I test utilizzano `pytest`. La struttura rispecchia l'albero di `src/`, garantendo test 1:1 rispetto alle funzioni esportate dal package.

## 💻 Analisi dei Componenti Core

### `test_model.py`
Questo modulo applica lo stress test ai casi estremi del processo stocastico. Assicura che le leggi fisiche del modello vengano rispettate.

```python
def test_conservation():
    """L'invariante S + I + R = N deve valere per ogni transizione."""
    n = 100
    s, i, r = 90, 10, 0
    next_s, next_i, next_r = next_state(s, i, r, 0.2, 0.1)
    
    assert next_s + next_i + next_r == n
    assert next_s >= 0
    assert next_i >= 0
    assert next_r >= 0
```

### `test_simulation.py`
Verifica che le traiettorie generate siano di formato corretto e raggiungano sempre l'assorbimento `I=0` nei tempi attesi senza sforare in loop infiniti o memory leak.

## 🔗 Dipendenze e Flusso Dati
- Dipende unicamente dalla cartella `src/`.
- Grazie al file `pyproject.toml` nella root, la cartella `src/` viene montata nel `PYTHONPATH` permettendo import puliti come `from model import next_state`.

## ⚙️ Usage
La directory deve essere consumata direttamente tramite pytest.

```bash
# Esegue tutti i test e mostra il report verbose
python -m pytest tests/ -v

# Esegue solo i test matematici del modello
python -m pytest tests/test_model.py
```

## ⚠️ Developer Notes

> [!IMPORTANT]  
> Quando viene testata la funzione `transition_matrix()`, usare una popolazione estremamente piccola ($N \le 6$). Generare la matrice con $N=100$ in fase di test causa timeout e out-of-memory a causa della dimensione della matrice stocastica $5151 \times 5151$.

> [!NOTE]
> Ogni test che invoca probabilità random (es. `next_state`) dovrebbe iniettare `--seed` o chiamare esplicitamente un RNG seeded per prevenire flakiness (falsi negativi dovuti al caso). In alternativa, testare gli invarianti matematici (es: conservazione della somma), i quali sono garantiti indipendentemente dall'estrazione aleatoria.
