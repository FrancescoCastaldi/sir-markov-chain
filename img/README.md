# 📊 Visual Assets (`img/`)

<p align="center">
  <em>Artifact repository per la storicizzazione, l'esportazione e la fruizione di output visivi vettoriali e raster generati dalla logica matematica.</em>
</p>

---

## 📖 Indice dei Contenuti
1. [L'Importanza dello Strato Visivo](#1-limportanza-dello-strato-visivo)
2. [Albero Architetturale](#2-albero-architetturale)
3. [Tipologia degli Asset Condivisi](#3-tipologia-degli-asset-condivisi)
4. [Flusso Esterno (Write-Only / Read-Only)](#4-flusso-esterno-write-only--read-only)
5. [Invarianti e Developer Gotchas](#5-invarianti-e-developer-gotchas)

---

## 1. L'Importanza dello Strato Visivo
Tutti i tensori N-dimensionali aggregati dalle migliaia di run di iterazione del modello di Markov stocastico sono opachi se visti nel terminale. Per dimostrare empiricamente le proprietà teoriche della catena discreta serve estrapolare il dato.
La cartella `img/` costituisce la cassaforte statica finale. L'unico formato ammesso qui è di altissima qualità e finalizzato all'erogazione diretta in documenti accademici e dashboard web.

## 2. Albero Architetturale

```text
img/
├── .gitkeep                     # Previene che Git elimini la cartella se svuotata
├── mean_trajectory.png          # Evidenza visiva della legge dei grandi numeri (Media/STD)
├── ode_comparison.png           # Validazione ibrida (Curve Continue vs Curve Stocastiche Discrete)
├── sensitivity_comparison.png   # Risultati della parametrizzazione di R_0 sulle 5 ipotesi di contagio
├── single_trajectory.png        # Ispezione del rumore stocastico nudo e crudo di 1 simulazione
└── tau_histogram.png            # Distribuzione empirica gaussiana (approssimata) del tempo di assorbimento
```

## 3. Tipologia degli Asset Condivisi
Ogni file è un Portable Network Graphic (`.png`) generato mediante backend specifici (`AGG`) con un fattore di ridimensionamento profondo (`DPI >= 150`). Questo serve per evitare lo sgradevole "sgranamento" che si osserva solitamente nelle tesi in LaTeX compilate con grafici in bassa definizione copiati e incollati a schermo intero.

## 4. Flusso Esterno (Write-Only / Read-Only)

Dal momento che `img/` non contiene un bit di codice logicamente eseguibile, il suo diagramma di comunicazione col resto del repo è netto:

* **Sorgenti in Scrittura (Write-Only Destinazione):** Moduli astratti come `src/plotting.py` scrivono distruttivamente e silenziosamente in questa cartella. Le vecchie immagini vengono polverizzate.
* **Consumatori in Lettura (Read-Only Sorgente):** Moduli passivi e frontend assorbono queste immagini:
  - Il documento in `report/relazione.tex` lo fa tramite primitive macro `\includegraphics`.
  - Il frontend web `docs/index.html` consuma copie speculari di questi grafici per il DOM.

## 5. Invarianti e Developer Gotchas

> [!WARNING]  
> Mai committare in questa directory plot temporanei o fallati (generati durante sessioni di puro debugging del core `src/`). A tale scopo, la repository mette a disposizione la directory nascosta **`plots/`**, esente dal versioning Git tramite `.gitignore`. Usa `img/` come una sorta di *Artifact Registry Pubblico*: salvi qui solo i risultati pronti per la pubblicazione della tesi.

> [!IMPORTANT]
> Quando le immagini in questa cartella cambiano (dopo un run di simulazione aggiornato), il nuovo hash del file PNG viene marcato modificato da Git. Eseguire un push di questi file triggera *automaticamente* le pipeline configurate (`.github/workflows`) e l'immagine si aggiornerà sul cloud (GitHub Pages) entro un minuto solare, senza dover toccare HTML o configurazioni server.

> [!NOTE]
> Per ottenere un set riproducibile di questi grafici, invocare la master CLI esplicitando il flag entropico costante: `$ python src/simulation.py --seed 42`
