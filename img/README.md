# 📊 Visual Assets (`img/`)

<p align="center">
  <em>Esportazione e stoccaggio degli output grafici e vettoriali finali della simulazione.</em>
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Architettura e Struttura dei File](#-architettura-e-struttura-dei-file)
- [💻 Analisi dei Componenti Core](#-analisi-dei-componenti-core)
- [🔗 Dipendenze e Flusso Dati](#-dipendenze-e-flusso-dati)
- [⚙️ Usage](#-usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- **High-Resolution Graphics**: Target specifico (DPI=150+) richiesto dalla stampa su foglio A4 (per la relazione accademica).
- **Tracciabilità via Git**: Mantenimento di versioni "pulite" e riproducibili delle pipeline stocastiche.
- **Supporto multi-media**: Formato PNG primario per garantire compatibilità con LaTeX (pdflatex) e i frontend web HTML (incluso GitHub Pages).

## 🏗️ Architettura e Struttura dei File

```text
img/
├── mean_trajectory.png          # Plot aggregato M-simulazioni con barre d'errore (std)
├── single_trajectory.png        # Plot campione di un'estrazione casuale
├── tau_histogram.png            # Distribuzione empirica del tempo di fine epidemia
├── ode_comparison.png           # Confronto tra traiettoria stocastica media ed equazione deterministica
└── sensitivity_comparison.png   # Studio sull'influenza del parametro R_0 = beta/gamma
```

A differenza di una directory di codice, questa directory costituisce il *Sink* (pozzo) della pipeline di dati. Non contiene logica o comportamento, ma rappresenta l'evidenza scientifica del corretto funzionamento della libreria.

## 💻 Analisi dei Componenti Core

(N/A - Non vi sono file di codice eseguibile, ma output passivi gestiti dal modulo `plotting.py`).

## 🔗 Dipendenze e Flusso Dati
- **Scrittura**: Aggiornata in sola scrittura (`Write-Only`) da `src/plotting.py` invocato da `src/simulation.py` o `src/sensitivity.py`.
- **Lettura**: Consumata in lettura (`Read-Only`) dai file LaTeX in `report/` e dai file HTML/JS in `docs/`.

## ⚙️ Usage
Per rigenerare tutte le immagini da zero usando i medesimi seed (riproducibilità):

```bash
# Esegui le simulazioni (rigenera mean_trajectory, single_trajectory, tau_histogram, ode_comparison)
python src/simulation.py --seed 42 --sims 1000

# Esegui la sensibilità (rigenera sensitivity_comparison)
python src/sensitivity.py --seed 42 --sims 500
```

## ⚠️ Developer Notes

> [!WARNING]  
> Poiché questi file binari causano problemi nell'history di Git se vengono aggiornati continuamente e con leggere variazioni impercettibili, consigliamo caldamente di generarli solo nelle versioni finali, usando i seed impostati. Modifiche temporanee per scopi di debugging dovrebbero essere salvate in `plots/` (che è opportunamente ignorata in `.gitignore`).

> [!NOTE]
> Su GitHub, puoi visualizzare in tempo reale questi asset cliccandoci sopra, ma per lo studio complessivo si raccomanda la navigazione della dashboard interattiva su GitHub Pages (vedi `docs/README.md`).
