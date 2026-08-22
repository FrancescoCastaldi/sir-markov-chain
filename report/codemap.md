# report/ — Deliverable Accademici

## Responsibility

**Documentation & Presentation Layer**: contiene tutti i materiali destinati alla
discussione orale dell'esame — relazione accademica, presentazione Beamer (27 slide), formato stampabile A4 (14 pagine), copione e note per l'orale.

---

## Design

- La relazione (`relazione.tex` / `.pdf`) usa la classe `article` LaTeX (14 pag., 11pt, A4) con pacchetti scientifici standard (`amsmath`, `booktabs`, `listings`, `hyperref`, `babel` italiano).
- La presentazione (`presentazione.tex` / `.pdf`) usa la classe `beamer` LaTeX con tema `Madrid` (27 slide, 16:9), diagrammi TikZ ($S \to I \to R$), illustrazioni concettuali, ritratto di fase $(S,I)$, matrice canonica e box informativi accademici per l'esposizione.
- La versione stampabile (`presentazione_stampabile_A4.tex` / `.pdf`) impagina 2 slide per foglio A4 (14 pagine totali con margini e cornici) ideale per la consultazione cartacea del docente.
- Il copione orale (`presentazione.md`) contiene il discorso sincronizzato frame-by-frame, traccia lavagna e Q&A preparatori.
- Le figure referenziate nella relazione e nelle presentazioni si trovano in `../img/` (path relativo).

---

## File Inventory

| File | Formato | Dimensione | Stato | Note |
|---|---|---|---|---|
| `relazione.tex` | LaTeX (article) | ~500 righe | ✅ Completo | 14 pagine A4 con prove, teoremi e grafici |
| `relazione.pdf` | PDF | ~350 KB | ✅ Compilato | Relazione ufficiale pronta per la consegna |
| `presentazione.tex` | LaTeX (beamer) | ~900 righe | ✅ Completo | 27 slide Beamer Madrid (16:9) con TikZ e tooltips |
| `presentazione.pdf` | PDF | ~2.5 MB | ✅ Compilato | Presentazione proiettabile all'orale |
| `presentazione_stampabile_A4.tex` | LaTeX (pdfpages) | ~40 righe | ✅ Completo | Layout 2-up per stampa A4 (14 fogli) |
| `presentazione_stampabile_A4.pdf` | PDF | ~2.5 MB | ✅ Compilato | Formato cartaceo per il docente |
| `presentazione.md` | Markdown | ~1350 righe | ✅ Completo | Copione parlato, traccia lavagna e risposte Q&A |
| `guida_studio_slide.md` | Markdown | ~550 righe | ✅ Completo | Guida di studio 27 slide (senso intuitivo, formule e Q&A esame) |
| `relazione.md` | Markdown | ~240 righe | 🟡 Legacy | Bozza iniziale testuale |
| `Lecture/` | Directory | — | ℹ️ Ignorato | Cartella locale dispense (protetta da .gitignore) |

---

## Struttura `relazione.tex`

```
\documentclass[11pt, a4paper]{article}
├── Frontespizio (titlepage)
├── \tableofcontents
├── Abstract (italiano)
├── §1 Introduzione
├── §2 Modello SIR come catena di Markov
│     ├── §2.1 Definizione spazio stati
│     ├── §2.2 Probabilità di transizione + Proposizione (proprietà di Markov)
│     └── §2.3 Matrice di transizione
├── §3 Esempio N=3 (Tabella transizioni con booktabs)
├── §4 Simulazione Monte Carlo
│     ├── §4.1 Parametri (Tabella)
│     └── §4.2 Algoritmo + listing Python
├── §5 Risultati
│     ├── §5.1 Singola traiettoria (Figure 1)
│     ├── §5.2 Traiettoria media (Figure 2)
│     └── §5.3 Distribuzione τ + Tabella statistiche (Figure 3)
├── §6 Analisi teorica
│     ├── §6.1 Classificazione stati (Proposition + Proof)
│     ├── §6.2 Assorbimento quasi certo (Theorem + Proof)
│     └── §6.3 Tempo medio di assorbimento (sistema lineare)
├── §7 Confronto limite fluido ODE (Figure 4)
├── §8 Conclusioni
└── Bibliography (4 riferimenti: Kermack, Norris, Federico, Allen)
```

---

## Struttura `presentazione.tex` (Beamer 24 Slide)

```
\documentclass[11pt, aspectratio=169]{beamer}
├── \usetheme{Madrid} + pacchetti TikZ, booktabs
├── Frontespizio (titlepage)
├── Slide 1-3: Introduzione, Obiettivi & Motivazione
├── Slide 4-7: Spazio degli Stati, Transizioni & Diagramma TikZ
├── Slide 8-11: Esempio N=3, Matrice Canonica & Proprietà Markoviane
├── Slide 12-16: Simulazione Monte Carlo, Traiettorie & Istogramma τ (con Tooltips)
├── Slide 17-21: Analisi Teorica, Assorbimento & Limite Fluidi ODE (con Tooltips)
├── Slide 22-23: Analisi di Sensibilità & R₀ (con Tooltips)
└── Slide 24: Conclusioni & Sintesi
```

---

## Integration Points

- **Consuma**: `../img/*.png` (prodotte da `src/plotting.py`)
- **Compilazione**: `pdflatex report/relazione.tex`, `pdflatex report/presentazione.tex`, `pdflatex report/presentazione_stampabile_A4.tex`
