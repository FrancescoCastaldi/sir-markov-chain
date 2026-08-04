# 📓 Interactive Analysis (`notebooks/`)

<p align="center">
  <em>Infrastruttura di analisi interattiva, esplorazione statistica EDA (Exploratory Data Analysis) e sperimentazione matematica iterativa.</em>
</p>

---

## 📖 Indice dei Contenuti
1. [Il Ruolo di Jupyter nell'Ecosistema](#1-il-ruolo-di-jupyter-nellecosistema)
2. [Albero Architetturale](#2-albero-architetturale)
3. [Deep-Dive nei Workflow Interattivi](#3-deep-dive-nei-workflow-interattivi)
   - [Isolamento Architetturale e Hacking del Path](#isolamento-architetturale-e-hacking-del-path)
   - [Pipeline End-to-End (`sir_pipeline.ipynb`)](#pipeline-end-to-end-sir_pipelineipynb)
4. [Riproducibilità vs Flessibilità](#4-riproducibilità-vs-flessibilità)
5. [Invarianti e Developer Gotchas](#5-invarianti-e-developer-gotchas)

---

## 1. Il Ruolo di Jupyter nell'Ecosistema
Sebbene l'astrazione OOP e funzionale nella cartella `src/` garantisca la massima purezza del software (ideale per la produzione), questo distacca lo sviluppatore dal loop di feedback istantaneo essenziale nella stocastica.
La directory `notebooks/` è lo spazio ludico/sperimentale (il *REPL environment*). Qui, gli script integrano blocchi formattati in markdown, equazioni $\LaTeX$ e frammenti di codice eseguibili singolarmente per ispezionare il comportamento di limitate estrazioni casuali del virus in tempo reale.

## 2. Albero Architetturale

```text
notebooks/
├── exploration.ipynb   # Ambiente "scratchpad" non lineare. Ispezione casuale dei modelli
└── sir_pipeline.ipynb  # Presentazione didattica formale eseguibile passo-passo
```

I documenti sono salvati come dizionari JSON formalizzati (formato `.ipynb`) e sono agganciati a kernel esecutivi IPython3 nativi.

## 3. Deep-Dive nei Workflow Interattivi

### Isolamento Architetturale e Hacking del Path
Poiché `notebooks/` vive allo stesso livello top-level di `src/`, Python precluderebbe le importazioni assolute standard come `import src.model`. Per iniettare le regole, le celle Jupyter d'inizializzazione alterano deliberatamente l'environment:
```python
# snippet essenziale (in testa ad ogni Notebook)
import sys
import os

# Raggiungiamo il percorso top-level ed espandiamo il PYTHONPATH per importare i moduli interni.
sys.path.insert(0, os.path.abspath("../src"))

from model import next_state, transition_matrix
from analysis import solve_ode_sir
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Theming inline di test preferenziale
```

### Pipeline End-to-End (`sir_pipeline.ipynb`)
Questo documento funge da **Guida Interattiva Definitiva** (Didattica). Attraversa fluidamente:
1. L'enunciazione accademica della Catena di Markov e i suoi parametri.
2. L'inizializzazione del modello $N=100$.
3. La prima transizione (debug della binomia passo-passo).
4. Un loop temporale `while` esploso e mostrato con plot line-graph.
5. Invocazioni ad alta densità per stressare il kernel calcolando gli andamenti di legge limite della statistica.

## 4. Riproducibilità vs Flessibilità
Nonostante la natura sperimentale, i Notebook presentati espongono i concetti chiave con seme casuale prefissato `np.random.seed(42)` per la stabilità documentale. Chi ispeziona localmente queste repository e riesegue le celle riga per riga, osserverà esattamente gli scossoni casuali documentati.

```bash
# Workflow per l'esecuzione in locale
python -m pip install jupyterlab
cd sir-markov-chain
jupyter lab notebooks/
```

## 5. Invarianti e Developer Gotchas

> [!WARNING]  
> L'estensione Jupyter per Visual Studio Code (e Jupyter in browser) tende ad appendere metadati giganti per i risultati (l'output base64 delle immagini, array lunghissimi). Questo è noto per causare spaventosi conflitti Git su file `.ipynb`.
> *Best Practice*: Usa la funzionalità **"Clear Output" / "Pulisci Output di tutte le Celle"** prima di fare *commit* su versioni esplorative, a meno che tu non voglia specificatamente archiviare il documento formale in cache per GitHub.

> [!IMPORTANT]
> Un blocco logico `def next_state()` sovrascritto in `src/` verrà assorbito dinamicamente dal notebook solo usando l'estensione cell-magic `%autoreload 2`. In caso di errori strani dopo cambiamenti strutturali nella lib nativa, l'azione salvavita è eseguire sempre **"Restart Kernel"** dal menu a tendina.
