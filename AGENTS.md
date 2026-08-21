# AGENTS.md — sir-markov-chain

Questo file viene caricato automaticamente dall'agente AI ad ogni sessione.
Contiene istruzioni di contesto per operare efficacemente su questo repository.

---

## Repository Map

Un codemap completo è disponibile in [`codemap.md`](codemap.md) nella root del progetto.

Prima di lavorare su qualsiasi task, leggi `codemap.md` per capire:
- Architettura del progetto e entry point principali
- Responsabilità di ogni directory e pattern di design
- Flusso dati e punti di integrazione tra i moduli

Per lavoro approfondito su una directory specifica, leggi anche il `codemap.md` di quella cartella:
- [`src/codemap.md`](src/codemap.md) — Modello Markov, simulatore, plotting, analisi
- [`tests/codemap.md`](tests/codemap.md) — Suite pytest e invarianti verificati
- [`report/codemap.md`](report/codemap.md) — Deliverable LaTeX, relazione PDF, presentazione Beamer (27 slide) e formato A4 stampabile
- [`references/codemap.md`](references/codemap.md) — Dispense per l'orale e progetti d'esempio
- [`notebooks/codemap.md`](notebooks/codemap.md) — Pipeline Jupyter end-to-end

---

## Contesto del Progetto

- **Tipo**: Progetto universitario, esame orale
- **Corso**: Modelli Probabilistici 518512, Unibo — Prof. Salvatore Federico
- **Argomento**: Simulazione SIR come catena di Markov discreta
- **Skill attiva**: `university-project-architect` (vedi `.agents/skills/university-project-architect/SKILL.md`)
- **Stato avanzamento**: vedi [`PROJECT_STATUS.md`](PROJECT_STATUS.md)

---

## Deliverable Principali

- **Relazione Ufficiale**: [`report/relazione.pdf`](report/relazione.pdf) (14 pag., LaTeX article, A4)
- **Presentazione Orale**: [`report/presentazione.pdf`](report/presentazione.pdf) (27 slide, Beamer Madrid 16:9 con TikZ e tooltips)
- **Presentazione Stampabile A4**: [`report/presentazione_stampabile_A4.pdf`](report/presentazione_stampabile_A4.pdf) (14 pag., 2 slide per foglio A4)
- **Copione & Q&A Orale**: [`report/presentazione.md`](report/presentazione.md) (guida parlata slide-by-slide + traccia lavagna)

---

## Regole operative

1. **Prima di modificare codice**: leggi il modulo interessato e tutti i suoi consumer (vedi grafo dipendenze in `codemap.md`).
2. **Dopo ogni modifica al codice**: esegui `python -m pytest tests/ -v` e verifica che tutti i test passino.
3. **Import nei test**: gli import funzionano senza `sys.path.insert` grazie a `pythonpath = ["src"]` in `pyproject.toml`.
4. **Figure**: generate in `img/` (dpi=150). Le figure in `plots/` sono temporanee e ignorate da git.
5. **Seed**: usa sempre `--seed 42` per simulazioni riproducibili nei test e nella documentazione.
6. **Pulizia compilazione**: non committare file ausiliari di LaTeX (`*.aux`, `*.log`, `*.nav`, `*.snm`, `*.toc`, `*.vrb`, `*.out`).
7. **EXAM_INFO.md e PROJECT_STATUS.md**: sono nella root ma entrambi in `.gitignore` (informazioni private).
