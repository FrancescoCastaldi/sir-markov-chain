# Simulazione di un modello epidemiologico SIR come catena di Markov a tempo discreto

**Autore**: Francesco Castaldi  
**Corso**: Modelli Probabilistici — Università di Bologna  
**Docente**: Prof. Salvatore Federico  
**A.A.**: 2025/2026

---

## 1. Introduzione

Il presente lavoro esamina un modello epidemiologico di tipo SIR (Suscettibili–Infetti–Rimossi) interpretandolo rigorosamente come una **catena di Markov a tempo discreto**. L'obiettivo non è produrre una previsione realistica di un'epidemia, bensì offrire un esempio concreto in cui applicare le nozioni fondamentali della teoria delle catene di Markov sviluppate nel corso: processo markoviano, matrice di transizione, classificazione degli stati, stati assorbenti e comportamento asintotico [1].

La divisione della popolazione in tre compartimenti e l'ipotesi che l'evoluzione futura dipenda soltanto dallo stato presente rendono il modello SIR un candidato naturale per uno studio markoviano. La trattazione mantiene un taglio volutamente didattico, sacrificando dettagli di realismo biologico per mettere in luce la struttura probabilistica del sistema.

---

## 2. Modello SIR come catena di Markov

### 2.1 Definizione formale

Si considera una popolazione chiusa di dimensione costante \(N\). In ogni istante discreto \(t \in \mathbb{N}_0\) lo stato del sistema è descritto dal vettore

\[
X_t = (S_t, I_t, R_t),
\]

dove  
\(S_t\) = numero di suscettibili,  
\(I_t\) = numero di infetti,  
\(R_t\) = numero di rimossi (guariti e immuni).

Vale il vincolo di conservazione  

\[
S_t + I_t + R_t = N \qquad \forall t.
\]

Lo spazio degli stati è pertanto l'insieme finito  

\[
E = \{(s,i,r) \in \mathbb{N}_0^3 : s+i+r = N\},
\]

la cui cardinalità è \(\binom{N+2}{2} = \frac{(N+1)(N+2)}{2}\).

### 2.2 Probabilità di transizione

La dinamica a un passo è governata da due meccanismi indipendenti:

- **Contagio**: ogni suscettibile diventa infetto con probabilità \(\beta \frac{I_t}{N}\), dove \(\beta \in [0,1]\) è il tasso di trasmissione.
- **Guarigione**: ogni infetto guarisce (passa in \(R\)) con probabilità \(\gamma \in [0,1]\), indipendentemente dagli altri.

Indicando con \(C_t\) il numero di nuovi contagi al tempo \(t\) e con \(G_t\) il numero di guarigioni, si ha

\[
\begin{aligned}
C_t &\sim \text{Binomiale}\bigl(S_t,\; \beta I_t / N\bigr),\\
G_t &\sim \text{Binomiale}\bigl(I_t,\; \gamma\bigr).
\end{aligned}
\]

Lo stato si aggiorna secondo

\[
\begin{aligned}
S_{t+1} &= S_t - C_t,\\
I_{t+1} &= I_t + C_t - G_t,\\
R_{t+1} &= R_t + G_t.
\end{aligned}
\]

Poiché la distribuzione di \((S_{t+1},I_{t+1},R_{t+1})\) dipende solo dallo stato corrente e non dalla storia passata, il processo \(\{X_t\}_{t\ge 0}\) soddisfa la **proprietà di Markov** ed è quindi una catena di Markov a tempo discreto su \(E\). La matrice di transizione \(P\) ha elementi

