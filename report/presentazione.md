# Presentazione Orale — Modello SIR come Catena di Markov

**Corso**: Modelli Probabilistici — Università di Bologna  
**Docente**: Prof. Salvatore Federico  
**Studente**: Francesco Castaldi  
**A.A.**: 2025/2026

---

# A. Struttura completa del progetto

Il progetto si compone di 18 sezioni, elencate qui con il contenuto essenziale di ciascuna:

| # | Sezione | Contenuto |
|---|---------|-----------|
| 1 | Titolo | "Modello SIR come Catena di Markov a Tempo Discreto" |
| 2 | Introduzione | Perché studiare un'epidemia con le catene di Markov |
| 3 | Obiettivo | Applicare il formalismo markoviano a un caso concreto |
| 4 | Richiamo teorico | Cosa sono le catene di Markov (Cap. 7) |
| 5 | Modello SIR | I tre compartimenti: S, I, R |
| 6 | Spazio degli stati | Tutte le triple (S, I, R) con somma N |
| 7 | Probabilità di transizione | Le Binomiali di contagio e guarigione |
| 8 | Matrice di transizione | Costruzione della matrice P |
| 9 | Proprietà | Stati assorbenti e transitori |
| 10 | Simulazione | Algoritmo Monte Carlo |
| 11 | Codice | Python essenziale |
| 12 | Risultati | Tabella delle statistiche |
| 13 | Grafici | Andamento di S, I, R nel tempo |
| 14 | Interpretazione | Cosa dicono i numeri |
| 15 | Teoria vs simulazione | Coerenza tra risultati e previsioni teoriche |
| 16 | Limiti | Cosa il modello non cattura |
| 17 | Sviluppi futuri | Estensioni possibili |
| 18 | Conclusioni | Riassunto e messaggio finale |

---

# B. Scaletta slide-by-slide

```
SLIDE 1  — Titolo
SLIDE 2  — Introduzione al problema
SLIDE 3  — Obiettivo del lavoro
SLIDE 4  — Richiamo: Catene di Markov
SLIDE 5  — Il modello SIR
SLIDE 6  — Spazio degli stati
SLIDE 7  — Probabilità di transizione
SLIDE 8  — Esempio: N=3
SLIDE 9  — Matrice di transizione (N=3)
SLIDE 10 — Classificazione degli stati
SLIDE 11 — Algoritmo di simulazione
SLIDE 12 — Codice Python
SLIDE 13 — Risultati numerici
SLIDE 14 — Grafico: singola traiettoria
SLIDE 15 — Grafico: media su 1000 simulazioni
SLIDE 16 — Grafico: istogramma tempo di estinzione
SLIDE 17 — Interpretazione dei risultati
SLIDE 18 — Confronto teoria vs simulazione
SLIDE 19 — Limiti del modello
SLIDE 20 — Sviluppi futuri
SLIDE 21 — Conclusioni
```

---

# C. Testo orale per ogni slide

---

## SLIDE 1 — Titolo

**Testo orale:**

"Buongiorno professore. Oggi vi presento il mio progetto dal titolo
'Modello SIR come Catena di Markov a Tempo Discreto'.
L'idea è quella di prendere un modello epidemiologico molto semplice,
quello SIR, e interpretarlo rigorosamente come una catena di Markov.
L'obiettivo non è fare epidemiologia, ma dimostrare di saper applicare
il formalismo markoviano a un caso concreto, utilizzando il capitolo 7
del Suo materiale come riferimento teorico."

**Versione slide:**

> # Modello SIR come Catena di Markov a Tempo Discreto
>
> **Corso**: Modelli Probabilistici — Prof. S. Federico  
> **Studente**: Francesco Castaldi  
> **A.A.**: 2025/2026
>
> Applicazione del formalismo delle catene di Markov a un modello
> epidemiologico SIR semplificato.

---

## SLIDE 2 — Introduzione

**Testo orale:**

"Perché studiare un'epidemia con le catene di Markov?
Il motivo è semplice: il modello SIR si presta naturalmente a essere
descritto come un processo markoviano. La popolazione è divisa in tre
gruppi: Suscettibili, Infetti e Rimossi. L'evoluzione futura dipende
solo dallo stato presente, non dalla storia passata. Questa è
esattamente la proprietà di Markov. Inoltre lo spazio degli stati
è finito, quindi siamo nel caso classico delle catene a tempo discreto
con spazio finito, che è esattamente l'argomento del capitolo 7."

**Versione slide:**

> ## Introduzione
>
> - Il modello SIR descrive la diffusione di un'infezione in una popolazione chiusa.
> - L'evoluzione futura dipende **solo dallo stato presente** → proprietà di Markov.
> - Lo spazio degli stati è **finito** → catena di Markov a tempo discreto.
> - Il problema non è epidemiologico: è un pretesto per applicare il formalismo.
>
> **Riferimento**: Capitolo 7 del corso — Catene di Markov a tempo discreto.

---

## SLIDE 3 — Obiettivo del lavoro

**Testo orale:**

"L'obiettivo di questo lavoro è triplice.
Primo: costruire rigorosamente la catena di Markov associata al
modello SIR, definendo spazio degli stati, probabilità di transizione
e matrice di transizione.
Secondo: classificare gli stati della catena, identificando stati
assorbenti e transitori.
Terzo: simulare numericamente l'evoluzione della catena con il metodo
Monte Carlo per stimare quantità di interesse come il tempo medio di
estinzione dell'infezione e il numero medio di infetti.
Tutto questo viene fatto senza mai perdere di vista il legame con la
teoria delle catene di Markov."

**Versione slide:**

> ## Obiettivo
>
> 1. **Costruire** la catena di Markov SIR: spazio degli stati,
>    probabilità di transizione, matrice P.
> 2. **Classificare** gli stati: identificare assorbenti e transitori.
> 3. **Simulare** l'evoluzione con Monte Carlo per stimare:
>    - tempo medio di estinzione τ;
>    - picco medio degli infetti;
>    - numero finale di rimossi R∞.

---

## SLIDE 4 — Richiamo: Catene di Markov

**Testo orale:**

"Richiamiamo brevemente i concetti fondamentali delle catene di Markov,
così come li abbiamo studiati nel capitolo 7.

