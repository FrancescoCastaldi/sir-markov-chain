# Presentazione Orale — Modello SIR come Catena di Markov

**Corso**: Metodi Probabilistici per le Applicazioni / Modelli Probabilistici (518512)  
**Docente**: Prof. Salvatore Federico  
**Studente**: Francesco Castaldi  
**A.A.**: 2025/2026

---

# A. Struttura Completa della Presentazione (27 Slide)

| # | Slide | Contenuto Principale | Supporto Visivo / Grafico |
|---|-------|----------------------|---------------------------|
| 1 | Titolo | Presentazione del progetto d'esame | Layout Beamer Madrid |
| 2 | Introduzione e Motivazione | Contestualizzazione e formalismo stocastico | Box didattico |
| 3 | Contesto Storico | Dal Determinismo ODE (1927) a Bartlett Stocastico (1949) | Confronto concettuale |
| 4 | Obiettivo del Lavoro | Formalizzazione, assorbimento, Monte Carlo | Elenco strutturato a 3 livelli |
| 5 | Richiamo Teorico | Proprietà di Markov, matrice stocastica, assorbimento | Formule matematiche |
| 6 | Il Modello SIR | Compartimenti $S, I, R$ e vincolo $S+I+R=N$ | **Diagramma a blocchi TikZ** + Tabella |
| 7 | Spazio degli Stati $E$ | Definizione e formula combinatoria $|E|=\binom{N+2}{2}$ | Esempi $N=3$ (10) e $N=100$ (5151) |
| 8 | Probabilità di Transizione | Contagio e guarigione Binomiali indipendenti | Formule di aggiornamento lineare |
| 9 | Esempio Analitico $N=3$ | Calcolo esplicito riga dello stato $(2,1,0)$ | **Tabella stocastica 6 transizioni** |
| 10 | Matrice di Transizione $P$ | Formula analitica e forma canonica a blocchi | Sottomatrici $Q, R, I$ |
| 11 | Struttura Matrice ($N=3$) | Heatmap matrice $P$ $10 \times 10$ e stati assorbenti | **Figura: `transition_heatmap.png`** |
| 12 | Classificazione Stati | Partizione $\mathcal{A}$ e $\mathcal{T}$, proof assorbimento | Teorema $\mathbb{P}(\tau<\infty)=1$, $(I-Q)\mathbf{t}=\mathbf{1}$ |
| 13 | Algoritmo Monte Carlo | Campionamento stocastico, seed 42, $M=1000$ | Tabella parametri ufficiali |
| 14 | Codice Python | Funzione `next_state` in `src/model.py` | Listing sintattico Python |
| 15 | Risultati Numerici | Statistiche ufficiali ($\mathbb{E}, \sigma, \min, \max$) | **Tabella statistiche aggregate** |
| 16 | Singola Traiettoria | Realizzazione campionaria discreta | **Figura: `single_trajectory.png`** |
| 17 | Traiettoria Media $\pm 1\sigma$ | Andamento medio e bande di confidenza | **Figura: `mean_trajectory.png`** |
| 18 | Ritratto di Fase $(S, I)$ | Simplesso 2D, orbita ODE e traiettorie stocastiche | **Figura: `phase_portrait.png`** |
| 19 | Distribuzione di $\tau$ | Istogramma empirico tempo estinzione | **Figura: `tau_histogram.png`** |
| 20 | Distribuzione di $R_\infty$ | Istogramma attacco finale e stati terminali $\mathcal{A}$ | **Figura: `r_infinity_histogram.png`** |
| 21 | Limite Fluido (ODE) | Confronto Kermack-McKendrick ed effetto taglia finita | **Figura: `ode_comparison.png`** |
| 22 | Sensibilità $R_0$ | Studio dei 5 scenari ($R_0 \in [0.8, 5.0]$) | **Figura: `sensitivity_comparison.png`** |
| 23 | Sintesi Evidenze | Estinzione certa, variabilità, biforcazione $R_0=1$ | Elenco ragionato |
| 24 | Teoria vs Simulazione | Parallelo tra previsione analitica e stima numerica | **Tabella comparativa** |
| 25 | Limiti del Modello | Popolazione chiusa, omogeneità, assenza reinfezione | **Tabella assunzioni e motivazioni** |
| 26 | Sviluppi Futuri | SEIR, parametri $\beta(t)$, matrici su grafi | Prospettive di ricerca |
| 27 | Conclusioni | Ringraziamenti e riassunto contributi | Link GitHub |

