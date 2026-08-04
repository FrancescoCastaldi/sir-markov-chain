# 🌐 Web Frontend (`docs/`)

<p align="center">
  <em>Dashboard web ed esperienza visiva sviluppata in purissimo ecosistema Vanilla (zero-framework) con stile Glassmorphic, pubblicata automaticamente tramite CI/CD.</em>
</p>

---

## 📖 Indice dei Contenuti
1. [L'Obiettivo del Modulo Web](#1-lobiettivo-del-modulo-web)
2. [Albero Architetturale](#2-albero-architetturale)
3. [Deep-Dive nell'Implementazione Client-Side](#3-deep-dive-nellimplementazione-client-side)
   - [Zero-Build Layout (`index.html`)](#zero-build-layout-indexhtml)
   - [Design System (`style.css`)](#design-system-stylecss)
   - [Stato e Interattività (`script.js`)](#stato-e-interattività-scriptjs)
4. [Infrastruttura CI/CD e Deployment](#4-infrastruttura-cicd-e-deployment)
5. [Gotchas sul Routing Relativo](#5-gotchas-sul-routing-relativo)

---

## 1. L'Obiettivo del Modulo Web
Il web è lo strato di presentazione finale della repository. Molto del focus computazionale nei tool statistici (es. Python, R) è penalizzato dalla scarsa manutenibilità delle interfacce grafiche legacy (es. Tkinter). 
Abbiamo superato questo limite bypassando framework pesanti come React.js, adottando una struttura Vanilla pura, veloce, sicura e compatibile nativamente per il web-hosting statico fornito da GitHub.

## 2. Albero Architetturale

```text
docs/
├── index.html       # Documento DOM primario (scheletro semantico accessibile)
├── style.css        # Folio di stile per il theming Glassmorphism e layout responsive
├── script.js        # Controller JavaScript per modali di espansione immagini e Tab navigazionali
└── img/             # Asset binari consumati dal DOM (copia esatta the root img/ per sandboxing)
```

## 3. Deep-Dive nell'Implementazione Client-Side

L'ecosistema non richiede alcun build step (niente bundler o traspiratori come Webpack o Babel). Tutto è interpretato direttamente dal browser.

### Zero-Build Layout (`index.html`)
L'impalcatura definisce chiaramente sezioni isolate tramite i tag `id`. Questo permette all'interfaccia interattiva di saltare logicamente tra la sezione "Overview Statistica" e i diagrammi approfonditi.

### Design System (`style.css`)
La punta di diamante dell'esperienza utente.
Implementa un engine "Glassmorphism" che crea layer semi-trasparenti con blurring (offuscamento) dinamico dello sfondo (che è una geometria a gradienti animati), in stile iOS/macOS moderno.
```css
/* snippet core del design in docs/style.css */
:root {
  --bg-color: #0f172a;               /* Tailwind Slate-900 equivalente */
  --glass-bg: rgba(30, 41, 59, 0.7); /* Background traslucido */
  --glass-border: rgba(255, 255, 255, 0.1);
}

.glass-panel {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);       /* Magia grafica per l'effetto vetro satinato */
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}
```

### Stato e Interattività (`script.js`)
L'applicativo JavaScript è delegato alla mutazione procedurale delle classi CSS per mostrare e nascondere (fade) il contenuto dei container (logica `data-target`). Questo modulo cattura anche i clic per l'espansione dei grafici su un viewport Modal oscurato, prevenendo un caricamento separato in nuove schede browser fastidiose.

## 4. Infrastruttura CI/CD e Deployment
Il sistema è autonomo (Self-Driving). Quando una qualsiasi patch va in merge su `master` e altera i plot Python o questo sorgente `docs/`, i workflow `.github/workflows/deploy-pages.yml` entrano in gioco, montano la cartella come artefatto web, allocano un server cloud runner tramite l'API `actions/deploy-pages` ed erogano in push l'URL finale del sito. Zero configurazione server richiesta (No-Ops).

## 5. Gotchas sul Routing Relativo

> [!WARNING]  
> Quando crei i collegamenti a script, link ai fogli di stile o riferimenti d'immagine in `index.html`, **NON usare mai path assoluti (es. `/img/plot.png`)**. Su GitHub Pages, la repository è spesso servita tramite una sotto-cartella URL del domain account (es. `user.github.io/sir-markov-chain/`). Usare path assoluti distruggerebbe il fetch degli asset risolvendoli nella radice del tuo dominio GitHub al posto del repo. Usa stringhe come `./img/plot.png`.

> [!NOTE]
> Il browser impone policy di cache rigorose sui file CSS e JS. Se si testa localmente usando un web server python nativo (`python -m http.server`), ricordarsi di inibire la cache dalle impostazioni di sviluppo o fare `CTRL+F5` massivo per forzare il fetch delle nuove direttive glassmorphism.
