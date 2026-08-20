# references/ — Codemap dei Materiali di Riferimento

## Responsabilità

**Knowledge & Reference Layer**: raccoglie la teoria estratta dalle dispense del corso, le schede riassuntive delle distribuzioni probabilistiche, le dispense complete di studio per l'orale, nonché le cartelle di consultazione locale (`dispense/` e `vecchie_prove/`).

---

## Mappa dei File

| File / Directory | Descrizione | Utilizzo |
|---|---|---|
| [`references/dispense_completa.md`](file:///c:/Users/franc/Documents/sir-markov-chain/references/dispense_completa.md) | Trattazione esaustiva della teoria del corso | Studio completo per l'esame orale |
| [`references/distribuzioni_fondamentali.md`](file:///c:/Users/franc/Documents/sir-markov-chain/references/distribuzioni_fondamentali.md) | Formulario e proprietà delle distribuzioni discrete/continue | Consultazione rapida proprietà e momenti |
| [`references/studio_orale_completo.pdf`](file:///c:/Users/franc/Documents/sir-markov-chain/references/studio_orale_completo.pdf) / `.tex` | Documento strutturato di studio teorico avanzato | Guida teorica e dimostrazioni |
| [`references/studio_orale_definitivo.pdf`](file:///c:/Users/franc/Documents/sir-markov-chain/references/studio_orale_definitivo.pdf) / `.tex` | Versione definitiva e raffinata per l'orale | Ripasso finale con focus su domande d'esame |
| `references/dispense/` | Dispense PDF originali del docente | Locale (ignorata da `.gitignore`) |
| `references/vecchie_prove/` | Progetti d'esempio e codice di riferimento | Locale (ignorata da `.gitignore`) |

---

## Integrazione nel Progetto

1. **Relazione SIR (`report/relazione.tex`)**: rigore notazionale allineato con le definizioni formali del corso.
2. **Presentazione Beamer (`report/presentazione.tex`)**: risposte ai quesiti teorici e formalizzazione degli invarianti coerenti con `references/distribuzioni_fondamentali.md`.
3. **Frontend Web (`docs/`)**: sezione teoria e dispense per consultazione rapida.