---

# B. Copione Parlato Slide-by-Slide

## SLIDE 1 — Titolo
> **Testo parlato**:  
> "Buongiorno professore. Oggi vi presento il mio lavoro dal titolo *'Modello SIR come Catena di Markov a Tempo Discreto'*.  
> L'idea del progetto è quella di prendere un modello epidemiologico classico, il modello SIR, e formalizzarlo con il massimo rigore matematico come una catena di Markov a tempo discreto su spazio di stati finito.  
> Ci tengo a sottolineare fin da subito che l'obiettivo primario non è epidemiologico, bensì applicare e verificare i risultati fondamentali della teoria delle Catene di Markov: la proprietà di Markov, la matrice di transizione stocastica, la classificazione degli stati in transitori e assorbenti, il tempo medio di assorbimento e il confronto con il limite fluido continuo."

---

## SLIDE 2 — Introduzione e Motivazione
> **Testo parlato**:  
> "Perché descrivere la diffusione di un'epidemia con le catene di Markov?  
> La propagazione di un virus in una popolazione chiusa è un fenomeno intrinsecamente stocastico: il contagio tra un suscettibile e un infetto è un evento casuale, così come la guarigione di ciascun individuo.  
> Se descriviamo lo stato del sistema al tempo $t$ attraverso il conteggio degli individui nei tre compartimenti Suscettibili, Infetti e Rimossi, la distribuzione dello stato al tempo $t+1$ dipende unicamente dallo stato al tempo $t$, e non dalla storia passata. Questa è esattamente la proprietà di Markov.  
> Essendo la popolazione finita $N$, lo spazio degli stati è finito e siamo perfettamente nel contesto formale delle catene di Markov su spazi finiti."

---

## SLIDE 3 — Contesto Storico: Dal Determinismo alla Stocasticità
> **Testo parlato**:  
> "Un breve inquadramento storico aiuta a capire il valore di questo formalismo.  
> Nel 1927 Kermack e McKendrick proposero la celebre formulazione continua basata su equazioni differenziali ordinarie (ODE), che assume densità fluide continue per $N \to \infty$.  
> Tuttavia, per popolazioni finite, gli individui sono entità discrete e quantizzate. Nel 1949 Bartlett e i probabilisti moderni introdussero l'approccio stocastico markoviano, dove ogni transizione è un evento probabilistico discreto.  
> Questo consente di modellare fenomeni che il continuo ignora: l'estinzione precoce dell'epidemia, la varianza del picco e l'assorbimento certo in tempo finito."

---

## SLIDE 4 — Obiettivo del Lavoro
> **Testo parlato**:  
> "Gli obiettivi del progetto si articolano su tre livelli:  
> 1. Formalizzazione teorica: definire lo spazio degli stati $E$, ricavare le probabilità di transizione esatte generate da meccanismi binomiali indipendenti e costruire la matrice stocastica $P$.  
> 2. Analisi analitica: partizionare $E$ negli stati assorbenti $\mathcal{A}$ e transitori $\mathcal{T}$, e dimostrare che l'estinzione dell'infezione avviene con probabilità 1 in tempo finito.  
> 3. Verifica computazionale: implementare una simulazione Monte Carlo riproducibile in Python per stimare grandezze quali il tempo medio di estinzione $\tau$, il picco infettivo $I_{\max}$, confrontare i risultati con il sistema deterministico ODE di Kermack-McKendrick e condurre un'analisi di sensibilità sul numero di riproduzione base $R_0$."

---

