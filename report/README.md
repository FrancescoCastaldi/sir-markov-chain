# 📄 Academic Report (`report/`)

<p align="center">
  <em>Sorgente per il document typesetting e la compilazione tipografica della tesi e delle diapositive. Formalità accademica tramite LaTeX.</em>
</p>

---

## 📖 Indice dei Contenuti
1. [Il Ruolo di LaTeX nel Progetto](#1-il-ruolo-di-latex-nel-progetto)
2. [Albero Architetturale](#2-albero-architetturale)
3. [Deep-Dive nei Documenti Finali](#3-deep-dive-nei-documenti-finali)
   - [Paper Accademico (`relazione.tex`)](#paper-accademico-relazionetex)
   - [Tracciamento AI (`codemap.md`)](#tracciamento-ai-codemapmd)
4. [Flusso di Compilazione (Data Flow)](#4-flusso-di-compilazione-data-flow)
5. [Invarianti e Developer Gotchas](#5-invarianti-e-developer-gotchas)

---

## 1. Il Ruolo di LaTeX nel Progetto
Mentre il comparto `src/` valida matematicamente il progetto e il comparto `docs/` ne facilita la divulgazione, la documentazione contenuta in `report/` è specificatamente concepita per essere letta da ricercatori e docenti (Università di Bologna). Il formato LaTeX assicura tipografia impeccabile per le equazioni delle catene di Markov e la rigorosa struttura referenziale e bibliografica richiesta da un elaborato accademico di alto rango.

## 2. Albero Architetturale

```text
report/
├── relazione.tex       # Root file del paper accademico (A4, twocolumn)
├── relazione.pdf       # Artifact: Compilato finale (solo su branch Release / o mantenuto statico)
├── presentazione.pdf   # Artifact: Slide estrapolate in Beamer per l'orale
└── codemap.md          # Meta-dato contestuale per la skill dell'AI (escluso dalla compilazione)
```

## 3. Deep-Dive nei Documenti Finali

### Paper Accademico (`relazione.tex`)
Questo documento è il fine ultimo del progetto. Integra i grafici high-dpi (generati dal core e depositati in `/img`) e ne fornisce l'analisi formale e le conclusioni.
```latex
% snippet architetturale da report/relazione.tex
\section{Il Modello Stocastico SIR}

Sia $\mathcal{E}$ lo spazio degli stati fisicamente ammissibili:
\begin{equation}
    E = \left\{ (S, I, R) \in \mathbb{N}^3 : S+I+R = N \right\}
\end{equation}
Si osserva che per ogni configurazione tale che $I=0$, lo stato è un \textit{absorbing state} o stato assorbente. Dal punto di vista probabilistico, la probabilità limite si attesta su:
\begin{equation}
    \lim_{t \to \infty} \mathbb{P}(I_t = 0 \mid I_0 > 0) = 1
\end{equation}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=\columnwidth]{../img/single_trajectory.png}
    \caption{Estrazione di traiettoria stocastica singola con $N=100$.}
\end{figure}
```

### Tracciamento AI (`codemap.md`)
File markdown ad uso esclusivamente interno (ingegneria del prompt) che permette all'intelligenza artificiale (agente Opencode) di "vedere" a colpo d'occhio la tassonomia documentale di questa sottocartella senza dover leggere file `.tex` massivi e appesantire il contesto.

## 4. Flusso di Compilazione (Data Flow)
I sistemi TeX non elaborano logica di business. Questa è un'infrastruttura passiva che *include* a tempo di compilazione frammenti e immagini generati altrove.
**Dipendenze Forti**:
- La cartella `../img/` deve contenere esattamente i filename definiti negli statement `\includegraphics`.
- Se si esegue uno script Python (`src/simulation.py`) sovrascrivendo l'immagine PNG, la compilazione del LaTeX non produrrà alcun errore (avrà successo) e semplicemente mostrerà il nuovo grafico.

```bash
# Workflow esecutivo consigliato per produrre il file PDF (relazione.pdf)
pdflatex -interaction=nonstopmode report/relazione.tex
# Oppure (per supporto font avanzati)
lualatex report/relazione.tex
```

## 5. Invarianti e Developer Gotchas

> [!IMPORTANT]  
> Il mantenimento dei PDF binari all'interno di una repository Git è generalmente considerato un anti-pattern a causa del *repository bloat*. In questo specifico framework accademico, sono preservati e versionati come snapshot utili al professore per visionare l'esame in tempo reale senza compilarlo. **Si sconsiglia di committare i PDF intermedi, facendolo solo all'atto della Release Definitiva.**

> [!NOTE]
> Evita di lanciare build LaTeX dalla root della repository se le macro interne ai file `.tex` usano path relativi al documento stesso. Entra nella cartella o assicurati che le direttive per le immagini (`../img/`) siano valutate dal resolver corretto.
