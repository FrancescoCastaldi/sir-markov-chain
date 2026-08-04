# 🧠 Core Engine (`src/`)

<p align="center">
  <em>Il cuore matematico, stocastico e architettonico della libreria SIR. Qui risiedono gli algoritmi di transizione probabilistica e l'infrastruttura di analisi statistica Monte Carlo.</em>
</p>

---

## 📖 Indice dei Contenuti
1. [Introduzione al Modulo Source](#1-introduzione-al-modulo-source)
2. [Modello Matematico e Astrazione](#2-modello-matematico-e-astrazione)
3. [Albero Architetturale](#3-albero-architetturale)
4. [Deep-Dive nei Componenti Core](#4-deep-dive-nei-componenti-core)
   - [`model.py` (Dominio Puro)](#modelpy-dominio-puro)
   - [`simulation.py` (Runner & Concurrency)](#simulationpy-runner--concurrency)
   - [`analysis.py` (Statistica & ODE)](#analysispy-statistica--ode)
5. [Infrastruttura di Plotting](#5-infrastruttura-di-plotting)
6. [Flusso dei Dati (Data Flow)](#6-flusso-dei-dati-data-flow)
7. [Invarianti e Developer Gotchas](#7-invarianti-e-developer-gotchas)

---

## 1. Introduzione al Modulo Source
La cartella `src/` racchiude la **business logic** dell'intero repository. Questa directory non contiene assets, documenti testuali o test, ma solo il codice Python sorgente che effettua le valutazioni. È disegnata seguendo pattern di astrazione chiari: nessun modulo importa file che non gli competono, creando un grafo delle dipendenze unidirezionale estremamente pulito (es. il modello non sa nulla di come viene plottato o simulato).

## 2. Modello Matematico e Astrazione
Il simulatore mappa il modello SIR su una Catena di Markov.
Se il sistema si trova allo stato $X_t = (S_t, I_t, R_t)$, le transizioni di stato nel tempo discreto $t \to t+1$ avvengono per via di:
1. **Infezioni (Nuovi Infetti)**: $C_{t+1} \sim \text{Binomial}\left(S_t, \beta \frac{I_t}{N}\right)$
2. **Guarigioni (Nuovi Rimossi)**: $G_{t+1} \sim \text{Binomial}\left(I_t, \gamma\right)$

Questa astrazione garantisce che il numero di infezioni non superi mai i suscettibili fisicamente disponibili e che le guarigioni non superino mai gli infetti correnti.

## 3. Albero Architetturale

```text
src/
├── __init__.py         # Esporta le API chiave, rendendo src/ una libreria matura
├── model.py            # Calcolo transizione di Markov (Stateless, Nessuna dipendenza)
├── simulation.py       # Loop di esecuzione temporale, CLI con argparse, aggregatore
├── analysis.py         # Statistica per aggregazione tensoriale, padding array, ODE solver
├── plotting.py         # Abstraction layer sopra Matplotlib per generazione grafici
└── sensitivity.py      # Esecutore parametrizzato (CLI indipendente)
```

## 4. Deep-Dive nei Componenti Core

L'ecosistema è suddiviso in responsabilità strette. Nessun file viola il principio di singola responsabilità (SRP).

### `model.py` (Dominio Puro)
Il file più fondamentale del progetto. Non sa nulla dell'utente, dei grafici o della simulazione temporale complessiva. Si limita a conoscere lo stato presente e a calcolare il futuro immediato.
```python
import numpy as np

def next_state(s, i, r, beta, gamma):
    """
    Funzione di transizione di Markov per il singolo passo.
    Utilizza distribuzioni Binomiali per estrarre infezioni e guarigioni, 
    assicurando che il RNG operi entro i limiti fisici della popolazione N.
    """
    n = s + i + r
    
    # Assicuriamo che la probabilità p_inf sia limitata in [0, 1] 
    # e che gestisca correttamente il caso I=0.
    p_inf = beta * i / n if n > 0 else 0.0
    
    # Estrazioni stocastiche da processi di Poisson approssimati a Binomiali
    new_inf = np.random.binomial(s, p_inf)
    new_rec = np.random.binomial(i, gamma)
    
    # Aggiornamento differenziale degli scompartimenti
    return s - new_inf, i + new_inf - new_rec, r + new_rec
```

### `simulation.py` (Runner & Concurrency)
Questo script fornisce la CLI. Ha il compito di iterare `next_state` nel dominio del tempo, costruendo una "storia" o "traiettoria" completa dell'epidemia.
Esporta la funzione `run_montecarlo()` che gestisce iterazioni parallele isolate (non interagenti). Quando $I_t = 0$, la simulazione interrompe il processo in anticipo (ottimizzazione early-stopping per stati assorbenti).

### `analysis.py` (Statistica & ODE)
L'epidemia stocastica termina in tempi differenti (tempi di assorbimento variabili). Per poter calcolare medie empiriche, i vettori (es. Suscettibili su t) hanno lunghezze diverse.
```python
def pad_results(results, t_max):
    """
    Estende con l'ultimo valore tutte le traiettorie fino a t_max per permettere
    la conversione in un Tensore NumPy rettangolare 3D in grado di essere 
    processato via np.mean() e np.std() in batch.
    """
    # [...]
```
Contiene inoltre il solutore per il sistema Differenziale Ordinario (ODE) SIR:
$$ \frac{dS}{dt} = -\beta \frac{S I}{N} $$
$$ \frac{dI}{dt} = \beta \frac{S I}{N} - \gamma I $$
Implementato usando un metodo di integrazione alle differenze finite (Eulero Esplicito).

## 5. Infrastruttura di Plotting
Il file `plotting.py` astrae totalmente Matplotlib. Questo previene la disseminazione di comandi `plt.figure()` in tutta la logica di dominio. L'infrastruttura è configurata per usare stili avanzati (`seaborn-v0_8-darkgrid`) e un sistema di generazione a DPI altissimi ($150$) per la stampa LaTeX.

## 6. Flusso dei Dati (Data Flow)

Il ciclo vitale dell'informazione all'interno di `src/` avviene nel seguente modo:
1. `simulation.py` raccoglie i parametri di `N`, `I0`, `beta`, `gamma` dal terminale (o da un notebook).
2. Lancia cicli temporali che invocano `model.py` ritornando tuple $(S, I, R)$.
3. I risultati (liste di vettori spuri) sono passati a `analysis.py`.
4. `analysis.py` effettua il *padding* e ritorna dizionari semantici (`{"mean_s": ..., "std_s": ...}`).
5. Il dizionario di output viene dato in pasto a `plotting.py` che esegue i render PNG salvandoli fisicamente su disco.

## 7. Invarianti e Developer Gotchas

> [!IMPORTANT]
> **Dimensione Dinamica del Tempo (Early Stopping)**. Una peculiarità del modello stocastico rispetto a quello continuo è che $\lim_{t \to \infty} I_t = 0$ con probabilità $1$. `simulation.py` arresta il loop se `I == 0` prima del compimento di `t_max`. Non bisogna assumere che le traiettorie in output siano lunghe `t_max + 1`. Esse sono sempre array frastagliati (ragged arrays) e vanno gestite con funzioni di utility apposite (`analysis.pad_results`).

> [!WARNING]
> Mai aggiungere `import plotting` in `model.py`. Il modello non deve conoscere la rappresentazione visiva per evitare cicli di dipendenze (circular imports) e per permetterne l'impiego pulito in API backend.

> [!NOTE]
> La generazione della vera matrice stocastica $P$ tramite la funzione `model.transition_matrix()` utilizza un mapping biunivoco tra lo stato $(S, I, R)$ e un indice intero ID in $0 \dots |E|-1$. Usala solo per debug su $N < 10$. Eseguire questa funzione con la popolazione completa di $N=100$ paralizzerà il kernel causando OOM (Out Of Memory) a causa della topologia quadrata $|E| \times |E|$ dell'iper-matrice.
