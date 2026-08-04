<p align="center">
  <img src="img/mean_trajectory.png" width="600" alt="SIR Markov Chain Mean Trajectory">
</p>

<h1 align="center">🦠 SIR Markov Chain Simulator</h1>

<p align="center">
  <em>Simulazione stocastica avanzata di un'epidemia SIR modellata come catena di Markov a tempo discreto su popolazione finita.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build">
  <img src="https://img.shields.io/badge/coverage-100%25-brightgreen.svg" alt="Coverage">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/academic-UniBo-red.svg" alt="UniBo">
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Directory Structure](#-directory-structure)
- [💻 Core Components](#-core-components)
- [⚙️ Quickstart & Usage](#-quickstart--usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- 🎲 **Motore Stocastico**: Modella dinamicamente il contagio e la guarigione usando distribuzioni Binomiali per approssimare la matrice di transizione di Markov.
- 📈 **Monte Carlo Analysis**: Simulazioni massive per derivare la media, deviazione standard e tempi di assorbimento (fine epidemia).
- 🔬 **Sensitivity Analysis**: Valuta l'impatto della variazione di $R_0 = \beta / \gamma$ sul picco epidemico.
- 📉 **Confronto ODE**: Valida il modello stocastico confrontandolo numericamente con la soluzione deterministica di Kermack-McKendrick (Eulero esplicito).
- 🌐 **Web Dashboard**: Output visuale pronto per il web ospitato su GitHub Pages.

## 🏗️ Directory Structure
```text
sir-markov-chain/
├── src/        # 🧠 Core matematico e motore stocastico
├── tests/      # 🧪 Test suite rigorosa per gli invarianti matematici
├── docs/       # 🌐 Frontend web Vanilla (HTML/CSS Glassmorphism)
├── report/     # 📄 Relazione accademica LaTeX e Beamer
├── notebooks/  # 📓 Pipeline Jupyter per analisi interattiva
└── img/        # 📊 Output visivi generati
```

Il progetto segue il pattern **Modello-Simulazione-Analisi**. La logica di transizione è puramente funzionale isolata in `model.py`, mentre le responsabilità di esecuzione, I/O e plotting sono delegate a moduli indipendenti.

## 💻 Core Components
Il punto d'ingresso principale per l'utente e per la CI è il file `src/simulation.py`.

```python
# snippet da src/simulation.py
def run_montecarlo(M, n, i0, t_max, beta, gamma):
    """Esegue M simulazioni Monte Carlo."""
    results = []
    for _ in range(M):
        results.append(run_single(n, i0, t_max, beta, gamma))
    return results
```

## ⚙️ Quickstart & Usage

### 1. Installazione
```bash
git clone https://github.com/FrancescoCastaldi/sir-markov-chain.git
cd sir-markov-chain
pip install -r requirements.txt
```

### 2. Simulazione Monte Carlo
Lancia 1000 simulazioni e genera i plot nella cartella `img/`:
```bash
python src/simulation.py --sims 1000 --seed 42
```

### 3. Analisi di Sensibilità
Valuta 5 scenari epidemici differenti:
```bash
python src/sensitivity.py --sims 500 --seed 42
```

### 4. Avvio dei Test
```bash
python -m pytest tests/ -v
```

## ⚠️ Developer Notes

> [!IMPORTANT]
> L'estensione dello spazio degli stati SIR è pari a `(N+1)(N+2)/2`. Per `N=100`, parliamo di **5151 stati**.
> A causa di queste dimensioni, il calcolo della matrice di transizione esatta `P` (via `transition_matrix()`) è supportato solo per $N \le 6$ (a scopo di test e visualizzazione). Per $N=100$, il sistema si affida **esclusivamente alle traiettorie stocastiche** generate in avanti (forward sampling).

> [!NOTE]
> Il progetto è progettato per la riproducibilità. L'utilizzo del flag `--seed` imposta il seed globale per `numpy.random`, garantendo che l'output della relazione LaTeX corrisponda sempre esattamente ai plot finali.