## SLIDE 5 — Richiamo Teorico: Catene di Markov a Tempo Discreto
> **Testo parlato**:  
> "Richiamiamo rapidamente le definizioni chiave. Un processo $\{X_t\}$ a tempo discreto su uno spazio discreto $E$ soddisfa la proprietà di Markov se la probabilità condizionata dello stato futuro, data l'intera storia passata, coincide con la probabilità condizionata al solo stato presente.  
> La dinamica a un passo è governata dalla matrice stocastica per righe $P$, in cui ogni elemento $P(i,j)$ è non negativo e la somma su ciascuna riga è pari a 1.  
> Uno stato $i$ si dice assorbente se $P(i,i)=1$, ovvero se una volta raggiunto non può più essere abbandonato."

---

## SLIDE 6 — Il Modello SIR (Compartimenti e Schema TikZ)
> **Testo parlato**:  
> "Nel nostro modello consideriamo una popolazione chiusa di $N$ individui costanti nel tempo, vincolati dalla relazione $S_t + I_t + R_t = N$.  
> Come illustrato nello schema a blocchi:  
> - I Suscettibili $S_t$ possono contrarre l'infezione passando nel compartimento $I_t$ attraverso un numero casuale di contagi $C_t \sim \text{Bin}(S_t, \beta I_t / N)$;  
> - Gli Infetti $I_t$ guariscono passando nel compartimento $R_t$ attraverso un numero casuale di guarigioni $G_t \sim \text{Bin}(I_t, \gamma)$;  
> - I Rimossi $R_t$ non possono più reinfettarsi né trasmettere il virus, per cui la sequenza $\{R_t\}$ è monotonicamente non decrescente."

---

## SLIDE 7 — Spazio degli Stati $E$
> **Testo parlato**:  
> "Lo spazio degli stati $E$ è l'insieme di tutte le terne $(s,i,r)$ di interi non negativi la cui somma è $N$.  
> Dal punto di vista combinatorio, la cardinalità corrisponde al numero di combinazioni con ripetizione di 3 elementi su $N$ posti, ovvero $|E| = \binom{N+2}{2} = \frac{(N+1)(N+2)}{2}$.  
> Per $N=3$ individui abbiamo 10 stati, il che consente il calcolo esplicito e l'ispezione della matrice $P$.  
> Per $N=100$ abbiamo 5151 stati, che generano una matrice $P$ con oltre 26 milioni di elementi: la struttura teorica rimane identica, ma il calcolo quantitativo viene affidato al campionamento Monte Carlo."

---

## SLIDE 8 — Probabilità di Transizione ed Equazioni di Aggiornamento
> **Testo parlato**:  
> "Per passare dallo stato attuale $(S_t, I_t)$ allo stato futuro $(S_{t+1}, I_{t+1})$, operano due variabili binomiali:  
> - I nuovi contagi $C_t \sim \text{Bin}(S_t, \beta I_t / N)$ tra i suscettibili;  
> - Le nuove guarigioni $G_t \sim \text{Bin}(I_t, \gamma)$ tra gli infetti.  
> Poiché i due processi biologici sono condizionatamente indipendenti dato lo stato presente, la **probabilità congiunta di transizione** è esattamente il **prodotto delle due probabilità marginali binomiali**:  
> $$\mathbb{P}(C_t = c, G_t = g \mid S_t, I_t) = \mathbb{P}(C_t = c \mid S_t, I_t) \cdot \mathbb{P}(G_t = g \mid I_t)$$  
> L'aggiornamento dello stato è lineare: $S_{t+1}=S_t-C_t$, $I_{t+1}=I_t+C_t-G_t$, $R_{t+1}=R_t+G_t$."

---

## SLIDE 9 — Esempio Analitico: $N=3$, $\beta=0.5$, $\gamma=0.3$
> **Testo parlato**:  
> "A cosa serve questa formula congiunta? Serve a calcolare numericamente ogni singola casella della matrice di transizione $P\bigl((s,i,r), (s',i',r')\bigr)$.  
> Consideriamo ad esempio lo stato $(S=2, I=1, R=0)$ con $N=3$, $\beta=0.5$ e $\gamma=0.3$. Le combinazioni ammissibili sono $(S+1) \times (I+1) = 3 \times 2 = 6$.  
> Applicando la formula, ad esempio per $C=0$ e $G=1$, otteniamo:  
> $$\mathbb{P}(C=0, G=1) = (5/6)^2 \times 0.3 = 0.2083$$  
> Questo risultato ci dice che c'è esattamente il $20.83\%$ di probabilità di passare direttamente allo stato assorbente $(2,0,1)$ in un solo passo.  
> La tabella elenca tutte e 6 le probabilità calcolate, la cui somma è esattamente $1.0000$, formando la riga della matrice stocastica associata a $(2,1,0)$."

