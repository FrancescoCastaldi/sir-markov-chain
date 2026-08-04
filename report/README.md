# 📄 Academic Report (`report/`)

<p align="center">
  <em>Asset documentali, presentazioni e tesine prodotte per il corso di Modelli Probabilistici (UniBo).</em>
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Architettura e Struttura dei File](#-architettura-e-struttura-dei-file)
- [💻 Analisi dei Componenti Core](#-analisi-dei-componenti-core)
- [🔗 Dipendenze e Flusso Dati](#-dipendenze-e-flusso-dati)
- [⚙️ Usage](#-usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- **Typesetting Matematico (LaTeX)**: Formattazione rigorosa per equazioni alle differenze finite e catene di Markov.
- **High-Quality Deliverables**: Produzione del PDF finale ufficiale (tesina) pronto per l'invio al docente.
- **Beamer Slides**: Generazione automatizzata (opzionale) per le slide dell'esame orale di Settembre.

## 🏗️ Architettura e Struttura dei File

```text
report/
├── relazione.tex       # Il documento sorgente LaTeX principale
├── relazione.pdf       # Artifact pre-compilato (PDF Finale)
├── presentazione.pdf   # Artifact per l'esame orale
└── codemap.md          # Informazioni interne sul tracciamento (solo per AI)
```

Il paradigma qui non è "eseguibile", bensì compilabile (TeTeX / pdfLaTeX).

## 💻 Analisi dei Componenti Core

### `relazione.tex`
Costituisce l'intera impalcatura del paper.
```latex
% snippet da report/relazione.tex
\section{Il Modello Stocastico SIR}
Definiamo lo spazio degli stati come:
$$ E = \{ (S,I,R) \in \mathbb{N}^3 : S+I+R = N \} $$
La transizione da uno stato al successivo segue una distribuzione Binomiale per modellare le probabilità indipendenti di infezione $\beta$ e guarigione $\gamma$.
```

## 🔗 Dipendenze e Flusso Dati
- **Input**: Importa le immagini ad alta risoluzione direttamente da `../img/`. Qualsiasi cambiamento al codice in `src/` rifletterà la matematica o le immagini discusse in questo documento.
- **Toolchain**: Richiede un compilatore LaTeX (es. `pdflatex` o `lualatex`).

## ⚙️ Usage
Se si possiede una distribuzione TeX locale installata:
```bash
# Compilazione (può richiedere doppio giro per i reference)
pdflatex report/relazione.tex
```

## ⚠️ Developer Notes

> [!IMPORTANT]
> Non includere alcun file PDF nel repository Git generato dinamicamente a meno che non si tratti del deliverable finale statico pre-consegna. In questo repository il PDF compilato funge da "Release Asset" per facilitare la correzione al Prof. Federico.

> [!NOTE]
> Quando vengono modificati script in `src/` che cambiano il layout o il colore dei grafici (DPI = 150), assicurarsi che la formattazione `\includegraphics[width=\textwidth]{../img/X.png}` su LaTeX rimanga centrata o non sfori i margini.
