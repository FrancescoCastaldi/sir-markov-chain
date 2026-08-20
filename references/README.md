# Materiali di Riferimento e Studio (`references/`)

Questa directory raccoglie tutti i materiali utili per la preparazione dell'esame di **Modelli Probabilistici (518512)** con il Prof. Salvatore Federico.

---

## 📁 Struttura della Cartella

```
references/
├── dispense/                                # Materiale di studio per l'esame orale
│   ├── probabilita_discreta.pdf             # Dispense ufficiali del Prof. Federico (167 pag.)
│   └── README.md                            # Indice argomenti teorici per l'orale
└── vecchie_prove/                           # Progetti di esempio (benchmark stilistico/strutturale)
    ├── relazione_mcmc_esempio.pdf           # Relazione di esempio (Alfonsi & Bucciarelli, 2025)
    ├── README.md                            # Analisi comparativa e spunti per il nostro progetto SIR
    └── code/                                # Codice sorgente Python del progetto di esempio
        ├── campionatore_gibbs.py
        ├── genera.py
        ├── genera_grafico_non_orientato.py
        ├── genera_risultati.py
        ├── generatore_colorazione.py
        ├── generazione_insiemi_indipendenti.py
        ├── generazione_insiemi_indipendenti_slow.py
        └── probabilities_vector.py
```

---

## 🎯 Scopo dei Materiali

### 1. Studio Orale (`references/dispense/`)
- **Dispense del Corso**: Documento di riferimento teorico (*Discrete probability theory with selected topics of discrete time stochastic processes*, Prof. S. Federico).
- **Utilizzo**: Studio approfondito della teoria su catene di Markov a tempo discreto, matrici di transizione, stati assorbenti, martingale e proprietà di Markov per la discussione orale.

### 2. Spunto Progetto (`references/vecchie_prove/`)
- **Progetto d'Esempio**: *Generazione casuale mediante catene di Markov* (Alfonsi & Bucciarelli, Luglio 2025).
- **Utilizzo**: Benchmark di riferimento per:
  - Struttura della relazione LaTeX (impostazione capitoli, grafici, rigore formale).
  - Stile delle presentazioni e del codice Python associato.
  - Livello di approfondimento richiesto dal docente.