---

## SLIDE 10 — Matrice di Transizione $P$ e Forma Canonica
> **Testo parlato**:  
> "La formula generale per qualsiasi coppia di stati si ottiene direttamente moltiplicando la probabilità di osservare $c = s - s'$ nuovi contagi per la probabilità di osservare $g = r' - r$ nuove guarigioni:  
> $$P\bigl((s,i,r),\, (s',i',r')\bigr) = \mathbb{P}(C = s - s') \cdot \mathbb{P}(G = r' - r)$$  
> sotto la condizione di conservazione sul compartimento infetti.  
> Se ordiniamo lo spazio degli stati raggruppando prima tutti i transitori $\mathcal{T}$ (con $I>0$) e poi tutti gli assorbenti $\mathcal{A}$ (con $I=0$), la matrice assume la classica **forma canonica a blocchi**:  
> $$P = \begin{pmatrix} Q & R \\ \mathbf{0} & I \end{pmatrix}$$  
> dove $Q$ governa la dinamica interna tra transitori, $R$ contiene le probabilità di transizione verso l'assorbimento, $\mathbf{0}$ garantisce che dagli stati assorbenti non si possa uscire, e $I$ è la matrice identità."

## SLIDE 11 — Struttura della Matrice $P$ ($N=3$, Heatmap)
> **Testo parlato**:  
> "In questa slide vediamo la visualizzazione grafica (Heatmap) della matrice di transizione $10 \times 10$ per $N=3$.  
> Si notano chiaramente:  
> - I 4 stati assorbenti $(3,0,0), (2,0,1), (1,0,2), (0,0,3)$ con valore 1.0 sulla diagonale principale;  
> - La struttura a blocchi e la natura triangolare superiore dovuta alla monotonicità di $R_t$, che impedisce al processo di tornare a stati con meno rimossi."

---

## SLIDE 12 — Classificazione degli Stati e Teorema di Assorbimento
> **Testo parlato**:  
> "La classificazione rigorosa degli stati ci dice che:  
> 1. Tutti gli stati con $i=0$ formano la classe assorbente $\mathcal{A}$. Esistono $N+1$ stati assorbenti distinti, corrispondenti ai possibili valori finali di $R_\infty \in \{0, 1, \dots, N\}$;  
> 2. Tutti gli stati con $i > 0$ sono transitori ($\mathcal{T}$), perché da ciascuno di essi esiste un cammino a probabilità positiva verso $\mathcal{A}$ da cui non si può più rientrare.  
> Poiché lo spazio $E$ è finito e tutti gli stati non assorbenti sono transitori, il Teorema di Assorbimento stabilisce che $\mathbb{P}(\tau < \infty) = 1$.  
> Inoltre, il tempo medio di assorbimento è dato dalla soluzione del sistema lineare $(I-Q)\mathbf{t} = \mathbf{1}$ tramite la matrice fondamentale $(I-Q)^{-1}$."

---

## SLIDE 13 — Algoritmo di Simulazione Monte Carlo
> **Testo parlato**:  
> "Perché passiamo alla simulazione Monte Carlo?  
> Per $N=100$, lo spazio degli stati conta 5151 stati e la matrice $P$ avrebbe oltre 26 milioni di entrate: calcolarne l'inversa $(I-Q)^{-1}$ richiederebbe un costo computazionale elevato.  
> La simulazione Monte Carlo ci permette di campionare direttamente le traiettorie stocastiche estraendo a ogni passo temporale due variabili binomiali indipendenti: $C_t \sim \text{Bin}(S_t, \beta I_t/N)$ e $G_t \sim \text{Bin}(I_t, \gamma)$.  
> Se $I_t=0$, la catena si arresta avendo raggiunto l'assorbimento ($\tau=t$).  
> Eseguiamo $M=1000$ repliche indipendenti con seed fissato a 42 per garantire la totale riproducibilità scientifica, su una popolazione $N=100$ con $I_0=5$, $\beta=0.20$ e $\gamma=0.10$ ($R_0=2.00$)."

---

## SLIDE 14 — Codice Python (`src/model.py`)
> **Testo parlato**:  
> "Il codice Python implementa la funzione `next_state`.  
> Come si può osservare, la funzione verifica se $I=0$: in tal caso restituisce lo stato invariato; altrimenti calcola $p_{\mathrm{SI}}$, estrae le due binomiali con `numpy.random.binomial` e aggiorna le variabili di stato.  
> Il codice riflette esattamente la formulazione probabilistica della catena."

---

## SLIDE 15 — Risultati Numerici Ufficiali ($M=1000$, Seed 42)
> **Testo parlato**:  
> "Ecco i risultati numerici aggregati su 1000 simulazioni:  
> - Il picco medio degli infetti $\mathbb{E}[I_{\max}]$ è pari a **21.94 individui** ($\pm 4.52$), raggiunto mediamente al passo temporale $t \approx 24$;  
> - Il tempo medio di estinzione dell'epidemia $\mathbb{E}[\tau]$ è di **86.66 passi** ($\pm 22.81$);  
> - L'attacco finale $\mathbb{E}[R_\infty]$ è pari a **76.59 individui** ($\pm 8.41$), indicando che circa il 77% della popolazione viene immunizzato.  
> Nel 100% dei casi l'epidemia si è estinta entro l'orizzonte $T_{\max}=200$, confermando sperimentalmente l'assorbimento quasi certo."

---

## SLIDE 16 — Singola Traiettoria Stocastica
> **Testo parlato**:  
> "Questo grafico mostra una singola traiettoria della catena.  
> Si notano la decrescita a gradini della curva blu dei suscettibili, l'ascesa al picco e la successiva discesa a zero della curva rossa degli infetti, e la saturazione asintotica della curva verde dei rimossi.  
> L'andamento frastagliato evidenzia la stocasticità intrinseca del processo a taglia finita."

---

## SLIDE 17 — Traiettoria Media e Bande di Confidenza
> **Testo parlato**:  
> "In questa figura osserviamo la traiettoria media su 1000 replicazioni con le bande di confidenza a $\pm 1$ deviazione standard.  
> Notiamo che la variabilità stocastica è massima in corrispondenza del picco epidemico (tra il passo 15 e il passo 40), dove traiettorie diverse possono raggiungere ampiezze notevolmente differenti."

---

## SLIDE 18 — Ritratto di Fase $(S, I)$ nello Spazio degli Stati
> **Testo parlato**:  
> "Questa visualizzazione nel piano di fase $(S, I)$ è particolarmente illuminante.  
> L'area azzurra rappresenta il simplesso degli stati ammissibili $S + I \le N$.  
> Le traiettorie stocastiche partono dal punto blu $(95, 5)$, salgono verso l'alto a sinistra e poi ricadono verso l'asse orizzontale in basso $I=0$, che rappresenta la linea assorbente $\mathcal{A}$.  
> La curva nera rappresenta l'orbita teorica continua ODE, attorno alla quale le traiettorie stocastiche fluttuano."

---

## SLIDE 19 — Distribuzione del Tempo di Estinzione $\tau$
> **Testo parlato**:  
> "L'istogramma del tempo di estinzione $\tau$ mostra una distribuzione asimmetrica a destra (skew-positive): la maggior parte delle epidemie si estingue attorno al passo 80-90, ma esiste una coda lunga dovuta a traiettorie in cui l'infezione persiste con pochi individui prima di spegnersi."

---

## SLIDE 20 — Distribuzione dell'Attacco Finale $R_\infty$
> **Testo parlato**:  
> "L'istogramma dell'attacco finale $R_\infty$ mostra la distribuzione del numero totale di individui immunizzati al termine dell'epidemia.  
> La media si attesta a 76.59 individui.  
> Dal punto di vista della teoria di Markov, ciascuna barra di questo istogramma rappresenta la probabilità di assorbimento in uno specifico stato terminale $(N-r, 0, r) \in \mathcal{A}$."

---

## SLIDE 21 — Confronto con il Limite Fluido Deterministico (ODE)
> **Testo parlato**:  
> "Quando la popolazione $N \to \infty$, la legge dei grandi numeri assicura che le frazioni scalate $(S_t/N, I_t/N, R_t/N)$ convergano alla soluzione del sistema di equazioni differenziali ordinarie di Kermack-McKendrick.  
> Confrontando la curva deterministica (in nero tratteggiato) con la media stocastica, osserviamo il cosiddetto *effetto di taglia finita*: il modello continuo sovrastima il picco ($I_{\max}^{\text{ODE}} \approx 30\%$ vs $\hat{I}_{\max} \approx 22\%$), poiché ignora la varianza e le possibili estinzioni stocastiche locali."

---

## SLIDE 22 — Analisi di Sensibilità su $R_0 = \beta / \gamma$
> **Testo parlato**:  
> "Abbiamo condotto un'analisi di sensibilità variando $R_0$ su 5 regimi:  
> - Per $R_0 = 0.8 \le 1$ (regime subcritico), non si forma alcuna epidemia: il picco rimane pari a $I_0=5$ e l'estinzione è rapidissima ($\tau \approx 18$ passi);  
> - Per $R_0 > 1$ (regime sovracritico), si sviluppa un'ondata epidemica la cui altezza cresce con $R_0$, mentre il tempo al picco si anticipa drasticamente (da 24 passi per $R_0=2$ a meno di 10 passi per $R_0=5$)."

---

## SLIDE 23 — Sintesi delle Evidenze Probabilistiche
> **Testo parlato**:  
> "Riassumendo le evidenze probabilistiche:  
> 1. L'assorbimento è certo nel 100% dei casi;  
> 2. La variabilità campionaria è quantificabile e rilevante;  
> 3. La soglia $R_0=1$ agisce da punto di biforcazione tra estinzione immediata e invasione stocastica;  
> 4. Il limite ODE descrive il trend qualitativo ma necessita di correzioni per popolazioni finite."

---

## SLIDE 24 — Confronto Metodologico: Teoria vs Simulazione
> **Testo parlato**:  
> "Questa tabella mette a confronto diretto le previsioni della teoria analitica con i risultati Monte Carlo.  
> Il messaggio fondamentale è che la simulazione non si sostituisce alla teoria, ma costituisce lo strumento per stimare e visualizzare quantità matematicamente ben definite quando le dimensioni dello spazio di stato ($5151 \times 5151$) precludono l'inversione simbolica esatta."

---

## SLIDE 25 — Limiti del Modello e Scelte Progettuali
> **Testo parlato**:  
> "I limiti assunti nel modello — popolazione chiusa, parametri costanti, mescolamento omogeneo e assenza di reinfezione — sono scelte progettuali deliberate: servono a mantenere la catena omogenea e a evidenziare con massima trasparenza le proprietà matematiche di assorbimento."

---

## SLIDE 26 — Possibili Sviluppi Futuri
> **Testo parlato**:  
> "Le possibili estensioni includono l'aggiunta dello stato degli Esposti (modello SEIR), l'introduzione di tassi tempo-varianti $\beta(t)$ per catene non omogenee (es. lockdown), il calcolo esatto della matrice fondamentale per $N \le 20$, e la modellazione su grafi di contatto."

---

## SLIDE 27 — Conclusioni
> **Testo parlato**:  
> "In conclusione, abbiamo formalizzato con successo il modello SIR come catena di Markov a tempo discreto, verificato l'assorbimento certo, quantificato l'effetto di taglia finita e validato l'intero codice con 16 test automatizzati.  
> Vi ringrazio per l'attenzione e sono pronto per le domande di approfondimento e le dimostrazioni alla lavagna."

---

# C. Domande e Risposte per la Discussione Orale (Q&A)

### D1: Perché questo modello è rigorosamente una Catena di Markov?
**Risposta**: Perché la distribuzione congiunta di $(S_{t+1}, I_{t+1}, R_{t+1})$ condizionata a tutta la storia passata $X_t, X_{t-1}, \dots, X_0$ dipende unicamente dallo stato presente $X_t = (S_t, I_t, R_t)$. I parametri delle distribuzioni binomiali di contagio e guarigione sono funzioni deterministiche del solo stato corrente. Inoltre lo spazio $E$ è discreto e il tempo è indicizzato su $\mathbb{N}_0$.

### D2: Quanti stati ha la catena e qual è la formula combinatoria?
**Risposta**: Gli stati sono le terne $(s,i,r) \in \mathbb{N}_0^3$ tali che $s+i+r=N$. La cardinalità è data dalle combinazioni con ripetizione:
$$|E| = \binom{N+3-1}{3-1} = \binom{N+2}{2} = \frac{(N+1)(N+2)}{2}$$
Per $N=3$ abbiamo 10 stati; per $N=100$ abbiamo 5151 stati.

### D3: Come si dimostra che gli stati con $I=0$ sono assorbenti e quelli con $I>0$ sono transitori?
**Risposta**:  
- Se $I=0$, la probabilità di contagio $\beta I/N = 0$, quindi $C_t = 0$ con probabilità 1. Inoltre non ci sono infetti da guarire ($G_t=0$). Quindi $P((s,0,r),(s,0,r)) = 1$, che è la definizione di stato assorbente.  
- Se $I > 0$, esiste una probabilità strettamente positiva di andare in $\mathcal{A}$ in un solo passo (es. estraendo $g=i$ guarigioni e $c=0$ contagi, evento di probabilità $\gamma^i (1-\beta i/N)^s > 0$). Poiché $R_t$ non può mai decrescere, una volta entrati in $\mathcal{A}$ non si può più tornare in $I>0$. Dunque ogni stato con $I>0$ è transitorio.

### D4: Come si calcola teoricamente il tempo medio di assorbimento $\mathbb{E}[\tau]$?
**Risposta**: Si scrive la matrice di transizione in forma canonica $P = \begin{pmatrix} Q & R \\ 0 & I \end{pmatrix}$. Per la proprietà di Markov e il teorema della probabilità totale, il vettore dei tempi medi $\mathbf{t} = (\mathbb{E}_i[\tau])_{i \in \mathcal{T}}$ soddisfa il sistema lineare $\mathbf{t} = \mathbf{1} + Q\mathbf{t}$, da cui:
$$(I - Q)\mathbf{t} = \mathbf{1} \implies \mathbf{t} = (I - Q)^{-1}\mathbf{1}$$
La matrice $(I-Q)^{-1} = \sum_{k=0}^\infty Q^k$ è la **matrice fondamentale** della catena assorbente.

### D5: Perché c'è discrepanza tra il picco della ODE deterministica e la media Monte Carlo?
**Risposta**: È l'**effetto di taglia finita**. Il sistema differenziale continuo assume $N \to \infty$ e densità fluide senza varianza. Per $N=100$, le fluttuazioni stocastiche e la possibilità di estinzioni premature o rallentamenti casuali abbassano la curva media reale ($\hat{I}_{\max} \approx 22$) rispetto al picco deterministico teorico ($I_{\max}^{\text{ODE}} \approx 30$).

---

# D. Traccia Sintetica da Scrivere alla Lavagna

```
1. SPAZIO STATI:
   E = {(s,i,r) in N_0^3 : s + i + r = N}
   |E| = (N+1)(N+2)/2   --->  N=3: 10 stati | N=100: 5151 stati

2. DINAMICA TRANSIZIONI:
          C ~ Bin(S, beta*I/N)         G ~ Bin(I, gamma)
      S ------------------------> I ----------------------> R

3. MATRICE CANONICA & ASSORBIMENTO:
      P = [ Q   R ]      Stati assorbenti A = {(s,0,r)} : P_ii = 1
          [ 0   I ]      Stati transitori T = {(s,i,r) : i > 0}
      
      Tempo medio: (I - Q) * t = 1  ===>  t = (I - Q)^(-1) * 1

4. RISULTATI NUMERICI (N=100, beta=0.2, gamma=0.1, R0=2, M=1000):
   - Picco medio I_max = 21.94 +- 4.52
   - Tempo estinzione tau = 86.66 +- 22.81
   - Attacco finale R_inf = 76.59 +- 8.41
```