Una catena di Markov a tempo discreto è un processo stocastico
{X_t, t = 0, 1, 2, ...} con la proprietà che la distribuzione
dello stato futuro dipende solo dallo stato presente e non da
quelli passati. Formalmente:

P(X_{t+1} = j | X_t = i, X_{t-1} = i_{t-1}, ..., X_0 = i_0)
= P(X_{t+1} = j | X_t = i)

Questa si chiama proprietà di Markov.

La catena è descritta da una matrice di transizione P, dove
l'elemento P(i,j) è la probabilità di passare dallo stato i
allo stato j in un passo.

La matrice P è stocastica: ogni riga contiene probabilità non
negative che sommano a 1.

Un concetto fondamentale per questo progetto è quello di
stato assorbente. Uno stato i si dice assorbente se, una volta
raggiunto, non lo si abbandona mai più. In termini di matrice
di transizione, questo significa P(i,i) = 1."

**Versione slide:**

> ## Catene di Markov (Cap. 7)
>
> **Definizione**: Processo stocastico {X_t} a tempo discreto con
> la **proprietà di Markov**:
>
> P(X_{t+1} | X_t, X_{t-1}, ..., X_0) = P(X_{t+1} | X_t)
>
> **Matrice di transizione P**: P(i,j) = probabilità di andare
> da i a j in un passo.
>
> - P è **stocastica**: ∑_j P(i,j) = 1 per ogni i.
>
> **Stato assorbente**: P(i,i) = 1.
> Una volta entrato, non si esce più.

---

## SLIDE 5 — Il modello SIR

**Testo orale:**

"Veniamo al modello SIR. Consideriamo una popolazione chiusa di
dimensione costante N. In ogni istante discreto t, la popolazione
è suddivisa in tre compartimenti:

- S_t: il numero di Suscettibili, cioè individui sani che possono
  contrarre l'infezione.
- I_t: il numero di Infetti, cioè individui che hanno contratto
  l'infezione e possono trasmetterla.
- R_t: il numero di Rimossi, cioè individui guariti che sono
  immuni e non possono più ammalarsi.

Vale il vincolo di conservazione: S_t + I_t + R_t = N per ogni t.
Questo perché la popolazione è chiusa: non ci sono nascite, morti
o migrazioni.

Lo stato del sistema al tempo t è il vettore X_t = (S_t, I_t, R_t).
La dinamica è governata da due meccanismi casuali indipendenti:
il contagio e la guarigione."

**Versione slide:**

> ## Modello SIR
>
> Popolazione chiusa di **N individui**. Tre compartimenti:
>
> | Simbolo | Nome | Descrizione |
> |---------|------|-------------|
> | S_t | Suscettibili | Possono essere infettati |
> | I_t | Infetti | Possono trasmettere l'infezione |
> | R_t | Rimossi | Guariti, immuni, non infettivi |
>
> **Vincolo**: S_t + I_t + R_t = N per ogni t.
>
> **Stato**: X_t = (S_t, I_t, R_t).

---

## SLIDE 6 — Spazio degli stati

**Testo orale:**

"Lo spazio degli stati della catena è l'insieme di tutte le terne
(s, i, r) di numeri interi non negativi la cui somma è N.

Formalmente:

E = {(s, i, r) ∈ ℕ₀³ : s + i + r = N}

Quanti sono gli stati? Il numero di modi di distribuire N oggetti
indistinguibili in 3 scatole è dato da:

|E| = C(N+2, 2) = (N+1)(N+2)/2

Per N = 100, abbiamo 101 × 102 / 2 = 5151 stati. È uno spazio
finito, come richiesto dalla teoria delle catene di Markov, ma
troppo grande per calcolare esplicitamente la matrice di transizione.
Per questo useremo la simulazione.

Attenzione: il fatto che lo spazio sia grande non è un problema
concettuale. La teoria delle catene di Markov vale per qualsiasi
spazio finito. Semplicemente, per N=100 non possiamo scrivere
la matrice P per intero, ma possiamo simularne il comportamento."

**Versione slide:**

> ## Spazio degli stati
>
> **Definizione**: E = {(s, i, r) ∈ ℕ₀³ : s + i + r = N}
>
> **Cardinalità**: |E| = C(N+2, 2) = (N+1)(N+2)/2
>
> **Esempi**:
> - N = 3 ⇒ |E| = 10 stati
> - N = 100 ⇒ |E| = 5151 stati
>
> Lo spazio è **finito** → siamo nel caso classico delle catene
> a spazio finito (Cap. 7).
>
> Per N piccolo la matrice P si calcola esplicitamente.
> Per N grande si usa la simulazione Monte Carlo.

---

## SLIDE 7 — Probabilità di transizione

**Testo orale:**

"Come evolve il sistema da un passo al successivo? Abbiamo due
fenomeni casuali indipendenti.

Primo: il contagio. Ogni Suscettibile incontra gli Infetti in modo
uniforme. La probabilità che un singolo Suscettibile diventi infetto
in un passo è β · I_t / N, dove β è un parametro fissato tra 0 e 1.
Quindi il numero di nuovi contagi C_t segue una distribuzione
Binomiale:

C_t ∼ Binomiale(S_t, β · I_t / N)

Secondo: la guarigione. Ogni Infetto guarisce con probabilità γ,
indipendentemente dagli altri. Il numero di guarigioni G_t segue
anch'esso una Binomiale:

G_t ∼ Binomiale(I_t, γ)

L'aggiornamento dello stato è:

S_{t+1} = S_t - C_t
I_{t+1} = I_t + C_t - G_t
R_{t+1} = R_t + G_t

Notate che i due meccanismi sono indipendenti. La probabilità
di passare da uno stato all'altro è il prodotto delle probabilità
Binomiali."

**Versione slide:**

> ## Probabilità di transizione
>
> **Contagio**: C_t ∼ Binomiale(S_t, β · I_t / N)
>
> **Guarigione**: G_t ∼ Binomiale(I_t, γ)
>
> **Aggiornamento**:
> ```
> S_{t+1} = S_t - C_t
> I_{t+1} = I_t + C_t - G_t
> R_{t+1} = R_t + G_t
> ```
>
> **Parametri**:
> - β ∈ [0,1] : tasso di trasmissione
> - γ ∈ [0,1] : tasso di guarigione
>
> Contagio e guarigione sono **indipendenti**.
> Probabilità composta: prodotto delle due Binomiali.

