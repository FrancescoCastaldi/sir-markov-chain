<p align="center">
  <img src="img/mean_trajectory.png" width="800" alt="SIR Markov Chain Mean Trajectory">
</p>

<h1 align="center">🦠 SIR Markov Chain Simulator: A Stochastic Epidemic Model</h1>

<p align="center">
  <em>Simulazione stocastica avanzata e parametrizzabile di un'epidemia SIR (Suscettibili, Infetti, Rimossi) modellata come Catena di Markov a tempo discreto su popolazione finita, corredata da analisi statistica, confronto deterministico ODE (Kermack–McKendrick) e deliverable accademici.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Course-Modelli%20Probabilistici-crimson.svg?style=flat-square" alt="Course">
  <img src="https://img.shields.io/badge/University-UniBo-red.svg?style=flat-square" alt="UniBo">
</p>

---

## 📖 Indice dei Contenuti
1. [Inquadramento Teorico](#1-inquadramento-teorico)
2. [Caratteristiche del Modello](#2-caratteristiche-del-modello)
3. [Architettura e Struttura del Progetto](#3-architettura-e-struttura-del-progetto)
4. [Invarianti e Proprietà Matematiche](#4-invarianti-e-propriet%C3%A0-matematiche)
5. [Installazione e Setup](#5-installazione-e-setup)
6. [Guida all'Uso e Interfaccia CLI](#6-guida-alluso-e-interfaccia-cli)
7. [Suite di Test e Validazione](#7-suite-di-test-e-validazione)
8. [Deliverable Accademici e Risorse](#8-deliverable-accademici-e-risorse)
9. [Note Computazionali sulla Complessità](#9-note-computazionali-sulla-complessit%C3%A0)

---

## 1. Inquadramento Teorico

Il progetto è sviluppato per il corso di **Modelli Probabilistici** (Università di Bologna) con l'obiettivo di implementare e analizzare una simulazione stocastica su popolazione finita $N$.

A differenza del classico approccio compartimentale deterministico continuo basato su equazioni differenziali ordinarie (ODE di Kermack–McKendrick), il sistema è formalizzato come una **Catena di Markov a tempo discreto (DTMC)** omogenea a stati finiti:

$$\mathcal{S} = \{ (s, i, r) \in \mathbb{N}_0^3 : s + i + r = N \}$$

La transizione temporale da $t$ a $t+1$ avviene mediante estrazioni condizionate da distribuzioni binomiali:
* Nuovi contagi: $C_t \sim \mathrm{Bin}\left(S_t, 1 - (1 - \frac{\beta}{N})^{I_t}\right) \approx \mathrm{Bin}\left(S_t, \frac{\beta I_t}{N}\right)$
* Nuove guarigioni: $G_t \sim \mathrm{Bin}(I_t, \gamma)$

Questo schema cattura intrinsecamente la variabilità stocastica, l'eventuale estinzione precoce dell'epidemia e la distribuzione del tempo di assorbimento $\tau$.

---

## 2. Caratteristiche del Modello

- 🎲 **Evoluzione Stocastica Esatta**: Nessuna discretizzazione euristica arbitraria; le transizioni di stato rispettano rigorosamente le probabilità di transizione binomiali.
- 📈 **Simulazione Monte Carlo Vettorializzata**: Generazione di traiettorie multiple ($M \ge 1000$) per calcolare medie empiriche, deviazioni standard, percentili e distribuzioni dei tempi di estinzione.
- 🔬 **Analisi di Sensibilità ($R_0$)**: Studio parametrico della dinamica al variare del numero di riproduzione di base $R_0 = \frac{\beta}{\gamma}$.
- ⚖️ **Validazione Ibrida Stocastico-Deterministica**: Confronto sistematico tra la media delle traiettorie stocastiche e la soluzione numerica dell'ODE (metodo di Eulero esplicito).
- 📊 **Visualizzazioni ad Alta Risoluzione**: Generazione automatizzata di grafici pronti per la pubblicazione scientifica (dpi 150/300) salvati in `img/`.

---

## 3. Architettura e Struttura del Progetto

```
sir-markov-chain/
├── .github/workflows/        # Automazioni CI/CD (GitHub Actions)
│   ├── ci.yml                # Pipeline di test automatici su matrici Python
│   └── deploy-pages.yml      # Deploy automatico della dashboard su GitHub Pages
├── src/                      # Modulo sorgente Python del simulatore SIR
│   ├── model.py              # Nucleo stocastico Markoviano (next_state, transition_matrix)
│   ├── simulation.py         # Entrypoint CLI e motore Monte Carlo vettorializzato
│   ├── analysis.py           # Calcolo statistiche, percentili e integrazione ODE
│   ├── sensitivity.py        # Analisi parametrica su scenari di R₀ e benchmark ODE
│   └── plotting.py           # Generazione grafici scientifici Matplotlib (dpi 150/300)
├── tests/                    # Suite di test di regressione e verifica invarianti (pytest)
│   └── test_model.py         # Test formali su conservazione massa, probabilità e stati assorbenti
├── report/                   # Deliverable accademici e sorgenti tipografiche
│   ├── relazione.tex         # Relazione tecnica in LaTeX (documento scientifico principale)
│   ├── presentazione.tex     # Slide Beamer (16:9, tema Madrid con grafica vettoriale TikZ)
│   ├── presentazione_stampabile_A4.tex # Formato compatto per stampa (2 slide per pagina A4)
│   ├── presentazione.md      # Copione di esposizione orale slide-by-slide
│   ├── distribuzioni_fondamentali.tex  # Compendio formale sulle distribuzioni probabilistiche
│   └── capitoli/             # Moduli teorici dettagliati dei singoli capitoli del corso
├── docs/                     # Dashboard Web interattiva (Vanilla JS/CSS, GitHub Pages)
│   ├── index.html            # Landing page con simulatore visuale interattivo
│   ├── simulator.js          # Motore di simulazione client-side in JavaScript
│   ├── style.css             # Design moderno e responsivo
│   ├── dispense.html         # Visualizzatore web dei materiali teorici
│   └── guida_orale.html      # Guida interattiva per l'esposizione
├── notebooks/                # Notebook interattivi Jupyter
│   ├── exploration.ipynb     # Prototipazione rapida ed esplorazione delle dinamiche
│   └── pipeline_completo.ipynb # Pipeline end-to-end riproducibile
├── img/                      # Figure e grafici generati ad alta risoluzione per la relazione
├── codemap.md                # Atlante e mappa architetturale navigabile del repository
├── pyproject.toml            # Configurazione packaging Python e standard di build
└── requirements.txt          # Dipendenze scientifiche minime (numpy, scipy, matplotlib, pytest)
```

| Directory / Modulo | Ruolo e Responsabilità |
|---|---|
| [`src/`](src/) | Motore computazionale del modello SIR, simulatore Monte Carlo, solutore ODE e plotting. |
| [`tests/`](tests/) | Validazione matematica continua degli invarianti stocastici e test di regressione. |
| [`report/`](report/) | Sorgenti e deliverable accademici ufficiali (relazione, presentazione Beamer, compendio). |
| [`docs/`](docs/) | Web app statica distribuita su GitHub Pages con simulatore interattivo real-time. |
| [`notebooks/`](notebooks/) | Notebook Jupyter per la prototipazione esplorativa e analisi visiva dei dati. |
| [`img/`](img/) | Raccolta delle figure e diagrammi per la documentazione e i report. |
| [`.github/`](.github/) | Workflow di Continuous Integration e deployment automatico su GitHub Pages. |

---

## 4. Invarianti e Proprietà Matematiche

L'implementazione verifica costantemente tre proprietà cardine:

1. **Conservazione della Popolazione**:
   $$\forall t \ge 0, \quad S_t + I_t + R_t = N$$
2. **Proprietà di Markov**:
   $$\mathbb{P}(X_{t+1} = x_{t+1} \mid X_t = x_t, \dots, X_0 = x_0) = \mathbb{P}(X_{t+1} = x_{t+1} \mid X_t = x_t)$$
3. **Stati Assorbenti e Assorbimento Quasi Certo**:
   Tutti gli stati con $I = 0$, ovvero della forma $(s, 0, N-s)$, costituiscono una classe chiusa assorbente. Il tempo di estinzione $\tau = \inf \{ t \ge 0 : I_t = 0 \}$ è quasi certamente finito:
   $$\mathbb{P}(\tau < \infty) = 1$$

---

## 5. Installazione e Setup

Il progetto richiede **Python 3.10** o versione successiva.

```bash
# 1. Clonazione del repository
git clone https://github.com/FrancescoCastaldi/sir-markov-chain.git
cd sir-markov-chain

# 2. Creazione e attivazione dell'ambiente virtuale
python -m venv .venv
source .venv/bin/activate       # Linux / macOS
# Su Windows (PowerShell): .venv\Scripts\Activate.ps1

# 3. Installazione delle dipendenze
pip install -r requirements.txt
```

---

## 6. Guida all'Uso e Interfaccia CLI

Il modulo espone comandi completi configurabili via parametri:

### 6.1. Simulazione Monte Carlo Singola o Multipla
Esegue una simulazione con $M=1000$ traiettorie e genera i grafici di traiettoria media, singola traiettoria e istogramma dei tempi di assorbimento:
```bash
python src/simulation.py --n 100 --i0 5 --beta 0.25 --gamma 0.10 --sims 1000 --seed 42
```

### 6.2. Analisi di Sensibilità e Confronto ODE
Esegue la scansione su scenari multipli di $\beta$ e $\gamma$, confrontando il modello stocastico con la traiettoria deterministica:
```bash
python src/sensitivity.py --sims 500 --seed 42
```

---

## 7. Suite di Test e Validazione

I test di unità verificano la correttezza algoritmica e gli invarianti probabilistici:

```bash
python -m pytest tests/ -v
```

Tra i controlli eseguiti:
* Rispetto della somma $S + I + R = N$ ad ogni passo temporale.
* Non negatività degli stati ($S, I, R \ge 0$).
* Stocasticità della matrice di transizione ($\sum_j P_{ij} = 1$).
* Stabilità degli stati assorbenti (nessuna ripartenza dopo $I=0$).

---

## 8. Deliverable Accademici e Risorse

I materiali accademici sono organizzati nella directory `report/`:
* **Relazione Scientifica**: [`report/relazione.pdf`](report/relazione.pdf) (Documento LaTeX con derivazioni teoriche, grafici e discussione dei risultati).
* **Presentazione Orale**: [`report/presentazione.pdf`](report/presentazione.pdf) (Slide Beamer 16:9 con grafici vettoriali e schemi concettuali).
* **Copione di Esposizione**: [`report/presentazione.md`](report/presentazione.md) (Guida parlata slide-per-slide per il colloquio).

---

## 9. Note Computazionali sulla Complessità

> [!NOTE]
> La dimensione dello spazio degli stati per una popolazione $N$ è data dal coefficiente binomiale con ripetizione:
> $$|\mathcal{S}| = \binom{N + 2}{2} = \frac{(N+1)(N+2)}{2}$$
> Per $N=100$, lo spazio consta di **5.151 stati**. Una matrice di transizione esplicita richiederebbe una memoria di circa $5151 \times 5151 \approx 26.5 \times 10^6$ elementi float (oltre 200 MB per singola matrice densa).
>
> Per garantire la massima efficienza computazionale e scalabilità, il simulatore adotta la **generazione forward-sampling diretta** delle traiettorie, calcolando la matrice esplicita solo per validazione su valori ridotti ($N \le 6$).

