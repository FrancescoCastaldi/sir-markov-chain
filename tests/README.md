# 🧪 Test Suite (`tests/`)

<p align="center">
  <em>Infrastruttura di Quality Assurance e validazione per gli invarianti matematici della catena di Markov, progettata per garantire resilienza accademica.</em>
</p>

---

## 📖 Indice dei Contenuti
1. [La Necessità del Testing Matematico](#1-la-necessità-del-testing-matematico)
2. [Albero Architetturale](#2-albero-architetturale)
3. [Deep-Dive nei Casi di Test](#3-deep-dive-nei-casi-di-test)
   - [Invarianti del Modello (`test_model.py`)](#invarianti-del-modello-test_modelpy)
   - [Robustezza dell'Esecutore (`test_simulation.py`)](#robustezza-dellesecutore-test_simulationpy)
4. [Flusso di Esecuzione in Continuous Integration](#4-flusso-di-esecuzione-in-continuous-integration)
5. [Invarianti e Developer Gotchas](#5-invarianti-e-developer-gotchas)

---

## 1. La Necessità del Testing Matematico
Trattandosi di un modello stocastico, il risultato di due estrazioni identiche produce due andamenti radicalmente diversi. Questa assenza di determinismo rende impossibile l'utilizzo dei tradizionali test di uguaglianza per l'output.
Al contrario, questa test suite si concentra interamente sulla dimostrazione logica e assiomatica degli **invarianti matematici** che devono sussistere *indipendentemente* dal seme aleatorio.

## 2. Albero Architetturale

```text
tests/
├── test_model.py       # Stress testing sulle distribuzioni stocastiche per conservazione masse
├── test_simulation.py  # Verifica dell'early stopping e della pipeline run-to-completion
└── __init__.py         # Definisce tests/ come modulo importabile (opzionale)
```

La suite usa le direttive native di `pytest`. L'integrazione è automatizzata nel workflow `pyproject.toml` per mappare `src/` nel `PYTHONPATH` automaticamente.

## 3. Deep-Dive nei Casi di Test

### Invarianti del Modello (`test_model.py`)
Valida le proprietà fisiche del processo compartimentale. Anche in caso di estremo over-fitting dei parametri casuali, gli atomi (individui) non possono generarsi dal nulla né scomparire.
```python
def test_conservation():
    """L'invariante S + I + R = N deve valere ad ogni step."""
    n = 100
    # Test esauriente su condizioni estreme
    s, i, r = 90, 10, 0
    next_s, next_i, next_r = next_state(s, i, r, 0.5, 0.5)
    
    # 1. Conservazione della massa totale
    assert next_s + next_i + next_r == n
    
    # 2. Nessuna probabilità deve ammettere popolazioni negative
    assert next_s >= 0
    assert next_i >= 0
    assert next_r >= 0
```
Include inoltre suite gravose sulla validazione matriciale completa per limitati range (es. per $N=5$, la matrice di transizione calcolata deve avere tutte le righe che sommano analiticamente a $1.0$).

### Robustezza dell'Esecutore (`test_simulation.py`)
Le traiettorie nel tempo richiedono di fermarsi dinamicamente se la curva di contagi collassa a zero per ragioni stocastiche.
```python
def test_simulation_early_stopping():
    """Se I scende a 0 per pure fluttuazioni, la simulazione si ferma e R_end + S_end = N"""
    # ...
    assert final_i == 0
    assert len(trajectory) < t_max  # Verificando l'early cutoff
```

## 4. Flusso di Esecuzione in Continuous Integration
La pipeline GitHub (in `.github/workflows/ci.yml`) invoca questi moduli automaticamente ad ogni commit verso il ramo master, applicando una regression protection in cross-platform testing su matrici (Python 3.10, 3.11, 3.12, 3.13).

```bash
# Esecuzione standard con verbosità
python -m pytest tests/ -v

# Esecuzione con fast-fail (si ferma al primo invariante rotto)
python -m pytest tests/ -x
```

## 5. Invarianti e Developer Gotchas

> [!CAUTION]  
> Testare la classe `transition_matrix()` causa un sovraccarico di memoria computando combinazioni fattoriali enormi se la popolazione data è $>10$. **Non scrivere test per matrici che usino l'impostazione di produzione $N=100$**.

> [!NOTE]
> Per validare invarianti fluttuanti (es. la convergenza teorica di ODE verso media stocastica) in fase di test, utilizzare `numpy.testing.assert_allclose` con una tolleranza relativa definita statisticamente, poiché a campioni bassi (M=50) la legge forte dei grandi numeri non ha un impatto sufficiente e i test falliranno (Flakiness).