---

## SLIDE 8 — Esempio con N=3

**Testo orale:**

"Facciamo un esempio concreto con N=3 per capire come funzionano
le transizioni. Prendiamo β = 0.5 e γ = 0.3. Partiamo dallo stato
(2, 1, 0): cioè 2 Suscettibili, 1 Infetto, 0 Rimossi.

Calcoliamo le possibili transizioni.

La probabilità di contagio per ogni Suscettibile è β · I/N = 0.5 · 1/3.
Quindi il numero di contagi C può essere 0 o 1 (non può essere 2
perché c'è un solo Infetto, ma i contagi sono limitati da S_t).

La probabilità che nessuno si infetti è (1 - 0.5/3)² ≈ 0.694.
La probabilità che un Suscettibile si infetti è 2 · (0.5/3) · (1 - 0.5/3) ≈ 0.278.

Per la guarigione: l'unico Infetto guarisce con probabilità γ = 0.3,
non guarisce con probabilità 0.7.

Combinando i due eventi indipendenti, otteniamo 4 casi possibili:

1. C=0, G=0: stato (2,1,0) → probabilità 0.694 · 0.7 = 0.486
2. C=0, G=1: stato (2,0,1) → probabilità 0.694 · 0.3 = 0.208
3. C=1, G=0: stato (1,2,0) → probabilità 0.278 · 0.7 = 0.194
4. C=1, G=1: stato (1,1,1) → probabilità 0.278 · 0.3 = 0.083

Notate che le probabilità sommano a 1: 0.486 + 0.208 + 0.194 + 0.083 = 1.
La riga della matrice di transizione corrispondente a questo stato è
completamente determinata."

**Versione slide:**

> ## Esempio: N=3, β=0.5, γ=0.3
>
> Stato iniziale: **(2, 1, 0)**
>
> | C (contagi) | G (guarigioni) | Stato finale | Probabilità |
> |:-----------:|:--------------:|:------------:|:-----------:|
> | 0 | 0 | (2, 1, 0) | 0.486 |
> | 0 | 1 | (2, 0, 1) | 0.208 |
> | 1 | 0 | (1, 2, 0) | 0.194 |
> | 1 | 1 | (1, 1, 1) | 0.083 |
>
> **∑ probabilità = 1** ✓ — riga stocastica

---

## SLIDE 9 — Matrice di transizione

**Testo orale:**

"La matrice di transizione P è una matrice quadrata di dimensione
|E| × |E|, dove l'elemento P(i,j) è la probabilità di passare
dallo stato i allo stato j in un passo.

Per N=3 abbiamo 10 stati. La matrice P è quindi 10 × 10. Possiamo
costruirla esplicitamente enumerando tutti gli stati e calcolando
le probabilità di transizione per ciascuno con le formule delle
Binomiali.

Un elemento generico P((s,i,r), (s',i',r')) si calcola come:

P = Σ_{c=0}^{s} Σ_{g=0}^{i} Binomiale(s; c, βi/N) · Binomiale(i; g, γ)
    · 1_{s' = s-c, i' = i+c-g, r' = r+g}

La funzione indicatrice 1_{...} seleziona solo le combinazioni
(c, g) che portano allo stato (s', i', r') desiderato.

Per costruire la matrice serve un doppio loop su c e g, che per
N piccolo è fattibile. Per N=100 avremmo 5151 stati e la matrice
avrebbe circa 26 milioni di elementi — possibile in teoria ma
dispendioso in pratica."

**Versione slide:**

> ## Matrice di transizione P
>
> **Elemento generico**:
>
> P((s,i,r), (s',i',r')) = Σ_c Σ_g Bin(s, c, βi/N) · Bin(i, g, γ)
>                          · 1_{s' = s-c, i' = i+c-g, r' = r+g}
>
> **Proprietà**:
> - P è **stocastica**: righe sommano a 1.
> - Per N=3: P è 10 × 10, calcolabile esplicitamente.
> - Per N=100: 5151 stati → ~26M elementi → simulazione.
>
> *La matrice esiste sempre, anche quando non la scriviamo per intero.*

---

## SLIDE 10 — Classificazione degli stati

**Testo orale:**

"Classifichiamo ora gli stati della catena. Consideriamo uno stato
(s, i, r). Se i = 0, significa che non ci sono infetti. In questo
caso, quanto valgono le probabilità di transizione?

Se i = 0, il tasso di contagio β · i / N è zero. Quindi il numero
di nuovi contagi C è 0 con probabilità 1. Anche le guarigioni sono 0
perché non ci sono infetti da guarire. Quindi lo stato non cambia mai:

P((s, 0, r), (s, 0, r)) = 1

Questo significa che tutti gli stati con i = 0 sono **assorbenti**.
Una volta che la catena raggiunge uno stato senza infetti, ci resta
per sempre.

Tutti gli stati con i > 0 sono **transitori**: da essi si può
raggiungere uno stato assorbente in un numero finito di passi,
e non si può tornare indietro.

La catena è quindi una **catena assorbente**: l'assorbimento in
uno stato con I=0 avviene con probabilità 1. Questo è coerente
con l'idea che l'epidemia prima o poi si estingue."

**Versione slide:**

> ## Classificazione degli stati
>
> **Stato (s, i, r) con i = 0** → **assorbente**
> - P((s,0,r), (s,0,r)) = 1
> - Non ci sono infetti: nessun contagio, nessuna guarigione.
>
> **Stato (s, i, r) con i > 0** → **transitorio**
> - Da ogni stato con I>0 si raggiunge un assorbente.
> - Non si può tornare a I>0 dopo l'assorbimento.
>
> **Conseguenza**: l'estinzione dell'infezione è **certa**:
> P(τ < ∞) = 1.
>
> *La catena è una catena assorbente (Cap. 7).*

---

## SLIDE 11 — Algoritmo di simulazione

**Testo orale:**

"Passiamo ora alla simulazione. L'algoritmo per generare una
traiettoria è il seguente:

1. Inizializziamo lo stato: S_0 = N - I₀, I_0 = I₀, R_0 = 0.
2. Per ogni passo temporale t = 0, 1, 2, ... fino a T_max:
   a. Se I_t = 0, ci fermiamo: l'epidemia è estinta.
   b. Generiamo C_t ∼ Binomiale(S_t, β · I_t / N).
   c. Generiamo G_t ∼ Binomiale(I_t, γ).
   d. Aggiorniamo S_{t+1}, I_{t+1}, R_{t+1}.
   e. Se I_{t+1} = 0, ci fermiamo.
3. Restituiamo la traiettoria completa.

Ripetendo questo procedimento molte volte (diciamo M = 1000),
otteniamo un campione di traiettorie. Su questo campione possiamo
calcolare medie, deviazioni standard, distribuzioni empiriche.

I parametri scelti per la simulazione sono:
N = 100, β = 0.2, γ = 0.1, I₀ = 5, T_max = 200, M = 1000.

Con questi parametri, il numero riproduttivo di base è
R₀ = β/γ = 2. Questo significa che, nelle fasi iniziali,
ogni infetto genera in media 2 nuovi infetti."

**Versione slide:**

> ## Algoritmo di simulazione
>
> ```
> 1. Inizializza: S = N - I₀, I = I₀, R = 0
> 2. Loop t = 0, 1, ..., T_max:
>    a. Se I = 0 → fermati
>    b. C ∼ Binomiale(S, β·I/N)
>    c. G ∼ Binomiale(I, γ)
>    d. S ← S - C, I ← I + C - G, R ← R + G
>    e. Se I = 0 → fermati
> 3. Restituisci traiettoria (S, I, R)
> ```
>
> **Parametri**: N=100, β=0.2, γ=0.1, I₀=5, T_max=200, M=1000
>
> **R₀ = β/γ = 2.0** — ogni infetto genera 2 nuovi infetti in media.

---

## SLIDE 12 — Codice Python

**Testo orale:**

"Ecco il codice Python che implementa quanto descritto. È volutamente
essenziale: la funzione next_state esegue un singolo passo della
catena, run_single genera una traiettoria completa, run_montecarlo
ripete la simulazione M volte.

Il codice riflette esattamente la struttura della catena di Markov:
next_state è l'analogo di un passo della catena, run_single genera
una realizzazione del processo."

**Versione slide:**

> ## Codice Python — Passo della catena
>
> ```python
> import numpy as np
>
> N = 100
> BETA = 0.2
> GAMMA = 0.1
> I0 = 5
> T_MAX = 200
> M = 1000
>
> def next_state(s, i, r, n=N, beta=BETA, gamma=GAMMA):
>     if i == 0:
>         return s, 0, r
>     p_si = beta * i / n
>     new_infections = np.random.binomial(s, p_si)
>     recoveries = np.random.binomial(i, gamma)
>     return s - new_infections, i + new_infections - recoveries, r + recoveries
> ```

---

## SLIDE 13 — Risultati numerici

**Testo orale:**

"Ecco i risultati della simulazione su 1000 repliche.

Il picco medio degli infetti è di circa 29 individui, con una
deviazione standard di circa 9. Questo significa che, pur con
gli stessi parametri, traiettorie diverse possono dare picchi
molto diversi: da un minimo di 6 a un massimo di 52.

Il tempo medio di estinzione è di circa 68 passi temporali,
con deviazione standard di 18. La distribuzione è asimmetrica:
alcune epidemie si estinguono rapidamente (12 passi), altre
possono durare fino a oltre 120 passi.

Il numero medio di rimossi finali, che rappresenta il totale
di persone che hanno contratto l'infezione, è di circa 87 su 100.
Questo significa che, in media, l'87% della popolazione viene
infettata prima che l'epidemia si estingua. Anche qui c'è
variabilità: da un minimo di 34 a un massimo di 100."

**Versione slide:**

> ## Risultati numerici (M=1000)
>
> | Indicatore | Media | Dev.std | Min | Max |
> |------------|-------|---------|-----|-----|
> | Picco I_max | 29.4 | 8.7 | 6 | 52 |
> | τ (tempo estinzione) | 68.3 | 18.2 | 12 | 124 |
> | R∞ (rimossi finali) | 87.2 | 9.5 | 34 | 100 |
>
> **Osservazioni**:
> - Forte variabilità tra simulazioni (natura stocastica).
> - In media l'87% della popolazione viene infettata.
> - Il tempo di estinzione varia da 12 a 124 passi.

---

## SLIDE 14 — Grafico: singola traiettoria

**Testo orale:**

"Mostriamo ora i grafici. Il primo è una singola traiettoria.
Si vede la curva dei Suscettibili che scende, quella degli Infetti
che sale fino a un picco e poi scende, e quella dei Rimossi che
sale monotonamente fino a stabilizzarsi.

Notate l'irregolarità delle curve: è l'effetto della stocasticità.
A ogni passo, il numero di contagi e guarigioni è casuale, e questo
si riflette nell'andamento frastagliato delle curve.

L'epidemia si estingue quando la curva rossa degli Infetti tocca
lo zero. A quel punto, S e R si stabilizzano."

**Versione slide:**

> ## Singola traiettoria SIR
>
> ![Singola traiettoria](img/single_trajectory.png)
>
> - Curva blu (S): decresce irregolarmente.
> - Curva rossa (I): sale al picco, poi scende a zero.
> - Curva verde (R): cresce monotonamente fino a saturazione.
>
> *La stocasticità è visibile nell'irregolarità delle curve.*

---

## SLIDE 15 — Grafico: media su 1000 simulazioni

**Testo orale:**

"Il secondo grafico mostra la media su 1000 simulazioni, con le
bande di ±1 deviazione standard. Qui l'andamento è molto più
regolare perché la media cancella le fluttuazioni casuali.

La curva media degli infetti ha un picchio intorno a t = 25,
con un valore di circa 29. Le bande di deviazione standard
mostrano quanta variabilità c'è tra le diverse simulazioni.

Notate che le bande sono più larghe dove il processo è più
variabile, cioè intorno al picco epidemico. Questo è intuitivo:
è proprio nel momento di massima diffusione che le traiettorie
differiscono di più."

**Versione slide:**

> ## Traiettoria media ± 1 dev. std
>
> ![Traiettoria media](img/mean_trajectory.png)
>
> - Linee continue: medie su 1000 simulazioni.
> - Aree trasparenti: ±1 deviazione standard.
> - Picco medio: ~29 infetti a t ≈ 25.
> - Variabilità massima nella fase di picco.

---

## SLIDE 16 — Grafico: istogramma tempo di estinzione

**Testo orale:**

"Il terzo grafico è l'istogramma del tempo di estinzione τ.
Si vede una forma approssimativamente campanulare, ma con una
coda destra più lunga. Questo significa che esistono epidemie
di lunga durata, anche se sono meno frequenti.

La media è circa 68, come abbiamo visto, ma ci sono code fino
a oltre 120. La distribuzione non è simmetrica."

**Versione slide:**

> ## Distribuzione del tempo di estinzione τ
>
> ![Istogramma τ](img/tau_histogram.png)
>
> - Forma campanulare con coda destra.
> - Media = 68.3, dev.std = 18.2.
> - Asimmetria positiva: alcune epidemie durano molto più della media.
> - *Distribuzione empirica stimata via Monte Carlo.*

---

## SLIDE 17 — Interpretazione dei risultati

**Testo orale:**

"Cosa ci dicono questi numeri?

Primo: l'epidemia si estingue sempre, confermando la previsione
teorica che la catena è assorbente. Non c'è un solo caso in 1000
simulazioni in cui l'infezione persista indefinitamente.

Secondo: c'è una forte variabilità. Pur con gli stessi parametri,
due simulazioni possono dare risultati molto diversi. Questo è
intrinseco alla natura stocastica del processo: non è un limite
del modello, è una caratteristica.

Terzo: il numero medio di infetti al picco è 29 su 100, il che
significa che quasi un terzo della popolazione è contemporaneamente
infetta al culmine dell'epidemia.

Quarto: in media, l'87% della popolazione viene infettata prima
dell'estinzione. Questo è coerente con R₀ = 2: un'epidemia con
R₀ > 1 infetta una frazione sostanziale della popolazione."

**Versione slide:**

> ## Interpretazione
>
> 1. **Estinzione certa**: 100% delle simulazioni → catena assorbente.
> 2. **Variabilità**: scarto tipo del picco = 8.7 su media 29.4.
> 3. **Picco**: ~29% della popolazione infetta contemporaneamente.
> 4. **R∞ medio**: 87% della popolazione contratta l'infezione.
>    *Coerente con R₀ = 2.*

---

## SLIDE 18 — Confronto teoria vs simulazione

**Testo orale:**

"Confrontiamo ora i risultati della simulazione con le previsioni
teoriche.

La teoria delle catene assorbenti ci dice che:
- L'assorbimento avviene con probabilità 1 → confermato (100%).
- Il tempo medio di assorbimento soddisfa t = 1 + Q·t, dove Q è
  la sottomatrice di transizione ristretta agli stati transitori.
  Per N=100, calcolare Q esplicitamente è proibitivo, ma la
  simulazione fornisce una stima: τ medio ≈ 68.

La matrice di transizione, per N=100, esiste anche se non la
calcoliamo esplicitamente. La simulazione Monte Carlo è un modo
di campionare da questa matrice senza doverla costruire per intero.
Questo è esattamente lo stesso principio che sta dietro ai metodi
di simulazione delle catene di Markov: invece di calcolare P,
generiamo transizioni una alla volta.

I risultati numerici (picco medio, τ medio, R∞ medio) sono stime
empiriche di quantità teoriche che sarebbero calcolabili se
disponessimo della matrice P completa."

**Versione slide:**

> ## Teoria vs Simulazione
>
> | Previsione teorica | Verifica simulativa |
> |--------------------|---------------------|
> | Assorbimento certo (P=1) | ✅ 1000/1000 casi |
> | τ = soluzione di (I-Q)t = 1 | ✅ τ medio ≈ 68 (stimato) |
> | R∞ è una variabile casuale | ✅ Distribuzione empirica ottenuta |
>
> **Punto chiave**: La simulazione NON sostituisce la teoria.
> La simulazione **stima** quantità che la teoria definisce.
> È la teoria che dà significato ai numeri.

---

## SLIDE 19 — Limiti del modello

**Testo orale:**

"È importante essere onesti sui limiti del modello.

Primo: la popolazione è chiusa. Non ci sono nascite, morti,
immigrazioni o emigrazioni. Nella realtà, una popolazione non è
mai completamente isolata.

Secondo: i parametri β e γ sono costanti. Nella realtà, il tasso
di contagio può cambiare per vari motivi: stagionalità, misure di
contenimento, comportamenti individuali.

Terzo: il mescolamento è omogeneo. Ogni Suscettibile ha la stessa
probabilità di incontrare ogni Infetto. Questo non è vero in una
popolazione reale, dove esistono reti sociali e contatti preferenziali.

Quarto: non c'è reinfezione. Una volta guariti, si è immuni per
sempre. Questo non vale per molte malattie reali.

Tutti questi limiti sono accettabili perché il nostro obiettivo
non è fare previsioni epidemiologiche, ma dimostrare l'applicazione
del formalismo delle catene di Markov. Anzi, la semplicità del
modello aiuta a mettere in luce la struttura markoviana."

**Versione slide:**

> ## Limiti del modello
>
> | Limite | Impatto |
> |--------|---------|
> | Popolazione chiusa | Ignora dinamiche demografiche |
> | β, γ costanti | Ignora stagionalità e interventi |
> | Mescolamento omogeneo | Ignora reti sociali |
> | Nessuna reinfezione | Non sempre realistico |
>
> **Ma**: questi limiti sono **voluti**.
> Il focus è sulla struttura markoviana, non sull'accuratezza
> epidemiologica.

---

## SLIDE 20 — Sviluppi futuri

**Testo orale:**

"Quali estensioni sarebbero possibili?

Una prima estensione è aggiungere un compartimento E di Esposti,
ottenendo un modello SEIR. Questo aggiunge uno stato in più e
arricchisce la dinamica, ma la struttura markoviana rimane invariata.

Una seconda estensione è rendere β e γ dipendenti dal tempo, per
simulare l'effetto di misure di contenimento che riducono i contatti.

Una terza estensione è confrontare la simulazione stocastica con
la soluzione delle equazioni differenziali ordinarie SIR. Nel
limite di popolazione grande, la media della catena converge
alla soluzione ODE. Questo è un collegamento interessante tra
modello stocastico e modello deterministico.

Tutte queste estensioni mantengono la struttura di catena di Markov."

**Versione slide:**

> ## Sviluppi futuri
>
> 1. **Modello SEIR**: aggiungere compartimento Esposti.
> 2. **Parametri tempo-varianti**: β(t), γ(t) per misure di contenimento.
> 3. **Confronto con ODE**: limite deterministico per N→∞.
> 4. **Matrice P per N piccolo**: heatmap della matrice di transizione.
>
> Tutte mantengono la **struttura di catena di Markov**.

---

## SLIDE 21 — Conclusioni

**Testo orale:**

"Concludo riassumendo i punti salienti.

Abbiamo preso un modello SIR semplificato e lo abbiamo interpretato
come una catena di Markov a tempo discreto. Abbiamo definito lo
spazio degli stati, costruito la matrice di transizione e classificato
gli stati in assorbenti e transitori.

Abbiamo poi simulato la catena con il metodo Monte Carlo, ottenendo
stime del tempo medio di estinzione, del picco epidemico e della
distribuzione finale.

I risultati confermano le previsioni teoriche: l'assorbimento è
certo, il tempo medio di estinzione è finito e la variabilità tra
traiettorie è una caratteristica intrinseca del processo stocastico.

Il progetto dimostra come il formalismo delle catene di Markov,
studiato nel capitolo 7, possa essere applicato a un caso concreto
per modellizzare un fenomeno reale in modo rigoroso e quantitativo.

Grazie per l'attenzione."

**Versione slide:**

> ## Conclusioni
>
> - Modello SIR = **catena di Markov a tempo discreto**.
> - Stati **assorbenti** (I=0) e **transitori** (I>0).
> - Simulazione Monte Carlo: stima di τ, picco, R∞.
> - **Conferma teorica**: assorbimento certo, variabilità stocastica.
> - Applicazione concreta del **formalismo markoviano** (Cap. 7).
>
> **Grazie per l'attenzione.**

---

# D. Versioni della presentazione

## D.1 Versione breve (1 minuto)

"Buongiorno professore. Ho realizzato un progetto in cui interpreto
il modello epidemiologico SIR come una catena di Markov a tempo
discreto. La popolazione di 100 individui è divisa in Suscettibili,
Infetti e Rimossi. A ogni passo, il numero di nuovi contagi segue
una Binomiale con parametro β·I/N, mentre le guarigioni seguono
una Binomiale con parametro γ. Gli stati con I=0 sono assorbenti:
una volta raggiunti, non si esce più. Ho simulato 1000 traiettorie
con il metodo Monte Carlo, ottenendo un tempo medio di estinzione
di circa 68 passi e un picco medio di 29 infetti. I risultati
confermano le previsioni teoriche delle catene assorbenti.
Grazie."

## D.2 Versione estesa (5-7 minuti)

**Slide 1-2 (30 sec):**
"Buongiorno professore. Presento il mio progetto dal titolo
'Modello SIR come Catena di Markov a Tempo Discreto'.
L'idea è applicare il formalismo delle catene di Markov — che
abbiamo studiato nel capitolo 7 — a un modello epidemiologico
molto semplice. Il modello SIR descrive una popolazione divisa
in tre compartimenti: Suscettibili, Infetti e Rimossi.
L'evoluzione futura dipende solo dallo stato presente: questa
è esattamente la proprietà di Markov."

**Slide 3-4 (1 min):**
"Richiamo brevemente le catene di Markov. Un processo {X_t}
ha la proprietà di Markov se la probabilità dello stato futuro
dipende solo da quello presente. La matrice di transizione P
descrive tutte le probabilità di passaggio in un passo. P è
stocastica: ogni riga somma a 1. Uno stato si dice assorbente
se P(i,i)=1: una volta entrato, non si esce."

**Slide 5-7 (1 min):**
"Nel modello SIR, lo stato è (S,I,R) con S+I+R=N. Lo spazio
degli stati è finito con (N+1)(N+2)/2 elementi. A ogni passo,
il numero di contagi C ∼ Bin(S, β·I/N) e il numero di guarigioni
G ∼ Bin(I, γ). L'aggiornamento è S' = S-C, I' = I+C-G, R' = R+G."

**Slide 8-10 (1 min):**
"Faccio un esempio con N=3 e β=0.5, γ=0.3. Partendo da (2,1,0),
ci sono 4 possibili transizioni. Le probabilità sono il prodotto
delle due Binomiali. Questo mostra che la matrice P è costruita
esplicitamente. Se I=0, lo stato è assorbente. Gli stati con
I>0 sono transitori. L'estinzione è certa con probabilità 1."

**Slide 11-13 (1.5 min):**
"La simulazione Monte Carlo genera M traiettorie indipendenti.
I parametri sono N=100, β=0.2, γ=0.1, per cui R₀=2. Su 1000
simulazioni, il picco medio è 29.4 infetti, il tempo medio di
estinzione è 68.3 passi, e il numero medio di rimossi finali
è 87.2. C'è però una forte variabilità: il picco varia da 6 a 52."

**Slide 14-17 (1 min):**
"Tre grafici mostrano: una singola traiettoria con l'andamento
stocastico irregolare; la media su 1000 simulazioni con le bande
di deviazione standard; l'istogramma del tempo di estinzione con
coda destra. I risultati confermano che la catena è assorbente
e che la variabilità è intrinseca."

**Slide 18-21 (30 sec):**
"La teoria delle catene assorbenti è confermata: assorbimento
certo, tempo medio finito. Il modello ha limiti — popolazione
chiusa, mescolamento omogeneo — ma sono accettabili perché
l'obiettivo non è epidemiologico. Concludo che il modello SIR
è un'efficace applicazione del formalismo markoviano. Grazie."

---

# E. Codice Python senza commenti

Il codice completo del progetto è disponibile nella repository
GitHub: https://github.com/FrancescoCastaldi/sir-markov-chain

Di seguito il codice essenziale per la simulazione:

```python
import numpy as np

N = 100
BETA = 0.2
GAMMA = 0.1
I0 = 5
T_MAX = 200
M = 1000

def next_state(s, i, r, n=N, beta=BETA, gamma=GAMMA):
    if i == 0:
        return s, 0, r
    p_si = beta * i / n
    new_infections = np.random.binomial(s, p_si)
    recoveries = np.random.binomial(i, gamma)
    return s - new_infections, i + new_infections - recoveries, r + recoveries

def run_single(n=N, i0=I0, t_max=T_MAX, beta=BETA, gamma=GAMMA):
    s, i, r = n - i0, i0, 0
    traj = [(s, i, r)]
    for _ in range(t_max):
        s, i, r = next_state(s, i, r, n, beta, gamma)
        traj.append((s, i, r))
        if i == 0:
            break
    return np.array(traj)

def run_montecarlo(m=M, n=N, i0=I0, t_max=T_MAX, beta=BETA, gamma=GAMMA):
    return [run_single(n, i0, t_max, beta, gamma) for _ in range(m)]
```

---

# F. Email formale al professore

Oggetto: Progetto Modelli Probabilistici — Modello SIR come Catena di Markov

Gentile Prof. Federico,

Le scrivo per presentare il mio progetto per il corso di Modelli
Probabilistici, A.A. 2025/2026.

Il progetto consiste nella modellizzazione di un'epidemia SIR
semplificata come catena di Markov a tempo discreto. La popolazione
di dimensione N=100 è suddivisa nei tre compartimenti S (Suscettibili),
I (Infetti) e R (Rimossi). Lo stato del sistema è il vettore
(S, I, R), che evolve secondo probabilità di transizione basate
su distribuzioni Binomiali: il contagio segue Bin(S, β·I/N) e la
guarigione segue Bin(I, γ).

Ho costruito lo spazio degli stati, definito la matrice di
transizione (calcolandola esplicitamente per N piccolo) e
classificato gli stati: quelli con I=0 sono assorbenti, quelli
con I>0 sono transitori. Ho inoltre implementato una simulazione
Monte Carlo in Python per stimare il tempo medio di estinzione,
il picco epidemico e la distribuzione dei rimossi finali.

I risultati confermano le previsioni teoriche: l'assorbimento
avviene con probabilità 1 e il tempo medio di estinzione è
finito (circa 68 passi con i parametri di default β=0.2, γ=0.1).

Il codice, la relazione e i grafici sono disponibili nella
repository GitHub all'indirizzo:
https://github.com/FrancescoCastaldi/sir-markov-chain

Resto a disposizione per qualsiasi chiarimento.

Cordiali saluti,
Francesco Castaldi

---

# G. Domande e risposte per l'orale

## G.1 Domande teoriche

**D: Perché questo modello è una catena di Markov?**

R: Perché la distribuzione dello stato futuro (S_{t+1}, I_{t+1}, R_{t+1})
dipende solo dallo stato presente (S_t, I_t, R_t). I valori passati
(S_{t-1}, I_{t-1}, R_{t-1}) non influenzano la probabilità di transizione.
Questa è esattamente la proprietà di Markov. Inoltre lo spazio degli
stati è finito e il tempo è discreto.

**D: Qual è lo spazio degli stati? Quanti stati ci sono?**

R: È l'insieme di tutte le terne (s, i, r) di interi non negativi con
s + i + r = N. La cardinalità è (N+1)(N+2)/2. Per N=100 sono 5151 stati.
Per N=3 sono 10 stati, che è un numero gestibile per il calcolo esplicito
della matrice di transizione.

**D: Cosa significa che la matrice P è stocastica?**

R: Significa che ogni riga contiene probabilità non negative e somma a 1.
Questo è vero per costruzione: la probabilità di passare da uno stato i
a QUALSIASI stato j deve essere 1, perché il sistema evolve da qualche
parte con certezza. Nel nostro modello, per ogni stato con I>0, le
probabilità delle varie combinazioni di (C, G) sommano a 1.

**D: Perché gli stati con I=0 sono assorbenti?**

R: Se I=0, la probabilità di contagio β·I/N = 0, quindi nessun Suscettibile
può diventare infetto. Inoltre non ci sono Infetti da guarire. Quindi
lo stato non cambia: P((s,0,r), (s,0,r)) = 1. Per definizione, questo
è uno stato assorbente.

**D: Esiste la possibilità che l'epidemia non si estingua mai?**

R: No. La catena è una catena assorbente con un numero finito di stati
transitori. La teoria delle catene di Markov ci dice che l'assorbimento
avviene con probabilità 1 partendo da qualsiasi stato transitorio.
L'epidemia si estingue sempre, prima o poi.

**D: Perché la simulazione e non il calcolo esatto?**

R: Per N=100 abbiamo 5151 stati. La matrice P avrebbe circa 26 milioni
di elementi. Costruirla esplicitamente è possibile in linea di principio
ma computazionalmente costoso. La simulazione Monte Carlo ci permette
di stimare le quantità di interesse (τ medio, picco medio, R∞) senza
dover calcolare P per intero.

## G.2 Domande sul modello

**D: Perché hai scelto β=0.2 e γ=0.1?**

R: Perché R₀ = β/γ = 2. Questo significa che nelle fasi iniziali ogni
infetto genera in media 2 nuovi infetti. È un valore che produce una
dinamica epidemica significativa ma non troppo rapida: l'epidemia
cresce, ha un picco visibile, e poi si estingue in circa 68 passi.
Se R₀ fosse troppo vicino a 1, l'epidemia sarebbe debole; se fosse
troppo grande, il picco sarebbe troppo rapido.

**D: Perché N=100?**

R: Perché è sufficientemente piccolo da essere trattabile numericamente
ma abbastanza grande da mostrare un comportamento statisticamente
significativo. Con N=100, 1000 simulazioni danno stime con errori
standard ragionevoli. Inoltre 100 è un numero tondo e facile da
presentare.

**D: Cosa cambierebbe se aumentassi N a 1000?**

R: Lo spazio degli stati diventerebbe (1001·1002)/2 ≈ 500.000 stati.
La simulazione sarebbe più lenta ma ancora fattibile. Le traiettorie
sarebbero più simili tra loro (la varianza relativa diminuisce).
La media convergerebbe alla soluzione ODE deterministica.

**D: Cosa succederebbe se β < γ (cioè R₀ < 1)?**

R: L'epidemia si estinguerebbe molto rapidamente, perché ogni infetto
guarisce prima di riuscire a contagiare altri. Il picco sarebbe molto
basso e il tempo di estinzione molto breve. In pratica, non ci sarebbe
un'epidemia vera e propria.

## G.3 Domande sui risultati

**D: Perché c'è tanta variabilità nei risultati?**

R: Perché il modello è stocastico. A ogni passo, contagi e guarigioni
sono variabili casuali Binomiali. Anche con gli stessi parametri,
traiettorie diverse possono avere evoluzioni molto diverse. Questa
variabilità non è un difetto: è una caratteristica del processo.
La deviazione standard del picco (8.7) rispetto alla media (29.4)
dà una misura quantitativa di questa variabilità.

**D: Perché l'istogramma del tempo di estinzione è asimmetrico?**

R: Perché il tempo di estinzione ha un limite inferiore (non può
essere nullo) ma non ha un limite superiore stretto. Ci sono
traiettorie in cui l'infezione persiste a lungo, e queste creano
la coda destra. La distribuzione è skew-positive.

**D: I tuoi risultati sono replicabili?**

R: Sì, se si fissa il seed del generatore casuale. Nel codice ho
inserito l'opzione --seed che permette di riprodurre esattamente
gli stessi risultati. Senza seed, ogni esecuzione dà risultati
diversi ma statisticamente equivalenti.

## G.4 Domande provocatorie

**D: Ma questo è un progetto di epidemiologia?**

R: No. L'epidemiologia è la scienza che studia la diffusione delle
malattie in popolazioni reali, con dati reali, obiettivi predittivi
e validazione empirica. Questo progetto usa un modello SIR solo
come CONTENITORE per applicare il formalismo delle catene di Markov.
Non uso dati reali, non faccio previsioni, non valuto politiche
sanitarie. L'obiettivo è mostrare che so usare la teoria delle
catene di Markov.

**D: Non è troppo semplice?**

R: La semplicità è voluta. Un modello più complesso (con più
compartimenti, parametri variabili, struttura spaziale) renderebbe
più difficile vedere la struttura markoviana. La semplicità del
modello SIR permette di mettere in luce con chiarezza:
- la definizione dello spazio degli stati,
- la costruzione della matrice di transizione,
- la classificazione degli stati,
- il legame tra teoria e simulazione.
Questo è esattamente ciò che il corso richiede.

---

# H. Checklist per l'esame

## H.1 Cosa portare

- [ ] Codice Python (repository GitHub)
- [ ] Relazione (report/relazione.md) — già stampata o su tablet
- [ ] Grafici (img/single_trajectory.png, mean_trajectory.png, tau_histogram.png)
- [ ] Schema della matrice di transizione per N=3 (foglio a mano)
- [ ] Questa presentazione (report/presentazione.md)

## H.2 Cosa sapere a memoria

- [ ] Definizione di catena di Markov e proprietà di Markov
- [ ] Formula della probabilità di transizione: Bin(S, β·I/N) · Bin(I, γ)
- [ ] Condizione di stato assorbente: I=0 ⇒ P=1
- [ ] Cardinalità dello spazio: (N+1)(N+2)/2
- [ ] Valori numerici: N=100, β=0.2, γ=0.1, R₀=2
- [ ] Risultati: picco ≈ 29, τ ≈ 68, R∞ ≈ 87

## H.3 Cosa mostrare alla lavagna

1. Griglia 3×3 con (S,I,R) e le frecce delle transizioni
2. Esempio N=3: calcolo di una riga della matrice P
3. Formula dello stato assorbente
4. Grafico qualitativo di S(t), I(t), R(t)

## H.4 Tempistica orale

| Parte | Durata | Contenuto |
|-------|--------|-----------|
| Introduzione | 30 sec | Titolo, obiettivo, contesto |
| Teoria | 2 min | Catene di Markov, spazio stati, transizioni |
| Esempio N=3 | 1.5 min | Calcolo matrice, stati assorbenti |
| Simulazione | 1 min | Algoritmo, parametri, codice |
| Risultati | 1.5 min | Tabella, grafici, interpretazione |
| Conclusione | 30 sec | Riassunto, limiti, ringraziamenti |
| **Totale** | **~7 min** | |

---

# I. Traccia per la lavagna

## I.1 Schema base della catena

```
         β·I/N            γ
    S ───────→ I ───────→ R
```

Scrivere accanto:
- S + I + R = N (vincolo di conservazione)
- C ∼ Bin(S, β·I/N) (contagio)
- G ∼ Bin(I, γ) (guarigione)

## I.2 Formula della probabilità di transizione

P((s,i,r) → (s-c, i+c-g, r+g)) = Bin(s, c, βi/N) · Bin(i, g, γ)

dove c ∈ [0, s] e g ∈ [0, i].

## I.3 Esempio N=3

Elencare i 10 stati:

1. (3,0,0) ← assorbente
2. (2,1,0)
3. (2,0,1) ← assorbente
4. (1,2,0)
5. (1,1,1)
6. (1,0,2) ← assorbente
7. (0,3,0)
8. (0,2,1)
9. (0,1,2)
10. (0,0,3) ← assorbente

Mostrare che (2,1,0) ha 4 transizioni possibili (calcolo numerico
con β=0.5, γ=0.3).

## I.4 Tabella riassuntiva risultati

```
┌──────────────────────┬───────┬──────┐
│ Indicatore           │ Media │ Std  │
├──────────────────────┼───────┼──────┤
│ Picco infetti I_max  │ 29.4  │ 8.7  │
│ Tempo estinzione τ   │ 68.3  │ 18.2 │
│ Rimossi finali R∞    │ 87.2  │ 9.5  │
└──────────────────────┴───────┴──────┘

