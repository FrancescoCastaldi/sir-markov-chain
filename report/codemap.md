# report/ — Deliverable Accademici

## Responsibility

**Documentation & Presentation Layer**: contiene tutti i materiali destinati alla
discussione orale dell'esame — relazione accademica, presentazione, dispense del corso.

---

## Design

- La relazione (`relazione.tex`) usa la classe `article` LaTeX con pacchetti scientifici
  standard (`amsmath`, `booktabs`, `listings`, `hyperref`, `babel` italiano).
- La presentazione (`presentazione.tex`) usa la classe `beamer` LaTeX con tema `Madrid`. Include note per l'esame inserite tramite il comando `\note{}`. La versione markdown (`presentazione.md`) è tenuta per riferimento testuale.
- Le dispense (`Lecture/`) sono PDF del corso — ignorati da git (`.gitignore`).
- Le figure referenziate nella relazione si trovano in `../img/` (path relativo).

---

## File Inventory

| File | Formato | Dimensione | Stato |
|---|---|---|---|
| `relazione.tex` | LaTeX (article) | ~340 righe | ✅ Completo — pronto per pdflatex |
| `relazione.md` | Markdown | 242 righe | 🟡 Legacy — sostituito da .tex |
| `presentazione.tex` | LaTeX (beamer) | ~340 righe | ✅ Completa — tema Madrid, 21 slide con note |
| `presentazione.pdf` | PDF | — | ✅ Compilata via pdflatex |
| `presentazione.md` | Markdown | 1253 righe | 🟡 Legacy — usato come sorgente testuale |
| `Lecture/1.pdf` | PDF | — | Teoria probabilità discreta (ignorato da git) |
| `Lecture/2.pdf` | PDF | — | Filtrazioni, martingale (ignorato da git) |
| `Lecture/3.pdf` | PDF | — | Catene di Markov (ignorato da git) |

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

**Figure referenziate** (via `\includegraphics{../img/...}`):
- `single_trajectory.png`, `mean_trajectory.png`, `tau_histogram.png`, `ode_comparison.png`

---

## Struttura `presentazione.tex` (Beamer)

```
\documentclass[11pt, aspectratio=169]{beamer}
├── \usetheme{Madrid} e settaggio opzioni show notes
├── Frontespizio (titlepage)
├── Slide 1-2: Introduzione e Obiettivi
├── Slide 3-8: Il Modello SIR
├── Slide 9-11: Implementazione (Codice e Parametri)
├── Slide 12-16: Risultati e Simulazioni Monte Carlo
├── Slide 17-20: Analisi Teorica e Limite ODE
└── Slide 21: Conclusioni
```
_Nota:_ Ogni frame include il testo orale tramite `\note{}` per guidare il discorso.

---

## Integration Points

- **Consuma**: `../img/*.png` (prodotte da `src/plotting.py`)
- **Compilazione**: `pdflatex report/relazione.tex` e `pdflatex report/presentazione.tex` (richiede LaTeX installato localmente o Overleaf)
- **Build command**: `cd report && pdflatex <file>.tex`
