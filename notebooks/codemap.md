# notebooks/ — Analisi Esplorativa Jupyter

## Responsibility

**Exploration & Demonstration Layer**: notebook Jupyter per analisi interattiva del modello
SIR, visualizzazione esplorativa e dimostrazione completa della pipeline end-to-end.
Destinati sia all'uso personale dello studente durante lo sviluppo, sia all'eventuale
demo dal vivo durante la presentazione orale.

---

## Design

- I notebook importano il pacchetto `src/` tramite `sys.path` relativo o installazione
  del pacchetto (`pip install -e .`).
- Nessuna logica di business è definita nei notebook: delegano tutto a `src/`.
- I notebook sono versionati in git (al contrario degli output, che variano tra esecuzioni).

---

## File Inventory

| File | Scopo | Dimensione |
|---|---|---|
| `exploration.ipynb` | Analisi esplorativa interattiva (sviluppo) | 9 KB |
| `pipeline_completo.ipynb` | Pipeline end-to-end in 10 sezioni (demo esame) | 21 KB |

---

## `exploration.ipynb`

Notebook leggero per:
- Prova rapida di `next_state` e `run_single` con parametri variabili.
- Visualizzazione di singole traiettorie.
- Esplorazione della matrice di transizione per N piccolo.

## `pipeline_completo.ipynb`

Pipeline strutturata in 10 sezioni:
1. Import e configurazione
2. Singola traiettoria
3. Monte Carlo (M=1000)
4. Statistiche aggregate
5. Distribuzione tempo di estinzione
6. Analisi di sensibilità su R₀
7. Confronto ODE vs MC
8. Matrice di transizione (N=4, heatmap)
9. Interpretazione teorica (markdown con LaTeX inline)
10. Conclusioni

---

## Integration Points

- **Dipende da**: `src/` (tutti i moduli)
- **Produce**: output visivi inline (non salvati su disco a meno di chiamate esplicite a `plot_*`)
- **Esecuzione**: `jupyter notebook notebooks/exploration.ipynb`