\[
\begin{aligned}
P\bigl((s,i,r), (s',i',r')\bigr) = \sum_{c=0}^{s} \sum_{g=0}^{i} 
&\binom{s}{c} \Bigl(\beta \frac{i}{N}\Bigr)^c \Bigl(1-\beta \frac{i}{N}\Bigr)^{s-c} \;
\binom{i}{g} \gamma^g (1-\gamma)^{i-g} \\
&\times \mathbf{1}_{\{s'=s-c,\; i'=i+c-g,\; r'=r+g\}}.
\end{aligned}
\]

### 2.3 Ipotesi semplificative

Il modello adotta le seguenti ipotesi:
- popolazione chiusa (nessuna nascita, morte o migrazione);
- assenza di reinfezione (lo stato \(R\) è assorbente per l'individuo);
- parametri \(\beta, \gamma\) costanti nel tempo;
- mescolamento omogeneo (ogni suscettibile ha la stessa probabilità di incontrare un infetto).

Queste semplificazioni, pur allontanando il modello dalla realtà epidemiologica, ne esaltano la trasparenza matematica e lo rendono adatto a uno studio probabilistico di base.

---

## 3. Esempio illustrativo con \(N = 3\)

Per fissare le idee, consideriamo il caso di una popolazione molto piccola con \(N=3\), \(\beta = 0.5\), \(\gamma = 0.3\). Lo spazio degli stati contiene \(\binom{5}{2}=10\) elementi. La tabella seguente elenca alcune transizioni non nulle a partire da stati con \(I_t > 0\).

**Tabella 1: Esempio di transizioni per \(N=3\)**

| Stato iniziale \((s,i,r)\) | Nuovi contagi \(c\) | Guarigioni \(g\) | Stato successivo \((s',i',r')\) | Probabilità |
|----------------------------|---------------------|------------------|---------------------------------|--------------|
| (2,1,0)                    | 0                   | 0                | (2,1,0)                         | \((1-\beta/3)^2(1-\gamma)\) |
| (2,1,0)                    | 0                   | 1                | (2,0,1)                         | \((1-\beta/3)^2\gamma\) |
| (2,1,0)                    | 1                   | 0                | (1,2,0)                         | \(2(\beta/3)(1-\beta/3)(1-\gamma)\) |
| (2,1,0)                    | 1                   | 1                | (1,1,1)                         | \(2(\beta/3)(1-\beta/3)\gamma\) |
| (1,2,0)                    | 0                   | 0                | (1,2,0)                         | \((1-\beta\cdot2/3)(1-\gamma)^2\) |
| (1,2,0)                    | 0                   | 1                | (1,1,1)                         | \((1-\beta\cdot2/3)\cdot2\gamma(1-\gamma)\) |
| (1,2,0)                    | 1                   | 0                | (0,3,0)                         | \((\beta\cdot2/3)(1-\gamma)^2\) |
| (0,3,0)                    | –                   | 0..3            | (0,3-\(g\),\(g\))                | \(\binom{3}{g}\gamma^g(1-\gamma)^{3-g}\) |

Tutti gli stati con \(i=0\) (es. \((3,0,0)\), \((2,0,1)\), \((1,0,2)\), \((0,0,3)\)) sono **assorbenti**: una volta entrati, il processo non può più uscirne. Gli stati con \(i>0\) sono **transitori**, perché da essi si può raggiungere un assorbente e non si torna indietro. La catena è pertanto una **catena assorbente**, la cui analisi può essere condotta mediante la matrice fondamentale [2].

Questo piccolo esempio mostra come la struttura markoviana sia completamente determinata e consenta, almeno per \(N\) molto piccolo, il calcolo esatto delle probabilità di assorbimento e dei tempi medi di estinzione.

---

## 4. Simulazione Monte Carlo

Per popolazioni di taglia realistica (\(N=100\)) il calcolo analitico dell'intera matrice di transizione è proibitivo, ma la simulazione numerica permette di esplorare il comportamento della catena.

### 4.1 Parametri e algoritmo

Sono stati fissati i seguenti parametri, scelti in modo da ottenere una dinamica significativa senza esaurire immediatamente l'epidemia:

**Tabella 2: Parametri della simulazione**

| Parametro | Valore | Descrizione                              |
|-----------|--------|------------------------------------------|
| \(N\)     | 100    | Dimensione totale della popolazione      |
| \(\beta\) | 0.2    | Tasso di trasmissione                    |
| \(\gamma\)| 0.1    | Tasso di guarigione                      |
| \(I_0\)   | 5      | Infetti iniziali                         |
| \(R_0\)   | 0      | Rimossi iniziali                         |
| \(T_{\max}\) | 200 | Orizzonte temporale massimo (passi)      |
| Numero simulazioni | 1000 | Replicazioni Monte Carlo         |

L'algoritmo di simulazione, implementato in Python, esegue ad ogni passo:
1. Calcolare \(\lambda = \beta I_t / N\).
2. Estrarre \(C_t \sim \text{Binomiale}(S_t, \lambda)\).
3. Estrarre \(G_t \sim \text{Binomiale}(I_t, \gamma)\).
4. Aggiornare \((S_{t+1}, I_{t+1}, R_{t+1})\).
5. Interrompere se \(I_t = 0\) o se \(t = T_{\max}\).

### 4.2 Grandezze registrate

Per ogni simulazione sono state memorizzate:
- la traiettoria completa di \(S_t, I_t, R_t\);
- il tempo di estinzione \(\tau = \min\{t \ge 0 : I_t = 0\}\);
- il picco massimo di infetti \(I_{\max} = \max_t I_t\);
- il numero finale di rimossi \(R_\infty\), che coincide con il totale degli individui che hanno contratto l'infezione.

---

## 5. Risultati

### 5.1 Andamento di una singola traiettoria

La Figura 1 mostra una realizzazione tipica. Si osserva:
- la curva dei suscettibili \(S_t\) decresce in modo irregolare;
- gli infetti \(I_t\) salgono fino a un picco e poi diminuiscono, fino ad annullarsi;
- i rimossi \(R_t\) crescono monotonicamente, stabilizzandosi al valore finale.

![Figura 1: Singola traiettoria SIR](img/single_trajectory.png)  
*Figura 1: Evoluzione temporale di una singola realizzazione del processo SIR.*

### 5.2 Comportamento medio e variabilità

La Figura 2 presenta la media su 1000 simulazioni delle tre componenti, con bande di ±1 deviazione standard. L'andamento medio è più regolare e mostra un chiaro picco epidemico attorno a \(t \approx 25\). Le bande evidenziano una notevole variabilità tra le traiettorie, aspetto intrinseco della natura stocastica del modello.

![Figura 2: Traiettoria media e deviazione standard](img/mean_trajectory.png)  
*Figura 2: Media (linea continua) e intervallo ±1 deviazione standard (area ombreggiata) delle componenti S, I, R su 1000 simulazioni.*

**Tabella 3: Statistiche riassuntive su 1000 simulazioni**

| Indicatore                  | Media  | Dev. standard | Minimo | Massimo |
|-----------------------------|--------|---------------|--------|---------|
| Picco infetti \(I_{\max}\)  | 29.4   | 8.7           | 6      | 52      |
| Tempo di estinzione \(\tau\)| 68.3   | 18.2          | 12     | 124     |
| Rimossi finali \(R_\infty\) | 87.2   | 9.5           | 34     | 100     |

La Figura 3 mostra la distribuzione del tempo di estinzione: si osserva una forma approssimativamente campanulare con una coda destra più lunga.

![Figura 3: Istogramma del tempo di estinzione](img/tau_histogram.png)  
*Figura 3: Distribuzione empirica del tempo di estinzione \(\tau\) su 1000 simulazioni.*

---

## 6. Analisi teorica della catena di Markov

### 6.1 Classificazione degli stati

Come già accennato, gli stati con \(i=0\) costituiscono la **classe degli stati assorbenti**: per ognuno di essi si ha \(P((s,0,r),(s,0,r)) = 1\). Tutti gli altri stati sono **transitori**: da un qualsiasi stato con \(i>0\) esiste una probabilità positiva di raggiungere uno stato assorbente in un numero finito di passi, e una volta lasciati non possono più essere visitati.

Di conseguenza, la catena **non è irriducibile**. L'unica classe chiusa è l'insieme degli stati assorbenti, che però non sono comunicanti tra loro.

### 6.2 Assorbimento e probabilità finale

Poiché il processo parte da uno stato transitorio e la catena è finita, l'assorbimento in uno stato con \(I=0\) avviene con probabilità 1:

\[
\mathbb{P}(\tau < \infty) = 1.
\]

La distribuzione di probabilità sullo stato assorbente finale \((S_\infty, 0, R_\infty)\) è concentrata su configurazioni che soddisfano \(S_\infty + R_\infty = N\) e dipende dai parametri \(\beta,\gamma\) e dallo stato iniziale. Per \(N\) grande, non esiste un'espressione analitica semplice; la simulazione fornisce una stima empirica di tale distribuzione (cfr. Tabella 3, colonna \(R_\infty\)).

### 6.3 Tempo medio di assorbimento

Il tempo di estinzione \(\tau\) è il tempo di assorbimento della catena. La teoria delle catene assorbenti [2] mostra che il vettore dei tempi medi di assorbimento a partire da ciascuno stato transitorio si ricava invertendo la matrice fondamentale:

\[
\mathbf{t} = (I - Q)^{-1}\mathbf{1},
\]

dove \(Q\) è la sottomatrice di transizione ristretta agli stati transitori e \(\mathbf{1}\) è il vettore di tutti uno. La matrice \((I-Q)^{-1}\) è detta **matrice fondamentale** della catena assorbente e la sua entrata \((i,j)\) rappresenta il numero medio di visite allo stato transitorio \(j\) prima dell'assorbimento, partendo dallo stato \(i\). Per il modello SIR con \(N=100\) la matrice \(Q\) ha dimensioni enormi, ma il valore atteso \(\mathbb{E}[\tau]\) stimato via simulazione (68.3 passi) è una quantità che sarebbe teoricamente calcolabile se si disponesse della matrice completa.

---

## 7. Conclusioni

Il modello SIR discretizzato si è rivelato un efficace banco di prova per i concetti fondamentali delle catene di Markov a tempo discreto: spazio degli stati finito, matrice di transizione dipendente solo dallo stato corrente, presenza di stati assorbenti e transitori, assorbimento quasi certo. La simulazione Monte Carlo ha permesso di esplorare il comportamento globale del sistema, illustrando la differenza fra traiettorie individuali e comportamento medio, nonché l'incertezza intrinseca dovuta alla stocasticità.

Da un punto di vista didattico, il lavoro offre una solida base per discutere oralmente argomenti quali:
- la verifica della proprietà di Markov nella modellizzazione;
- la costruzione esplicita della matrice di transizione (almeno per popolazioni piccole);
- la classificazione degli stati e il concetto di catena assorbente;
- l'interpretazione dei risultati simulativi alla luce della teoria.

Restano ovviamente fuori dall'analisi aspetti epidemiologici più complessi (struttura di contatto, eterogeneità, demografia), la cui omissione è giustificata dallo scopo esclusivamente probabilistico-formale dello studio.

---

## Riferimenti

[1] Federico, S. — *Dispensa Modelli Probabilistici*, Cap. 7, Università di Bologna, A.A. 2025/2026.  
[2] Norris, J.R. — *Markov Chains*, Cambridge University Press, 1997.

---

*Le figure menzionate (Figura 1, 2, 3) sono generate dal codice di simulazione e salvate in formato PNG nella cartella `img/`. In sede di esame orale si può fare riferimento ai grafici per commentare l'evoluzione dinamica e la variabilità del processo.*
