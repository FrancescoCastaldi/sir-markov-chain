# Contenuto della cartella `src`

| Nome file | Descrizione / Esempio |
|-----------|------------------------|
| `analysis.py` | Script Python. Esempio:<br><code>"""<br>Analisi statistica e confronto con ODE per il modello SIR.<br><br>Funzioni:<br>  - extinction_time()     : tempo di estinzione da una traiettoria</code> |
| `codemap.md` | File Markdown. Esempio:<br><code># src/ — Core Library<br><br>## Responsibility<br><br>**Service Layer** del progetto: implementa il modello probabilistico SIR come catena di Markov,</code> |
| `model.py` | Script Python. Esempio:<br><code>from __future__ import annotations<br><br>import numpy as np<br>from itertools import product<br>from typing import Optional</code> |
| `plotting.py` | Script Python. Esempio:<br><code>"""<br>Funzioni di plotting per il modello SIR.<br>Separate da simulation.py per modularità.<br>"""</code> |
| `sensitivity.py` | Script Python. Esempio:<br><code>"""<br>Analisi di sensibilità: varia β e γ, mostra l'impatto su picco, τ e R∞.<br><br>Esecuzione:<br>  python src/sensitivity.py</code> |
| `simulation.py` | Script Python. Esempio:<br><code>"""<br>Simulazione Monte Carlo del modello SIR.<br>Supporta parametri da riga di comando e seed per riproducibilità.<br><br>Esempi:</code> |
| `__init__.py` | Script Python. Esempio:<br><code>from .model import next_state, transition_matrix, N, BETA, GAMMA, I0, T_MAX, M, SEED<br>from .simulation import run_single, run_montecarlo<br>from .analysis import extinction_time, compute_stats, solve_ode_sir, get_mc_mean_std<br>from .plotting import (plot_single_trajectory, plot_mean_trajectory,<br>                        plot_tau_histogram, plot_sensitivity_comparison,</code> |
