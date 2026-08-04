# 📓 Interactive Analysis (`notebooks/`)

<p align="center">
  <em>Esplorazione interattiva e data pipeline prototipali per il modello SIR.</em>
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Architettura e Struttura dei File](#-architettura-e-struttura-dei-file)
- [💻 Analisi dei Componenti Core](#-analisi-dei-componenti-core)
- [🔗 Dipendenze e Flusso Dati](#-dipendenze-e-flusso-dati)
- [⚙️ Usage](#-usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- **Exploratory Data Analysis (EDA)**: Sperimentazione rapida "live" per valutare il comportamento stocastico al variare dei seed.
- **Inline Rendering**: Visualizzazione immediata di plot Matplotlib con stili `ggplot` / `seaborn-darkgrid`.
- **Teaching Tool**: Ambito ideale per la didattica, permettendo all'utente di eseguire il codice passo passo comprendendo la teoria sottostante.

## 🏗️ Architettura e Struttura dei File

```text
notebooks/
├── exploration.ipynb   # Esplorazioni preliminari e test di convergenza
└── sir_pipeline.ipynb  # Pipeline analitica end-to-end con documentazione markdown inline
```

L'ambiente è basato sul kernel IPython. A differenza di `src/`, dove la priorità è l'ingegnerizzazione e l'astrazione, qui l'obiettivo è la linearità e l'ispezione immediata del dato stocastico.

## 💻 Analisi dei Componenti Core

### `sir_pipeline.ipynb`
Questo è il file definitivo che racconta una "storia". Inizia dall'inizializzazione del modello, mostra l'andamento di una singola estrazione, poi aggrega su $M=1000$ per mostrare le code statistiche e chiude con la verifica del limite $N \to \infty$.
```python
# snippet concettuale di una cella interattiva
import sys
sys.path.insert(0, "../src") # Hack per importare da src
from model import transition_matrix
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')
# plot interattivo...
```

## 🔗 Dipendenze e Flusso Dati
- **`jupyter` / `ipykernel`**: Richiesti per eseguire il codice.
- **`src/`**: Il notebook consuma le funzioni esportate da `src/model.py` e `src/analysis.py`. Esegue un'iniezione di `sys.path` per bypassare le limitazioni di scoping Python standard.

## ⚙️ Usage
```bash
# Avvia il server Jupyter in locale
jupyter notebook notebooks/

# Oppure con JupyterLab
jupyter lab notebooks/
```

## ⚠️ Developer Notes

> [!NOTE]
> Lo stato interno dei Jupyter Notebook può diventare inconsistente se le celle non vengono eseguite in ordine. Per assicurare la correttezza matematica, eseguire sempre l'intero notebook dall'inizio alla fine (Restart & Run All) prima di fare commit su git.

> [!WARNING]
> I notebook memorizzano dati in output in Base64 (immagini PNG) direttamente nel JSON del file `.ipynb`. Questo gonfia il peso del file e crea diff complessi su Git. Si consiglia di ripulire l'output (`Clear All Outputs`) prima del commit, se non espressamente richiesto mantenerli.
