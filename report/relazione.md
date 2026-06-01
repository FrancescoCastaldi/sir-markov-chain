# Simulazione di un modello epidemiologico SIR come catena di Markov a tempo discreto

**Autore**: Francesco Castaldi  
**Corso**: Modelli Probabilistici — Università di Bologna  
**Docente**: Prof. Salvatore Federico  
**A.A.**: 2025/2026

---

## 1. Introduzione

In questo progetto si studia un modello SIR semplificato come applicazione delle catene di Markov a tempo discreto. L’obiettivo non è descrivere un fenomeno epidemiologico reale in modo predittivo, ma usare un esempio intuitivo per applicare in modo concreto i concetti teorici del capitolo sulle catene di Markov della dispensa del corso, in particolare definizione di processo markoviano, matrice di transizione e comportamento nel tempo.[cite:1]

Il modello SIR è adatto a questo scopo perché permette di rappresentare una popolazione divisa in tre compartimenti: suscettibili, infetti e rimossi. L’evoluzione del sistema dipende solo dallo stato corrente, quindi è naturale interpretarlo come un processo stocastico markoviano a tempo discreto.[cite:1]

---

## 2. Definizione del Modello SIR

Si considera una popolazione chiusa di ampiezza fissata \(N=100\), suddivisa nei tre stati:

- \(S_t\): numero di suscettibili al tempo \(t\);
- \(I_t\): numero di infetti al tempo \(t\);
- \(R_t\): numero di rimossi al tempo \(t\).

Per ogni istante discreto vale la relazione di conservazione

\[
S_t + I_t + R_t = N.
\]

Il modello assume:

- popolazione chiusa;
- tempo discreto;
- probabilità di contagio \(\beta\) costante;
- probabilità di guarigione \(\gamma\) costante;
- assenza di nascite, morti e reinfezioni;
- stato \(R\) assorbente.

Nel progetto si usa una versione volutamente semplificata del modello, coerente con un’analisi didattica basata sulle catene di Markov. La semplificazione rende il modello matematicamente trasparente, ma limita il realismo biologico.

---

## 3. Costruzione della Catena di Markov

Il processo è definito da

\[
X_t = (S_t, I_t, R_t),
\]

con spazio degli stati

\[
E = \{(s,i,r)\in\mathbb{N}^3 : s+i+r=N\}.
\]

Poiché lo spazio degli stati è discreto e finito, il processo può essere descritto tramite una catena di Markov a tempo discreto con matrice di transizione.[cite:1]

La dinamica in un passo temporale è la seguente:

- ogni suscettibile può diventare infetto con probabilità \(p_{SI}(t)=\beta \frac{I_t}{N}\);
- ogni infetto può guarire con probabilità \(p_{IR}=\gamma\).

Indichiamo con \(C_t\) il numero di nuovi contagi e con \(G_t\) il numero di guarigioni. Allora:

\[
S_{t+1}=S_t-C_t,
\]
\[
I_{t+1}=I_t+C_t-G_t,
\]
\[
R_{t+1}=R_t+G_t.
\]

In questo modo la distribuzione dello stato futuro dipende solo dallo stato presente, che è esattamente la proprietà di Markov.[cite:1]

Lo stato con \(I_t=0\) è assorbente dal punto di vista epidemiologico: se non ci sono infetti, non si generano nuovi contagi e il processo rimane bloccato in una configurazione finale senza diffusione.

---

## 4. Simulazione Numerica

La simulazione è stata implementata in Python con aggiornamento iterativo dello stato. A ogni passo:

1. si calcola la probabilità di contagio;
2. si estraggono casualmente nuovi contagi e guarigioni;
3. si aggiorna il vettore di stato;
4. si interrompe la simulazione quando \(I_t=0\) oppure quando si raggiunge il tempo massimo.

Sono state eseguite simulazioni Monte Carlo per osservare sia una singola traiettoria sia il comportamento medio del sistema. Questo approccio è utile perché il processo è stocastico: una sola traiettoria non è sufficiente per descrivere in modo affidabile la dinamica complessiva.

---

## 5. Risultati

I risultati attesi della simulazione sono i seguenti:

- \(S_t\) tende a diminuire nel tempo;
- \(I_t\) cresce inizialmente, raggiunge un massimo e poi si estingue;
- \(R_t\) cresce in modo monotono;
- il processo termina in uno stato senza infetti.

La traiettoria media ottenuta su molte simulazioni mostra un andamento più regolare rispetto a una singola realizzazione. In particolare, il numero medio di infetti presenta un picco iniziale e successivamente si riduce fino all’estinzione.

Nel report finale vanno inseriti:

- il grafico dell’evoluzione di \(S_t\), \(I_t\), \(R_t\);
- la tabella con media degli infetti e tempo medio di estinzione;
- eventualmente anche la deviazione standard delle grandezze osservate.

---

## 6. Confronto Teoria e Simulazione

Dal punto di vista teorico, il modello è coerente con il formalismo delle catene di Markov: il futuro dipende solo dallo stato corrente, e la dinamica è descritta da transizioni probabilistiche tra stati del sistema.[cite:1]

La simulazione conferma qualitativamente quanto previsto dalla teoria. In particolare:

- l’assenza di memoria è rispettata;
- lo stato senza infetti corrisponde a una condizione di assorbimento;
- la variabilità tra traiettorie è una conseguenza naturale della natura stocastica del processo.

Va però sottolineato che la simulazione non fornisce una “prova” del modello, ma solo una verifica numerica del suo comportamento. La teoria resta il riferimento principale, mentre la simulazione serve a illustrare concretamente il processo e a osservare i risultati su campioni finiti.

---

## 7. Conclusioni

Il modello SIR discretizzato fornisce un esempio semplice ma efficace di catena di Markov. La sua utilità, in questo progetto, è didattica: permette di collegare una situazione intuitiva ai concetti teorici del corso, come spazio degli stati, probabilità di transizione, stati assorbenti e simulazione di processi stocastici.[cite:1]

Il principale limite del lavoro è la forte semplificazione del fenomeno: il modello non include struttura di contatto, eterogeneità tra individui, nascite, decessi o reinfezioni. Tuttavia, proprio questa semplicità lo rende adatto a uno studio universitario di probabilità, perché consente di focalizzarsi sulla costruzione markoviana del processo.

In conclusione, il progetto mostra come un modello SIR possa essere interpretato in modo rigoroso come catena di Markov a tempo discreto e simulato numericamente per studiarne il comportamento qualitativo.

---

## Riferimenti

- Federico, S. — *Dispensa Modelli Probabilistici*, Cap. 7, Unibo 2025/2026
- Norris, J.R. — *Markov Chains*, Cambridge University Press, 1997
