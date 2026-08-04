# 🌐 Web Frontend (`docs/`)

<p align="center">
  <em>Landing page e dashboard interattiva ospitata nativamente su GitHub Pages per la presentazione dei risultati.</em>
</p>

## 📖 Table of Contents
- [🚀 Features](#-features)
- [🏗️ Architettura e Struttura dei File](#-architettura-e-struttura-dei-file)
- [💻 Analisi dei Componenti Core](#-analisi-dei-componenti-core)
- [🔗 Dipendenze e Flusso Dati](#-dipendenze-e-flusso-dati)
- [⚙️ Usage](#-usage)
- [⚠️ Developer Notes](#-developer-notes)

## 🚀 Features
- **Zero-Build Vanilla Stack**: Sviluppato interamente in HTML, CSS e JS puri, senza l'uso di bundler (no Vite, no Webpack) o framework JS pesanti (no React).
- **Glassmorphism Design**: Interfaccia grafica mozzafiato che usa gradienti avanzati e filtri `backdrop-filter: blur` per creare effetti traslucidi.
- **Image Modals & Tabs**: Sistema di navigazione tra analisi a schede con espansione modale per i grafici e animazioni fluide, il tutto codificato da zero.
- **Auto-Deploy GitHub Actions**: La pipeline invia automaticamente la cartella `docs/` online tramite `.github/workflows/deploy-pages.yml`.

## 🏗️ Architettura e Struttura dei File

```text
docs/
├── index.html       # Entry-point HTML5 semantico
├── style.css        # Variabili CSS, layout Grid/Flex e design system Glassmorphic
├── script.js        # Gestore di stato per i Tab, le Modali e gli event listener
└── img/             # (Copia in sync) Assets grafici serviti pubblicamente
```

Il design pattern è un frontend statico classico. Gli stili (CSS) e i comportamenti (JS) sono separati rigorosamente dall'impalcatura (HTML) per massimizzare la leggibilità.

## 💻 Analisi dei Componenti Core

### `style.css`
Il CSS utilizza variabili CSS native per il theming e funzioni moderne per l'ancoraggio e l'adattabilità.
```css
/* snippet da docs/style.css */
:root {
  --bg-color: #0f172a;
  --glass-bg: rgba(30, 41, 59, 0.7);
  --glass-border: rgba(255, 255, 255, 0.1);
  --accent: #38bdf8;
  --text-main: #f8fafc;
}
.glass-panel {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
}
```

### `script.js`
Il JavaScript ascolta gli eventi di interazione, garantendo la pulizia dello stato precedente e applicando le classi per scatenare i reflow CSS.

## 🔗 Dipendenze e Flusso Dati
- Non ci sono dipendenze `npm`.
- Il frontend dipende dalle immagini generate dagli script Python.
- Tutte le immagini contenute in `c:\Users\franc\Documents\sir-markov-chain\img\` devono essere sincronizzate dentro `docs/img/` prima del deploy, per poter essere risolte dal path statico di GitHub Pages.

## ⚙️ Usage
Puoi servire o visualizzare il sito in locale molto semplicemente:
```bash
# Entra nella directory e avvia il server python
cd docs/
python -m http.server 8000
# Apri http://localhost:8000
```
*(Oppure puoi fare doppio clicca su `index.html` per aprirlo direttamente dal browser!)*

## ⚠️ Developer Notes

> [!WARNING]  
> Mantenere `base: '/'` per i path degli asset statici. Poiché la root del dominio su GitHub Pages coincide con la radice del repo (se l'azione è configurata correttamente), non usare path assoluti. Usa sempre path relativi (es. `img/grafico.png`).

> [!IMPORTANT]
> L'aggiornamento automatico e il deploy in CI su GitHub avvengono solo tramite workflow. Qualsiasi modifica in questa directory andrà automaticamente online pochi secondi dopo un `git push`.
