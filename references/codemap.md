# references/ — Codemap dei Materiali di Riferimento

## Responsabilità

**Knowledge & Reference Layer**: raccoglie la teoria estratta dalle dispense del corso, le schede riassuntive delle distribuzioni probabilistiche, le dispense complete di studio per l'orale, nonché le cartelle di consultazione locale (`dispense/` e `vecchie_prove/`).

---

## Mappa dei File

| File / Directory | Descrizione | Utilizzo |
|---|---|---|
| [`references/dispense_completa.md`](references/dispense_completa.md) | Trattazione esaustiva della teoria del corso | Studio completo per l'esame orale |
| [`references/distribuzioni_fondamentali.md`](references/distribuzioni_fondamentali.md) | Formulario e proprietà delle distribuzioni discrete/continue | Consultazione rapida proprietà e momenti |
| [`references/guida_studio_presentazione.md`](references/guida_studio_presentazione.md) / `.tex` / `.pdf` | Guida integrale allo studio slide-by-slide con Q&A e dimostrazioni | Studio e preparazione dell'esposizione orale |
| [`references/formulario_dimostrazioni_secche.md`](references/formulario_dimostrazioni_secche.md) / `.tex` / `.pdf` | Formulario rapido con dimostrazioni chiave per l'orale | Ripasso rapido formule e teoremi |
| [`references/risposte_domande_teoriche.md`](references/risposte_domande_teoriche.md) / `.tex` / `.pdf` | Raccolta con risposte dettagliate alle domande teoriche d'esame | Preparazione colloquio orale |
| [`references/domande_teoriche.pdf`](references/domande_teoriche.pdf) | Quesiti teorici frequenti del corso | Autovalutazione e test |
| [`references/studio_orale_completo.pdf`](references/studio_orale_completo.pdf) / `.tex` | Documento strutturato di studio teorico avanzato | Guida teorica e dimostrazioni |
| [`references/studio_orale_definitivo.pdf`](references/studio_orale_definitivo.pdf) / `.tex` | Versione definitiva e raffinata per l'orale | Ripasso finale con focus su domande d'esame |
| `references/dispense/` | Dispense PDF originali del docente | Locale (ignorata da `.gitignore`) |
| `references/vecchie_prove/` | Progetti d'esempio e codice di riferimento | Locale (ignorata da `.gitignore`) |

---

## Integrazione nel Progetto

1. **Relazione SIR (`report/relazione.tex`)**: rigore notazionale allineato con le definizioni formali del corso.
2. **Presentazione Beamer (`report/presentazione.tex`)**: risposte ai quesiti teorici e formalizzazione degli invarianti coerenti con `references/distribuzioni_fondamentali.md`.
3. **Frontend Web (`docs/`)**: sezione teoria e dispense per consultazione rapida.
