# Guida di Studio Slide-by-Slide: Modello SIR come Catena di Markov
**Corso**: Modelli Probabilistici (518512) — Università di Bologna  
**Docente**: Prof. Salvatore Federico  
**Deliverable di Riferimento**: `report/presentazione.pdf` (27 Slide) e `report/relazione.pdf` (14 Pagine)

---

## Indice delle Slide
1. [Slide 1 — Titolo e Frontespizio](#slide-1--titolo-e-frontespizio)
2. [Slide 2 — Introduzione e Motivazione](#slide-2--introduzione-e-motivazione)
3. [Slide 3 — Contesto Storico: Dal Determinismo alla Stocasticità](#slide-3--contesto-storico-dal-determinismo-alla-stocasticit)
4. [Slide 4 — Obiettivo del Lavoro](#slide-4--obiettivo-del-lavoro)
5. [Slide 5 — Richiamo Teorico: Catene di Markov a Tempo Discreto](#slide-5--richiamo-teorico-catene-di-markov-a-tempo-discreto)
6. [Slide 6 — Il Modello SIR: Compartimenti e Dinamica](#slide-6--il-modello-sir-compartimenti-e-dinamica)
7. [Slide 7 — Spazio degli Stati E](#slide-7--spazio-degli-stati-e)
8. [Slide 8 — Probabilità di Transizione ed Equazioni di Aggiornamento](#slide-8--probabilit-di-transizione-ed-equazioni-di-aggiornamento)
9. [Slide 9 — Esempio Analitico: N=3, beta=0.5, gamma=0.3](#slide-9--esempio-analitico-n3-beta05-gamma03)
10. [Slide 10 — Matrice di Transizione P e Forma Canonica](#slide-10--matrice-di-transizione-p-e-forma-canonica)
11. [Slide 11 — Struttura della Matrice P (Heatmap N=3, 10 Stati)](#slide-11--struttura-della-matrice-p-heatmap-n3-10-stati)
12. [Slide 12 — Classificazione degli Stati e Teorema di Assorbimento](#slide-12--classificazione-degli-stati-e-teorema-di-assorbimento)
13. [Slide 13 — Algoritmo di Simulazione Monte Carlo](#slide-13--algoritmo-di-simulazione-monte-carlo)
14. [Slide 14 — Implementazione Python (src/model.py)](#slide-14--implementazione-python-srcmodelpy)
15. [Slide 15 — Risultati Numerici della Simulazione (M=1000, Seed 42)](#slide-15--risultati-numerici-della-simulazione-m1000-seed-42)
16. [Slide 16 — Singola Traiettoria Stocastica](#slide-16--singola-traiettoria-stocastica)
17. [Slide 17 — Traiettoria Media e Bande di Dispersione (+-1 sigma)](#slide-17--traiettoria-media-e-bande-di-dispersione--1-sigma)
18. [Slide 18 — Ritratto di Fase (S, I) nello Spazio di Stato](#slide-18--ritratto-di-fase-s-i-nello-spazio-di-stato)
19. [Slide 19 — Distribuzione del Tempo di Estinzione tau](#slide-19--distribuzione-del-tempo-di-estinzione-tau)
20. [Slide 20 — Distribuzione dell'Attacco Finale R_infinito](#slide-20--distribuzione-dellattacco-finale-r_infinito)
21. [Slide 21 — Confronto con il Limite Fluido Deterministico (ODE)](#slide-21--confronto-con-il-limite-fluido-deterministico-ode)
22. [Slide 22 — Analisi di Sensibilità su R0 = beta / gamma](#slide-22--analisi-di-sensibilit-su-r0--beta--gamma)
23. [Slide 23 — Sintesi delle Evidenze Probabilistiche](#slide-23--sintesi-delle-evidenze-probabilistiche)
24. [Slide 24 — Confronto Metodologico: Teoria vs Simulazione](#slide-24--confronto-metodologico-teoria-vs-simulazione)
25. [Slide 25 — Limiti Modellistici e Scelte Progettuali](#slide-25--limiti-modellistici-e-scelte-progettuali)
26. [Slide 26 — Possibili Sviluppi ed Estensioni](#slide-26--possibili-sviluppi-ed-estensioni)
27. [Slide 27 — Conclusioni](#slide-27--conclusioni)

---

# SLIDE 1 — Titolo e Frontespizio

### 💡 A parole semplici: a cosa serve la slide
È la copertina di presentazione del lavoro. Serve a dichiarare l'argomento (simulare un'epidemia SIR come processo stocastico discreto), il corso universitario e la tecnologia/rigore impiegati.

### 📐 Spiegazione matematica & Formule
- **Processo Stocastico**: $\{X_t\}_{t \in \mathbb{N}}$ a valori nello spazio discreto $E$.
- **Vettore di Stato**: $X_t = (S_t, I_t, R_t) \in \mathbb{N}^3$ con vincolo $S_t + I_t + R_t = N$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"In due parole, qual è la differenza fondamentale tra il vostro approccio e il modello SIR classico dei libri di testo?"*
- **Tua Risposta**: *"Il modello classico usa equazioni differenziali ordinarie deterministiche e assume popolazioni infinite e continue. Il nostro approccio modella una popolazione finita di individui discreti mediante una Catena di Markov a tempo discreto, catturando la casualità intrinseca dei singoli contagi e guarigioni."*

---

# SLIDE 2 — Introduzione e Motivazione

### 💡 A parole semplici: a cosa serve la slide
Spiega cos'è un'epidemia a compartimenti in una popolazione chiusa (senza nascite né morti): chi è sano ($S$) può ammalarsi ($I$) e poi guarire diventando immune ($R$). Mostra perché la casualità è cruciale quando le persone sono poche.

### 📐 Spiegazione matematica & Formule
- **Popolazione Chiusa**: $N = \text{costante} \implies \forall t \ge 0, \; S_t + I_t + R_t = N$.
- **Flusso Unidirezionale**: $S \xrightarrow{\text{contagio}} I \xrightarrow{\text{guarigione}} R$ (non c'è reinfezione, immunità permanente).

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché nei piccoli focolai il modello deterministico fallisce?"*
- **Tua Risposta**: *"Perché per piccoli numeri di infetti (es. $I=1$ o $2$) la probabilità che tutti guariscano contemporaneamente prima di contagiare altri è alta. La versione deterministica predice sempre un'ondata epidemica media liscia, mentre nella realtà stocastica l'epidemia può spegnersi subito all'inizio con probabilità positiva."*

---

# SLIDE 3 — Contesto Storico: Dal Determinismo alla Stocasticità

### 💡 A parole semplici: a cosa serve la slide
Mette a confronto la storia: il modello a equazioni differenziali continue di Kermack-McKendrick (1927) contro il modello stocastico discreto introdotto da Bartlett (1949).

### 📐 Spiegazione matematica & Formule
- **ODE Continua (Kermack-McKendrick, 1927)**:
  $$\frac{ds}{dt} = -\beta si, \quad \frac{di}{dt} = \beta si - \gamma i, \quad \frac{dr}{dt} = \gamma i$$
  Traiettoria unica, liscia e deterministica.
- **Catena di Markov (Bartlett, 1949)**:
  Spazio di probabilità $(\Omega, \mathcal{F}, \mathbb{P})$, traiettorie aleatorie discrete, varianza campionaria $\text{Var}(X_t) > 0$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Cosa accade al modello stocastico quando la popolazione $N \to \infty$?"*
- **Tua Risposta**: *"Per il Teorema del Limite Fluido di Kurtz, normalizzando le variabili $s^{(N)}(t) = S_t/N$, il processo stocastico converge quasi certamente e uniformemente su intervalli finiti alla soluzione deterministica delle ODE."*

---

# SLIDE 4 — Obiettivo del Lavoro

### 💡 A parole semplici: a cosa serve la slide
Presenta la scaletta e i 3 pilastri metodologici del progetto:
1. **Analisi Teorica Esatta**: formalizzazione dello spazio degli stati $E$ e della matrice $P$.
2. **Simulazione Monte Carlo**: campionamento efficiente di 1000 traiettorie con Python/NumPy per $N=100$.
3. **Confronto e Validazione**: studio di sensibilità su $R_0$, ritratto di fase e verifica dei teoremi di assorbimento.

### 📐 Spiegazione matematica & Formule
- **Pilastro 1 (Algebra Lineare)**: $P \in \mathbb{R}^{|E| \times |E|}, \; (I-Q)\mathbf{t} = \mathbf{1}, \; B = (I-Q)^{-1}R$.
- **Pilastro 2 (Statistica Computazionale)**: Stimatori Monte Carlo $\bar{X} = \frac{1}{M}\sum_{m=1}^M X^{(m)}$ con errore $\sigma/\sqrt{M}$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché non avete calcolato la matrice teorica esatta anche per $N=100$?"*
- **Tua Risposta**: *"Perché per $N=100$ lo spazio degli stati ha cardinalità $\binom{102}{2} = 5151$. La matrice di transizione avrebbe oltre 26 milioni di elementi ($5151 \times 5151$) e la sua inversione richiederebbe miliardi di operazioni. Il metodo Monte Carlo fornisce stime statisticamente convergenti con una frazione minima del costo computazionale."*

---

# SLIDE 5 — Richiamo Teorico: Catene di Markov a Tempo Discreto

### 💡 A parole semplici: a cosa serve la slide
Fornisce le definizioni matematiche universali delle catene di Markov su cui si basa l'intero lavoro (assenza di memoria, matrice di transizione e stati assorbenti).

### 📐 Spiegazione matematica & Formule
- **Proprietà di Markov**:
  $$\mathbb{P}(X_{t+1} = j \mid X_t = i, X_{t-1} = i_{t-1}, \dots, X_0 = i_0) = \mathbb{P}(X_{t+1} = j \mid X_t = i) = P_{ij}$$
- **Omogeneità Temporale**: $P_{ij}$ non dipende dal tempo $t$.
- **Matrice Stocastica**:
  $$P_{ij} \ge 0, \quad \sum_{j \in E} P_{ij} = 1 \quad \forall i \in E$$
- **Stato Assorbente**: Uno stato $i$ tale che $P_{ii} = 1$ e $P_{ij} = 0$ per ogni $j \neq i$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Cosa garantisce l'omogeneità temporale nel nostro modello SIR?"*
- **Tua Risposta**: *"Garantisce che i parametri biologici $\beta$ (tasso di contagio) e $\gamma$ (tasso di guarigione) rimangano costanti durante tutta l'evoluzione temporale, cioè le regole di transizione non cambiano nel tempo."*

---

# SLIDE 6 — Il Modello SIR: Compartimenti e Dinamica

### 💡 A parole semplici: a cosa serve la slide
Mostra il diagramma a blocchi $S \to I \to R$ e spiega come nascono i nuovi contagi $C_t$ e le nuove guarigioni $G_t$ a ogni passo temporale.

### 📐 Spiegazione matematica & Formule
- **Probabilità di Infezione Individuale**:
  $$p_{\mathrm{SI}} = \beta \frac{I_t}{N}$$
- **Nuovi Contagiati ($C_t$)**: Somma di $S_t$ prove indipendenti di Bernoulli $\implies C_t \sim \text{Bin}\left(S_t, \, \beta \frac{I_t}{N}\right)$.
- **Nuovi Guariti ($G_t$)**: Somma di $I_t$ prove indipendenti di Bernoulli $\implies G_t \sim \text{Bin}(I_t, \, \gamma)$.
- **Indipendenza Condizionale**: Dati $S_t$ e $I_t$, $C_t$ e $G_t$ sono variabili aleatorie mutuamente indipendenti.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché la probabilità di contagio è proporzionale a $I_t / N$ e non solo a $I_t$?"*
- **Tua Risposta**: *"Perché assumiamo una trasmissione standard (*frequency-dependent* o a popolazione ben mescolata): un suscettibile ha un numero medio di contatti proporzionale alla frazione di infetti presenti nella popolazione totale, non al loro numero assoluto."*

---

# SLIDE 7 — Spazio degli Stati E

### 💡 A parole semplici: a cosa serve la slide
Risponde alla domanda: *"Quante sono tutte le possibili combinazioni di persone sane, malate e guarite?"* e spiega perché lo spazio degli stati cresce rapidamente con la popolazione.

### 📐 Spiegazione matematica & Formule
- **Insieme degli Stati**:
  $$E = \left\{ (s, i, r) \in \mathbb{N}^3 : s + i + r = N \right\}$$
- **Formula Combinatoria (Stars and Bars)**:
  $$|E| = \binom{N + 3 - 1}{3 - 1} = \binom{N + 2}{2} = \frac{(N+2)(N+1)}{2}$$
- **Esempi Calcolati**:
  - Per $N = 3 \implies |E| = \frac{5 \times 4}{2} = \mathbf{10 \text{ stati}}$.
  - Per $N = 100 \implies |E| = \frac{102 \times 101}{2} = \mathbf{5151 \text{ stati}}$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Come si dimostra la formula $\binom{N+2}{2}$?"*
- **Tua Risposta**: *"Fissato il numero di suscettibili $s \in \{0, 1, \dots, N\}$, rimangono $N-s$ individui da dividere tra $i$ ed $r$. Poiché $r = N - s - i$, l'indice $i$ può assumere $N - s + 1$ valori distinti. Sommando su tutti gli $s$ possibili: $\sum_{s=0}^N (N - s + 1) = \sum_{k=1}^{N+1} k = \frac{(N+1)(N+2)}{2}$."*

---

# SLIDE 8 — Probabilità di Transizione ed Equazioni di Aggiornamento

### 💡 A parole semplici: a cosa serve la slide
Spiega come il sistema passa dallo stato attuale $(S_t, I_t, R_t)$ allo stato del giorno successivo $(S_{t+1}, I_{t+1}, R_{t+1})$ sottraendo e sommando i contagi $C_t$ e le guarigioni $G_t$.

### 📐 Spiegazione matematica & Formule
- **Sistema di Aggiornamento di Stato**:
  $$\begin{cases}
  S_{t+1} = S_t - C_t \\
  I_{t+1} = I_t + C_t - G_t \\
  R_{t+1} = R_t + G_t
  \end{cases}$$
- **Conservazione della Popolazione**:
  $$S_{t+1} + I_{t+1} + R_{t+1} = (S_t - C_t) + (I_t + C_t - G_t) + (R_t + G_t) = S_t + I_t + R_t = N$$
- **Monotonicità**: $S_{t+1} \le S_t$ (decrescente), $R_{t+1} \ge R_t$ (crescente).

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"È possibile che da uno stato si torni indietro a uno stato precedente?"*
- **Tua Risposta**: *"No, la catena è rigorosamente aciclica. Poiché il numero di rimossi $R_t$ è monotonicamente non decrescente ($G_t \ge 0$), non esiste alcuna sequenza di transizioni a probabilità positiva che possa riportare il sistema a uno stato con un numero inferiore di rimossi."*

---

# SLIDE 9 — Esempio Analitico: N=3, beta=0.5, gamma=0.3

### 💡 A parole semplici: a cosa serve la slide
Mostra il calcolo manuale esatto passo-passo della riga della matrice per lo stato iniziale $(2, 1, 0)$ (2 sani, 1 malato, 0 guariti) su una popolazione piccolissima di $N=3$.

### 📐 Spiegazione matematica & Formule
- **Parametri**: $N=3, \; \beta=0.5, \; \gamma=0.3, \; s=2, \; i=1, \; r=0$.
- **Probabilità di Contagio**: $p_{\mathrm{SI}} = \beta \frac{i}{N} = 0.5 \times \frac{1}{3} = \frac{1}{6}$.
- **Distribuzioni Binomiali**:
  - Nuovi contagi $C \sim \text{Bin}(2, 1/6)$:
    - $P(C=0) = (5/6)^2 = \frac{25}{36}$
    - $P(C=1) = 2 \times \frac{1}{6} \times \frac{5}{6} = \frac{10}{36}$
    - $P(C=2) = (1/6)^2 = \frac{1}{36}$
  - Nuove guarigioni $G \sim \text{Bin}(1, 0.30)$:
    - $P(G=0) = 0.70$
    - $P(G=1) = 0.30$
- **Tabella delle 6 Transizioni Possibili**:
  $$\begin{array}{cccclc}
  \hline
  C & G & \text{Nuovo Stato } (s', i', r') & \text{Calcolo } P(C) \times P(G) & \text{Frazione} & \text{Decimale} \\
  \hline
  0 & 0 & (2, 1, 0) & \frac{25}{36} \times 0.7 & 17.5 / 36 & \mathbf{0.4861} \\
  0 & 1 & (2, 0, 1) & \frac{25}{36} \times 0.3 & 7.5 / 36 & \mathbf{0.2083} \\
  1 & 0 & (1, 2, 0) & \frac{10}{36} \times 0.7 & 7.0 / 36 & \mathbf{0.1944} \\
  1 & 1 & (1, 1, 1) & \frac{10}{36} \times 0.3 & 3.0 / 36 & \mathbf{0.0833} \\
  2 & 0 & (0, 3, 0) & \frac{1}{36} \times 0.7 & 0.7 / 36 & \mathbf{0.0194} \\
  2 & 1 & (0, 2, 1) & \frac{1}{36} \times 0.3 & 0.3 / 36 & \mathbf{0.0083} \\
  \hline
  \end{array}$$
- **Verifica Somma Stocastica**: $\sum P = \frac{17.5 + 7.5 + 7.0 + 3.0 + 0.7 + 0.3}{36} = \frac{36}{36} = \mathbf{1.0000}$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché moltiplica direttamente $P(C) \times P(G)$?"*
- **Tua Risposta**: *"Perché condizionatamente allo stato corrente $(S_t, I_t)$, il processo di contagio dei suscettibili e il processo di guarigione degli infetti avvengono tra individui disgiunti e sono variabili aleatorie stocasticamente indipendenti."*

---

# SLIDE 10 — Matrice di Transizione P e Forma Canonica

### 💡 A parole semplici: a cosa serve la slide
Scrive la formula generale della matrice $P$ per qualunque stato e mostra come riordinare le righe dividendo gli stati in due gruppi: quelli transitori ($Q$) e quelli assorbenti ($I$).

### 📐 Spiegazione matematica & Formule
- **Formula Generale a Doppia Sommatoria**:
  $$P\big((s,i,r), (s',i',r')\big) = \sum_{c=0}^s \sum_{g=0}^i \binom{s}{c} p_{\mathrm{SI}}^c (1-p_{\mathrm{SI}})^{s-c} \binom{i}{g} \gamma^g (1-\gamma)^{i-g} \cdot \mathbf{1}_{\{s'=s-c, \; i'=i+c-g, \; r'=r+g\}}$$
- **Forma Canonica a Blocchi**:
  $$P = \begin{pmatrix} 
  Q & R \\ 
  0 & I 
  \end{pmatrix}$$
  - $Q \in \mathbb{R}^{d_T \times d_T}$: transizioni tra stati transitori ($\mathcal{T} \to \mathcal{T}$).
  - $R \in \mathbb{R}^{d_T \times d_A}$: transizioni da transitori verso assorbenti ($\mathcal{T} \to \mathcal{A}$).
  - $0$: dall'insieme assorbente non si può tornare nei transitori.
  - $I$: matrice identità ($P_{xx} = 1$).

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché tutti gli autovalori di $Q$ sono strettamente minori di 1 in modulo ($\rho(Q) < 1$)?"*
- **Tua Risposta**: *"Perché tutti gli stati in $\mathcal{T}$ sono transitori e la catena è a stati finiti con assorbimento quasi certo. Ciò implica $\lim_{n \to \infty} Q^n = 0$, condizione necessaria e sufficiente affinché il raggio spettrale sia $\rho(Q) < 1$ e la serie di Neumann converga a $(I-Q)^{-1}$."*

---

# SLIDE 11 — Struttura della Matrice P (Heatmap N=3, 10 Stati)

### 💡 A parole semplici: a cosa serve la slide
Mostra la foto/mappa a colori della matrice $10 \times 10$ calcolata per $N=3$, evidenziando dove si concentrano le probabilità e dove ci sono gli zeri.

### 📐 Spiegazione matematica & Formule
- **I 4 Stati Assorbenti ($I=0$)**:
  $(0,0,3), (1,0,2), (2,0,1), (3,0,0)$.
  Hanno probabilità $1.00$ sulla diagonale principale ($P_{xx}=1.0$).
- **Regione Triangolare Superiore a Zeri**:
  Tutte le celle con $r' < r$ valgono rigorosamente $0.00$, confermando visivamente l'irreversibilità e l'aciclicità della catena.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Come individua a colpo d'occhio gli stati assorbenti sulla heatmap?"*
- **Tua Risposta**: *"Sono le righe che presentano una sola cella con valore 1.0 sulla diagonale principale e valore 0.0 su tutte le altre colonne. Corrispondono esattamente agli stati con $I=0$ contrassegnati con l'asterisco."*

---

# SLIDE 12 — Classificazione degli Stati e Teorema di Assorbimento

### 💡 A parole semplici: a cosa serve la slide
È il cuore teorico del progetto: dimostra che l'epidemia deve finire per forza al 100% in tempo finito ($\mathbb{P}(\tau < \infty)=1$) e fornisce la formula esatta per calcolare il tempo medio di durata.

### 📐 Spiegazione matematica & Formule
- **Partizione dello Spazio degli Stati**:
  $$E = \mathcal{A} \cup \mathcal{T}, \quad \mathcal{A} \cap \mathcal{T} = \emptyset$$
  - $\mathcal{A} = \{(s,i,r) \in E : i=0\}$ con cardinalità $|\mathcal{A}| = N + 1$.
  - $\mathcal{T} = \{(s,i,r) \in E : i>0\}$ con cardinalità $|\mathcal{T}| = \binom{N+2}{2} - (N+1) = \frac{N(N+1)}{2}$.
- **Teorema di Assorbimento Quasi Certo**:
  $$\mathbb{P}(\tau < \infty) = 1, \quad \text{dove } \tau = \inf\{t \ge 0 : I_t = 0\}$$
- **Tempo Medio di Assorbimento (First-Step Analysis)**:
  $$t_i = 1 + \sum_{j \in \mathcal{T}} Q_{ij} t_j \implies (I - Q)\mathbf{t} = \mathbf{1} \implies \mathbf{t} = (I - Q)^{-1}\mathbf{1}$$

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Cosa rappresenta ogni singolo elemento $N_{ij}$ della matrice fondamentale $(I-Q)^{-1}$?"*
- **Tua Risposta**: *"L'elemento $(I-Q)^{-1}_{ij}$ rappresenta il numero medio atteso di visite allo stato transitorio $j$ prima dell'assorbimento finale, partendo dallo stato iniziale $i$."*

---

# SLIDE 13 — Algoritmo di Simulazione Monte Carlo

### 💡 A parole semplici: a cosa serve la slide
Spiega come funziona il computer: la procedura di campionamento passo per passo e la tabella ufficiale dei 7 parametri usati nelle simulazioni ($N=100$, $\beta=0.20$, $\gamma=0.10$, $R_0=2.00$, $M=1000$, Seed 42).

### 📐 Spiegazione matematica & Formule
- **Durata Media Infezione**: $D = \frac{1}{\gamma} = \frac{1}{0.10} = \mathbf{10 \text{ passi}}$.
- **Numero di Riproduzione di Base**:
  $$R_0 = \frac{\beta}{\gamma} = \frac{0.20}{0.10} = \mathbf{2.00} > 1 \quad (\text{Regime Sovracritico})$$
- **Errore Standard Monte Carlo**:
  $$\text{SE}(\bar{X}) = \frac{\sigma}{\sqrt{M}} = \frac{\sigma}{\sqrt{1000}} \approx \frac{\sigma}{31.62} \approx 3\% \text{ di } \sigma$$

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"A cosa serve specificare 'Seed 42'?"*
- **Tua Risposta**: *"Garantisce la totale riproducibilità scientifica deterministica: impostando il generatore pseudo-casuale con lo stesso seed, qualsiasi ricercatore otterrà esattamente gli stessi identici numeri e grafici al decimale."*

---

# SLIDE 14 — Implementazione Python (`src/model.py`)

### 💡 A parole semplici: a cosa serve la slide
Mostra il codice sorgente Python che esegue un passo dell'epidemia in tempo istantaneo $O(1)$ sfruttando NumPy.

### 📐 Spiegazione matematica & Formule
```python
def next_state(s, i, r, n=100, beta=0.2, gamma=0.1):
    if i == 0:
        return s, 0, r  # Stato assorbente P_xx = 1
    p_si = beta * i / n
    new_infections = int(np.random.binomial(s, p_si))  # C_t ~ Bin
    recoveries = int(np.random.binomial(i, gamma))  # G_t ~ Bin
    return s - new_infections, i + new_infections - recoveries, r + recoveries
```

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché ha usato `np.random.binomial` invece di simulare singolarmente ogni individuo?"*
- **Tua Risposta**: *"Perché sotto l'ipotesi di popolazione ben mescolata, tutti i suscettibili hanno la stessa probabilità indipendente di contagio $p_{\mathrm{SI}}$. La somma di $S$ prove di Bernoulli indipendenti è analiticamente identica a una Binomiale $\text{Bin}(S, p_{\mathrm{SI}})$, ma computazionalmente infinitamente più veloce."*

---

# SLIDE 15 — Risultati Numerici della Simulazione (M=1000, Seed 42)

### 💡 A parole semplici: a cosa serve la slide
Presenta la tabella riassuntiva ufficiale con i 4 numeri chiave dell'epidemia calcolati su 1000 simulazioni.

### 📐 Spiegazione matematica & Formule
$$\begin{array}{lcccc}
\hline
\textbf{Indicatore} & \textbf{Media } \mathbb{E} & \textbf{Dev. Std } \sigma & \textbf{Minimo} & \textbf{Massimo} \\
\hline
\text{Picco Infetti } I_{\max} & \mathbf{21.94} & 4.52 & 5 & 39 \\
\text{Tempo al Picco } t_{\text{peak}} & \mathbf{24.12} & 6.31 & 0 & 48 \\
\text{Tempo Estinzione } \tau & \mathbf{86.66} & 22.81 & 18 & 195 \\
\text{Attacco Finale } R_\infty & \mathbf{76.59} & 8.41 & 5 & 94 \\
\hline
\end{array}$$

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché il picco medio stocastico è circa 22 mentre la curva ODE deterministica arriva a 30?"*
- **Tua Risposta**: *"È l'effetto di taglia finita (*finite-size effect*) per $N=100$: le traiettorie stocastiche non raggiungono il picco tutte nello stesso giorno. Facendo la media temporale su curve sfasate nel tempo, i picchi si mediano con valori più bassi, abbassando la media aggregata a $\sim 22$."*

---

# SLIDE 16 — Singola Traiettoria Stocastica

### 💡 A parole semplici: a cosa serve la slide
Mostra il grafico di un'epidemia reale (con Seed 42): si vedono la latenza iniziale, l'impennata dei contagi a gradini e l'arresto finale a zero.

### 📐 Spiegazione matematica & Formule
- **Condizione Iniziale**: $X_0 = (95, 5, 0)$.
- **Latenza Stocastica**: $t \in [0, 50]$ con $I_t \le 10$.
- **Picco Reale**: $I_{\max} = 18$ infetti al passo $t = 78$.
- **Estinzione & Assorbimento**: $\tau = 124$ con stato finale $(17, 0, 83) \in \mathcal{A}$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Cosa rappresentano i piccoli gradini visibili sulla curva blu dei suscettibili?"*
- **Tua Risposta**: *"Rappresentano la natura discreta dei contagi: la popolazione è quantizzata in individui interi, quindi ad ogni passo $S_t$ scende a salti di ampiezza intera $C_t \in \{0, 1, 2, \dots\}$."*

---

# SLIDE 17 — Traiettoria Media e Bande di Dispersione (+-1 sigma)

### 💡 A parole semplici: a cosa serve la slide
Mostra cosa succede mediando 1000 epidemie: le curve diventano lisce e la fascia colorata mostra dove cade la maggior parte delle epidemie reali ($68\%$).

### 📐 Spiegazione matematica & Formule
- **Media Monte Carlo**: $\bar{S}(t) = \frac{1}{M}\sum_{m=1}^M S^{(m)}(t)$.
- **Banda di Dispersione**: $[\bar{I}(t) - \sigma_I(t), \; \bar{I}(t) + \sigma_I(t)]$.
- **Massima Dispersione**: $\sigma_I(t)$ raggiunge il massimo nella fase centrale $t \in [15, 35]$ (massima eterogeneità di fase).

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché la fascia di dispersione diventa strettissima per $t > 120$?"*
- **Tua Risposta**: *"Perché oltre il passo 120 la quasi totalità delle simulazioni ha già raggiunto l'assorbimento ($I_t=0$), quindi la varianza della frazione di infetti decade a zero."*

---

# SLIDE 18 — Ritratto di Fase (S, I) nello Spazio di Stato

### 💡 A parole semplici: a cosa serve la slide
Elimina il tempo e mostra la traiettoria geometrica nel piano $(S, I)$ come un triangolo in cui tutte le curve rosse finiscono per schiantarsi sul pavimento verde $I=0$.

### 📐 Spiegazione matematica & Formule
- **Simplesso 2D**: $S \ge 0, \; I \ge 0, \; S + I \le N$.
- **Equazione dell'Orbita Deterministica**:
  $$\frac{dI}{dS} = \frac{\beta S I - \gamma I}{-\beta S I} = -1 + \frac{\gamma}{\beta S} = -1 + \frac{N}{R_0 S}$$
- **Soglia di Picco**:
  $$\frac{dI}{dS} = 0 \iff S^* = \frac{N}{R_0} = \frac{100}{2.0} = \mathbf{50 \text{ individui}}$$

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché la pendenza dell'orbita cambia segno quando $S$ scende sotto 50?"*
- **Tua Risposta**: *"Perché quando $S > 50$, abbiamo $S > N/R_0 \implies \frac{dI}{dS} < 0$, quindi muovendoci verso sinistra ($S$ decresce) $I$ cresce. Quando $S < 50$, la pendenza diventa positiva, quindi $I$ comincia a calare verso l'asse $I=0$."*

---

# SLIDE 19 — Distribuzione del Tempo di Estinzione tau

### 💡 A parole semplici: a cosa serve la slide
Mostra l'istogramma di quanto dura l'epidemia: la maggior parte finisce tra 60 e 90 giorni, ma alcune durano fino a quasi 200 giorni a causa di pochi infetti che resistono a lungo.

### 📐 Spiegazione matematica & Formule
- **Media Empirica**: $\bar{\tau} = 86.66$ passi.
- **Asimmetria Positiva (*Right-Skewed*)**: Moda a $75-80$ passi, coda allungata fino a $\tau_{\max} = 195$.
- **Legame con la Teoria**: Stima Monte Carlo dell'elemento iniziale del vettore $\mathbf{t} = (I - Q)^{-1}\mathbf{1}$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché la distribuzione dei tempi di estinzione non è simmetrica come una Gaussiana?"*
- **Tua Risposta**: *"A causa del comportamento a bassi numeri infettivi nella fase finale: quando rimane 1 solo infetto, il passaggio di testimone tramite contagi singoli rari può protrarsi casualmente a lungo prima dell'estinzione, generando una coda allungata verso destra."*

---

# SLIDE 20 — Distribuzione dell'Attacco Finale R_infinito

### 💡 A parole semplici: a cosa serve la slide
Mostra quante persone si ammalano complessivamente alla fine dell'epidemia: la massa si concentra attorno al $77\%$ per effetto dell'immunità di gregge.

### 📐 Spiegazione matematica & Formule
- **Attacco Finale Medio**: $\bar{R}_\infty = 76.59 \pm 8.41$ individui.
- **Matrice delle Probabilità di Assorbimento**:
  $$B = (I - Q)^{-1} R \in \mathbb{R}^{|\mathcal{T}| \times |\mathcal{A}|}$$
  Ciascuna barra stima la probabilità $B_{(95,5,0), \, (100-r, 0, r)}$.
- **Soglia di Immunità di Gregge**:
  $$p_c = 1 - \frac{1}{R_0} = 1 - \frac{1}{2.0} = 50\%$$

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché si vedono alcune rare barre isolate a $R_\infty = 5$ all'estrema sinistra?"*
- **Tua Risposta**: *"Rappresentano le estinzioni precoci: eventi rari (probabilità teorica $\approx (1/R_0)^5 \approx 3.1\%$) in cui tutti i 5 infetti iniziali guariscono subito senza generare una pandemia maggiore."*

---

# SLIDE 21 — Confronto con il Limite Fluido Deterministico (ODE)

### 💡 A parole semplici: a cosa serve la slide
Mette a confronto diretto la curva stocastica reale con la curva ideale continua delle equazioni differenziali classiche.

### 📐 Spiegazione matematica & Formule
- **Sistema ODE**:
  $$\frac{ds}{dt} = -\beta si, \quad \frac{di}{dt} = (\beta s - \gamma)i, \quad \frac{dr}{dt} = \gamma i$$
- **Differenza al Picco**:
  - Picco ODE: $I_{\max}^{\text{ODE}} \approx 30.0\%$ a $t \approx 20$.
  - Picco Stocastico Medio: $\bar{I}_{\max} \approx 21.9\%$ a $t \approx 24$.
- **Limite Fluido (Kurtz)**: Convergenza esatta per $N \to \infty$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Qual è la causa principale della differenza di altezza del picco tra ODE e stocastico?"*
- **Tua Risposta**: *"La desincronizzazione temporale (*phase jitter*) tra le traiettorie stocastiche: poiché ogni simulazione raggiunge il picco a giorni diversi a causa della latenza casuale, la media punto a punto spalma e abbassa il picco medio rispetto all'ODE deterministica."*

---

# SLIDE 22 — Analisi di Sensibilità su R0 = beta / gamma

### 💡 A parole semplici: a cosa serve la slide
Fa vedere cosa succede se il virus è più debole o più forte: dimostra che sotto $R_0 = 1$ non c'è epidemia, mentre sopra $R_0 = 1$ più il virus è aggressivo più il picco è alto e rapido (effetto "appiattire la curva").

### 📐 Spiegazione matematica & Formule
- **I 5 Scenari Testati ($\gamma=0.10$)**:
  1. $R_0 = 0.8 \; (\beta=0.08) \implies$ Nessun picco, estinzione immediata ($\tau \approx 18$).
  2. $R_0 = 1.2 \; (\beta=0.12) \implies$ Picco $I \approx 8\%$ al passo $t \approx 45$.
  3. $R_0 = 2.0 \; (\beta=0.20) \implies$ Picco $I \approx 22\%$ al passo $t \approx 24$.
  4. $R_0 = 3.0 \; (\beta=0.30) \implies$ Picco $I \approx 38\%$ al passo $t \approx 15$.
  5. $R_0 = 5.0 \; (\beta=0.50) \implies$ Picco $I \approx 57\%$ al passo $t \approx 9.8$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Cosa accade matematicamente al punto fisso $I=0$ quando $R_0$ attraversa il valore 1?"*
- **Tua Risposta**: *"Si verifica una biforcazione transcritica: per $R_0 \le 1$ lo stato privo di malattia (*disease-free equilibrium*) è asintoticamente stabile; per $R_0 > 1$ perde stabilità e il sistema viene attratto verso lo stato epidemico endemico/transitorio."*

---

# SLIDE 23 — Sintesi delle Evidenze Probabilistiche

### 💡 A parole semplici: a cosa serve la slide
Riepiloga i 4 risultati scientifici e probabilistici più importanti ottenuti dall'intero studio.

### 📐 Spiegazione matematica & Formule
1. **Assorbimento Certo**: $\mathbb{P}(\tau < \infty) = 1$ confermato al 100% su 1000 simulazioni.
2. **Variabilità Intrinseca**: Ampio intervallo campionario sul picco ($I_{\max} \in [5, 39]$).
3. **Biforcazione a Soglia $R_0=1$**: Separazione netta tra estinzione immediata e invasione.
4. **Accordo Asintotico con le ODE**: Validazione qualitativa del limite continuo.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Qual è la conclusione principale dal punto di vista della teoria della probabilità?"*
- **Tua Risposta**: *"Che la dinamica epidemica su scala di popolazione finita è intrinsecamente non deterministica: la media non descrive da sola la realtà, ed è indispensabile quantificare la distribuzione di probabilità dei tempi di estinzione e dell'attacco finale."*

---

# SLIDE 24 — Confronto Metodologico: Teoria vs Simulazione

### 💡 A parole semplici: a cosa serve la slide
Mette a confronto i due strumenti usati: quando conviene usare l'algebra lineare esatta ($(I-Q)^{-1}$) e quando conviene usare il Monte Carlo.

### 📐 Spiegazione matematica & Formule
- **Approccio Algebrico Esatto**:
  - Vantaggi: Soluzione chiusa esatta, nessun errore statistico.
  - Limiti: Complessità $\mathcal{O}(|E|^3) = \mathcal{O}(N^6)$ per l'inversione matriciale. Trattabile solo per $N \le 10$.
- **Approccio Monte Carlo**:
  - Vantaggi: Complessità lineare $\mathcal{O}(M \cdot \bar{\tau})$, scalabile per qualsiasi $N$.
  - Limiti: Errore campionario residuo $\mathcal{O}(1/\sqrt{M})$.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Perché l'inversione matriciale scala come $N^6$?"*
- **Tua Risposta**: *"Poiché la dimensione dello spazio degli stati è $|E| \approx N^2/2$, la matrice $Q$ ha dimensione $\frac{N^2}{2} \times \frac{N^2}{2}$. L'algoritmo di inversione di Gauss-Jordan ha costo cubico nella dimensione della matrice: $(N^2)^3 = N^6$."*

---

# SLIDE 25 — Limiti Modellistici e Scelte Progettuali

### 💡 A parole semplici: a cosa serve la slide
Dimostra maturità critica evidenziando le ipotesi semplificative adottate (popolazione chiusa, miscelamento omogeneo, parametri costanti).

### 📐 Spiegazione matematica & Formule
- **Ipotesi di Omogeneità**: Tutti i contatti sono equiprobabili (nessuna rete sociale complessa).
- **Assenza di Demografia**: Nessuna nascita ($\mu = 0$) né morte non epidemica.
- **Parametri Stazionari**: $\beta$ e $\gamma$ costanti nel tempo.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Cosa cambierebbe introducendo un tasso di natalità $\mu > 0$ e mortalità $\mu > 0$?"*
- **Tua Risposta**: *"I nuovi nati entrerebbero nel compartimento dei suscettibili ($S$), rimpiazzando continuamente gli individui immunizzati. In questo caso gli stati con $I=0$ non sarebbero più l'unico destino inevitabile e potrebbe instaurarsi uno stato stazionario endemico con persistenza indefinita del virus."*

---

# SLIDE 26 — Possibili Sviluppi ed Estensioni

### 💡 A parole semplici: a cosa serve la slide
Mostra come espandere il modello verso applicazioni avanzate di ricerca (modelli su grafi, compartimento esposto $E$, tassi tempo-varianti).

### 📐 Spiegazione matematica & Formule
1. **Catene di Markov su Grafi di Contatto**: Matrice di adiacenza $A_{ij} \in \{0, 1\}$, probabilità individuale $p_i(t) = 1 - \prod_{j \in \mathcal{N}(i)} (1 - \beta A_{ij} I_j)$.
2. **Modello SEIR**: Inserimento del periodo di latenza/incubazione ($S \to E \to I \to R$).
3. **Controllo Ottimo e Tassi Variabili $\beta(t)$**: Modellazione di lockdown e campagne vaccinali.

### ⚠️ Possibile domanda del Prof & Risposta perfetta
- **Prof**: *"Come cambierebbe la matrice di transizione introducendo il compartimento degli esposti $E$ (modello SEIR)?"*
- **Tua Risposta**: *"Lo stato diventerebbe una quadrupla $(S, E, I, R)$ con vincolo $S+E+I+R=N$. La dimensione dello spazio degli stati crescerebbe a $\binom{N+3}{3} \approx \mathcal{O}(N^3)$, aumentando la complessità combinatoria ma consentendo di modellare il periodo di incubazione asintomatico."*

---

# SLIDE 27 — Conclusioni

### 💡 A parole semplici: a cosa serve la slide
Chiude la presentazione riassumendo il valore scientifico del lavoro e ringraziando la commissione per l'attenzione.

### 📐 Spiegazione matematica & Formule
- **Sintesi del Contributo**:
  - Integrazione completa tra teoria analitica delle Catene di Markov e simulazione stocastica Monte Carlo.
  - Validazione sperimentale dei teoremi di assorbimento e del limite fluido continuo.
  - Repository aperto, documentato, modulare e testato al 100%.

### ⚠️ Possibile domanda finale del Prof & Risposta perfetta
- **Prof**: *"Se dovesse riassumere in una sola frase il messaggio chiave del vostro progetto?"*
- **Tua Risposta**: *"La modellazione probabilistica dimostra che la casualità microscopica modella in modo determinante l'evoluzione macroscopica delle epidemie su popolazioni finite, rendendo la Catena di Markov uno strumento indispensabile per quantificare il rischio e la variabilità reale rispetto ai modelli continui classici."*
