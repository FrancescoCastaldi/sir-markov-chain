# I 16 Teoremi "Puri" (con Dimostrazioni Snelle e Guida all'Orale)

Questo documento contiene **esclusivamente** i 16 enunciati che nelle dispense in inglese (esclusi capitoli 6 e 8) sono chiamati espressamente "Theorem". Abbiamo rimosso tutte le *Proposition* e i *Lemma*, e semplificato le dimostrazioni per renderle facili da capire, da ricordare e da esporre all'orale.

---

## 📖 Glossario: Le Parole Chiave (Spiegate in modo semplice)

Prima di iniziare, fissiamo il significato di ogni termine che incontreremo. Se all'esame ti viene un dubbio, torna mentalmente a queste definizioni semplici.

*   **Spazio di Probabilità $(\Omega, \mathcal{F}, \mathbb{P})$**: È "l'universo" del nostro esperimento casuale. $\Omega$ è la scatola con tutti i risultati possibili (es. le facce del dado). $\mathcal{F}$ è l'insieme delle domande a cui possiamo rispondere (es. "è uscito pari?"). $\mathbb{P}$ è il righello che misura quanto è probabile ogni evento (da 0 a 1).
*   **Variabile Aleatoria (v.a.) $X$**: Una funzione che prende un risultato astratto di $\Omega$ (es. "è uscita croce") e gli appiccica un numero (es. $X=1$). È semplicemente una misurazione casuale.
*   **i.i.d. (Indipendenti e Identicamente Distribuite)**: Il pane quotidiano della probabilità. Significa che lanci lo stesso dado più volte: il risultato di ieri non influenza quello di oggi (*Indipendenti*), e il dado è sempre lo stesso (*Identicamente Distribuite*).
*   **Valore Atteso $\mathbb{E}[X]$**: È la media aritmetica pesata. Se ripeti l'esperimento all'infinito, è il valore che ti aspetti di ottenere in media.
*   **Successione Monotona $X_n \uparrow X$**: Una sequenza di variabili che "cresce sempre" senza mai tornare indietro, avvicinandosi progressivamente a un tetto $X$.
*   **Quasi Certamente (q.c. o a.s.)**: Una cosa succede con probabilità 1 (ovvero 100%). Potrebbe esserci un'eccezione teorica bizzarra, ma è così remota che ha probabilità zero. All'atto pratico, significa "di sicuro".
*   **Misurabile (rispetto a un'informazione)**: Significa "non ha segreti". Se dico che $X$ è $\mathcal{F}_n$-misurabile, intendo che al tempo $n$ io conosco perfettamente il valore di $X$ guardando solo i dati passati.
*   **Catena di Markov**: Un processo "senza memoria". Il futuro dipende **solo** dal presente (dove mi trovo ora), non da tutto il tragitto passato per arrivarci.
*   **Tempo di Arresto $\tau$**: Una regola per fermare un gioco basata *solo* su ciò che hai visto finora, senza usare sfere di cristallo per guardare il futuro. (Es: "Mi fermo appena perdo 10 euro").
*   **Stato Ricorrente vs Transiente**: 
    *   *Ricorrente*: Un posto dove, se ci parti, prima o poi ci torni con certezza assoluta (probabilità 1).
    *   *Transiente*: Un posto dove c'è la probabilità che, se te ne vai, potresti non tornarci mai più.
*   **Distribuzione Stazionaria $\pi$**: L'equilibrio finale. È la situazione in cui, se fai partire la catena di Markov in quel modo, la catena rimarrà statisticamente identica per sempre, in perfetto equilibrio.

---

## 📌 I TEOREMI

### Capitolo 2 - Convergenze e Leggi dei Grandi Numeri

#### 1. Teorema 2.4.1 — Teorema di Estensione di Kolmogorov
**Cosa significa:** Dice che possiamo sempre "costruire" un universo matematico $(\Omega, \mathcal{F}, \mathbb{P})$ grande a piacere per ospitare una sequenza infinita di variabili aleatorie indipendenti. 
**Da dire al prof:** *"Professore, ci assicura che il nostro modello matematico non 'si rompe' se lanciamo una moneta infinite volte: esiste uno spazio di probabilità rigoroso che lo supporta."*
*   **Dimostrazione snella:** La dimostrazione completa è profonda (teoria della misura). All'orale, si dice semplicemente che per ogni famiglia di probabilità discrete $\mu_i$, è possibile costruire uno spazio prodotto infinito $\Omega = \prod E_i$ con una misura $\mathbb{P}$ che sui cilindri finiti fattorizza come prodotto delle $\mu_i$. 

#### 2. Teorema 2.7.6 — Convergenza Monotona (Beppo-Levi per serie)
**Cosa significa:** Se ho una sequenza di v.a. positive che crescono costantemente ($X_n \uparrow X$), allora il limite della loro media è uguale alla media del loro limite: $\lim \mathbb{E}[X_n] = \mathbb{E}[X]$.
**Dimostrazione snella:** 
1. Siccome $X_n$ cresce, anche la sequenza di numeri $\mathbb{E}[X_n]$ cresce, quindi ha un limite (chiamiamolo $L \le \mathbb{E}[X]$). 
2. Scrivendo $X_n$ come serie delle sue probabilità $x \mathbb{P}(X_n=x)$, poiché tutto è positivo e cresce, i teoremi sui limiti delle successioni monotone reali garantiscono che si può scambiare la somma (o l'integrale) con il limite.

#### 3. Teorema 2.7.10 — Convergenza Dominata di Lebesgue
**Cosa significa:** Permette di scambiare il limite con il valore atteso ($\lim \mathbb{E}[X_n] = \mathbb{E}[X]$) purché la sequenza sia "schiacciata" o dominata da una variabile $Z$ più grande ma con media finita ($|X_n| \le Z$).
**Da dire al prof:** *"Questo è essenziale per la Rovina del Giocatore, per far passare il limite sotto il valore atteso."*
**Dimostrazione snella (usando Fatou):**
1. Abbiamo $|X_n| \le Z$, quindi $Z + X_n \ge 0$ e $Z - X_n \ge 0$.
2. Usiamo Fatou sulle due: $\mathbb{E}[Z+X] \le \liminf \mathbb{E}[Z+X_n]$ implica $\mathbb{E}[X] \le \liminf \mathbb{E}[X_n]$.
3. $\mathbb{E}[Z-X] \le \liminf \mathbb{E}[Z-X_n]$ implica $\mathbb{E}[X] \ge \limsup \mathbb{E}[X_n]$.
4. Ne segue che liminf e limsup coincidono, quindi il limite esiste ed è $\mathbb{E}[X]$.

#### 4. Teorema 2.7.11 — Versioni Condizionate delle Convergenze
**Cosa significa:** Ripete i 3 teoremi principali (Monotona, Fatou, Dominata) ma mettendoci "condizionato a $Y$" ovunque ($\mathbb{E}[X_n | Y] \to \mathbb{E}[X|Y]$). 
**Dimostrazione snella:** Deriva direttamente dalle definizioni delle versioni "normali", applicate in ogni sottomondo (atomo) definito dall'informazione nota $Y=y$.

#### 5. Teorema 2.8.1 — Legge Debole dei Grandi Numeri (WLLN)
**Cosa significa:** All'aumentare dei tentativi $n$, la media campionaria si avvicina sempre di più alla media teorica $m$. (Converge *in probabilità*: la probabilità di sbagliare clamorosamente va a zero).
**Da dire al prof:** *"Si dimostra usando il trucco della Disuguaglianza di Chebyshev sulla varianza della somma."*
**Dimostrazione snella:** 
1. La media empirica è $S_n/n$. Calcoliamo $\mathbb{E}[S_n/n] = m$.
2. Troviamo la varianza: $\text{Var}(S_n/n) = \frac{n \sigma^2}{n^2} = \frac{\sigma^2}{n}$.
3. Applichiamo Chebyshev: $\mathbb{P}(|S_n/n - m| \ge \epsilon) \le \frac{\sigma^2}{n \epsilon^2}$.
4. Per $n \to \infty$, questa roba fa chiaramente 0. Fine.

#### 6. Teorema 2.8.2 — Legge Forte di Borel (SLLN per v.a. limitate)
**Cosa significa:** Ancora più forte della Debole: la media campionaria va alla media vera *quasi certamente* (non "forse con molta probabilità", ma proprio al 100% delle volte in infinito).
**Dimostrazione snella:** Si dimostra con i momenti quarti (elevando alla quarta). Facendo $\mathbb{E}[S_n^4]$, si nota che cresce come $O(n^2)$. Dividendo per $n^4$, si ottiene $1/n^2$. Poiché la somma $\sum (1/n^2)$ è finita, usiamo il lemma di Borel-Cantelli per dire che gli errori grandi accadono solo un numero finito di volte (quasi mai all'infinito).

---

### Capitolo 5 - Passeggiate Aleatorie e Borel-Cantelli

#### 7. Teorema 5.1.2 — Legge 0-1 di Kolmogorov
**Cosa significa:** Gli "eventi coda" (eventi che dipendono dal lunghissimo periodo e non dai primi tentativi, es. "la moneta esce all'infinito") non conoscono vie di mezzo: o hanno probabilità 0 (impossibili) o probabilità 1 (certi).
**Dimostrazione snella:** Se un evento è nella coda $\mathcal{T}$, è indipendente da tutto ciò che è successo al tempo finito (le prime $n$ variabili). Ma alla fine, l'evento coda è misurabile da tutte le variabili, quindi deve essere indipendente *da se stesso*. Un evento indipendente da sé deve avere probabilità 0 o 1 (perché $P(A) = P(A \cap A) = P(A)P(A) \Rightarrow P(A)=P(A)^2$, da cui le uniche radici sono 0 o 1).

#### 8. Teorema 5.2.2 — Sup infinito per passeggiate di media 0
**Cosa significa:** Una passeggiata aleatoria (random walk) infinita senza "spinta" continuerà a oscillare all'infinito. Il massimo che raggiungerà è $+\infty$ e il minimo $-\infty$. Prima o poi visiterà tutti i possibili traguardi, non importa quanto lontani!
**Dimostrazione snella:** Se la passeggiata avesse un tetto massimo finito $M$, significherebbe che da un certo punto in poi va solo verso il basso. Ma siccome è simmetrica e i passi sono i.i.d., la legge 0-1 di Kolmogorov ci assicura che il limite superiore deve essere una costante (fissa) o infinita, e la simmetria costringe a scartare le costanti finite, lasciando solo $+\infty$.

---

### Capitolo 7 - Catene di Markov (Il Cuore dell'Esame)

#### 9. Teorema 7.3.1 — Esistenza e Unicità della legge (Catene di Markov)
**Cosa significa:** Se ti do un "punto di partenza" (distribuzione $\mu_0$) e una mappa di come ci si sposta (matrice di transizione $P$), posso costruire in modo unico le probabilità dell'intera storia futura del processo.
**Dimostrazione snella:** Segue dal teorema di Kolmogorov sulle distribuzioni finito-dimensionali. Moltiplicando la probabilità iniziale per le probabilità di transizione per ogni salto, definiamo coerentemente la probabilità su qualsiasi orizzonte finito.

#### 10. Teorema 7.4.1 — Catene di Markov da Equazioni alle Differenze Stocastiche
**Cosa significa:** Ogni Catena di Markov si può costruire "informaticamente" scrivendo $X_{n+1} = f(X_n, \xi_{n+1})$, dove $f$ è una funzione e $\xi$ è un rumore esterno i.i.d. (tipo lanciare un dado).
**Da dire al prof:** *"Questo è esattamente come si programma una simulazione Monte Carlo su Python: lo stato nuovo dipende da quello vecchio più un numero random indipendente."*
**Dimostrazione snella:** Si definisce una funzione $f$ cumulando le probabilità di transizione per scomparti. Se genero $U \sim Uniforme$, a seconda dello scaglione in cui cade $U$, assegno il nuovo stato. Essendo la $U$ indipendente dal passato, la proprietà di Markov è garantita.

#### 11. Teorema 7.6.3 — Proprietà Forte di Markov (Strong Markov Property)
**Cosa significa:** La perdita di memoria vale non solo a un tempo fisso ($n=5$), ma anche a "tempi casuali" o Tempi di Arresto (es. "il momento esatto in cui arrivi a 10 euro"). Da quel momento in poi, il futuro riparte da zero.
**Dimostrazione snella:** Si sfrutta l'identità $1_{\{\tau < \infty\}} = \sum_{k=0}^\infty 1_{\{\tau = k\}}$. Condizionando il futuro a un evento $A$, sommiamo su tutti i possibili istanti $k$ in cui il tempo di arresto $\tau$ è scattato. Ma siccome in ogni tempo $k$ (fisso) vale la Markov debole, la si estende per somma su tutti i tempi, ottenendo l'indipendenza dal passato (forte).

#### 12. Teorema 7.7.4 — Formula della probabilità dei ritorni infiniti
**Cosa significa:** Se la probabilità di ritornare a casa (partendo da casa) almeno una volta è $F$, allora la probabilità di ritornarci $k$ volte è esattamente $F^k$. (Se $F=1$, ci torni infinite volte. Se $F<1$, smetti di tornarci prima o poi).
**Dimostrazione snella:** Per la **Proprietà Forte di Markov**, il momento del primo ritorno a $x$ è un Tempo di Arresto. Nel momento in cui torni, il processo "riparte da zero" e dimentica il viaggio. Dunque la probabilità del secondo ritorno è identica a quella del primo (un'altra estrazione indipendente). Ecco spiegata l'elevazione a potenza: $F \times F \times \dots = F^k$.

#### 13. Teorema 7.7.10 — Solidarietà della Ricorrenza
**Cosa significa:** Se siamo in un sistema chiuso in cui ci si scambia passaggi (classe comunicante), tutti seguono lo stesso destino. Se uno stato è ricorrente, anche tutti gli stati con cui comunica lo sono (nessuno viene lasciato indietro).
**Dimostrazione snella:** Sia $x$ ricorrente e $x \leftrightarrow y$. Ci sono dei percorsi probabili per andare da $x$ a $y$ e da $y$ a $x$. Poiché a $x$ si torna infinite volte con probabilità 1, e in ogni ritorno c'è una certa probabilità fissa $>0$ di fare un giretto verso $y$, per il lemma di Borel-Cantelli è impossibile evitare di sbattere contro $y$ un numero infinito di volte. Dunque anche $y$ è ricorrente!

#### 14. Teorema 7.8.9 — Unicità della Misura Invariante (per stati ricorrenti)
**Cosa significa:** Se una catena è una "grande città irriducibile" in cui tutti ritornano ovunque (ricorrente), c'è **al massimo un solo** equilibrio finale perfetto. Non ci possono essere due distribuzioni stazionarie diverse.
**Dimostrazione snella:** L'esistenza è data dai tempi medi di ritorno a uno stato ancoraggio. L'unicità viene dal fatto che l'unica soluzione per l'equilibrio $\pi = \pi P$ per una classe ricorrente deve essere proporzionale al tempo medio trascorso in ogni stato tra le visite allo stato ancoraggio. Essendo proporzionale in modo unico, la misura è unica a meno di moltiplicazione scalare.

#### 15. Teorema 7.8.10 — Equivalenza "Positiva" (Il Grande Teorema d'Equilibrio)
**Cosa significa:** Se un solo stato è "Ricorrente Positivo" (cioè ci torni, e il tempo medio di attesa per tornarci è *finito*), allora miracolosamente tutta la catena irriducibile è formata da stati ricorrenti positivi, ed esiste sicuramente una distribuzione stazionaria $\pi$. Le due cose (ricorrenza positiva e stazionarietà) sono indissolubilmente collegate.
**Dimostrazione snella:** È un ciclo di implicazioni.
*   $(i) \Rightarrow (ii)$: Se c'è uno stato positivo, si costruisce la stazionaria contando le frazioni di tempo spese in giro prima di tornare a lui. Essendo il suo tempo medio finito, la probabilità non svanisce nel vuoto (la somma converge a 1).
*   $(ii) \Rightarrow (iii)$: Se c'è l'equilibrio, ogni probabilità stazionaria è l'inverso del tempo medio di ritorno: $\pi(x) = 1 / \mu_x$. Essendo $\pi(x)>0$, $\mu_x$ deve essere finito, quindi sono tutti positivi.

#### 16. Teorema 7.9.1 — Teorema Ergodico
**Cosa significa:** "La media temporale eguaglia la media spaziale". Se osservi il viaggio infinito della catena di Markov, la media dei valori raccolti lungo il viaggio (es. soldi spesi nel tempo) equivale alla media calcolata pesando i valori con le probabilità dell'equilibrio finale (stazionaria).
**Da dire al prof:** *"È la generalizzazione della Legge dei Grandi Numeri per eventi che non sono indipendenti (come la Catena di Markov), ma convergono a una stabilità stazionaria."*
**Dimostrazione snella:** Si divide la traiettoria immensa in piccoli "cicli di ritorno" (escursioni) a uno stato fisso di ancoraggio $x$. Per la Proprietà Forte di Markov, queste escursioni (viaggi tra un ritorno e l'altro ad $x$) sono i.i.d. (Indipendenti e Identicamente Distribuite). A questo punto, si applica la Legge Forte dei Grandi Numeri sui blocchi i.i.d., e si ottiene il risultato.

---

## 💡 Strategia da 30L all'orale
*   **Non fare elenchi a memoria**. Parti dicendo a parole semplici l'Intuizione, il "Cosa fa". Al prof piacciono gli studenti che "vedono" il concetto dietro la formula.
*   **Parole magiche:** "Sfruttiamo l'indipendenza", "Torre dei Valori Attesi", "Disintegriamo usando la partizione al primo passo", "Per la Proprietà Forte di Markov, da qui in poi il processo riparte da zero come se nulla fosse successo". Usale spesso.
*   Se ti dimentichi le $X$ e le $Y$, fai il disegno! (es. un pallino e le frecce per gli stati ricorrenti/comunicanti). La matematica serve solo a dimostrare che quel pallino e quelle frecce hanno un senso logico rigoroso.
