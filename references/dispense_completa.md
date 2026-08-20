# Discrete probability theory 

with selected topics of discrete time stochastic processes 

Salvatore Federico 

May 6, 2026 

2 

# **Contents** 

|**1**<br>**Pro**|**babilit**|**y theory in finite spaces**|**7**|
|---|---|---|---|
|1.1|Proba|bility spaces<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>7|
||1.1.1|Sample space . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>7|
||1.1.2|Space of events . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>8|
||1.1.3|Probability measure . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>10|
|1.2|Rand|om variables. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>13|
||1.2.1|Random variables<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>13|
||1.2.2|Measurability of a random variable . . . . . . . . . . . . . . .|. . . . . . . .<br>16|
||1.2.3|Law (or distribution) of random variables . . . . . . . . . . .|. . . . . . . .<br>21|
|1.3|Condi|tional probability<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>23|
|1.4|Indep|endence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>30|
||1.4.1|Independence of two random variables . . . . . . . . . . . . .|. . . . . . . .<br>30|
||1.4.2|Independent families . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>32|
|1.5|Three|important distributions (on finite sets) . . . . . . . . . . . . .|. . . . . . . .<br>34|
||1.5.1|Uniform Distribution . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>34|
||1.5.2|Bernoulli Distribution . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>35|
||1.5.3|Binomial Distribution . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>35|
|1.6|Expec|ted value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
|1.7|Condi|tional expected value<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>41|
|1.8|Select|ed exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>46|
|**2**<br>**The**|**discr**|**ete case: from finite to countable**|**49**|
|2.1|Gener|al probability spaces . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>50|
|2.2|Discre|te random variables . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>51|
||2.2.1|Poisson distribution<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>51|
|2.3|Condi|tional probability and independence . . . . . . . . . . . . . . .|. . . . . . . .<br>52|
|2.4|The B|ernoulli scheme<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>53|
||2.4.1|Geometric distribution . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>54|
|2.5|Expec|ted value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>55|
|2.6|Condi|tional expected value in the general discrete case . . . . . . . .|. . . . . . . .<br>59|
|2.7|Conve|rgences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>62|
||2.7.1|Three types of convergences for random variables . . . . . . .|. . . . . . . .<br>62|
||2.7.2|Mean convergence theorems . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>66|
|2.8|The l|aw of large numbers<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>70|
|2.9|Select|ed exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>72|
|**3**<br>**Sto**|**chastic**|**processes in discrete time**|**79**|
|3.1|Notio|n of stochastic process . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>79|
|3.2|Filtra|tion as information structure . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>79|
|3.3|Stopp|ing times and hitting times . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>80|
|3.4|Exerc|ises<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>81|



3 

_CONTENTS_ 

4 

|**4**<br>**Ma**|**rtingal**|**es**|**83**|
|---|---|---|---|
|4.1|Notio|n of martingale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>83|
|4.2|Some|useful results on martingales . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>85|
|**5**<br>**Ran**|**dom **|**walks**|**87**|
|5.1|Kolm|ogorov’s 0-1 law and Borel-Cantelli lemmas . . . . . . . . . . . . . .|. . . . .<br>87|
|5.2|Limit|behavior of symmetric random walks<br>. . . . . . . . . . . . . . . . .|. . . . .<br>90|
|5.3|An in|terlude: Gambler’s ruin in the fair case<br>. . . . . . . . . . . . . . . .|. . . . .<br>92|
|5.4|Still o|n the limit behavior of symmetric random walks . . . . . . . . . . .|. . . . .<br>93|
|**6**<br>**Fin**|**ancial **|**models in finite probability spaces**|**95**|
|6.1|One p|eriod models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>95|
||6.1.1|Market model: one single risky asset . . . . . . . . . . . . . . . . .|. . . . .<br>95|
||6.1.2|Portfolio, arbitrage, and martingale measures . . . . . . . . . . . .|. . . . .<br>96|
||6.1.3|Contingent claims: pricing, hedging, and completeness . . . . . . .|. . . . . 100|
||6.1.4|Completeness of the market . . . . . . . . . . . . . . . . . . . . . .|. . . . . 105|
|6.2|Multi|-period financial models . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 106|
||6.2.1|The market model . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 106|
||6.2.2|Self-financed portfolios, arbitrage, and martingale measures . . . .|. . . . . 106|
||6.2.3|Contingent claims: pricing, hedging, and completeness . . . . . . .|. . . . . 109|
||6.2.4|Completeness of the market . . . . . . . . . . . . . . . . . . . . . .|. . . . . 112|
||6.2.5|The binomial model . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 113|
|**7**<br>**An **|**introd**|**uction to Markov chains**|**119**|
|7.1|A heu|ristic introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 119|
|7.2|The c|oncept of Markov chain . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 120|
|7.3|Quest|ions of existence: construction of Markov chains<br>. . . . . . . . . . .|. . . . . 121|
|7.4|Mark|ov chains and stochastic difference equations. . . . . . . . . . . . . .|. . . . . 123|
|7.5|Trans|ition of Markov chains: three points of view . . . . . . . . . . . . . .|. . . . . 125|
|7.6|The s|trong Markov property. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 127|
|7.7|Visits|and state classification<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 130|
|7.8|Invari|i<br>ant measures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 135|
||7.8.1|Existence and uniqueness . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 137|
|7.9|The E|rgodic Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 139|
||7.9.1|The ergodic theorem and the law of large numbers . . . . . . . . .|. . . . . 140|
|7.10|Select|ed exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 140|
|**8**<br>**Dis**|**crete t**|**ime stochastic optimal control**|**143**|
|8.1|A clas|s of stochastic control problems in discrete time<br>. . . . . . . . . . .|. . . . . 143|
|8.2|Exam|ples of stochastic optimal control problems<br>. . . . . . . . . . . . . .|. . . . . 145|
||8.2.1|Optimal stochastic growth . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 145|
||8.2.2|Optimal portfolio allocation over finite horizon . . . . . . . . . . .|. . . . . 147|
||8.2.3|i<br>Optimal inventory . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 149|
|8.3|Dyna|mic Programming<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 150|
||8.3.1|Value function<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 150|
||8.3.2|Bellman’s equation . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 152|
||8.3.3|The DP algorithm in the finite horizon case . . . . . . . . . . . . .|. . . . . 153|
||8.3.4|The DP algorithm in the infinite horizon stationary case . . . . . .|. . . . . 154|
|8.4|Soluti|on of selected problems . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 156|
||8.4.1|Optimal stochastic growth . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 156|
||8.4.2|Optimal portfolio . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 157|
||8.4.3|Optimal inventory . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 159|



_CONTENTS_ 5 

|**A Liminf and limsup of real sequences**|**163**|
|---|---|
|**B Series**|**165**|
|B.1<br>Series with nonnegative terms . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . 165|
|B.2<br>Absolutely convergent series . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . 166|



_CONTENTS_ 

6 

### **General notations** 

We set here the general notations that will be used throughout these notes. 

- (N1) N denotes the set of natural numbers including 0, i.e. N := _{_ 0 _,_ 1 _,_ 2 _, ...}_ . 

- (N2) N0 := N _\ {_ 0 _}_ . 

- (N3) The symbol _∃_ means “there exists”. 

- (N4) The symbol _∀_ means “for all”. 

- (N5) Given a finite set _S_ , by _|S|_ we denote the cardinality of _S_ , i.e. the number of its elements. 

- (N6) Unless differently specified, the symbols _n, m, i, j, k, N, M_ denote positive natural numbers, i.e. elements of N0. 

- (N7) _⊆_ denotes the (large) containment. 

- (N8) _A_ 1 _× ... × An_ denotes the Cartesian product of a finite number of sets _A_ 1 _, ..., An_ ; and, given a stream _a_ 1 _∈ A_ 1 _, ..., an ∈ An_ , the symbol ( _a_ 1 _, ..., an_ ) denotes the (ordered) _n_ -ple belonging to _A_ 1 _× ... × An_ . _A_<sup>_n_</sup> denotes the Cartesian product _A × ... × A_ ( _n_ times). 

- (N9) _∅_ denotes the empty set. 

- (N10) The symbol _A_<sup>_c_</sup> denotes the complement of the set _A_ (with respect to a larger set which is usually implicitly intended). 

- (N11) _A ∪ B_ and _A ∩ B_ denote, respectively, the union and the intersection of two sets _A, B_ . 

- (N12) The symbols _s.t._ or : mean “such that” – apart from its use in (N13) and (N15) below. 

- (N13) The symbol := means “equal by definition”. 

- (N14) The symbol _≡_ means “identically equal”. 

- (N15) The symbol _f_ : _A → B_ means “ _f_ is a function from _A_ to _B_ ”. 

- (N16) Given a set _S_ , the symbol 2<sup>_S_</sup> denotes the _set of all subsets of S_ . 

- (N17) Given _a, b ∈_ R, the symbols _a ∨ b_ and _a ∧ b_ denote, respectively, the maximum and the minimum between _a_ and _b_ , i.e. 

   - _a ∨ b_ := max _{a, b}, a ∧ b_ := min _{a, b}._ 

- (N18) Given _a ∈_ R, the symbols _a_<sup>+</sup> denotes the positive part of _a_ , i.e. 

_a_<sup>+</sup> := max _{a,_ 0 _}._ 

- (N19) Given two functions _f_ : _A → B_ and _g_ : _B → C_ , we denote by _g ◦ f_ the composition of _f_ and _g_ , i.e. _g ◦ f_ : _A → C, a �→_ ( _g ◦ f_ )( _a_ ) := _g_ ( _f_ ( _a_ )) _._ 

## **Chapter 1** 

# **Probability theory in finite spaces** 

The mathematical theory of probability aims at building a theoretical formalism to describe _random phenomena_ . It relies on the concept of _random experiment_ , which can roughly be defined as “an experiment whose outcome cannot be predicted in advance”. An agent may be naturally led to associate a _degree of confidence_ about the different possible outcomes of this experiment. Let us see how to model this idea, always keeping in mind that there are three different stages in each good theory: 

- (i) Choice of the mathematical model; 

- (ii) Mathematical elaboration within the chosen model; 

- (iii) Interpretation of the obtained results. 

### **1.1 Probability spaces** 

The structure of probability spaces consists of three ingredients: 

1. The sample (or state) space Ω; 

2. The set of events _F_ ; 

3. The probability measure P. 

Hence, a probability space is a triple: (Ω _, F,_ P). Let us describe the objects of this triple in detail. 

#### **1.1.1 Sample space** 

The _sample space_ is the set whose elements represent all possible _mutually exclusive_ “future/unknown outcomes of the world”.<sup>1</sup> It is traditionally denoted by Ωand the generic element of Ω is denoted by _ω_ . In this chapter, we assume that the sample space Ωis finite, i.e., _|_ Ω _| < ∞_ . Of course, this is a restrictive assumption, as it does not allow us to deal with many real phenomena whose possible outcomes are not finite. However, it still allows us to model many other phenomena. 

> 1The elements of Ωare mathematical labels for these potential world states. They need not be the actual physical results themselves, as shown in Example 1.1.1(ii) and (iv) where different mathematical representations model the same physical experiment. Moreover, Ωmay contain many elements that are irrelevant to the specific random experiment we are studying - we only require that it encompasses all outcomes we wish to consider. In general, the choice of an appropriate sample space is crucial in probability theory because it determines how we model the random phenomenon. 

7 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

8 

Coins and Dice 

**Example 1.1.1.** _Let us consider some examples._ 

- _(i)_ **_Coin toss._** _A reasonable choice for the sample space of this experiment is_ Ω= _{H, T } or also_ Ω= _{_ 0 _,_ 1 _}. Notice that the label/name that we associate to the outcome is not important._ 

- _(ii)_ **_Two tosses of a coin (or a toss of two coins)._** _A reasonable choice for the sample space of these experiments is a space listing all the pairs of possible outcomes of the two tosses, i.e._ 

Ω:= �( _H, H_ ) _,_ ( _H, T_ ) _,_ ( _T, H_ ) _,_ ( _T, T_ )� _or_ Ω:= �(0 _,_ 0) _,_ (1 _,_ 0) _,_ (0 _,_ 1) _,_ (1 _,_ 1)� _. course, one can also choose_ Ω:= _{_ 1 _,_ 2 _,_ 3 _,_ 4 _} using the one-to-one correspondence_ 1 _↔_ (0 _,_ 0) _,_ 2 _↔_ (1 _,_ 0) _,_ 3 _↔_ (0 _,_ 1) _,_ 4 _↔_ (1 _,_ 1) _,_ 

_Of course, one can also choose_ Ω:= _{_ 1 _,_ 2 _,_ 3 _,_ 4 _} using the one-to-one correspondence_ 

_but clearly this is not an ideal choice, as it requires establishing a one-to-one correspondence to “read” the result of the experiment._ 

- _(iii)_ **_Rolling of a die with six sides._** _A reasonable choice for the sample space of this experiment is_ 



_(iv)_ **_Rolling of two dice with six sides._** _A reasonable choice for the sample space of this experiment is_ Ω:= �( _i, j_ ) : _i, j ∈{_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _}_ � _._ 

_Notice that |_ Ω _|_ = 36 _. Clearly one could also choose_ 



_again this would not be an ideal choice — though not incorrect — choice to represent the experiment._ 

#### **1.1.2 Space of events** 

Mathematically, an _event_ is a subset _A ⊆_ Ωof outcomes _ω_ . We interpret _A_ as an event which _occurred_ if _ω ∈ A_ , and which _did not occur_ if _ω ∈/ A_ . This mathematical representation allows us to translate intuitive questions about experimental results into precise set-theoretic terms. Let us see how to read some sets and some logical operations with sets in this framework. 

- (i) The event Ωis the _sure_ event. 

- (ii) The event _∅_ is the _impossible_ event. 

- (iii) The singleton _{ω}_ , where _ω ∈_ Ω, is an _elementary_ event. 

- (iv) Given the event _A ⊆_ Ω, the event _A_<sup>_c_</sup> is the “contrary event of _A_ ”. 

- (v) Given the events _A, B ⊆_ Ω, the event _A ∪ B_ is the event “ _A_ and/or _B_ occurs”. 

- (vi) Given the events _A, B ⊆_ Ω, the event _A ∩ B_ is the event “both the event _A_ and the event _B_ occur”. 

_1.1. PROBABILITY SPACES_ 

9 

Coins and Dice 

**Example 1.1.2.** _Let us consider some examples of events related to Example 1.1.1. (i) The subset A_ := �( _H, H_ ) _,_ ( _T, T_ )� _in Example 1.1.1(ii) represents the event “same result in the two tosses”. (ii) The subset A_ := _{_ 2 _,_ 4 _,_ 6 _} in Example 1.1.1(iii) represents the event “even result in the toss”. (iii) The subset A_ := �(1 _,_ 1) _,_ (2 _,_ 2) _,_ (3 _,_ 3) _,_ (4 _,_ 4) _,_ (5 _,_ 5) _,_ (6 _,_ 6)� _in Example 1.1.1(iv) represents the event “same result in the rolling of the two dice”._ 

The set of all the events in which one is interested is usually denoted by _F_ . Notice that this is a set of subsets of Ω. In order to build a consistent theory, one needs to require some “stability properties” for _F_ , precisely that it is an _algebra_ , according to the following definition. 

Algebra of sets and atoms 

**Definition 1.1.3.** _A set of subsets F ⊆_ 2<sup>Ω</sup> _is called an_ algebra _(of sets) if the following properties hold:_ (F1) Ω _∈F;_ (F1) _A ∈F ⇒ A_<sup>_c_</sup> _∈F;_ (F1) _A, B ∈F ⇒ A ∪ B ∈F. If F is an algebra, a set A ∈F is called an_ atom of _F if it cannot be decomposed as the union of two disjoint nonempty sets of F; that is if_ 

_A_ = _A_ 1 _∪◦ A_ 2 _, A_ 1 _, A_ 2 _∈F ⇒ either A_ 1 = _∅ or A_ 2 = _∅._ 

As one can see, the concept of algebra ensures that the space of events space is “closed” under the natural operations we want to perform. If we know that certain events can occur, we automatically know that their complements, unions, and intersections can also be discussed meaningfully. This closure property is essential for building a consistent probability theory where we can combine events in natural ways. A natural question should arise at this point: Why not consider all the possible subsets of Ωas events, taking _F_ = 2<sup>Ω</sup> , which is clearly an algebra? The reason for that cannot be appreciated in the context of finite (or even countable) sample spaces; hence, actually there is no problem in this chapter. Nonetheless, it becomes a technical issue when one wants to consider uncountable sample spaces; in this case, unfortunately, it is not always possible to deal with _F_ = 2<sup>Ω</sup> . In order to prepare to this case, we start already here to propose the issue and to introduce the formalism. Note that, if _F_ = 2<sup>Ω</sup> , the atoms of _F_ are the singletons _{ω}_ , with _ω ∈_ Ω. 

**Exercise 1.1.4.** _If F is an algebra, a certain number of consequences follow from the three properties required by the definition. Verify the following ones._ 

_(a) ∅∈F;_ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

10 

_(b) A, B ∈F ⇒ A ∩ B ∈F (hint: use the De Morgan laws); (c) A_ 1 _, . . . , An ∈F ⇒_ � _n Ak ∈F; k_ =1 _(d) A_ 1 _, . . . , An ∈F ⇒_ � _n Ak ∈F. k_ =1 **Solution:** 

- (a) Since Ω _∈F_ by (F1) and Ω<sup>_c_</sup> = _∅∈F_ by (F2), we have _∅∈F_ . 

- (b) Using De Morgan’s law: _A ∩ B_ = ( _A_<sup>_c_</sup> _∪ B_<sup>_c_</sup> )<sup>_c_</sup> . Since _A, B ∈F_ , we have _A_<sup>_c_</sup> _, B_<sup>_c_</sup> _∈F_ by (F2). Then _A_<sup>_c_</sup> _∪ B_<sup>_c_</sup> _∈F_ by (F3), and finally ( _A_<sup>_c_</sup> _∪ B_<sup>_c_</sup> )<sup>_c_</sup> _∈F_ by (F2). 

- (c) We proceed by induction. For _n_ = 2, this is exactly (F3). Assume true for _n −_ 1, then � _nk_ =1<sup>_Ak_= (�</sup> _k_<sup>_n_</sup> =1<sup>_−_1</sup><sup>_Ak_)</sup><sup>_∪An∈F_bytheinductionhypothesisand(F3).</sup> 

- (d) Similarly, by induction and using the identity<sup>�</sup><sup>_n_</sup> _k_ =1<sup>_Ak_= (�</sup><sup>_n_</sup> _k_ =1<sup>_Ac_</sup> _k_<sup>)</sup><sup>_c_.</sup> 

**Exercise 1.1.5.** _Let_ Ω= _{_ 1 _,_ 2 _,_ 3 _,_ 4 _} and consider the collection of subsets: F_ = _{∅, {_ 1 _,_ 2 _}, {_ 3 _,_ 4 _},_ Ω _}._ 

_(a) Verify that F is an algebra of sets._ 

_(b) Is F closed under arbitrary intersections? Justify your answer._ 

**Solution:** 

(a) _F_ is an algebra because: • Ω _∈F_ • Closed under complements: **–** _∅_<sup>_c_</sup> = Ω _∈F_ **–** _{_ 1 _,_ 2 _}_<sup>_c_</sup> = _{_ 3 _,_ 4 _} ∈F_ **–** _{_ 3 _,_ 4 _}_<sup>_c_</sup> = _{_ 1 _,_ 2 _} ∈F_ **–** Ω<sup>_c_</sup> = _∅∈F_ • Closed under unions: **–** _∅∪ A_ = _A ∈F_ **–** _{_ 1 _,_ 2 _} ∪{_ 3 _,_ 4 _}_ = Ω _∈F_ **–** All other unions are trivial 

(b) Yes, _F_ is closed under intersections: • _{_ 1 _,_ 2 _} ∩{_ 3 _,_ 4 _}_ = _∅∈F_ • All other intersections are trivial. 

#### **1.1.3 Probability measure** 

Once the space of events _F_ is fixed, given an event _A ∈F_ , one can associate to it a “degree of confidence” called _probability of the event A_ . From the mathematical point of view, this idea is 

_1.1. PROBABILITY SPACES_ 

11 

formalized by a function, called _probability measure_ : 



Hence, the “degree of confidence” on an event _A ∈F_ is just a real number, belonging to the interval [0 _,_ 1], measuring the confidence that the outcome _ω_ of the random experiment will lie in _A_ : the higher P( _A_ ) is, the more confidence the individual has that the result of the random experiment will lie in _A_ . 

The **choice of the probability measure is a subjective operation** , depending on the individual who operates this choice. Indeed, as for the choice of the set of events _F_ , one has a degree of freedom in choosing the probability measure. For instance, in the case of the toss of a coin, it would be natural to choose P( _{H}_ ) = P( _{T }_ ) = 1 _/_ 2, if one thinks that the coin is “fair” or “well-balanced”. On the other hand, if one thinks that the coin is “unfair” or “not well balanced”, other choices might turn out to be reasonable, for instance P( _{H}_ ) = 1 _/_ 4 and P( _{T }_ ) = 3 _/_ 4. However, there are some natural _consistency requirements_ to exclude “illogical” choices, such as the choice P( _{H}_ ) = 1 _/_ 4, P( _{T }_ ) = 1 _/_ 2 in the previous experiment. These are the “three axioms of probability”. 

Probability Measure 

**Definition 1.1.6** (Probability measure) **.** _Let_ Ω _be a finite set and let F ⊆_ 2<sup>Ω</sup> _be an algebra. A_ probability measure _on F is a map_ P : _F →_ R _such that_ (A1) 0 _≤_ P( _A_ ) _≤_ 1 _for all A ∈F;_<sup>_a_</sup> (A2) P(Ω) = 1 _;_ (A3) _A, B ∈F and A ∩ B_ = _∅⇒_ P( _A ∪ B_ ) = P( _A_ ) + P( _B_ ) _. a_ Notice that this requirement is already contained in (1.1.1). 

The three probability axioms (A1)–(A3) above have natural interpretations: 

**Axiom (A1)** : Probabilities are numbers between 0 and 1, representing degrees of belief. 

**Axiom (A2)** : The probability that sure event Ωhappens is 1. 

**Axiom (A3)** : For mutually exclusive events, the probability that at least one occurs is the sum of their individual probabilities. 

These axioms, while simple, form the foundation upon which all of modern probability theory is built. Kolmogorov’s 1933 formulation using these axioms unified previous approaches to probability. 

**Notation.** For notational convenience, often we will write 

P _{ω}_ for P( _{ω}_ ) _,_ P _{ω_ 1 _, ω_ 2 _}_ for P( _{ω_ 1 _, ω_ 2 _}_ ) _,_ etc. 

**Remark 1.1.7.** _It is clear that, in the example of a coin toss, the choice_ P _{H}_ = 1 _/_ 4 _,_ P _{T }_ = 1 _/_ 2 _is ruled out by_ (A2)-(A3) _._ 

**Exercise 1.1.8.** _Many consequences may be derived from the three axioms above. Prove the following._ 

_(a) For every A ∈F, one has_ P( _A_<sup>_c_</sup> ) = 1 _−_ P( _A_ ) _._ 

_(b) If A, B ∈F and A ⊆ B, then_ P( _B\A_ ) = P( _B_ ) _−_ P( _A_ ) _; in particular_ P( _A_ ) _≤_ P( _B_ ) _._ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

12 

- _(c) If A_ 1 _, . . . , An ∈F are mutually disjoint sets_<sup>_a_</sup> _, then_ P (<sup>�</sup><sup>_n_</sup> _k_ =1<sup>_Ak_)=�</sup><sup>_n_</sup> _k_ =1<sup>P(</sup><sup>_Ak_)</sup><sup>_;this_</sup> _property is called_ finite additivity _(of the probability measure)._ 

- _(d) If A, B ∈F, then_ 



_in particular,_ 



##### **Solution:** 

(a) Since _A ∪ A_<sup>_c_</sup> = Ωand _A ∩ A_<sup>_c_</sup> = _∅_ , by (A2) and (A3) we have: 



Thus P( _A_<sup>_c_</sup> ) = 1 _−_ P( _A_ ). 

(b) Since _B_ = _A ∪_ ( _B \ A_ ) and _A ∩_ ( _B \ A_ ) = _∅_ , by (A3): 



So P( _B \ A_ ) = P( _B_ ) _−_ P( _A_ ). Since P( _B \ A_ ) _≥_ 0, we have P( _A_ ) _≤_ P( _B_ ). 

(c) We proceed by induction. For _n_ = 2, this is (A3). Assume true for _n −_ 1, then: 



- (d) Note that _A ∪ B_ = _A ∪_ ( _B \ A_ ) and this union is disjoint. Also _B_ = ( _A ∩ B_ ) _∪_ ( _B \ A_ ) is a disjoint union. Therefore: 



Rearranging gives the desired equality. The inequality follows since P( _A ∩ B_ ) _≥_ 0. 

> _a_ That is, _Ai ∩ Aj_ = _∅_ as soon as _i̸_ = _j_ . 

Typically, in general probability theory, one needs to deal with the notion of _negligible event_ . A negligible event _A ∈F_ is an event such that P( _A_ ) = 0 and if a property holds outside of a negligible event, one says that it holds _almost surely_ (a.s.) or, stressing the probability P, that it holds P- _almost surely_ (P-a.s.). Considering finite sample spaces Ω, typically one can assume, without loss of generality, that 



Indeed, if P( _A_ ) = 0 for some _A ∈F_ such that _A̸_ = _∅_ , we can remove the set _A_ from the sample space Ωand deal with the new sample space Ω<sup>_′_</sup> := Ω _\ A_ . 

As long as we deal with finite sample spaces Ωthe probability measure is determined by additivity on the whole set _F_ once it is assigned on the atoms of _F_ . If _F_ = 2<sup>Ω</sup> , this amounts to assign the probability to singletons _{ω}_ . Then, by the additivity property, one has 



_1.2. RANDOM VARIABLES_ 

13 

### **1.2 Random variables** 

In probability theory, the concept of _random variables_ plays a fundamental role. We begin by considering a _random map_ , i.e., just a function 



where _E_ is another set, typically _E ⊆_ R. Since in this chapter we are currently considering finite sample spaces, we assume without loss of generality (by restricting the codomain if necessary) that _E_ is also finite. 

#### **1.2.1 Random variables** 

Throughout this subsection, the couple (Ω _, F_ ) is given. Note that the probability measure P does not affect the concept of measurability we are going to discuss here. To simplify exposition, we assume throughout the chapter the following. 

**Assumption 1.2.1.** _The arrival (finite) sets of the random maps, denoted by E, E_<sup>_′_</sup> _, S, S_<sup>_′_</sup> _. . . , are endowed with their power set algebras E_ = 2<sup>_E_</sup> _, E_<sup>_′_</sup> = 2<sup>_E′_</sup> _, S_ = 2<sup>_S_</sup> _, S_<sup>_′_</sup> = 2<sup>_S′_</sup> _, etc._ 

Random Variable **Definition 1.2.2.** _A random map X_ : Ω _→ E is a_ random variable _if it is F-measurable, i.e., if X_<sup>_−_1</sup> ( _B_ ) _∈F ∀B ∈E._ 

Since _F_ is the reference algebra, the random maps that one can manage from the point of view of the probability are the random variables, as they are the ones whose preimages are events. So, from now on, we will deal only with random variables. Note that: 

- (i) When _F_ = 2<sup>Ω</sup> (typical in finite probability spaces), all maps _X_ : Ω _→ E_ are random variables. 

- (ii) Under Assumption 1.2.1 If _X_ is a random variable and _f_ : _E → E_<sup>_′_</sup> , then _f ◦ X_ is also a random variable. 

For a random variable _X_ : Ω _→ E_ and any subset _B ⊆ E_ , we use the shorthand: 

_{X ∈ B}_ for _{ω ∈_ Ω: _X_ ( _ω_ ) _∈ B}_ (read as “the event that _X_ falls in _B_ ”) 

and, accordingly, 

P _{X ∈ B}_ for P( _{ω ∈_ Ω: _X_ ( _ω_ ) _∈ B}_ ) (read as “the probability that _X_ falls in _B_ ”). We will adopt this notation and terminology throughout. 

##### Two coin tosses 

**Example 1.2.3.** _Consider tossing two coins. We model it in the sample space:_ 



_On this sample space, we may describe several events through the use of random maps describing the outcomes of the first and of the second toss. Define the random variables: (a)_ Outcome of first toss: 

_X_ : Ω _→ E_ := _{H, T }, X_ ( _ω_ ) = _result of the first toss,_ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

14 

_explicitly given by_ 



_(b)_ Outcome of second toss: 



_Some interesting events can be described using X and Y :_ 









_(iii)_ Both tosses show the same result: 



_(iv)_ At least one Head in the two tosses: 



_(v)_ Exactly one Head in the two tosses: 



_(vi)_ First toss is Head and second is Tail: 



_(vii)_ First toss is different from second toss: 



_These examples show how random variables allow us to describe complex events in a compact and intuitive mathematical language._ 

##### Two dice roll 

**Example 1.2.4.** _Consider rolling two six-sided dice. We model it in the sample space:_ 



_On this sample space, we may describe several events through the use of random maps describing the outcomes of the first and of the second die. Define the random variables:_ 

_1.2. RANDOM VARIABLES_ 

15 

_(a)_ Outcome of first die: 



_which gives the result shown on the first die._ 

_(b)_ Outcome of second die: 



_which gives the result shown on the second die._ 

_(c)_ The sum of the two dice is described by: 



_which gives the total of both dice._ 

_Some interesting events can be described using X, Y , and S:_ 

_(i)_ First die shows an even number: 



_(ii)_ Second die shows a prime number: 



_(iii)_ Both dice show the same result: 



_(iv)_ The sum of the two tosses yields 7: 



_(v)_ The sum of the two tosses yield an even number: 



_(vi)_ First die shows more than the second die: 





_(viii)_ First die is 1 and sum is odd: 



_These examples demonstrate how random variables provide a powerful framework for describing complex probabilistic events in a structured mathematical way, making it easier to compute probabilities and analyze relationships between different outcomes._ 

**_Exercise:_** _Write explicitly the events described before as subsets of_ Ω _._ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

16 

In the previous two examples there was no probability given: we just described some random experiments and some events related to them through a suitable sample space and suitable random variables. In the next example we let the notion of probability enter in the game to quantify the degree of confidence of an event. 

##### Birthday problem 

**Example 1.2.5.** _Consider a group of n ≤_ 365 _individuals. We want to model the event “at least two individuals share a birthday” in a suitable probability space, and compute its probability—assuming that the probability of being born on any given day is_ 1 _/_ 365 _._ 

_1. Consider the sample space:_ 



_with F_ = 2<sup>Ω</sup> _. The n-tuple ω ∈_ Ω _represents the birthday dates of the n individuals. Due to the symmetric structure of the problem, we take_ P _to be the uniform distribution:_ 



_2. Define the random maps:_ 



_3. It is easier to start by computing the probability of the complement:_ 







_Thus,_ 



**_Remark._** _For n_ = 23 _,_ P( _A_ ) _>_ 1 _/_ 2 _; for n_ = 50 _,_ P( _A_ ) _≈_ 0 _._ 974 _. With just 50 people, the probability of at least two sharing a birthday is very high._ 

#### **1.2.2 Measurability of a random variable** 

In order to describe and measure the information brought by a random variable, we need to introduce the concept of measurability and of generated algebra. 

_1.2. RANDOM VARIABLES_ 

17 

##### Measurability of a map and generated algebra 

**Definition 1.2.6.** 

- _(i) Let G ⊆F be an algebra (not necessarily G_ = _F). A random variable X_ : Ω _→ E is G-measurable if: X_<sup>_−_1</sup> ( _B_ ) := _{X ∈ B} ∈G ∀B ∈E._ 

- _(ii) Let X_ : Ω _→ E be a random variable. The_ algebra generated by _X, denoted σ_ ( _X_ ) _, is the smallest algebra on_ Ω _making X measurable:_ 



Note that: 

- (i) By construction any random variable _X_ is _σ_ ( _X_ )-measurable; 

- (ii) By Assumption 1.2.1, the atoms of _σ_ ( _X_ ) are the sets _{X_ = _x}_ with _x ∈ E_ . 

- (iii) By Assumption 1.2.1, the requirement in Definition 1.2.6 is equivalent to: 



(iv) By Assumption 1.2.1, 



- (v) For a constant (trivial) random variable _X ≡ c_ , it is _σ_ ( _X_ ) = _{∅,_ Ω _}_ . The atoms of _σ_ ( _X_ ) are the trivial ones: _∅,_ Ω. 

The fundamental result in this context is represented by the following theorem, which will have numerous consequences for interpreting the information brought by the knowledge of random variables. 

Doob’s measurability criterion 

**Proposition 1.2.7.** _Let X_ : Ω _→ E and Y_ : Ω _→ E_<sup>_′_</sup> _be random variables. X is σ_ ( _Y_ ) _- measurable if and only if there exists f_ : _E_<sup>_′_</sup> _→ E such that X_ = _f ◦ Y ._ 



<!-- Start of picture text -->
Y<br>Ω E ′<br>X<br>∃f s.t. X =  f ( Y  )<br>E<br><!-- End of picture text -->

Figure 1.1: Commutative diagram for the Doob criterion. 

_Proof._ ( _⇒_ ) Assume _X_ is _σ_ ( _Y_ )-measurable, where _Y_ : Ω _→ E_<sup>_′_</sup> . Since Ωis finite, _Y_ takes only finitely many values, say _y_ 1 _, . . . , yn ∈ E_<sup>_′_</sup> . For each _yi_ , the set _Ai_ = _Y_<sup>_−_1</sup> _{yi}_ is an atom of _σ_ ( _Y_ ). 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

18 

##### **POSSIBLE** 



<!-- Start of picture text -->
B 3<br>B 4<br>B 1<br>B 2<br><!-- End of picture text -->

_σ_ ( _X_ ) _⊆ σ_ ( _Y_ ) 

##### **IMPOSSIBLE** 



Illegal: _X_ cuts _Y_ -atoms 

Figure 1.2: Comparison of measurability: Left side shows a valid sub-partition; Right side shows an invalid partition that creates information not present in _Y_ . 

##### **Why the second case is impossible** 

In the second figure, the dashed red lines split the _Y_ -atoms. This means _X_ takes different values (on either side of the red line) while _Y_ remains the same. If you know _Y_ (which square you are in), you **still don’t know** _X_ because _Y_ doesn’t tell you which side of the red line you are on. Therefore, _X_ cannot be a function of _Y_ ( _X̸_ = _f_ ( _Y_ )). 

Since _X_ is _σ_ ( _Y_ )-measurable, it must be constant on each atom _Ai_ of _σ_ ( _Y_ ). Given _yi ∈ E_<sup>_′_</sup> , picking an arbitrary _ωi ∈ Y_<sup>_−_1</sup> _{yi}_ , define 



This definition is well posed, as it does not depend on the choice of _ωi ∈ Y_<sup>_−_1</sup> _{yi}_ , since _X_ is constant on the preimage _Y_<sup>_−_1</sup> _{yi}_ . Doing that for each _i_ = 1 _, ..., n_ , we have defined a map _f_ : _E_<sup>_′_</sup> _→ E_ . 

Then, for each given and fixed _ω ∈_ Ω, setting let _y_ := _Y_ ( _ω_ ) we have: 



Thus, by arbitrariness of _ω ∈_ Ωwe obtain _X_ = _f ◦ Y_ . 

( _⇐_ ) Let _f_ : _E_<sup>_′_</sup> _→ E_ and let _X_ = _f ◦ Y_ . We want to show _X_ is _σ_ ( _Y_ )-measurable; this means that, for every _B ∈E_ , one has _X_<sup>_−_1</sup> ( _B_ ) _∈ σ_ ( _Y_ ). Let _B ∈E_ ; we have 



Let _A_ = _{y ∈ E_<sup>_′_</sup> : _f_ ( _y_ ) _∈ B} ∈E_<sup>_′_</sup> . Then: 



Since _A ∈E_<sup>_′_</sup> , we have _Y_<sup>_−_1</sup> ( _A_ ) _∈ σ_ ( _Y_ ) by definition of _σ_ ( _Y_ ). We conclude _X_<sup>_−_1</sup> ( _B_ ) _∈ σ_ ( _Y_ ). 

We stress again the importance of the result above and its meaning: it says that, if (and only if) _X_ is _σ_ ( _Y_ )-measurable, then _X_ is “determined” by _Y_ . Indeed, in this case, _X_ is constant on each event of the form _{Y_ = _y}_ , as it can be expressed as a deterministic transformation of _Y_ ; hence, once the value of _Y_ (the realization _Y_ ( _ω_ )) is known/observed, then also the value of _X_ (the realization _X_ ( _ω_ )) is known: indeed, 



This fact will play a crucial role when introducing information structures (filtrations). 

_1.2. RANDOM VARIABLES_ 

19 

Information brought by random variables 

The fact that _X_ is _σ_ ( _Y_ )-measurable can be expressed by the inclusion 



By interpreting generated algebras as information brought by random variables, the above inclusion can be viewed as representing the fact that the information brought by _X_ is smaller than the one brought by _Y_ . 



_(i) Show that X is σ_ ( _Y_ ) _-measurable._ 

_(ii) Find g_ : _{_ 0 _,_ 1 _,_ 4 _,_ 9 _} →{−_ 1 _,_ 1 _} such that X_ = _g ◦ Y ._ 

**Solution:** 

(i) We compute the preimages: 



On each of these sets, _X_ is constant: _X_ = 1 on _{_ 0 _}_ , _X_ = _−_ 1 on _{−_ 1 _,_ 1 _}_ , _X_ = 1 on _{−_ 2 _,_ 2 _}_ , _X_ = _−_ 1 on _{−_ 3 _,_ 3 _}_ . (ii) Define _g_ : _{_ 0 _,_ 1 _,_ 4 _,_ 9 _} →{−_ 1 _,_ 1 _}_ by: _g_ (0) = 1 _, g_ (1) = _−_ 1 _, g_ (4) = 1 _, g_ (9) = _−_ 1 _._ Then _X_ = _g ◦ Y_ . 

Measurability and information 

**Exercise 1.2.9.** _Consider an experiment consisting of rolling two fair dice (one red die and one blue die). Let:_ 

Ω= ( _i, j_ ) : _i, j ∈{_ 1 _, . . . ,_ 6 _} , F_ = 2<sup>Ω</sup> _._ � � _Define the random variables: R_ ( _ω_ ) := _i (outcome of red die) B_ ( _ω_ ) := _j (outcome of blue die) S_ ( _ω_ ) := _i_ + _j (sum of the two dice) E_ ( _ω_ ) := **1** _{even}_ ( _i_ + _j_ ) _(indicator that sum is even) (i) Show that E is σ_ ( _S_ ) _-measurable. Explain what this means in terms of information. (ii) Find h_ : _{_ 2 _,_ 3 _, . . . ,_ 12 _} →{_ 0 _,_ 1 _} such that E_ = _h ◦ S._ 

_Define the random variables:_ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

20 

_(iii) Is R σ_ ( _S_ ) _-measurable? Explain intuitively._ 

##### **Solution:** 

(i) The preimages of _S_ are: 



On each set, _E_ is constant: _E_ = 1 for sums 2 _,_ 4 _,_ 6 _,_ 8 _,_ 10 _,_ 12 and _E_ = 0 for sums 3 _,_ 5 _,_ 7 _,_ 9 _,_ 11. So knowing _S_ determines _E_ . 

(ii) Define: 



Then _E_ = _h ◦ S_ . 

(iii) No. For example, consider _S_<sup>_−_1</sup> _{_ 5 _}_ = _{_ (1 _,_ 4) _,_ (2 _,_ 3) _,_ (3 _,_ 2) _,_ (4 _,_ 1) _}_ . This event contains _ω_ ’s corresponding to different values of the possible outcomes of _R_ (precisely, 1 _,_ 2 _,_ 3 _,_ 4); in other terms, _R_ is not constant on the _σ_ ( _S_ )-atom _S_<sup>_−_1</sup> _{_ 5 _}_ . This is consistent with the intuition: knowing the sum does not determine the red die’s value. 

##### **Indicator Functions** 

_Indicator functions_ are special important random variables. For any event _A ∈F_ , the indicator function of the event _A_ is the random map: 



Since _A ∈F_ , this is easily seen to be a random variable **1** _A_ : Ω _→{_ 0 _,_ 1 _}_ . Key properties include: 

(i) **1** Ω _≡_ 1 

(ii) **1** _Ac_ = 1 _−_ **1** _A_ 

(iii) **1** _A∩B_ = **1** _A ∧_ **1** _B_ = **1** _A ·_ **1** _B_ 

(iv) **1** _A∪B_ = **1** _A ∨_ **1** _B_ = **1** _A_ + **1** _B −_ **1** _A∩B_ 

These relations mirror the set-theoretic properties of events and will be crucial when discussing expectations. 

_1.2. RANDOM VARIABLES_ 

21 

#### **1.2.3 Law (or distribution) of random variables** 

The concept of distribution is central to probability theory, as it allows us to quantify the likelihood of different outcomes of random variables. In this section, we explore how probability measures are transferred from sample spaces to the ranges of random variables, and how multiple random variables interact through joint and marginal distributions. In this section, a probability space (Ω _, F,_ P) is given. 

##### **Law or distribution of a random variable** 

When we have a random variable _X_ : Ω _→ E_ , we can “push forward” the probability measure from the sample space (Ω _, F_ ) to the codomain ( _E, E_ ). This transferred measure captures the essential probabilistic behavior of _X_ . 

Law or distribution of a random variable 

**Definition 1.2.10.** _Given a random variable X_ : Ω _→ E, we transfer the probability structure from_ (Ω _, F,_ P) _to_ ( _E, E_ ) _by_ 

_µX_ ( _B_ ) := P _{X ∈ B} ∀B ∈E._ 

_The latter is a probability measure on_ ( _E, E_ ) _called the_ law _or the_ probability distribution _of X. When emphasizing dependence on_ P _, we write µX,_ P _. Other common notations are L_ ( _X_ ) _and L_ P( _X_ ) _._ 

_The function fX_ : _E →_ [0 _,_ 1] _defined as_ 

_fX_ ( _x_ ) := _µX {x}_ = P _{X_ = _x}, ∀x ∈ E,_ 

_is called the_ discrete density function _of X (with respect to the law µX )._ 

Since we are assuming that _E_ is finite, the probability distribution (law) of a random variable _X_ : Ω _→ E_ is completely determined by its discrete density function _fX_ . Indeed, for any _B ⊆ E_ , we recover the law _µX_ ( _B_ ) by summing: 



This additive property makes probability distributions on finite spaces particularly tractable. The relationship between laws and their discrete density functions provides a powerful framework for working with probability distributions on finite spaces. While the law gives the abstract probability measure, the density function provides a concrete computational tool for calculating probabilities through simple summation operations. 

##### Sum of two dice 

**Example 1.2.11.** _Consider Example 1.2.4. The random variable “sum” is_ 



_with codomain E_ = _{_ 2 _, . . . ,_ 12 _}. The law µS_ = _L_ ( _S_ ) _is described by the discrete density function fS computed by counting favorable outcomes:_ 



_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

22 

_The law µS assigns to each subset B ⊆ E the probability µS_ ( _B_ ) =<sup>�</sup> _x∈B_<sup>_fS_(</sup><sup>_x_)</sup><sup>_._</sup> 

##### **Joint distribution and marginal distributions** 

When studying multiple random variables simultaneously, we need to understand not only their individual behaviors but also how they relate to each other. This leads to the concepts of joint and marginal distributions. 

Joint and marginal laws and densities 

**Definition 1.2.12.** _Given random variables Xj_ : Ω _→ Ej, with j_ = 1 _, . . . , n, we can view the vector X_ = ( _X_ 1 _, . . . , Xn_ ) _as a random variable taking values in the product space E_ = _E_ 1 _× · · · × En._ 

_The_ joint law _µ_ ( _X_ 1 _,...,Xn_ ) = _L_ ( _X_ 1 _, . . . , Xn_ ) _is the probability measure on E_ 1 _× · · · × En defined by:_ 



_The_ marginal laws _µXi_ = _L_ ( _Xi_ ) _are obtained from the joint law by:_ 



_The corresponding_ marginal discrete density _of Xi is obtained by summing over all other variables:_ 

If _µ_ ( _X_ 1 _,...,Xn_ ) is a joint law with discrete density function _fX_ 1 _,...,Xn_ , then _µ_ is recovered from _fX_ 1 _,...,Xn_ by 



Moreover, we have the following properties: 

(i) **Non-negativity** : _fX_ 1 _,...,Xn_ ( _x_ 1 _, . . . , xn_ ) _≥_ 0 for all ( _x_ 1 _, . . . , xn_ ) 



(iii) **Marginalization** : The marginal law _µXi_ has density<sup>2</sup> 



Conversely, any function _f_ : _E_ 1 _× · · · × En →_ [0 _,_ 1] satisfying (i) and (ii) defines a valid joint probability law through (1.2.1). 

The joint law contains complete information about the probabilistic relationships between the variables. From a joint law, we can recover individual variable laws through _marginalization_ . 2Note that<sup><u>�</u></sup> _xi∈Ei_<sup>_fX_</sup> _i_<sup>(</sup><sup>_xi_) = 1.</sup> 

_1.3. CONDITIONAL PROBABILITY_ 

23 

There is a crucial fact: while the joint law determines the marginal laws, the converse is not true. Different joint laws can yield the same marginal laws, as shown by the following examples. 

Two coin tosses under different probability distributions 

**Example 1.2.13.** _Consider two different experiments with two coin tosses with outcomes labeled by_ 0 _,_ 1 _. The tables below show the joint discrete density functions fX,Y_ ( _x, y_ ) _that define the joint laws L_ ( _X, Y_ ) _._ 

**_Case 1_** 

**_Case 2_** 



_(a) In both cases, the marginal densities are identical:_ 

• _fX_ (0) = _fX_ (1) = 1 _/_ 2 • _fY_ (0) = _fY_ (1) = 1 _/_ 2 

_(b) However, the joint densities are completely different:_ 

- _In Case 1: fX,Y_ ( _x, y_ ) = 1 _/_ 4 _for all_ ( _x, y_ ) _, showing independence_ 

- • _In Case 2: fX,Y_ (0 _,_ 0) = _fX,Y_ (1 _,_ 1) = 1 _/_ 2 _, showing perfect correlation_ 

_This demonstrates that marginal laws alone cannot capture the dependencies between variables. Only the joint law contains complete information about their relationship._ 

### **1.3 Conditional probability** 

In this section, we explore two fundamental concepts that capture how probabilities change with new information and how different random phenomena relate to each other. Throughout, unless otherwise specified, (Ω _, F,_ P) will be a given reference probability space. 

Conditional probability 



Conditional probability represents the rational update of an agent’s beliefs when they learn that event _H_ has occurred. If (Ω _, F,_ P) models the initial uncertainty, then (Ω _, F,_ P _H_ ) models the updated uncertainty after learning that _ω ∈ H_ . The operation “renormalizes” the original probability by concentrating it on _H_ , proportionally redistributing the probability mass to events of the form _A ∩ H_ . 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

24 

##### Dice roll revisited 

**Example 1.3.1.** _Consider the toss a fair die, modeled as usual in the probability space_ Ω= _{_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _}, F_ = 2<sup>Ω</sup> _, and uniform distribution_ P _{i}_ = 1 _/_ 6 _. Let H_ = _{_ 2 _,_ 4 _,_ 6 _} (even outcome). Then:_ 



_Hence, conditional on an even outcome, the probability becomes uniformly distributed over {_ 2 _,_ 4 _,_ 6 _}._ 

A celebrated probability paradox: the Monty Hall problem 

**Example 1.3.2.** _The Monty Hall problem, named after the host of the game show “Let’s Make a Deal,” became famous in the 1990s when it sparked intense debate among mathematicians and the general public. Even renowned mathematician Paul Erd˝os initially refused to believe the correct solution!_ 

_Suppose you are on a game show, and you are given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No._ 1 _, and the host,_ _<u>who knows what’s behind the doors,</u> opens another door, say No._ 3 _, which has a goat. He then says to you, “Do you want to switch to door No._ 2 _?” Is it to your advantage to switch your choice?_ «aR **_Crucial Rule:_** _The host_ always _opens a door with a goat (either No._ 2 _or No._ 3 _) and_ never _opens the contestant’s initially chosen door (No._ 1 _)._ 

**_Mathematical formalization:_** _Let the sample space be:_ 



_where the triple indicates the car position (_ 1 _= car,_ 0 _= goat). The rational choice for the probability is the uniform one:_ 



##### **_Events interpretation:_** 

- _“Good initial choice = car behind door No._ 1 _” corresponds to the event A_ = _{_ (1 _,_ 0 _,_ 0) _} with_ P( _A_ ) = 1 _/_ 3 _._ 

- _“Bad initial choice= car either behind door No._ 2 _or behind door No._ 3 _” corresponds to the event A_<sup>_c_</sup> = _{_ (0 _,_ 1 _,_ 0) _,_ (0 _,_ 0 _,_ 1) _} with_ P( _A_<sup>_c_</sup> ) = 2 _/_ 3 _._ 

**_Solution:_** _When the host reveals a goat behind one of the other doors, this provides_ no new information _about your initial choice because:_ 

_1.3. CONDITIONAL PROBABILITY_ 

25 

- _The host was_ guaranteed _to be able to show a goat regardless of where the car actually is: the conditioning event was_ 

_H_ = _{second or third component of ω_ = 0 _}._ 

_Clearly_ _<u>H</u>_ = Ω _<u>.</u>_ 

- _Since H_ = Ω _, the conditional probability remains the original one:_ 



_Hence, switching doors doubles your chances of winning from_ 1 _/_ 3 _to_ 2 _/_ 3 _!_ 

**_Why is this counterintuitive?_** _Most people assume that after the host reveals a goat, the remaining two doors have equal probability (_ 1 _/_ 2 _). However, the host’s knowledge and constrained behavior provide information that updates the probabilities asymmetrically._ 

##### Variation: ignorant host 

**Exercise 1.3.3.** _Consider this variation: the host_ **_does not know_** _where the car is and randomly opens one of the two unchosen doors. If he happens to reveal a goat (lucky for the game to continue!), should you switch?_ 

**_Hint:_** _In this case, the host’s action_ does _provide information: with the labeling of the discussed example it is the information “the car is not behind the door No._ 3 _._ 

##### Historical Note 

The Monty Hall problem gained notoriety in 1990 when Marilyn vos Savant presented the correct solution in her Parade magazine column. She received thousands of letters, many from Ph.D. mathematicians insisting she was wrong. The controversy was so intense that it prompted academic papers and computer simulations that empirically verified the 2/3 probability for switching. 

The key insight is that the host’s action is _not random_ but constrained by the rules and his knowledge. 

##### **Some relevant rules on conditional probability** 

The following proposition establishes two fundamental tools in probability theory that allow us to compute probabilities through decomposition and sequential conditioning. These formulas are particularly useful when dealing with complex events that can be broken down into simpler components. 

Law of total probability and Bayes’ rule 

**Proposition 1.3.4.** _The following fundamental formulas hold:_ 

_1._ **_Law of total probability_** _: If A_ 1 _, . . . , An form a partition of_ Ω _, then for any A ∈F:_ 



_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

26 

_2._ **_Bayes’ formula_** _: For two events A and B with_ P( _A_ ) _>_ 0 _and_ P( _B_ ) _>_ 0 _:_ 





_Proof. 1._ Since _A_ 1 _, . . . , An_ partition Ω, we have: 



The sets _A ∩ Ai_ are disjoint because the _Ai_ are disjoint. Therefore: 



By definition of conditional probability, P( _A∩Ai_ ) = P( _Ai_ )P( _A|Ai_ ) when P( _Ai_ ) _>_ 0. If P( _Ai_ ) = 0, then P( _A ∩ Ai_ ) = 0 and by convention P( _Ai_ )P( _A|Ai_ ) = 0. Thus: 



_2._ By definition of conditional probability: 



But P( _A ∩ B_ ) = P( _B|A_ )P( _A_ ), so: 



_3._ We proceed by induction. For _n_ = 1: 



which is trivially true. Assume the formula holds for _n −_ 1: 



For _n_ , we have: 



The claim is proved. 

_1.3. CONDITIONAL PROBABILITY_ 

27 

Law of total probability (I) 

**Example 1.3.5** (Quality control) **.** _A factory has two production lines: Line 1 produces 60% of items, Line 2 produces 40%. The defect rates are 2% for Line 1 and 5% for Line 2. What is the probability that a randomly selected item is defective?_ 

**_Heuristic approach._** _In practice, we can compute this directly without formal construction:_ 

P( _D_ ) = 0 _._ 6 _×_ 0 _._ 02 + 0 _._ 4 _×_ 0 _._ 05 = 0 _._ 012 + 0 _._ 02 = 0 _._ 032 _._ 

_This heuristic approach uses the readily available operational data._ 

**_Theoretical foundation._** _To provide a rigorous foundation, we construct a probability space that models this scenario. We take the sample space_ 



_where:_ 

• _L_ 1 _, L_ 2 _denote the production lines_ 

• _G, D denote good and defective items_ 

_Define the events:_ 

• _A_ 1 = _{_ ( _L_ 1 _, G_ ) _,_ ( _L_ 1 _, D_ ) _} = “item comes from Line 1”_ • _A_ 2 = _{_ ( _L_ 2 _, G_ ) _,_ ( _L_ 2 _, D_ ) _} = “item comes from Line 2”_ 

• _D_ = _{_ ( _L_ 1 _, D_ ) _,_ ( _L_ 2 _, D_ ) _} = “item is defective”_ 

_The key observation is that A_ 1 _and A_ 2 _form a partition of_ Ω _. Based on the given data, we naturally assign:_ 



_Applying the Law of Total Probability:_ 



**_Remark._** _Note that in this theoretical construction, we have not explicitly defined the probability measure on the individual outcomes (singletons) of_ Ω _. Instead, we directly assigned values to the probabilities of the events A_ 1 _, A_ 2 _and the conditional probabilities_ P( _D|A_ 1) _,_ P( _D|A_ 2) _, which are the quantities naturally available from the operational data. This shows an important aspect of probability theory: we can often work with probabilities of relevant events without needing to specify the whole probability space. The law of total probability provides a powerful tool that allows us to compute probabilities of interest using only partial information about the system. The heuristic approach and the theoretical foundation yield the same result, but the latter ensures mathematical rigor and clarifies the assumptions behind the practical calculation._ 

Law of total probability (II) 

**Example 1.3.6** (Medical testing) **.** _A disease affects 1% of population. A test is 99% accurate for sick people and 95% accurate for healthy people. What is the probability of a positive test?_ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

28 

**_Heuristic approach._** _In practice, we can compute this directly using available data:_ 

P( _T_<sup>+</sup> ) = 0 _._ 01 _×_ 0 _._ 99 + 0 _._ 99 _×_ 0 _._ 05 = 0 _._ 0099 + 0 _._ 0495 = 0 _._ 0594 _._ 

_This approach uses epidemiological data (disease prevalence) and test performance characteristics._ 

**_Theoretical foundation._** _To provide a rigorous foundation, we construct a probability space that models this medical scenario. We take:_ 

Ω= _{_ ( _D, P_ ) _,_ ( _D, N_ ) _,_ ( _H, P_ ) _,_ ( _H, N_ ) _},_ 

_where:_ 

• _D, H denote diseased and healthy individuals_ • _P, N denote positive and negative test results Define the events:_ 

• _A_ 1 = _{_ ( _D, P_ ) _,_ ( _D, N_ ) _} = “person has the disease”_ • _A_ 2 = _{_ ( _H, P_ ) _,_ ( _H, N_ ) _} = “person is healthy”_ • _T_<sup>+</sup> = _{_ ( _D, P_ ) _,_ ( _H, P_ ) _} = “test is positive”_ 

_The key observation is that A_ 1 _and A_ 2 _form a partition of_ Ω _. Based on the given data, we naturally assign:_ 

P( _A_ 1) = 0 _._ 01; P( _A_ 2) = 0 _._ 99; P( _T_<sup>+</sup> _|A_ 1) = 0 _._ 99; P( _T_<sup>+</sup> _|A_ 2) = 0 _._ 05 _._ 

_Applying the Law of Total Probability:_ 

P( _T_<sup>+</sup> ) = P( _A_ 1)P( _T_<sup>+</sup> _|A_ 1) + P( _A_ 2)P( _T_<sup>+</sup> _|A_ 2) = 0 _._ 01 _×_ 0 _._ 99 + 0 _._ 99 _×_ 0 _._ 05 = 0 _._ 0594 _._ 

**_Remark._** _As in the previous example, we have not explicitly defined the probability measure on the individual outcomes of_ Ω _. Instead, we worked directly with the probabilities of the relevant events A_ 1 _, A_ 2 _and the conditional probabilities_ P( _T_<sup>+</sup> _|A_ 1) _,_ P( _T_<sup>+</sup> _|A_ 2) _, which correspond to the epidemiological data typically available. This example highlights the practical utility of the Law of Total Probability: measuring the overall positive test rate_ P( _T_<sup>+</sup> ) _directly in a population can be challenging and expensive, while disease prevalence_ P( _A_ 1) _and test accuracy measures,_ P( _T_<sup>+</sup> _|A_ 1) _,_ P( _T_<sup>+</sup> _|A_ 2) _, are more readily obtainable through focused studies._ 

Bayes’ Rule 

**Example 1.3.7** (Medical testing revisited) **.** _A certain disease affects 1% of the population. A test for the disease has 95% sensitivity and 90% specificity. If a person tests positive, what is the probability she actually has the disease?_ 

**_Theoretical foundation._** _To provide a rigorous foundation, we use the same sample space as in the previous example:_ 

Ω= _{_ ( _D, P_ ) _,_ ( _D, N_ ) _,_ ( _H, P_ ) _,_ ( _H, N_ ) _},_ 

_where:_ 

_1.3. CONDITIONAL PROBABILITY_ 

29 

• _D, H denote diseased and healthy individuals_ 

• _P, N denote positive and negative test results Define the events:_ 

• _A_ 1 = _{_ ( _D, P_ ) _,_ ( _D, N_ ) _} = “person has the disease”_ • _A_ 2 = _{_ ( _H, P_ ) _,_ ( _H, N_ ) _} = “person is healthy”_ • _T_<sup>+</sup> = _{_ ( _D, P_ ) _,_ ( _H, P_ ) _} = “test is positive” The key observation is that A_ 1 _and A_ 2 _form a partition of_ Ω _. Based on the given data, we assign:_ 

P( _A_ 1) = 0 _._ 01; P( _A_ 2) = 0 _._ 99; P( _T_<sup>+</sup> _|A_ 1) = 0 _._ 95 _(sensitivity)_ ; P( _T_<sup>+</sup> _|A_ 2) = 0 _._ 10 _(false positive rate). Applying Bayes’ Rule:_ P( _A_ 1 _|T_<sup>+</sup> ) =<sup>P(</sup><sup>_T_+</sup><sup>_<u>|A</u>_1)P(</sup><sup>_A_1)</sup> P( _T_<sup>+</sup> ) P( _T_<sup>+</sup> _<u>|A</u>_ 1)P( _A_ 1) = P( _A_ 1)P( _T_<sup>+</sup> _|A_ 1) + P( _A_ 2)P( _T_<sup>+</sup> _|A_ 2) 0 _._ 95 _×_ 0 _._ 01 = (0 _._ 01 _×_ 0 _._ 95) + (0 _._ 99 _×_ 0 _._ 10) 0 _._ 0095 = 0 _._ 0095 + 0 _._ 099<sup>_≈_0</sup><sup>_._0876</sup><sup>_._</sup> 

**_Remark._** _As in the Law of Total Probability example, we work directly with the probabilities of the relevant events A_ 1 _, A_ 2 _and the conditional probabilities_ P( _T_<sup>+</sup> _|A_ 1) _,_ P( _T_<sup>+</sup> _|A_ 2) _, which correspond to the epidemiological data typically available. Bayes’ Rule allows us to_ reverse _the conditioning: from knowing_ P( _T_<sup>+</sup> _|A_ 1) _(test sensitivity) we obtain_ P( _A_ 1 _|T_<sup>+</sup> ) _(probability of disease given positive test). This example highlights the practical utility of Bayes’ Rule: while it is challenging to measure_ P( _A_ 1 _|T_<sup>+</sup> ) _directly, we can compute it from more readily available data—disease prevalence_ P( _A_ 1) _and test accuracy measures_ P( _T_<sup>+</sup> _|A_ 1) _,_ P( _T_<sup>+</sup> _|A_ 2) _._ 

Bayes’ sequential rule 

**Example 1.3.8** (Multi-stage quality control) **.** _A product goes through_ 3 _quality checks. The probabilities of passing each check given the previous one was passed are:_ 95% _for Check_ 1 _,_ 90% _for Check_ 2 _(given passed Check_ 1 _), and_ 85% _for Check_ 3 _(given passed Check_ 2 _). What is the probability that a product passes all three checks?_ 

**_Heuristic approach._** _In practice, we can compute this directly using the multiplicative rule:_ 



_This approach uses the stage-to-stage transition probabilities that are typically monitored in quality control systems._ 

**_Theoretical foundation._** _To provide a rigorous foundation, we construct a probability space that models this multi-stage process. We take as sample space_ 



_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

30 

_where each sequence indicates pass/fail for checks_ 1 _,_ 2 _,_ 3 _of the product. Define the events:_ 

- _A_ 0 = Ω _;_ 

- _A_ 1 = _{PPP, PPF, PFP, PFF } = “passes check_ 1 _”;_ 

- _A_ 2 = _{PPP, PPF } = “passes checks_ 1 _and_ 2 _”;_ 



_Based on the given data, we naturally assign:_ 



_Applying Bayes’ Sequential Rule:_ 



**_Remark._** _As in previous examples, we have not explicitly defined the probability measure on_ Ω _. Instead, we worked directly with the conditional probabilities between successive stages, which are the quantities naturally tracked in quality management systems. The theoretical construction validates the intuitive multiplicative approach used in practice, while the practical calculation shows how complex multi-stage probabilities can be efficiently computed using conditional information._ 

### **1.4 Independence** 

The concept of independence is fundamental in probability theory, capturing situations where knowledge of one random phenomenon provides no information about another. Intuitively, due to the lack of ”interaction,” two events or random variables are independent if the occurrence or outcome of one does not influence our probabilistic view on the other. 

#### **1.4.1 Independence of two random variables** 

We begin with the formal definition of independence for random variables, which captures the idea that knowing the value of one variable does not change our probabilistic assessment of the other. 

Independence of random variables 

**Definition 1.4.1.** _Given two random variables X_ : Ω _→ E and Y_ : Ω _→ E_<sup>_′_</sup> _, we say that X_ is independent of _Y if for every event in the form H_ = _{Y ∈ B} with B ∈E_<sup>_′_</sup> _and_ P( _H_ ) _>_ 0 _, we have:_ 



The independence of _X_ and _Y_ is equivalent to the symmetric factorization: 



The notion of independence naturally extends to the events. We define independence between events by looking at whether knowing that one has occurred changes the probability of the other. 

_1.4. INDEPENDENCE_ 

31 

Independece of events 

**Definition 1.4.2** (Independence of events) **.** _Two events A, B ∈F are_ independent _if their indicator functions_ **1** _A and_ **1** _B are independent random variables. This is equivalent to:_<sup>_a_</sup> 



> _a_ Typically this is the primary definition of independence in the old view of probability theory. 

To characterize independence, we introduce the concept of product measure. 

Product measure and product density 

**Definition 1.4.3.** _Let µ and ν be probability measures on_ ( _E, E_ ) _and_ ( _E_<sup>_′_</sup> _, E_<sup>_′_</sup> ) _, respectively. The_ **_product measure_** _µ ⊗ ν is the unique probability measure on_ ( _E × E_<sup>_′_</sup> _, E ⊗E_<sup>_′_</sup> ) _defined on the rectangles A × B as_ 



Proposition: Characterization of Independence (2 Variables) 

**Proposition 1.4.4.** _Two random variables X and Y are independent if and only if their joint distribution is the product of their marginals:_ 



_Equivalently, if and only if their joint density factors as:_ 



Independent vs. Fully Dependent Dice 

**Example 1.4.5.** _Consider two dice X and Y on_ Ω= _{_ 1 _, . . . ,_ 6 _}_<sup>2</sup> _._ 

##### **_Case 1: Independent flips (Uniform distribution)_** 

_The dice are fair and unrelated. The joint distribution is uniform distribution assigning probability_ 1 _/_ 36 _to each singleton_ ( _i, j_ ) _._ 

|_X \ Y_|1|_. . ._<br>6|**_Marginal_** _fX_|
|---|---|---|---|
|1|1_/_36|_. . ._<br>1_/_36|1_/_6|
|_..._|_..._|_..._<br>_..._|_..._|
|6|1_/_36|_. . ._<br>1_/_36|1_/_6|
|**_Marginal_** _fY_|1_/_6|_. . ._<br>1_/_6||



_Note that the joint density is the product of the marginal densities:_ 



_It follows that the random variables that we constructed are independent._ 

##### **_Case 2: Perfectly dependent dice (Diagonal distribution)_** 

_In this scenario, the dice are “fully linked” (e.g., connected by a rod) such that they always_ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

32 

_show the same value (X_ = _Y ). Although the joint distribution is now concentrated on the diagonal, the_ **_marginal densities_** _fX and fY remain identical to the independent case._ 

|_X \ Y_|1|_. . ._|6|**_Marginal_** _fX_|
|---|---|---|---|---|
|1|1_/_6|_. . ._|0|1_/_6|
|_..._|_..._|_..._|_..._|_..._|
|6|0|_. . ._|1_/_6|1_/_6|
|**_Marginal_** _fY_|1_/_6|_. . ._|1_/_6||



_Note that for any diagonal element_ 



_This concentration of mass along the diagonal is a clear visual indicator that_ **_independence fails_** _._ 

#### **1.4.2 Independent families** 

While independence between two random variables is conceptually straightforward, extending this notion to a larger collection requires care. It is not sufficient for the variables to be independent “two by two” (pairwise independence); rather, any information gathered from a group of variables must not influence our knowledge about any other disjoint group. This lead us to a definition based on sub-collections (or blocks) of variables. 

Definition: Independence of a family 

**Definition 1.4.6.** _A finite family of random variables {X_ 1 _, . . . , Xn} is said to be_ independent _if for any two disjoint subfamilies (or “blocks”) S_ = ( _Xi_ 1 _, . . . , Xik_ ) _and T_ = ( _Xj_ 1 _, . . . , Xjm_ ) _, the random vectors S and T are independent._ 

This ”block independence” ensures (somehow) that “no probabilistic relationship” exists within the family. Practically, this property is verified through the factorization of the joint distribution, which generalizes the result seen in the bivariate case. 

Joint distribution of _n_ independent random variables 

**Proposition 1.4.7.** _A family {Xi}_<sup>_n_</sup> _i_ =1<sup>_isindependentifandonlyiftheirjointdistribution_</sup> _is the product of their marginals:_ 



_Equivalently, in terms of discrete densities, the joint density must factorize into the product of marginal densities for all possible outcomes_ ( _x_ 1 _, . . . , xn_ ) _:_ 



A common pitfall is assuming that if all pairs in a family are independent, then the whole family is independent. The following famous example by Bernstein shows that ”local” independence does not necessarily imply “global” independence. 

_1.4. INDEPENDENCE_ 

33 

Pairwise vs. joint independence (Bernstein’s example revisited) 

**Example 1.4.8.** _Consider two independent fair coin tosses X_ 1 _, X_ 2 _∈{−_ 1 _,_ 1 _} and define a third variable as their product: X_ 3 = _X_ 1 _· X_ 2 _. We demonstrate that while any two variables are independent, the triplet is not._ 

**_Step 1: The joint table of_** ( _X_ 1 _, X_ 2) **_with_** _X_ 3 **_labels_** 

_The variables X_ 1 _and X_ 2 _are independent and uniform and the values of X_ 3 _are determined by their._ 

|_X_1_\ X_2|**_-1_**|**_1_**|**_Marginal_** _fX_1|
|---|---|---|---|
|**_-1_**|**_1/4_**|**_1/4_**|_1/2_|
||_(X_3 = 1_)_|_(X_3 =_−_1_)_||
|**_1_**|**_1/4_**|**_1/4_**|_1/2_|
||_(X_3 =_−_1_)_|_(X_3 = 1_)_||
|**_Marginal_** _fX_2|_1/2_|_1/2_||



_Note that_ 

##### _fX_ 1 _,X_ 2( _i, j_ ) = 1 _/_ 4 = _fX_ 1( _i_ ) _fX_ 2( _j_ ) _,_ 

_confirming X_ 1 _⊥ X_ 2 _._ 

**_Step 2: The joint table of_** ( _X_ 1 _, X_ 3) 

_To check the relationship between X_ 1 _and X_ 3 _, we rearrange the data. X_ 3 = 1 _occurs when X_ 1 _and X_ 2 _have the same sign:_ 

|_X_1_\ X_3|**_-1_**|**_1_**|**_Marginal_** _fX_1|
|---|---|---|---|
|**_-1_**|**_1/4_**|**_1/4_**|_1/2_|
||_(X_2 = 1_)_|_(X_2 =_−_1_)_||
|**_1_**|**_1/4_**|**_1/4_**|_1/2_|
||_(X_2 =_−_1_)_|_(X_2 = 1_)_||
|**_Marginal_** _fX_3|_1/2_|_1/2_||



_Again,_ 



_Knowing the product X_ 3 _gives no information about the first toss X_ 1 _. Thus,_ **_pairwise independence holds_** _for all pairs._ 

##### **_Step 3: Lack of joint independence_** 

_Joint independence requires that the product rule holds for the entire triplet. However, if we know both X_ 1 _and X_ 2 _, the outcome of X_ 3 _is determined with certainty:_ 



_Checking the factorization at the point_ (1 _,_ 1 _,_ 1) _:_ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

34 

   - **_Joint Density_** _: fX_ 1 _,X_ 2 _,X_ 3(1 _,_ 1 _,_ 1) = 1 _/_ 4 

- **_Product of Marginals_** _: fX_ 1(1) _fX_ 2(1) _fX_ 3(1) = 1 _/_ 2 _·_ 1 _/_ 2 _·_ 1 _/_ 2 = 1 _/_ 8 

- _Since_ 1 _/_ 4 _̸_ = 1 _/_ 8 _, joint independence_ **_fails_** _._ 

This distinction is crucial in applications. Pairwise independence means that no single variable gives information about any other single variable, but family independence means that no group of variables gives information about any other group. The counterexample shows that variables can be pairwise independent while still having complex interdependencies when considered together. 

A crucial property of independence is its robustness under deterministic processing. If a set of random variables is independent, any new variables derived from them—whether by transforming each one individually or by grouping them into separate blocks —will maintain this lack of interaction. This principle ensures that applying functions to independent data does not “create” correlation where there was none. 

Preservation under transformations 

**Proposition 1.4.9.** _Let {X_ 1 _, . . . , Xn} be a family of independent random variables._ 

_1._ **_Componentwise transformation:_** _For any collection of deterministic functions {fi_ : _Ei → Si}_<sup>_n_</sup> _i_ =1<sup>_,therandomvariables_</sup> 



_are also independent._ 



### **1.5 Three important distributions (on finite sets)** 

We define and discuss the three main distributions on finite sets: the uniform distribution (previously encountered in examples), the Bernoulli distribution, and the binomial distribution. 

#### **1.5.1 Uniform Distribution** 

The uniform distribution models experiments where an object is chosen randomly and fairly from a set of _n >_ 1 distinct elements. 

Let _E_ be a set with _n_ elements; without loss of generality, take _E_ = _{_ 1 _, . . . , n}_ . The _uniform distribution on E_ is the probability distribution _µ_ defined on singletons by: 



A random variable _X_ : Ω _→ E_ is said to have the uniform distribution if its law _µX_ coincides with the uniform distribution on _E_ .<sup>3</sup> 

> 3An explicit probability space supporting such a random variable is straightforward to construct. Take: 



then the identity map _X_ ( _ω_ ) = _ω_ is a random variable with uniform distribution. 

_1.5. THREE IMPORTANT DISTRIBUTIONS (ON FINITE SETS)_ 

35 

#### **1.5.2 Bernoulli Distribution** 

The Bernoulli distribution models binary experiments, such as tossing a (possibly biased) coin with outcomes labeled 0 and 1. 

Let _E_ = _{_ 0 _,_ 1 _}_ . The _Bernoulli distribution on E with parameter p ∈_ (0 _,_ 1), denoted by _B_ ( _p_ ) is the probability distribution _µ_ defined on the singletons _{_ 0 _}, {_ 1 _}_ by: 



A random variable _X_ : Ω _→ E_ is said to have the Bernoulli distribution with parameter _p_ if _µX_ is the Bernoulli distribution with parameter _p_ on _E_ .<sup>4</sup> 

#### **1.5.3 Binomial Distribution** 

Let _n >_ 1 and _p ∈_ (0 _,_ 1). Consider a probability space (Ω _, F,_ P) supporting a family _X_ 1 _, . . . , Xn_ of independent Bernoulli random variables, each with parameter _p_ .<sup>5</sup> This family models the random experiment of “ _n_ independent tosses of a coin” where each toss results in success (labeled by 1) with probability _p_ and failure (labeled by 0) with probability 1 _− p_ . 

Define the random variable 



which takes values in _E_ = _{_ 0 _, . . . , n}_ . The variable _S_ counts the total number of successes in the _n_ trials. Its distribution is called the _binomial distribution with parameters_ ( _n, p_ ), denoted by _B_ ( _n, p_ ). To compute the value that such distribution takes on singletons, i.e, the values _B_ ( _n, p_ ) _{i}_ = P _{S_ = _i}_ for _i_ = 0 _, . . . , n_ , we require some basic tools from _combinatorial calculus_ . 

##### **Basic Combinatorial Calculus** 

Suppose we have _n_ distinct objects. How many ways can we arrange them in order? For example, with 9 balls labeled 1 _, . . . ,_ 9, possible arrangements include (1 2 3 4 5 6 7 8 9) and (9 8 7 6 5 4 3 2 1). Each such arrangement is called a _permutation_ . 

To count permutations, imagine drawing balls from an urn without replacement. For the first ball, there are _n_ choices; for the second, _n −_ 1 choices; continuing this way, we get _n_ ( _n −_ 1) _· · ·_ 2 _·_ 1 total arrangements. This product is called _n factorial_ , denoted: 



By convention, we define 0! := 1. Note that _n_ ! = _n ·_ ( _n −_ 1)!. 

Now consider a different problem: from _n_ distinct objects, how many subsets of size _i ≤ n_ can we form, _ignoring the order_ of elements? If we select _i_ objects sequentially without replacement, we get _n_ ( _n −_ 1) _· · ·_ ( _n − i_ + 1) ordered selections. Since each subset of _i_ objects can be arranged in _i_ ! different orders, the number of _unordered_ subsets is: 



This expression is denoted � _ni_ � and called a _binomial coefficient_ : 



> 4An explicit construction is given by: 



with _X_ ( _ω_ ) = _ω_ . 

> 5The existence of such a space is guaranteed by more general results that will be stated later (see Theorem 2.4.1). For an explicit construction, one can take Ω= _{ω_ = ( _k_ 1 _, . . . , kn_ ) : _kj ∈{_ 0 _,_ 1 _}}_ , _F_ = 2<sup>Ω</sup> , and define P on singletons by P _{ω}_ = _p_<sup>_k_1+</sup><sup>_···_+</sup><sup>_kn_</sup> (1 _− p_ )<sup>_n−_(</sup><sup>_k_1+</sup><sup>_···_+</sup><sup>_kn_)</sup> . 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

36 

The terminology comes from the binomial expansion: 





Binomial coefficients 

Binomial coefficients appear throughout mathematics. They can be constructed using _Pascal’s triangle_ (also known as Tartaglia’s triangle), based on the recurrence relation: 



##### **Computing the Binomial Distribution** 

We now compute _B_ ( _n, p_ ). Fix _i ∈{_ 0 _, . . . , n}_ and let _I_ be a subset of _{_ 1 _, . . . , n}_ with _|I|_ = _i_ . Consider the event: 



This corresponds to the outcome where toss _j_ yields success if _j ∈ I_ and failure if _j ∈ I_<sup>_c_</sup> . By independence of the _Xj_ ’s and since _|I_<sup>_c_</sup> _|_ = _n − i_ , we have: 



There are exactly � _ni_ � such events _AI_ (one for each _I_ with _|I|_ = _i_ ) and those events are mutually disjoint. Since: 



we obtain: 



When _p_ = 1 _/_ 2, the distribution is symmetric: 



equivalently: 



In the following two exercises (taken from G. Letta [10]), a fair coin with sides labeled by 0 and 1 is used. “Fair” means that the probability of getting 0 and the probability of getting 1 in a toss is 1 _/_ 2. The outcome 0 is read as “failure” and the outcome 1 is read as “success”. In both them, (1.5.1) (or, equivalently, (1.5.2)) must be used. 

_1.5. THREE IMPORTANT DISTRIBUTIONS (ON FINITE SETS)_ 

37 

##### Binomial Distribution _n_ = 10, _p_ = 0 _._ 5 



<!-- Start of picture text -->
0 . 3<br>0 . 25<br>0 . 2<br>0 . 15<br>0 . 1<br>5  ·  10 − 2<br>0<br>0 1 2 3 4 5 6 7 8 9 10<br>Number of successes ( i )<br>() fiS<br><!-- End of picture text -->

Figure 1.3: Binomial distribution with _n_ = 10 and _p_ = 1 _/_ 2. The distribution is symmetric around the mean _np_ = 5. 

##### Two players and a game with coins 

**Exercise.** Consider the following game. Two players, say (A) and (B), toss a fair coin. Player (A) performs _n_ tosses, player ( _B_ ) performs _n_ + 1 tosses. If the number of success of (A) is larger or equal to the number of success of (B), then (A) wins; otherwise (B) wins. 

- (a) Model in a suitable probability space the game and write formally the event “(A) wins” and the event “(B) wins”. 

- (b) Say if the game is fair (i.e., the probability of the events “(A) wins” and “(B) wins” is 1 _/_ 2). 

**Solution** . As in the construction of the probability space that we did to define the binomial law, by a general result that will be proved later (Theorem 2.4.1), we may suppose the existence of a probability space (Ω _, F,_ P) supporting a sequence _X_ 1 _, X_ 2 _, . . . , X_ 2 _n_ +1 of independent Bernoulli random variables with parameter 1 _/_ 2. 

We may take the outcomes of the tosses of Player (A) to be represented by _X_ 1 _, . . . , Xn_ , while the outcomes of the tosses of Player (B) are represented by _Xn_ +1 _, . . . , X_ 2 _n_ +1. The number of successes of Player (A) is then given by the random variable 



while the number of successes of Player (B) is given by 



Then, _SA_ and _SB_ are independent, with distributions _B_ ( _n,_ 1 _/_ 2) and _B_ ( _n_ + 1 _,_ 1 _/_ 2) respectively. 

The event _{SA ≥ SB}_ formally represents “(A) wins”; its complement, _{SA < SB}_ represents “(B) wins”. Let us compute their probability. We have 



Partitioning over the possible values of _SB_ , and using the law of total probability and the 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

38 

independence of _SA_ and _SB_ , we obtain: 

_n_ +1 P _{n − SA < n_ + 1 _− SB}_ = � P _{SB_ = _k}_ P _{n − SA < n_ + 1 _− k | SB_ = _k} k_ =0 _n_ +1 = � P _{SB_ = _k}_ P _{n − SA < n_ + 1 _− k}. k_ =0 

Then, using the symmetry property of the binomial distribution with _p_ = 1 _/_ 2 (1.5.2), we get 

_n_ +1 _n_ +1 � P _{SB_ = _k}_ P _{n − SA < n_ + 1 _− k}_ = � P _{SB_ = _k}_ P _{SA < n_ + 1 _− k}. k_ =0 _k_ =0 

By a change of index and the same reasoning as above, we have: 

_n_ +1 � P _{SB_ = _k}_ P _{SA < n_ + 1 _− k} k_ =0 _n_ +1 = � P _{SB_ = _n_ + 1 _− k}_ P _{SA < n_ + 1 _− k} k_ =0 _n_ +1 = � P _{SB_ = _n_ + 1 _− k}_ P _{SA < n_ + 1 _− k | SB_ = _n_ + 1 _− k} k_ =0 _n_ +1 = � P _{SB_ = _n_ + 1 _− k}_ P _{SA < SB | SB_ = _n_ + 1 _− k} k_ =0 = P _{SA < SB}._ 

Combining the equalities above, we have proved that 



Therefore, both probabilities must equal 1 _/_ 2, and the game is fair. 

One player playing a with a coin 

**Exercise.** Consider the following experiment. One player tosses a fair coin in two rounds: 

   - In the first round she/he tosses the coin _n_ times; 

   - In the second round she/he tosses the coin a number of times equal to the number of successes of the first round. 

- (a) Model in a suitable probability space the game and define two random variables _U, V_ representing, respectively, the number of successes and failures in the second round. 

- (b) Determine the laws of _U_ and of _V_ . 

- (c) Say if _U_ and _V_ are independent. 

**Solution** . Again we may postulate by a general result (Theorem 2.4.1) the existence of a probability space (Ω _, F,_ P) supporting a sequence _X_ 1 _, X_ 2 _, . . . , X_ 2 _n_ of independent Bernoulli random variables with parameter 1 _/_ 2. 

_1.6. EXPECTED VALUE_ 

39 

We interpret the experiment as follows: 

- (i) The random variables _X_ 1 _, . . . , Xn_ represent the _n_ tosses of the first round; 

- (ii) The random variables _Xn_ +1 _, . . . , X_ 2 _n_ represent the tosses of the second round, with the understanding that the _j_ -th toss of the second round is considered only if the _j_ -th toss of the first round was successful (i.e., if _Xj_ = 1). 

Define the random variables: 



Here _U_ counts the number of successes in the validated tosses of the second round, while _V_ counts the number of failures in the validated tosses. 

To determine the distribution of _U_ , consider the family ( _Zj_ ) _j_ =1 _,...,n_ where _Zj_ := _XjXn_ + _j_ . Since _Xj_ and _Xn_ + _j_ are independent Bernoulli(1 _/_ 2) random variables, we have: 



Moreover, the _Zj_ ’s are independent. Therefore, _U_ is the sum of _n_ independent Bernoulli(1 _/_ 4) random variables, so _L_ ( _U_ ) = _B_ ( _n,_ 1 _/_ 4). 

A similar argument applies to _V_ . For each _j_ , define _Wj_ := _Xj_ (1 _− Xn_ + _j_ ). Then: 



and the _Wj_ ’s are independent. Hence, _L_ ( _V_ ) = _B_ ( _n,_ 1 _/_ 4). The random variables _U_ and _V_ are not independent. To see this, observe that if _U_ = _n_ (all validated second-round tosses are successes), then necessarily _V_ = 0 (no failures in the validated tosses). This dependency shows that _U_ and _V_ cannot be independent. 

### **1.6 Expected value** 

We now define an object associated to concept random variables _valued in_ R. Since our sample space Ωis finite, the range _E_ of any random map _X_ : Ω _→_ R is finite. When we say that _X_ : Ω _→_ R is a random variable, we actually view it as a map _X_ : Ω _→ E_ , which is measurable as a map (Ω _, F_ ) _→_ ( _E, E_ ) with _E_ = 2<sup>_E_</sup> . A fundamental concept in probability theory that quantifies the tendency of a random variable is the concept of _expected value_ . 

Expected value (or mean) of a real-valued random variable 

**Definition 1.6.1.** _Let X_ : Ω _→_ R _be a random variable. Its_ expected value _(or_ mean _) is the real number_ 



The intuitive meaning of E[ _X_ ] is clear: it is the average of the values of _X_ weighted by their probabilities of occurrence. In this sense, E[ _X_ ] can be interpreted as the best constant approximation of the random variable _X_ . Note that this object depends on the probability measure P; sometimes this dependence is emphasized by using the notation E<sup>P</sup> [ _X_ ]. 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

40 

Expected value and mean of a distribution 



The following properties of the expected value operator are immediate from its definition. The proof is left for exercise. 

Properties of expected value 

**Proposition 1.6.2.** 

_(i) For all c ∈_ R _, A ∈F, we have_ E[ _c ·_ **1** _A_ ] = _c ·_ P( _A_ ) _; in particular, taking c_ = 1 _,_ E[ **1** _A_ ] = P( _A_ ); 

_taking A_ = Ω _,_ E[ _c_ ] = _c._ 

- _(ii) The expected value is a linear operator acting on the space of real-valued random variables; i.e., if α, β ∈_ R _and X, Y_ : Ω _→_ R _are random variables, then_ 



_(iii) The expected value operator is monotone; i.e., if X, Y_ : Ω _→_ R _are random variables,_ 



_(iv) (Integration by discrete density) If Xj_ : Ω _→ Ej, for j_ = 1 _, . . . , n, are random variables and g_ : _E_ := _E_ 1 _× · · · × En →_ R _, then_ 



_(v) Let X_ : Ω _→_ R+ _. Then,_ E[ _X_ ] = 0 _if and only if X ≡_ 0 _._ 

Variance of a random variable 

**Definition 1.6.3.** _Let X_ : Ω _→_ R _be a random variable. The_ variance _of X is the number_ 



The variance measures how much a random variable deviates from its mean value. Clearly, Var[ _X_ ] _≥_ 0 and Var[ _X_ ] = 0 if and only if _X_ is constant. Moreover, for all _α, β ∈_ R, 

Var[ _αX_ + _β_ ] = _α_<sup>2</sup> Var[ _X_ ] _._ (1.6.1) 

_1.7. CONDITIONAL EXPECTED VALUE_ 

41 

Expected value and variance of Bernoulli and binomial random variable 

**Example 1.6.4.** 

- _(i) Let X_ : Ω _→{_ 0 _,_ 1 _} be a random variable having Bernoulli distribution with parameter p ∈_ (0 _,_ 1) _. We have_ 



_and_ 



- _(ii) Let S_ : Ω _→{_ 0 _,_ 1 _, . . . , n} be a random variable having binomial distribution with parameters n ≥_ 1 _, p ∈_ (0 _,_ 1) _. This means that its distribution equals the distribution of the sum of n independent random variables with Bernoulli distribution, i.e.,_ 



_where each Xj, for j_ = 1 _, . . . , n, is a random variable with Bernoulli distribution of parameter p. By linearity of the expected value,_ 



_As for the variance, the computation can be done using the formula for the variance of the sum of independent random variables_ (1.7.6) _that will be proved later: by the independence of the Xj’s, we have_ 



### **1.7 Conditional expected value** 

We are going to define the fundamental notion of conditional expected value of a random variable. For that, we start by considering the expected value with respect to the conditional probability. Let _H ∈F_ be such that P( _H_ ) _>_ 0, and let _X_ : Ω _→_ R be a random variable. We may consider the expected value of a real valued random variable _X_ with respect to P _H_ , i.e. 



By convention, we also set 



which will be useful to keep the sense in many formulas. Notice that if P( _H_ ) _>_ 0, 



First of all, let us state a formula that is typically useful in some computations, that is so called _disintegration formula_ . 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

42 

Disintegration formula for expected value 

**Proposition 1.7.1.** _Let X_ : Ω _→_ R _be a random variable and let A_ 1 _, . . . , An be a partition of_ Ω _(i.e., Ai ∈F for i_ = 1 _, . . . , n, Ai ∩ Aj_ = _∅ for i̸_ = _j, and_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Ai_= Ω</sup><sup>_).Then_</sup> 



_Proof._ We compute the expected value of _X_ by conditioning on the partition _A_ 1 _, . . . , An_ : 



where we have used the definition of conditional probability 



for P( _Ai_ ) _>_ 0, and the convention that P( _Ai_ )E[ _X | Ai_ ] = 0 when P( _Ai_ ) = 0. 

Alternatively, we can prove this using the indicator functions approach: 



where the last equality follows from the identity E[ _X | Ai_ ] = 



Now we introduce the concept of _conditional expected value with respect to another random variable_ or, more precisely, _with respect to the σ-algebra generated by another random variable_ . Throughout the rest of this section, _Y_ : Ω _→ E_ will be a conditioning random variable. For notational convenience, given _y ∈ E_ , we set 



notice that, recalling the convention (1.7.1), if _X_ : Ω _→_ R is a random variable, we have 

E _y_ [ _X_ ] = 0 if P _{Y_ = _y}_ = 0 _._ 

Conditional expected value with respect to a random variable 

**Definition 1.7.2.** _Let X_ : Ω _→_ R _be a random variable and let Y_ : Ω _→ E be another random variable. The_ conditional expected value of _X_ given _Y is the σ_ ( _Y_ ) _-measurable real-valued random variable_ 



_1.7. CONDITIONAL EXPECTED VALUE_ 

43 

Often the notation is lightened by setting 



Note that the conditional expected value also depends on the probability measure P; sometimes this dependence is emphasized by using the notation E<sup>P</sup> [ _X | σ_ ( _Y_ )]. 

Interpretation of the conditional expected value 



it turns out that E[ _X | σ_ ( _Y_ )] can be interpreted as the best _σ_ ( _Y_ )-measurable approximation of _X_ , or, in other words, as the best approximation of the random variable _X_ given the knowledge of the random variable _Y_ . 

When the conditioning random variable _Y_ is an _n_ -tuple of random variables, i.e., 



we can consider _Y_ as a single random variable valued in _E_ := _E_ 1 _× · · · × En_ , then consider the _σ_ -algebra _σ_ ( _Y_ 1 _, . . . , Yn_ ) := _σ_ ( _Y_ ) generated by it – i.e., the minimal _σ_ -algebra making all the _Yj_ ’s measurable – and consider the conditional expected value of _X_ with respect to _σ_ ( _Y_ 1 _, . . . , Yn_ ), i.e., the object 



defined in an analogous way: 



Often, the notation is lightened by setting 



Properties of conditional expected value 

**Proposition 1.7.3.** _Let X_ : Ω _→_ R _and Y_ : Ω _→ E be random variables._ 

- _(i) The conditional expected value is a linear operator; i.e., given α, β ∈_ R _, X, Z_ : Ω _→_ R _, we have_ E[ _αX_ + _βZ | σ_ ( _Y_ )] = _α_ E[ _X | σ_ ( _Y_ )] + _β_ E[ _Z | σ_ ( _Y_ )] _._ 

_(ii) If X is constant, i.e., X ≡ c ∈_ R _, then_ 



_(iii) If X and Y are independent, then_ 



_(iv) If X is σ_ ( _Y_ ) _-measurable and Z_ : Ω _→_ R _is another real random variable, then_ 



_In particular,_ 



_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

44 

_(v) We have_ E [E[ _X | σ_ ( _Y_ )]] = E[ _X_ ] _._ 

- _(vi) (Tower property) Let Z_ : Ω _→ E_<sup>_′_</sup> _be another random variable. If σ_ ( _Y_ ) _⊆ σ_ ( _Z_ ) _(i.e., if Y is σ_ ( _Z_ ) _-measurable), then_ 



_Proof._ The proofs follow directly from the definition of conditional expected value and basic properties of expectation. 

(i) By linearity of the expected value and the definition: 



(ii) If _X ≡ c_ , then E _y_ [ _X_ ] = _c_ for all _y ∈ E_ (with the convention for P _{Y_ = _y}_ = 0). Thus: 



- (iii) If _X_ and _Y_ are independent, then for each _y ∈ E_ with P _{Y_ = _y} >_ 0, we have E _y_ [ _X_ ] = E[ _X_ ] because the conditional distribution of _X_ given _{Y_ = _y}_ equals the unconditional distribution of _X_ . Thus: 



- (iv) Since _X_ is _σ_ ( _Y_ )-measurable, by Doob’s measurability criterion (Proposition 1.2.7), there exists _f_ : _E →_ R such that _X_ = _f ◦ Y_ . Then on each set _{Y_ = _y}_ , _X_ takes the constant value _f_ ( _y_ ). For any _y ∈ E_ with P _{Y_ = _y} >_ 0: 



Therefore: 



The particular case follows by taking _Z ≡_ 1. 

(v) Using the definition and the law of total expectation: 



_1.7. CONDITIONAL EXPECTED VALUE_ 

45 

But E _y_ [ _X_ ]P _{Y_ = _y}_ = E[ _X_ **1** _{Y_ = _y}_ ], so: 



- (vi) Since _σ_ ( _Y_ ) _⊆ σ_ ( _Z_ ), by Doob’s measurability criterion, there exists _g_ : _E_<sup>_′_</sup> _→ E_ such that _Y_ = _g ◦ Z_ . Then for each _z ∈ E_<sup>_′_</sup> , on the set _{Z_ = _z}_ , _Y_ takes the constant value _g_ ( _z_ ). Using the definition: 



For fixed _y_ , let _A_ = _{z ∈ E_<sup>_′_</sup> : _g_ ( _z_ ) = _y}_ . Then: 



- Since E[ _X | Z_ ] is _σ_ ( _Z_ )-measurable, by property (iv) we have E[E[ _X | Z_ ] **1** _{Z∈A}_ ] = E[ _X_ **1** _{Z∈A}_ ]. Thus: 



Therefore: 



##### Freezing lemma 

**Proposition 1.7.4** (Freezing lemma) **.** _Let X_ : Ω _→ E and Y_ : Ω _→ E_<sup>_′_</sup> _be discrete random variables, and let ϕ_ : _E × E_<sup>_′_</sup> _→_ R _be a function. The conditional expectation of ϕ_ ( _X, Y_ ) _given Y is obtained by “freezing” the second argument of ϕ at the observed value of Y and then averaging over X; precisely_ 



_Proof._ By definition of conditional expectation with respect to _Y_ 



On the event _{Y_ = _y}_ we have _Y_ = _y_ and (1.7.3) follows. 

Consequences and applications of the freezing lemma 

Let us see some important consequences of the result above. 

- (i) When _X_ and _Y_ are independent, the result simplifies. In this case E _y_ = E for every _y ∈ E_<sup>_′_</sup> , so 

   - E[ _ϕ_ ( _X, Y_ ) _| Y_ ] = E[ _ϕ_ ( _X, y_ )] _y_ = _Y ._ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

46 

(ii) We get the following generalization of Proposition 1.7.1: 



When _X_ and _Y_ are independent, this reduces to 



This provides an efficient method for computing expected values of functions of independent random variables by first conditioning on one variable. 

(iii) If _X, Y_ are independent, using (1.7.5) with _ϕ_ ( _x, y_ ) = _xy_ , we get 

As consequence, 



### **1.8 Selected exercises** 

Exercise 1 

Let Ω= _{_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _}_ be a sample space representing a fair die, with P( _ω_ ) = 1 _/_ 6 for each _ω ∈_ Ω. Consider the random variable _X_ ( _ω_ ) = _ω_<sup>2</sup> . Let _{A_ 1 _, A_ 2 _}_ be a partition of Ωdefined by _A_ 1 = _{_ 1 _,_ 2 _,_ 3 _}_ and _A_ 2 = _{_ 4 _,_ 5 _,_ 6 _}_ . 

- (i) Calculate E[ _X | A_ 1] and E[ _X | A_ 2]. 

- (ii) Use the disintegration formula to compute E[ _X_ ]. 

**Solution.** (i) We first compute the probabilities of the atoms of the partition: 



By definition of conditional expectation given an event: 



Similarly, for the second atom: 



(ii) Applying the disintegration formula E[ _X_ ] =<sup>�</sup> _i_<sup>P(</sup><sup>_Ai_)E[</sup><sup>_X| Ai_],weobtain:</sup> 



This matches the direct computation 



_1.8. SELECTED EXERCISES_ 

47 

□ 

Exercise 2 

Let _X_ and _Y_ be discrete random variables with joint distribution given by the following table: 

|_X \ Y_|_y_ = 1|_y_ = 2|
|---|---|---|
|_x_= 0|1_/_8|3_/_8|
|_x_= 1|2_/_8|2_/_8|



Determine expression of the random variable _Z_ = E[ _X | Y_ ] and verify that E[ _Z_ ] = E[ _X_ ]. 

**Solution.** The random variable _Z_ is _σ_ ( _Y_ )-measurable, hence it takes constant values on the atoms _{Y_ = 1 _}_ and _{Y_ = 2 _}_ . We compute the marginals of _Y_ : 



Over the event _{Y_ = 1 _}_ , the r.v. _Z_ takes the value: 



Over the event _{Y_ = 2 _}_ , the r.v. _Z_ takes the value: 



Thus _Z_ =<sup><u>2</u></sup> 3<sup>**1**</sup><sup>_{Y_=1</sup><sup>_}_+</sup><sup><u>2</u></sup> 5<sup>**1**</sup><sup>_{Y_=2</sup><sup>_}_.Finally,</sup> 



which is exactly E[ _X_ ] = 1 _·_ P _{X_ = 1 _}_ = 4 _/_ 8. 

□ 

##### Exercise 3 

Let _X_ and _Y_ be independent discrete random variables, with _X_ having Bernoulli distribution of parameter _p ∈_ (0 _,_ 1), and _Y_ taking values in _{_ 1 _,_ 2 _}_ with P _{Y_ = 1 _}_ = 1 _/_ 2. Let _ϕ_ ( _x, y_ ) = _x_<sup>_y_</sup> . Compute E[ _X_<sup>_Y_</sup> _| Y_ ] using the freezing lemma. 

**Solution.** By the freezing lemma for independent variables, we have 



where _ψ_ ( _y_ ) = E[ _X_<sup>_y_</sup> ]. Since _X_ is _B_ ( _p_ ), for any fixed _y_ we have: 



The function _ψ_ ( _y_ ) is constant and equal to _p_ for _y ∈{_ 1 _,_ 2 _}_ . Consequently, 



□ 

_CHAPTER 1. PROBABILITY THEORY IN FINITE SPACES_ 

48 

##### Exercise 4: Application of Disintegration 

Consider two independent rolls of a fair die. Let _X_ be the result of the first roll and _Y_ the result of the second roll. Compute E[max( _X, Y_ )] by conditioning on _Y_ . 

**Solution.** Using the disintegration formula (1.7.5): 



□ 

## **Chapter 2** 

# **The discrete case: from finite to countable** 

So far, we have only considered finite probability spaces Ω. This is a significant limitation for describing many natural phenomena. In particular, restricting random variables to finite ranges prevents us from modeling important cases where outcomes may take values in countable or even uncountable sets. For instance, we would like to consider random variables _X_ : Ω _→_ N, _X_ : Ω _→_ [0 _,_ 1], or _X_ : Ω _→_ R, possibly with _X_ being _surjective_ . 

Moreover, this is not the only limitation, nor the most important one for the developments in subsequent chapters. We need to consider _countable families_ of random variables _{Xj}j∈_ N to describe random phenomena occurring over discrete time without fixing a finite time horizon—what we will call discrete-time stochastic processes over an infinite time horizon. In this case, even if each _Xj_ takes values in a finite set _Ej_ , the overall outcome of the countable family _{Xj}j∈_ N belongs to the product space _E_<sup>N</sup> , which is uncountable. Consider this example. 

Infinite sequence of coin tosses 

Consider tossing a fair coin infinitely many times. The natural way to model this random experiment is to take as sample space 



The sequence of coin tosses is naturally represented by the sequence of random variables _Xi_ ( _ω_ ) = _ωi_ . In this example, Ωis uncountable. In fact: 



This canonical example motivates the extension from finite probability spaces to infinite and possible uncountable spaces that can accommodate infinite sequences. To handle such objects, we must extend our theoretical framework. The following scheme illustrates the extension program that we are going to carry out. 

Key extensions from finite to general probability spaces 

- **Sample space** Ω **:** finite _−→_ infinite 

- _σ_ **-algebra:** closure under finite unions _−→_ closure under countable unions 

- **Probability measure:** finite additivity _−→_ countable additivity ( _σ_ -additivity) 

- **Random variables:** finite range _−→_ infinite range 

- **Families of random variables:** finite collections _−→_ countable collections _{Xj}j∈_ N 

49 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

50 

We will not review all definitions and results from the finite case in full detail for this new setting. Instead, we highlight the main differences. 

### **2.1 General probability spaces** 

Consider a possibly infinite (countable or uncountable) sample space Ω. We now adapt the definitions of _F_ and P. 

Definition: _σ_ -algebra 

A collection _F ⊆_ 2<sup>Ω</sup> is called a _σ-algebra_ on Ωif: 

1. Ω _∈F_ , 2. _A ∈F ⇒ A_<sup>_c_</sup> _∈F_ (closure under complement), 3. For any countable collection _{An}n∈_ N _⊆F_ ,<sup>�</sup> _n∈_ N<sup>_An∈F_(closureundercountable</sup> unions). 

From 2 and 3, it follows that _F_ is also closed under countable intersections. If _F_ is a _σ_ -algebra on Ω, the pair (Ω _, F_ ) is called a _measurable space_ . 

Definition: Probability measure 

Let _F ⊆_ 2<sup>Ω</sup> be a _σ_ -algebra. A function P : _F →_ [0 _,_ 1] is called a _probability measure_ on (Ω _, F_ ) if: (A1) 0 _≤_ P( _A_ ) _≤_ 1 for all _A ∈F_ , (A2) P(Ω) = 1, 



“Continuity properties” and subadditivity of probability measures 

For a probability measure P on (Ω _, F_ ): 

- (i) **Continuity from below:** Let _{An}n∈_ N _⊆F_ be such that _An ⊆ An_ +1 for all _n_ . We have P( _n_ lim _→∞_<sup>_An_) =</sup> _n_<sup>lim</sup> _→∞_<sup>P(</sup><sup>_An_)</sup><sup>_,_</sup> 

- where 



_2.2. DISCRETE RANDOM VARIABLES_ 

51 

(iii) **Countable subadditivity:** For any countable collection _{An}n∈_ N _⊆F_ , 



_Proof sketch._ (i) Define _B_ 1 = _A_ 1 and _Bn_ = _An \ An−_ 1 for _n ≥_ 2. The sets _Bn_ are disjoint and � _nk_ =1<sup>_Bk_=</sup><sup>_An_,�</sup><sup>_∞_</sup> _n_ =1<sup>_Bn_= �</sup><sup>_∞_</sup> _n_ =1<sup>_An_.Then:</sup> 



(ii) Apply (i) to the complements _A_<sup>_c_</sup> _n_<sup>,whichformanincreasingsequence.</sup> (iii) Use the disjointification trick: define _Bn_ = _An \_<sup>�</sup><sup>_n_</sup> _k_ =1<sup>_−_1</sup><sup>_Ak_.Then �</sup> _n_<sup>_An_= �</sup> _n_<sup>_Bn_with the</sup> _Bn_ disjoint, and P( _Bn_ ) _≤_ P( _An_ ). 

### **2.2 Discrete random variables** 

We limit our theory to random maps with at most countable range<sup>1</sup> . Hence, we consider maps 



where _E_ may be a (truly) countable space, with the care of substituting the notion of _algebra_ with the notion of _σ_ - _algebra_ for what concerns measurability features. 

With this restriction, the concept of random variables and the related notions of measurability defined in Section 1.2 can be extended to this larger setting basically in the same way. We will not repeat these concepts. Also, we assume that the arrival spaces are endowed with the so called discrete _σ_ -algebra; precisely, we assume the following. 

Assumption: discrete _σ_ -algebra 

**Assumption 2.2.1.** _The range of the random maps, denoted by E, E_<sup>_′_</sup> _, S, S_<sup>_′_</sup> _etc., are at most countable and are endowed with their power set algebras: E_ = 2<sup>_E_</sup> _, E_<sup>_′_</sup> = 2<sup>_E′_</sup> _, S_ = 2<sup>_S_</sup> _, S_<sup>_′_</sup> = 2<sup>_S′_</sup> _, etc._ 

Discrete measurable spaces and discrete random variables 

**Definition 2.2.2.** _We call the measurable spaces_ ( _E, E_ ) _etc. of Assumption 2.2.1_ discrete _and we call random variables valued in these kind of spaces_ discrete _._ 

Also the definitions and the notations introduced in Section 1.2 for (joint and marginal) laws/distributions and discrete density functions extend naturally to the present case where random variables take values in countable sets. They will be not repeated. 

#### **2.2.1 Poisson distribution** 

Let us see a notable probability distribution on _E_ = N. 

> 1While the theory for random variables valued in countable spaces remains relatively accessible, deeper measuretheoretic machinery is required for the case when the random variables take values in uncountable spaces—a topic beyond the scope of this course. 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

52 

Definition: Poisson distribution 

The _Poisson distribution of parameter λ >_ 0, denoted by _P_ ( _λ_ ), is the probability distribution 



The construction of a random variable _X_ : Ω _→_ N having Poisson distribution is obvious: 



Then, 



realizes the desired object. 

### **2.3 Conditional probability and independence** 

Also the notion of conditional probability remains the same, with the same type of carefulness in substituting the notion of algebra with the notion of _σ_ -algebra for what concerns measurability features. 

Example: Sum of independent Poisson random variables 

The distribution of the sum of two independent random variables _X, Y_ : Ω _→_ N with Poisson distributions _L_ ( _X_ ) = _P_ ( _λ_ 1) and _L_ ( _Y_ ) = _P_ ( _λ_ 2) has still Poisson distribution: precisely _L_ ( _X_ + _Y_ ) = _P_ ( _λ_ 1 + _λ_ 2). 

**Proof:** We have 



where in the last equality we used the binomial theorem: 

Let us detail more about independence, where generalization to infinite sequences becomes important. Indeed, as we will see, countable probability spaces are rich enough to support (infinite) sequences of independent discrete random variables _{Xi_ : Ω _→ Ei}_<sup>_∞_</sup> _i_ =1<sup>,inthefollowing</sup> sense. 

_2.4. THE BERNOULLI SCHEME_ 

53 

Definition: Independent sequence of random variables 

Let _{Xi_ : Ω _→ Ei}_<sup>_∞_</sup> _i_ =1<sup>beasequenceofdiscreterandomvariables.Wesaythatitisan</sup> _independent sequence of random variables_ (or, briefly, an _independent sequence_ ) if, for each couple of nonoverlapping finite subfamilies _{Xik }_<sup>_m_</sup> _k_ =1<sup>and</sup><sup>_{Xj_</sup> _k_<sup>_}n_</sup> _k_ =1 _a_ , the random variables _S_ = ( _Xi_ 1 _, ..., Xim_ ) : Ω _→ Ei_ 1 _× ... × Eim, T_ = ( _Xj_ 1 _, ..., Xjn_ ) : Ω _→ Ej_ 1 _× ... × Ejn,_ are independent. 

> _a_ Nonoverlapping means that _{i_ 1 _, ..., im} ∩{j_ 1 _, ..., jn}_ = _∅_ . 

Proposition: Characterization of independent families 

Let _N ≥_ 2, possibly _N_ = _∞_ , and let _{Xi_ : Ω _→ Ei}_<sup>_N_</sup> _i_ =1<sup>beafamilyofdiscreterandom</sup> variables. The following statements are equivalent. 



### **2.4 The Bernoulli scheme** 

The following result is fundamental, as it has, as a consequence, the fact that it is possible to construct a probability space supporting a random experiment consisting in an “infinite number of identical and independent trials”. 

We address the question: given a family of probability laws _{µi}_<sup>_N_</sup> _i_ =1<sup>,with</sup><sup>_N_finiteorinfinite,</sup> on a sequence of spaces _{_ ( _Ei, Ei_ ) _}_<sup>_N_</sup> _i_ =1<sup>,isitpossibletoconstructaprobabilityspace(Ω</sup><sup>_, F,_P)and</sup> a sequence of independent random variables _{Xi_ : Ω _→ Ei}_<sup>_N_</sup> _i_ =1<sup>suchthat</sup><sup>_L_(</sup><sup>_Xi_)=</sup><sup>_µi_foreach</sup><sup>_i_?</sup> The answer is positive. 

Existence of independent random variables with given laws 

**Theorem 2.4.1** (Kolmogorov’s extension theorem) **.** _For each family of probability laws {µi}_<sup>_N_</sup> _i_ =1<sup>_,whereN≥_2</sup><sup>_(finiteorinfinite),onasequenceofdiscretespaces{_(</sup><sup>_Ei, Ei_)</sup><sup>_}N_</sup> _i_ =1<sup>_,_</sup> _it is always possible to construct a probability space_ (Ω _, F,_ P) _and a family of independent random variables {Xi_ : Ω _→ Ei}_<sup>_N_</sup> _i_ =1<sup>_suchthatL_(</sup><sup>_Xi_) =</sup><sup>_µiforeachi._</sup> 

_Proof._ **Case** _N < ∞_ **.** Consider the space _E_ = _E_ 1 _× E_ 2 _× ... × EN_ endowed with the _σ_ -algebra _E_ = 2<sup>_E_</sup> . Given _x_ = ( _xi_ )<sup>_N_</sup> _i_ =1<sup>_∈E_definethelaw</sup><sup>_µ_astheproductofthemarginallaws</sup><sup>_µi_,i.e.</sup> 



_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

54 

and 



Then take 



and 



i.e. _Xi_ : _E → Ei_ is the projection on the _i_ -th component. Then, one easily checks that this construction provides the desired objects. 

**Case** _N_ = _∞_ **.** The general proof relies on results of abstract measure theory (Kolmogorov’s extension theorem) and we omit it. When sup _i |Ei| < ∞_ , an “handmade” construction is provided in [5, Th. 5.3]. 

We shall make use of the case when _Ei_ = _E_ (typically, the case when _|E| < ∞_ ) and _µi_ = _µ_ for each _i ∈{_ 1 _, ..., N }_ , which corresponds to the construction of so called _independent identically distributed_ (briefly, i.i.d.) finite or infinite sequences. This is the so called Bernoulli scheme. 

Corollary: Bernoulli scheme (existence of i.i.d. sequences) 

Let ( _E, E_ ) be a discrete space, let _µ_ be a probability distribution on it, and let _N ≥_ 2 be finite or infinite. There exists a probability space (Ω _, F,_ P) and a family of i.i.d. ( _independent and identically distributed_ ) random variables valued in ( _E, E_ ) with law _µ_ ; that is a family of independent random variables _{Xi_ : Ω _→ E}_<sup>_N_</sup> _i_ =1<sup>suchthat</sup><sup>_L_(</sup><sup>_Xi_)=</sup><sup>_µ_</sup> for each _i_ = 1 _, ..., N_ . 

#### **2.4.1 Geometric distribution** 

Consider a probability space on which it is defined an i.i.d. sequence of random variables with (common) Bernoulli law of parameter _p ∈_ (0 _,_ 1): 



Define the random variable “first success time”: 



with the convention inf _∅_ = _∞_ . Then _T_ is a random variable valued in N0 _∪{∞}_ . 

Definition: Geometric distribution 

The law of _T_ is called _geometric law or geometric distribution of parameter p_ . 

Let us compute the geometric distribution. Setting _q_ := 1 _− p_ , by independence we have 

Note that 



Hence, 



_2.5. EXPECTED VALUE_ 

55 

i.e., the event _{T_ = _∞}_ representing “the absence of success” of the sequence _{Xi}i∈_ N0 is negligible. Next, since 



we have 



Property: Memoryless property of geometric distribution 

The geometric law has a nice feature which characterizes it, the so-called _memoryless property_ (or absence of memory). Let _n ∈_ N0 and consider the non-negligible event 



The latter represents the “absence of success in the first _n_ trials” of a given independent sequence of experiments of Bernoulli type (e.g. repeated tosses of a coin or repeated extractions in lotteries). 

On this event the difference _T − n_ represents the time we need to await, after the first _n_ unsuccessfully trials, before to have the first success. This is the first success time of the translated Bernoulli process 



that is 



Because of the independence of the sequence _{Xi}i∈_ N0, the sequence _{Yi}i∈_ N0 is also an i.i.d. Bernoulli sequence of parameter _p_ with respect to P _H_ . Hence, the law of _T − n_ under P _H_ coincides with the law of _Z_ under P _H_ , i.e. the geometric law of parameter _p_ . It follows that 



Intuitively, this means that, at a given time _n ∈_ N0, _knowing that the success did not occur yet_ , the confidence on the residual time that we need to wait to see the first success of our sequence of experiments is the same _whatever is n_ (the “delay of success”). 

This property actually characterizes the geometric law, i.e. if _T_ is valued in N0 _∪{∞}_ and (2.4.1) holds (and _T_ is not identically equal to _∞_ ), then _T_ has the geometric distribution. Indeed, taking _i_ = 1 in (2.4.1) and setting _q_ := P _{T >_ 1 _}_ , we get 





### **2.5 Expected value** 

In this section, we extend the concepts of expected value and conditional expected value from finite probability spaces to the general discrete case. While the intuitive ideas remain the same, we need to handle infinite sums (series) carefully. 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

56 

For the extension of the notion of expected value, more carefulness is needed. Basically, finite sums must be replaced by series. 

Given _x ∈_ R, with the symbols _x_<sup>+</sup> _, x_<sup>_−_</sup> we shall denote, respectively, the positive and negative part of _x_ : 



Note that _x_ = _x_<sup>+</sup> _− x_<sup>_−_</sup> and _|x|_ = _x_<sup>+</sup> + _x_<sup>_−_</sup> . For basic results on the theory of numeric series we refer to the Appendix. It is convenient to consider random variables taking values in the extended set of real numbers 



the latter being only a notation. We also use the notation 



and extend on R the product<sup>2</sup> 0 _· ∞_ as 



In the following, we shall consider R-valued random variables taking at most a countable set _E_ of values and will hold a similar observation as the one done in Section 1.6: saying that _X_ : Ω _→_ R is a random variable will mean that one actually looks at _X_ as a map 



and that this map is measurable as a map (Ω _, F_ ) _→_ ( _E, E_ ), with _E_ = 2<sup>_E_</sup> being the discrete _σ_ -algebra and that the random variable is a discrete random variable. This point of view will be not repeated in what follows. 

Expected value for general discrete real random variables 

**Definition 2.5.1.** _Let X_ : Ω _→_ R _be a discrete random variable. We define_ 



_Assuming that at least one of the quantities in_ (2.5.1) _is finite, we say that X is_ semiintegrable _and define the_ expectation _or_ expected value _of X as the (possibly infinite) value_ 



To emphasize the dependence on the probability P, one can also write (and we shall do if needed) E<sup>P</sup> [ _X_ ]. It is clear that the expectation of a random variable is characterized by its distribution: random variables with the same distribution have the same expectation (if welldefined). 

Consider the space of integrable random variables 



We denote it simply by _L_<sup>1</sup> if no confusion may arise; if it is needed to stress the dependence on the probability P, we write _L_<sup>1</sup> (P). Clearly, _L_<sup>1</sup> is a linear vector space. 

> 2The other operations are extended from R to R as in the usual rules of the calculus of limits from basic calculus. 

_2.5. EXPECTED VALUE_ 

57 

Remarks on the definition 

- (i) When _X ≥_ 0, we have _X_<sup>_−_</sup> = 0 and E[ _X_ ] = E[ _X_<sup>+</sup> ] _∈_ [0 _,_ + _∞_ ]. 

- (ii) _X ∈ L_<sup>1</sup> (Ω _, F,_ P) if and only if E[ _|X|_ ] = E[ _X_<sup>+</sup> ] + E[ _X_<sup>_−_</sup> ] _< ∞_ . 

- (iii) If _X ∈ L_<sup>1</sup> (Ω _, F,_ P), then necessarily P _{X ∈_ R _}_ = 1 (i.e., _X_ takes infinite values with probability zero). 

- (iv) The expected value depends only on the distribution of _X_ : if _L_ ( _X_ ) = _L_ ( _Y_ ), then E[ _X_ ] = E[ _Y_ ] whenever defined. 

The properties of expected value extend naturally to the general discrete case: 

Properties of expected value 

**Proposition 2.5.2.** 

_(i) For any constant c ∈_ R _and event A ∈F:_ E[ _c ·_ **1** _A_ ] = _c ·_ P( _A_ ) _._ 

_In particular,_ E[ **1** _A_ ] = P( _A_ ) _and_ E[ _c_ ] = _c. (ii) (Linearity) If X, Y ∈ L_<sup>1</sup> _and α, β ∈_ R _, then:_ E[ _αX_ + _βY_ ] = _α_ E[ _X_ ] + _β_ E[ _Y_ ] _. (iii) (Monotonicity) If X, Y ∈ L_<sup>1</sup> _and X ≤ Y almost surely, then:_ E[ _X_ ] _≤_ E[ _Y_ ] _. (iv) (Integration by discrete density) Let X_ 1 _, . . . , Xn be discrete random variables with ranges E_ 1 _, . . . , En, and let g_ : _E_ 1 _× · · · × En →_ R _. If either: (a) g ≥_ 0 _, or (b) g_ ( _X_ 1 _, . . . , Xn_ ) _∈ L_<sup>1</sup> _, then_ E[ _g ◦_ ( _X_ 1 _, ..., Xn_ )] = � _g_ ( _x_ 1 _, . . . , xn_ ) _·_ P _{X_ 1 = _x_ 1 _, . . . , Xn_ = _xn}_ ( _x_ 1 _,...,xn_ ) _∈E_ 1 _×···×En_ = � _g_ ( _x_ 1 _, . . . , xn_ ) _· fX_ 1 _,...,Xn_ ( _x_ 1 _, . . . , xn_ ) _,_ ( _x_ 1 _,...,xn_ ) _∈E_ 1 _×···×En where fX_ 1 _,...,Xn is the joint discrete density function of_ ( _X_ 1 _, ..., Xn_ ) _. (v) (Positivity) If X ≥_ 0 _is a discrete random variable and_ E[ _X_ ] = 0 _, then X_ = 0 _almost surely._ 

- _Proof sketch._ (i) Follows directly from the definition. 

- (ii) For nonnegative _X, Y_ , linearity follows from rearrangement of absolutely convergent series. The general case follows by splitting into positive and negative parts. 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

58 

- (iii) If _X ≤ Y_ , then _Y − X ≥_ 0, so E[ _Y − X_ ] _≥_ 0, hence E[ _Y_ ] _≥_ E[ _X_ ]. 

- (iv) For nonnegative _g_ , the equality holds by Tonelli’s theorem for sums. For _g_ ( _X_ 1 _, . . . , Xn_ ) _∈ L_<sup>1</sup> , we use absolute convergence. 

- (v) If _X ≥_ 0 and E[ _X_ ] = 0, then for any _x >_ 0 in the range of _X_ , we must have P _{X_ = _x}_ = 0. 

The following proposition provides a useful method to compute the expected value of random variables valued in N. 

Alternative formula for expected value 

**Proposition 2.5.3.** _Let X be a discrete random variable defined on a probability space_ (Ω _, F,_ P) _, taking values in_ N _∪{∞}. Then:_ 



_Proof._ If P( _X_ = _∞_ ) _>_ 0 the equality is fulfilled. So, assume that P( _X_ = _∞_ ) = 0. By the definition of expected value for discrete random variables, we have: 



where the summation can start from _k_ = 1 since the term for _k_ = 0 is zero. We can rewrite the integer coefficient _k_ as a sum of units: 



Substituting this expression into the formula for the expected value, we obtain: 



Since all terms in the summation are non-negative, by Fubini’s theorem for series, we can swap the order of summation. The summation region in the ( _n, k_ ) plane is defined by the inequalities 1 _≤ n ≤ k < ∞_ . By changing the order, the region is described by 1 _≤ n < ∞_ and _n ≤ k < ∞_ : 



##### Variance (general discrete case) 

**Definition 2.5.4** (Variance) **.** _Let X ∈ L_<sup>1</sup> _be a discrete random variable. The_ variance _(finite or infinite) of X is defined as:_ 



_2.6. CONDITIONAL EXPECTED VALUE IN THE GENERAL DISCRETE CASE_ 

59 

Properties of variance 

**Proposition 2.5.5.** _Let X, Y ∈ L_<sup>1</sup> _be discrete random variables with finite variance._ 



_(ii) If X and Y are independent, then:_ 



_(iii)_ Var[ _X_ ] _≥_ 0 _, and_ Var[ _X_ ] = 0 _if and only if X is constant almost surely._ 

Markov and Chebyshev inequalities 

**Proposition 2.5.6.** _Let X be a discrete random variable._ 

_1. (_ **_Markov’s Inequality_** _) For any a >_ 0 _:_ 





_Proof._ 1. Fix _a >_ 0. Clearly we have the pointwise inequality: 



Taking the expectation on both sides: 



concluding. 

2. The event _{|X − m| ≥ ε}_ is equivalent to _{_ ( _X − m_ )<sup>2</sup> _≥ ε_<sup>2</sup> _}_ . Let _Y_ = ( _X − m_ )<sup>2</sup> and _a_ = _ε_<sup>2</sup> . Since _Y ≥_ 0, we can apply Markov’s inequality: 



concluding. 

### **2.6 Conditional expected value in the general discrete case** 

The concept of conditional expected value extends to the general discrete case with minor adjustments. The definitions and fundamental properties are analogous to those presented in Chapter 1 for finite spaces (Section 1.7). The proofs are essentially the same, replacing finite sums with numerical series when necessary. We therefore refer to the corresponding proofs in Chapter 1 for details. 

Throughout this section, let _Y_ : Ω _→ E_ be a discrete random variable. For each _y ∈ E_ with P _{Y_ = _y} >_ 0, the conditional probability P _{ · | Y_ = _y}_ is a well-defined probability measure, and we denote by E[ _· | Y_ = _y_ ] the expectation under this measure. 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

60 

Conditional expected value (given a random variable) 

**Definition 2.6.1.** _Let X_ : Ω _→_ R _be a discrete semi-integrable random variable. The_ conditional expected value of _X_ given _Y is the σ_ ( _Y_ ) _-measurable random variable_ 



As in the finite case, we often write E[ _X | Y_ ] for E[ _X | σ_ ( _Y_ )] and interpret it as the best approximation of _X_ based on the knowledge of _Y_ . 

The properties listed in Proposition 1.7.3 (Chapter 1) remain valid, with the same proofs once we replace finite sums by series. The only points that require extra care are those involving linearity and monotone convergence, where one must justify the interchange of sums. Since all sums are either over countable sets and involve non-negative terms (in the non-negative case) or are absolutely convergent (in the _L_<sup>1</sup> case), the standard theorems of summation theory (Tonelli and Fubini for series) legitimise all operations. 

Properties of conditional expected value 

**Proposition 2.6.2.** _Let X, Z be discrete random variables and Y a discrete random variable._ 

- _(i) (Linearity) If X, Z are semi-integrable and α, β ∈_ R _are such that αX_ + _βZ is semi-integrable, then_ 

   - E[ _αX_ + _βZ | Y_ ] = _α_ E[ _X | Y_ ] + _β_ E[ _Z | Y_ ] _._ 

- _(ii) (Constants) If X ≡ c ∈_ R _, then_ E[ _X | Y_ ] _≡ c._ 

- _(iii) (Independence) If X, Y are independent and X is semi-integrable, then_ E[ _X | Y_ ] _≡_ E[ _X_ ] _._ 

- _(iv) (Measurability) If X is σ_ ( _Y_ ) _-measurable, then_ E[ _X | Y_ ] = _X._ 

- _(v) (Tower property) If X ≥_ 0 _or X ∈ L_<sup>1</sup> _, then_ 

         - E�E[ _X | Y_ ]� = E[ _X_ ] _._ 

- _(vi) (Taking out what is known) If Z is σ_ ( _Y_ ) _-measurable and X is such that XZ is semi-integrable, then_ 

      - E[ _XZ | Y_ ] = _Z_ E[ _X | Y_ ] _._ 

- _(vii) (Monotonicity) If X ≤ Z a.s. and both are non-negative or in L_<sup>1</sup> _, then_ 

E[ _X | Y_ ] _≤_ E[ _Z | Y_ ] _._ 

- _(viii) (Conditional Jensen’s inequality) If ϕ_ : R _→_ R _is convex and X ∈ L_<sup>1</sup> _, then_ 



_2.6. CONDITIONAL EXPECTED VALUE IN THE GENERAL DISCRETE CASE_ 

61 

##### Freezing lemma 

**Proposition 2.6.3** (Freezing lemma) **.** _Let X_ : Ω _→ E and Y_ : Ω _→ E_<sup>_′_</sup> _be discrete random variables, and let ϕ_ : _E × E_<sup>_′_</sup> _→_ R _be a function. If either ϕ ≥_ 0 _or ϕ_ ( _X, Y_ ) _∈ L_<sup>1</sup> _, then the conditional expectation of ϕ_ ( _X, Y_ ) _given Y satisfies_ 



_Equivalently,_ 



##### Consequences and applications of the freezing lemma 

Let us see some important consequences of the freezing lemma. 

- (i) **Independent case:** When _X_ and _Y_ are independent, E[ _ϕ_ ( _X, y_ ) _| Y_ = _y_ ] = E[ _ϕ_ ( _X, y_ )] for every _y_ (provided the expectation exists). Hence 



- (ii) **Disintegration formula:** Taking the expectation on both sides of (2.6.1) and using the tower property gives the disintegration formula: 



If in addition _X_ and _Y_ are independent, this simplifies to 



- (iii) **Expectation of a product:** When _X_ and _Y_ are independent and _ϕ_ ( _x, y_ ) = _xy_ , the last formula yields 



provided _XY ∈ L_<sup>1</sup> . 

Example: Wald’s equation for random sums 

**Example 2.6.4.** _Let_ ( _Xi_ ) _i≥_ 1 _be a sequence of i.i.d. nonnegative discrete random variables with_ E[ _X_ 1] = _µ ∈_ [0 _,_ + _∞_ ] _. Let N be an_ N _-valued random variable independent of the sequence_ ( _Xi_ ) _. Define the random sum S as:_ 



_The result can be derived elegantly using the disintegration formula. By conditioning on the_ 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

62 

_random variable N , we compute the conditional expectation of S given the event {N_ = _n}:_ 



_Thus_ 

Example: Mean of the geometric distribution 

**Example 2.6.5.** _Let T be a random variable with the geometric distribution of parameter p ∈_ (0 _,_ 1) _; that is, T models the number of independent Bernoulli trials (with success probability p) needed to obtain the first success. We have already computed its distribution, given by_ 



_To compute_ E[ _T_ ] _we use conditioning on the outcome of the first trial. Let X_ 1 _be the indicator of success on the first trial: X_ 1 = 1 _if the first trial is a success, X_ 1 = 0 _otherwise. If the first trial succeeds, then clearly T_ = 1 _; if it fails, one trial is wasted and the process starts anew, so the remaining number of trials required has the same distribution as T . Hence_ 



_Applying the disintegration formula, we obtain_ 



_Now, considering the absence of memory, therefore that_ E[ _T −_ 1 _| T >_ 1] = E[ _T_ ] _, we have_ E[ _T | X_ 1 = 0] = E[ _T −_ 1 _| T >_ 1] + 1 = E[ _T_ ] + 1 _._ 

_Combining, we get_ 

E[ _T_ ] = _p_ + (1 _− p_ ) + (1 _− p_ )E[ _T_ ] = 1 + (1 _− p_ )E[ _T_ ] _. Hence, we conclude that_ 



### **2.7 Convergences** 

In the context of sequences of random variables, it is very important to have convergence notions and results. In the following (Ω _, F,_ P) is a given and fixed reference probability space. The real random variables we shall consider are intended to be valued in the extended set R and defined on (Ω _, F,_ P). 

#### **2.7.1 Three types of convergences for random variables** 

Let us provide the most common notions of convergence of real random variables. 

_2.7. CONVERGENCES_ 

63 

Types of convergence for real random variables 

**Definition 2.7.1.** _Let_ ( _Xn_ ) _n∈_ N _be a sequence of discrete real valued random variables and let X be another discrete real valued random variable. We say that_<sup>_a_</sup> 



_(iii) A sequence of random variables_ ( _Xn_ ) _converges_ in law _to X if_ 

> _a_ Notice that all the convergence notions we are introducing do depend on the chosen probability P. 

Pointwise convergence implies convergence in law 

**Proposition 2.7.2.** _Let_ ( _Xn_ ) _and X be discrete random variables valued in E ⊂_ R<sup>_a_</sup> _. If_ 



_then Xn converges to X in law._ 

> _a_ The fact that the a countable family of discrete random variables take values in the same countable set _E_ can be assumed without loss of generality. Indeed if _En_ is the countable range of _Xn_ , then the countable set _E_ :=<sup>�</sup> _n∈_ N<sup>_En_isthecommonrangeofthe</sup><sup>_Xn_’s.</sup> 

_Proof._ Assume that (2.7.1) holds true. Let _ϕ_ : R _→_ R be bounded and continuous, and set _M_ := sup _t∈_ R _|ϕ_ ( _t_ ) _| < ∞_ . Then 



Fix _ε >_ 0. Since<sup>�</sup> _x∈E_<sup>P</sup><sup>_{X_=</sup><sup>_x}_= 1,wecanchooseafiniteset</sup><sup>_F⊂E_suchthat</sup> 



Then, 

(i) From (2.7.1) and (2.7.2), 



Hence, there exists an integer _N_ such that for all _n ≥ N_ 

(ii) Since _F_ is finite, there exists an integer _N_ such that for all _n ≥ N_ and all _x ∈ F_ 



where _|F |_ denotes the cardinality of _F_ . 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

64 

Thus, taking the maximum between these _N_ ’s, we have for all _n ≥ N_ 



Since _ε >_ 0 was arbitrary, we conclude. 

Remark: Pointwise convergence of probability mass functions 

Proposition 2.7.2 shows that checking the pointwise condition (2.7.1) is a convenient way to verify convergence in law for discrete random variables. However, the converse is not true in general: convergence in law does not imply pointwise convergence of the probability mass functions. 

A simple counterexample is obtained by taking _Xn ≡_ 1 _/n_ and _X ≡_ 0 (all constant random variables). Then for every bounded continuous _ϕ_ , 



so _Xn → X_ in law. If we consider the common range _E_ = _{_ 0 _} ∪{_ 1 _/n_ : _n ≥_ 1 _}_ , we have P _{Xn_ = 0 _}_ = 0 for all _n_ while P _{X_ = 0 _}_ = 1; thus condition (2.7.1) fails for _x_ = 0. In practice, when dealing with discrete random variables, one often verifies convergence in law by establishing the pointwise limit (2.7.1). Only when (2.7.1) fails does one need to resort directly to the definition involving bounded continuous functions. 

Relationships between convergences 

**Proposition 2.7.3.** _Let_ ( _Xn_ ) _and X be discrete real random variables taking values in a countable set E ⊂_ R _. The following implications hold:_ 



_Proof._ **(a.s. convergence** _⇒_ **convergence in probability)** 

Assume _Xn → X_ almost surely. For any _ε >_ 0, we want to show that 



Define the sequence of events 



The sequence ( _Bk_ ) _k∈_ N is increasing. Moreover, since _Xn → X_ a.s., for a.e. _ω_ there exists an index _k_ ( _ω_ ) such that _|Xn_ ( _ω_ ) _− X_ ( _ω_ ) _| < ε_ for all _n ≥ k_ ( _ω_ ). Hence, lim _k→∞ Bk_ = Ωa.s. and, by the continuity of the probability measure for increasing sequences, we get 



_2.7. CONVERGENCES_ 

65 

**(convergence in probability** _⇒_ **convergence in law)** 

Assume _Xn → X_ in probability. Let _ϕ_ : R _→_ R be bounded and continuous, and set _M_ := sup _t∈_ R _|ϕ_ ( _t_ ) _| < ∞_ . Fix _ε >_ 0. Since _E_ is countable and<sup>�</sup> _x∈E_<sup>P</sup><sup>_{X_=</sup><sup>_x}_=1,there</sup> exists a finite set _F ⊂ E_ such that 



For each _x ∈ F_ , by continuity of _ϕ_ at _x_ , there exists _δx >_ 0 such that for every _y ∈_ R with _|y − x| < δx_ we have _|ϕ_ ( _y_ ) _− ϕ_ ( _x_ ) _| < ε_ . Define _δ_ := min _x∈F δx >_ 0. Consider the event 



Then, 



Now we estimate the probability of the complement: 



By convergence in probability, lim _n→∞_ P _{|Xn − X| ≥ δ}_ = 0. Hence, for all sufficiently large _n_ , 

P _{|Xn − X| ≥ δ} < ε._ 

Consequently, by (2.7.5) and the above inequality, for such _n_ we have 



Finally, using (2.7.6) and (2.7.7) 



Since _ε >_ 0 was arbitrary, we conclude. 

Counterexamples to the reverse implications 

The chain of implications 

a.s. convergence _⇒_ convergence in probability _⇒_ convergence in law 

cannot be reversed in general. 

**Convergence in law does not imply convergence in probability.** Consider the probability space Ω= _{a, b}_ with P _{a}_ = P _{b}_ = 1 _/_ 2. Define 



Then both _Xn_ and _X_ have the Bernoulli distribution with parameter 1 _/_ 2; hence _L_ ( _Xn_ ) = _L_ ( _X_ ) and trivially _Xn → X_ in law. However, 

P _{|Xn − X|_ = 1 _}_ = P _{a, b}_ = 1 for every _n,_ 

so _Xn_ does not converge to _X_ in probability. 

**Convergence in probability does not imply almost-sure convergence.** 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

66 

Consider the probability space ([0 _,_ 1] _, B_ ([0 _,_ 1]) _, λ_ ) where _λ_ denotes the Lebesgue measure. For _n ≥_ 1 and _k_ = 1 _, . . . , n_ , define the intervals _In,k_ = [<sup>_<u>k−</u>_</sup> _n_<sup><u>1</u></sup><sup>_,_</sup> _n_<sup>_<u>k</u>_].Enumerate</sup> these intervals in a single sequence _A_ 1 _, A_ 2 _, . . ._ (for instance, first all intervals with _n_ = 1, then with _n_ = 2, and so on). Set _Xn_ = **1** _An_ . For any _ε ∈_ (0 _,_ 1), 

P _{|Xn| ≥ ε} −→_ 0 _,_ 

hence _Xn →_ 0 in probability. Nevertheless, for every _ω ∈_ [0 _,_ 1] the point _ω_ belongs to infinitely many intervals _An_ ; therefore _Xn_ ( _ω_ ) = 1 for infinitely many _n_ , and the sequence ( _Xn_ ( _ω_ )) does not converge to 0. Thus _Xn_ does not converge to 0 almost surely. 

Example: From binomial to Poisson 

**Example 2.7.4** (From binomial to Poisson) **.** _Let α >_ 0 _. The sequence of laws B_ ( _n, α/n_ ) _, seen as probability laws on_ N _∪{∞}, converges to the Poisson law P_ ( _α_ ) _._ **_Proof:_** _Recall that_ 

_B_ ( _n, p_ ) _{k}_ = _p_<sup>_k_</sup> (1 _− p_ )<sup>_n−k_</sup> _, k_ = 0 _, ..., n._ � _nk_ � _Set bk_ ( _n_ ) := _B_ ( _n, α/n_ ) _{k}_ = 1 _−_<sup>_α_</sup> _, k_ = 0 _, ..., n._ � _nk_ �� _αn_ � _k_ � _n_ � _n−k For fixed k ∈_ N _, we compute:_ lim 1 _−_<sup>_α_</sup> _n→∞_<sup>_bk_(</sup><sup>_n_) =</sup> _n_<sup>lim</sup> _→∞_ <u>�</u> _nk_ <u>�</u> � _αn_ � _k_ � _n_ � _n−k_ = lim _n_ <u>(</u> _n −_ 1) _· · ·_ <u>(</u> _n − k_ + 1) _·_<sup>_αk_</sup> 1 _−_<sup>_α_</sup> _·_ 1 _−_<sup>_α_</sup> _n→∞ k_ ! _n_<sup>_k·_</sup> � _n_ � _n_ <u>�</u> _n_ � _−k n_ <u>(</u> _n −_ 1) _· · ·_ <u>(</u> _n − k_ + 1) =<sup>_αk_</sup> _·_ lim 1 _−_<sup>_α_</sup> _·_ lim 1 _−_<sup>_α_</sup> _k_ !<sup>_·_</sup> _n_<sup>lim</sup> _→∞ n_<sup>_k_</sup> _n→∞_ � _n_ � _n n→∞_ � _n_ � _−k_ =<sup>_α_</sup> _k_<sup>_k_</sup> !<sup>_·_1</sup><sup>_· e−α ·_1 =</sup><sup>_e−α α_</sup> _k_<sup>_k_</sup> !<sup>_._</sup> 

_Thus B_ ( _n, α/n_ ) _→P_ ( _α_ ) _in distribution._ 

#### **2.7.2 Mean convergence theorems** 

The main results concerning the passage to the limit of the expected value operator are the so called _Fatou’s lemma_ , the _monotone convergence theorem_ and the _dominated convergence theorem_ . We start with a characterization of the expected value of nonnegative discrete random variables in terms of random variables with finite range. 

Characterization of expectation for nonnegative discrete random variables 

**Lemma 2.7.5.** _Let X ≥_ 0 _be a discrete random variable. Then:_ E[ _X_ ] = sup _{_ E[ _Z_ ] : 0 _≤ Z ≤ X, Z discrete with finite range} ._ 

_Proof._ The inequality 



_2.7. CONVERGENCES_ 

67 

is clear by monotonicity of the expected value operator. 

Let us prove the other inequality by constructing a sequence of nonnegative random variables _X_<sup>(</sup><sup>_n_)</sup> with finite range such that E[ _X_<sup>(</sup><sup>_n_)</sup> ] _→_ E[ _X_ ]. Let _E_ = _{x_ 1 _, x_ 2 _, . . . }_ be the range of _X_ with 0 _≤ x_ 1 _< x_ 2 _< · · ·_ (we can order and enumerate since _E_ is countable). For each _n ≥_ 1, define the truncated variable: 



That is, _X_<sup>(</sup><sup>_n_)</sup> takes the value _xk_ if _X_ = _xk_ for some _k ≤ n_ and takes the value 0 otherwise. Then 

(i) _X_<sup>(</sup><sup>_n_)</sup> _≥_ 0 and _X_<sup>(</sup><sup>_n_)</sup> _≤ X_ , 

(ii) _X_<sup>(</sup><sup>_n_)</sup> has finite range: _{x_ 1 _, . . . , xn}_ , 

(iii) _X_<sup>(</sup><sup>_n_)</sup> _↑ X_ pointwise as _n →∞_ . 

Consider the sequence _{X_<sup>(</sup><sup>_n_)</sup> _}_ defined above. Since _X_<sup>(</sup><sup>_n_)</sup> _↑ X_ and _X_<sup>(</sup><sup>_n_)</sup> _≥_ 0, by the definition of expectation for nonnegative discrete random variables: 



Monotone convergence theorem 

**Theorem 2.7.6** (Monotone convergence theorem) **.** _Let_ ( _Xn_ ) _n∈_ N _be a sequence of discrete_ R _-valued random variables such that:_ 

_(i) Xn ≥_ 0 _for all n ∈_ N _; (ii) Xn ↑ X. Then:_ 



_Proof. Step 1: Upper bound._ Since _Xn ≤ X_ for every _n_ , monotonicity of expectation yields E[ _Xn_ ] _≤_ E[ _X_ ]. Consequently, 



_Step 2: Lower bound._ Recall Lemma 2.7.5. Fix an arbitrary _Z_ with finite range such that 0 _≤ Z ≤ X_ . We shall show that 



Since _Z_ is arbitrary taking the supremum over all such _Z_ and using Lemma 2.7.5 will provide 



Let _ε ∈_ (0 _,_ 1) and define the events 



Note that _Bn_ is an increasing sequence of sets. Now 

- (i) If _Z_ ( _ω_ ) = 0, then _ω ∈ Bn_ for all _n_ ; 

- (ii) If _Z_ ( _ω_ ) _>_ 0, then, since _Xn_ ( _ω_ ) _↑ X_ ( _ω_ ) _≥ Z_ ( _ω_ ) _>_ (1 _− ε_ ) _Z_ ( _ω_ ), there must exists _n_ 0( _ω_ ) such that _Xn_ ( _ω_ ) _≥_ (1 _− ε_ ) _Z_ ( _ω_ ) for all _n ≥ n_ 0( _ω_ ). 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

68 

Therefore, we have lim _n→∞ Bn_ = Ω(a.s.). On the other hand 



Taking expectations gives 



Write _Z_ in its canonical form _Z_ =<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_aj_</sup><sup>**1**</sup><sup>_A_</sup> _j_<sup>with</sup><sup>_aj≥_0andthe</sup><sup>_Aj_’sdisjoint.Then</sup> 



Since _Bn ↑_ Ω(a.s.), we have _Aj ∩ Bn ↑ Aj_ (a.s.), and by continuity of the probability measure, 



Therefore 



Passing to lim inf in (2.7.9) and using (2.7.10) yields 



The inequality holds for every _ε ∈_ (0 _,_ 1); letting _ε →_ 0<sup>+</sup> we obtain (2.7.8). 

##### Remark: Weakened monotonicity condition 

**Remark 2.7.7.** _The condition Xn ≥_ 0 _can be weakened. If there exists a random variable Y ∈ L_<sup>1</sup> _such that Xn ≥ Y for all n, then the theorem still holds. Indeed, consider X_<sup>�</sup> _n_ = _Xn − Y ≥_ 0 _. Then X_<sup>�</sup> _n ↑ X − Y , and by the monotone convergence theorem:_ 



_Since_ E[ _Y_ ] _is finite, we obtain:_ 



_Thus, it suffices that the sequence_ ( _Xn_ ) _is bounded from below by an integrable random variable._ 

##### Corollary: Expectation of infinite sums 

**Corollary 2.7.8.** _Let_ ( _Xn_ ) _n∈_ N _be a sequence of_ [0 _,_ + _∞_ ] _-valued discrete random variables. Then_ 



_Proof._ Define _SN_ =<sup>�</sup><sup>_N_</sup> _n_ =0<sup>_Xn_.Then</sup><sup>_SN↑S_:=�</sup> _n∈_ N<sup>_Xn_almostsurely.Bythemonotone</sup> convergence theorem: 



_2.7. CONVERGENCES_ 

69 

Fatou’s lemma 

**Lemma 2.7.9** (Fatou’s lemma) **.** _Let_ ( _Xn_ ) _n∈_ N _be a sequence of discrete_ R _-valued random variables such that Xn ≥ Z for all n, where Z ∈ L_<sup>1</sup> _. Then:_ 



_Proof._ Define _Yn_ = inf _k≥n Xk_ . Then: 





By the monotone convergence theorem (with the weakened condition from the remark above): 



Since _Yn ≤ Xn_ for all _n_ , we have E[ _Yn_ ] _≤_ E[ _Xn_ ], and thus: 



Combining the two inequalities gives the result. 

Dominated convergence theorem 

**Theorem 2.7.10** (Dominated convergence theorem) **.** _Let_ ( _Xn_ ) _n∈_ N _be a sequence of discrete_ R _-valued random variables such that:_ 

_(i) Xn → X;_ 

_(ii) There exists G ∈ L_<sup>1</sup> _such that |Xn| ≤ G for all n. Then X ∈ L_<sup>1</sup> _and:_ 



_Proof._ Since _|Xn| ≤ G_ and _Xn → X_ , we have _|X| ≤ G_ a.s., therefore _X ∈ L_<sup>1</sup> . Moreover, _|Xn − X| ≤_ 2 _G ∈ L_<sup>1</sup> . Apply Fatou’s lemma to the sequence 2 _G −|Xn − X| ≥_ 0: 



Thus lim sup _n→∞_ E[ _|Xn − X|_ ] _≤_ 0, so E[ _|Xn − X|_ ] _→_ 0. For the convergence of expectations, note that: 



_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

70 

Remark on _L_<sup>1</sup> convergence 

We have shown more, that is E[ _|Xn − X|_ ] _→_ 0. This is expressed by saying that _Xn → X_ in _L_<sup>1</sup> . 

Conditional versions of convergence theorems 

**Theorem 2.7.11.** _Let Y_ : Ω _→ E_<sup>_′_</sup> _be a discrete random variable. The following hold for sequences of discrete real random variables on_ (Ω _, F,_ P) _:_ 

- _(i)_ **_Conditional monotone convergence theorem:_** _If_ 0 _≤ Xn ↑ X almost surely, then_ 



_(ii)_ **_Conditional Fatou’s lemma_** _: If Xn ≥_ 0 _almost surely for all n, then_ 



_(iii)_ **_Conditional dominated convergence theorem_** _: If Xn → X almost surely and there exists Z ∈ L_<sup>1</sup> _such that |Xn| ≤ Z a.s. for all n, then_ 



_Proof._ (Sketch) Since _Y_ is discrete, the conditional expectations given _Y_ are constant on each set _{Y_ = _y}_ . For every _y ∈ E_ with P _{Y_ = _y} >_ 0, consider the conditional probability P _y_ and apply the ordinary monotone convergence, Fatou, and dominated convergence theorems. This yields the limits for E _y_ [ _Xn_ ]. Since E[ _Xn | Y_ ] =<sup>�</sup> _y∈E_<sup>_′_E</sup><sup>_y_[</sup><sup>_Xn_]</sup><sup>**1**</sup><sup>_{Y_=</sup><sup>_y}_,thestatementsfollow.</sup> 

### **2.8 The law of large numbers** 

One of the most celebrated results in probability is the so called law of large numbers. There are various version of this result, depending on the assumptions. In any case, roughly speaking it states that, under certain conditions, 

- _“the empirical mean of a sequence of identically distributed random variables converges (in a suitable sense) to their common expectation”_ . 

##### Weak law of large numbers 

**Theorem 2.8.1** (Weak law of large numbers) **.** _Let_ ( _Xn_ ) _n∈_ N0 _be an i.i.d. sequence of discrete real valued random variables such that_ E[ _X_ 1<sup>2]</sup><sup>_< ∞(so that, in particular, X_1</sup><sup>_∈L_1</sup><sup>_)._</sup> _Set_ 





_Proof._ Let _σ_<sup>2</sup> := Var[ _X_ 1]. Since the _Xi_ are i.i.d., we have: 



_2.8. THE LAW OF LARGE NUMBERS_ 

71 

By Chebyshev’s inequality, for any _ε >_ 0: 



Thus<sup>_<u>S</u>_</sup> _n_<sup>_<u>n</u>→m_inprobability.</sup> 

##### Strong law of large numbers 

**Theorem 2.8.2** (Borel’s strong law of large numbers) **.** _Let_ ( _Xn_ ) _n∈_ N0 _be an i.i.d. sequence of discrete real valued and bounded random variables, i.e., there exists a constant C >_ 0 _such that_ 

_Set Then,_ 



_Proof._ Without loss of generality, we may assume _m_ = 0 (otherwise consider _Xn − m_ ). Rescale so that _|Xn| ≤_ 1. We compute: 



By independence and E[ _Xi_ ] = 0, the only nonzero terms are: 







Now consider: 



Remarks on the law of large numbers 

- (i) The boundedness assumption in Borel’s theorem can be weakened. With more sophisticated techniques, one can prove Kolmogorov’s strong law of large numbers which only requires E[ _|X_ 1 _|_ ] _< ∞_ . 

> 3Obtained as = _n_ ( _n−_ 1) _/_ 2 choices of two indices _i, j_ from a set of _n_ indices times = 6 arrangements <u>�</u> _n_ 2 <u>�</u> � 24 � 

> of the chosen indices: explicitly, ( _i, i, j, j_ ) _,_ ( _i, j, i, j_ ) _,_ ( _i, j, j, i_ ) _,_ ( _j, i, i, j_ ) _,_ ( _j, i, j, i_ ) _,_ ( _j, j, i, i_ ). 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

72 

- (ii) The condition E[ _X_ 1<sup>2]</sup><sup>_< ∞_in the weak law can also be weakened to E[</sup><sup>_|X_1</sup><sup>_|_]</sup><sup>_< ∞_using</sup> truncation arguments. 

- (iii) (DA RIVEDERE O ELIMINARE) As pointed out in [9], it is fundamental to avoid a common logical circularity regarding the frequentist interpretation of Probability Theory. 

The mistake: Defining the probability P( _A_ ) as the limit of the relative frequency _fn_ ( _A_ ). If P( _A_ ) were defined this way, the Law of Large Numbers would be a tautology (a definition disguised as a theorem). 

The correct view: Within the Kolmogorov axiomatic framework, probability is a primitive measure assigned _a priori_ . The Law of Large Numbers is then a mathematical consequence of these axioms. 

The Law of Large Numbers _does not prove_ that the frequency converges to probability by necessity of nature; rather, it ensures _internal consistency_ of the model. It guarantees that, if we accept the axioms and the parameters are properly chosen, then the observed realization — the empirical mean — will align with the predicted one — the theoretical mean. 

As [9] suggests, the Law of Large Numbers provides the bridge that allows us to use the model to describe the real world, justifying the frequentist intuition without making it a rigid (and logically flawed) definition. 

### **2.9 Selected exercises** 

In this section, we propose a list of exercises, selected from the book G. Letta [10]. 

Exercise 1 

Model the following problem and solve it. Consider a sequence of tosses of a fair coin, with sides labeled by 0 _,_ 1. 

- (a) What is the probability of getting 1 for the first time in an odd toss? 

- (b) Let _A ⊆_ N0 and let _pA_ the probability of getting 1 for the first time in a toss of index belonging to _A_ . Is it possible to choose _A_ such that _pA_ = 15 _/_ 16? Possibly, exhibit such a set _A_ . Possibly, exhibit two of these sets _A_ . 

- (c) More generally, given any _x ∈_ [0 _,_ 1], is it possible to choose _A ⊆_ N0 such that the probability of getting 1 for the first time in a toss of index belonging to _A_ is _x_ ? 

**Solution.** We may associate to the described random experiment the Bernoulli scheme of Corollary 2.4, with given law _µ_ = _B_ (1 _/_ 2). So let ( _Xn_ ) _n∈_ N0 be a sequence of i.i.d. random variables, valued in _{_ 0 _,_ 1 _}_ , defined on a probability space (Ω _, F,_ P), such that _L_ ( _Xn_ ) = _B_ (1 _/_ 2). Denote by _T_ the random variable representing the first success time of the process ( _Xn_ ), i.e. 



We know that _T_ has geometric law of parameter 1 _/_ 2 (cf. Section 2.4.1), so that 



_2.9. SELECTED EXERCISES_ 

73 

- (a) Denoting by _D_ the set of odd numbers, considering (2.9.1), the required probability is 



- (b) Arguing as in item (a), we need to find _A ⊆_ N0 such that 



This can be obtained in several ways: for instance, taking _A_ = _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ or _A_ = N0 _\ {_ 4 _}_ . 

- (c) Given _x ∈_ [0 _,_ 1], we may consider its binary representation ( _xn_ ) _n∈_ N0, with ( _xn_ ) sequence valued in _{_ 0 _,_ 1 _}_ . Then, taking _A_ = _{n ∈_ N0 : _xn_ = 1 _}_ , we have 



##### Exercise 2 

Two players, say Player (A) and Player (B), play a sequence of rounds of a game as follows. There are two urns, each one containing _r_ red balls and _b_ black balls. At each round, Player (A) extracts a ball from her urn and replaces it. Similarly does Player (B). The game stops at the first round in which there is a different result in the extractions of the two players. In this case, the player who extracted the red ball wins 1 Euro. 

- (a) Define, on a suitable probability space (Ω _, F,_ P), two random variables _N, V_ representing, respectively, the number of rounds played and the amount won by (A). 

- (b) Determine the law of _N_ , the law of _V_ , and say if they are independent. 

**Solution.** To simplify the formalism, we may imagine that the game goes on without ending, but considering not valid the rounds after the first round when different outcomes occur. Then, in the usual way, we may construct a probability space (Ω _, F,_ P) and an i.i.d. sequence of random variables 



such that _L_ ( _Xn_ ) = _L_ ( _Yn_ ) = _B_ ( _r/_ ( _r_ + _b_ )). We read the event _{Xn_ = 1 _}_ (respectively, _{Yn_ = 1 _}_ ) as the event expressed in words as “Player (A) (resp., Player (B)) extracted a red ball at the round _n_ ”. 

- (a) We define the sequence 



Clearly, this is still an i.i.d. sequence of Bernoulli random variables of parameter 



Then, _N_ can be defined as the first success time of the process ( _Zn_ ), i.e. 



Then, _V_ can be defined as the random variable<sup>4</sup> 



- 4Notice that _{N_ = _∞}_ is negligible. 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

74 

- 2 _rb_ 

- (b) The law of _N_ is the geometric law of parameter ( _r_ + _b_ )<sup>2.Wewillcomputethelawof</sup><sup>_V_and</sup> show that it is independent of _N_ at the same time. Clearly, by symmetry, given _n ≥_ 1, we have 



This is as to say that 



which means that the law of _V_ is _B_ (1 _/_ 2) and that it is independent of _N_ . 

Exercise 3 

Let _T_ 1 and _T_ 2 be the random variables representing, respectively, the first success time and the second success time of a Bernoulli scheme of parameter _p ∈_ (0 _,_ 1) given on a probability space (Ω _, F,_ P). Set 



where _N ≥_ 2 is fixed. Determine the law of _T_ 1 under Q. 

**Solution.** Notice that, by definition, Q _{T_ 2 = _N }_ = 1. On the Q-sure event _{T_ 2 = _N }_ , the random variable _T_ 1 takes values in the set _{_ 1 _, ..., N −_ 1 _}_ . We are going to show that 



is constant. As a consequence, under Q, the r.v. _T_ 1 is uniformly distributed on _{_ 1 _, ..., N −_ 1 _}_ . Multiplying by P _{T_ 2 = _N }_ , we need to show that 



is constant. Notice that 



The probability of the event in the right hand side is clearly equal to _p_<sup>2</sup> (1 _− p_ )<sup>_N−_2</sup> and does not depend on _k_ , concluding. 

_2.9. SELECTED EXERCISES_ 

75 

Exercise 4 

Given _k, n ∈_ N0 such that 1 _≤ k ≤ n_ , consider the following random experiment. From an urn, containing _n_ balls labeled by 1 _, ..., n_ , one extracts _k_ balls without replacement. 

- (a) Define, on a suitable probability space (Ω _, F,_ P) this random experiment. 

- (b) In this space, define, for each _i_ = 1 _, ..., k_ , a random variable _Xi_ representing the _i_ -th extraction and compute its law. 

- (c) Given an integer _x ∈{_ 1 _, ..., n}_ , compute the probability that _x_ is extracted. 

- (d) Given _i, j ∈{_ 1 _, ..., k}_ , and _x ∈{_ 1 _, ..., n}_ , compute the law of _Xj_ under 



- (e) Compute the law of the couple ( _Xi, Xj_ ) for _i, j ∈{_ 1 _, ..., k}_ and _i̸_ = _j_ . Is _Xi_ independent of _Xj_ ? 

- (f) What is the probability that both _x_ and _y_ are extracted? 

- (g) What is the probability that at least one between _x_ and _y_ is extracted? 

- (h) What is the probability that one and only one between _x_ and _y_ is extracted? 

_Hint._ For (a), consider as Ωthe space 



##### **Solution.** 

- (a) Let _I_ = _{_ 1 _, ..., n}_ . We consider as probability space 



with the uniform probability (for reasons of symmetry). Since _|_ Ω _|_ = _n_ ( _n −_ 1) _· · ·_ ( _n − k_ + 1) _,_ we have 

P _{ω}_ = � _n_ ( _n −_ 1) _· · ·_ ( _n − k_ + 1)� _−_ 1 _, ∀ω ∈_ Ω _._ extraction, for _i_ = 1 _, ..., k_ , through the random i.e. _Xi_ ( _ω_ ) := _ω_ ( _i_ ) _._ 

- (b) We describe the _i_ -th extraction, for _i_ = 1 _, ..., k_ , through the random variable _Xi_ defined as the canonical projection, i.e. 

To compute the law of _Xi_ , let _x, y ∈ I_ , and notice that the events _{Xi_ = _x}_ and _{Xi_ = _y}_ have the same cardinality. This means that the law of _Xi_ is the uniform distribution in _I_ , i.e. 



- (c) The event expressed by the words “ _x_ is extracted” corresponds formally to 



The events _{Xi_ = _x}_ , _i_ = 1 _, ..., k_ , are disjoints, so that, taking account also of item (b), 



_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

76 

- (d) Clearly, for _i̸_ = _j_ , 



By reasons of symmetry, under P( _· | Xi_ = _x_ ) the distribution of _Xj_ is the uniform distribution on _I \ {x}_ , i.e. 



- (e) Clearly _Xi_ is not independent of _Xj_ (see items above). Let us compute the law of ( _Xi, Xj_ ). Given _x, y ∈ I_ , we have, according to the results of the previous items, 



(f) Set 



We need to compute P( _A ∩ B_ ). We have 



The events in the union above are disjoint, their probability is 1 _/_ [ _n_ ( _n −_ 1)] (see the previous item) and are in number of _k_ ( _k −_ 1) (ordered choice of two elements in the set _{_ 1 _, ..., k}_ ), thus 



- (g) In this case, we need to compute, with the notation of the previous item, P( _A ∪ B_ ). We have 



- (h) Again with the notation of the previous two items, we need to compute 



##### Exercise 5 

On a probability space (Ω _, F,_ P), let a sequence 



of independent random variables such that _N_ has Poisson law of parameter _λ_ and each _Xi_ has Bernoulli law of parameter _p ∈_ (0 _,_ 1) be given. Set 



Then, let 



- (a) Determine the law of _SN_ . 

- (b) Determine the law of _N − SN_ . 

- (c) Are _N_ and _N − SN_ independent? 

_2.9. SELECTED EXERCISES_ 

77 

##### **Solution.** 

(a) We use the disintegration formula. For _k ≥_ 0, 



since _Sn_ is independent of _N_ . Now _Sn ∼B_ ( _n, p_ ), so 



Thus 



Hence _SN ∼P_ ( _λp_ ). 

(b) Note that _N − SN_ =<sup>�</sup><sup>_N_</sup> _i_ =1<sup>(1</sup><sup>_−Xi_).Since1</sup><sup>_−Xi∼B_(1</sup><sup>_,_1</sup><sup>_−p_)andthe</sup><sup>_Xi_arei.i.d.,thesame</sup> computation as in (a) shows that _N − SN ∼P_ ( _λ_ (1 _− p_ )). 

(c) To check independence, we compute the joint probability generating function. For _u, v >_ 0, 



where we used that E[ _u_<sup>_SN_</sup> ] = exp( _λp_ ( _u −_ 1)) and E[ _v_<sup>_N−SN_</sup> ] = exp( _λ_ (1 _− p_ )( _v −_ 1)). Hence _SN_ and _N − SN_ are independent. Since _N_ = _SN_ + ( _N − SN_ ), knowing _SN_ determines _N_ up to the independent increment _N −SN_ , but _N_ itself is not independent of _SN_ (nor of _N −SN_ ). In fact, _N_ and _N − SN_ are not independent because Var[ _N_ ] = _λ_ while Var[ _N − SN_ ] = _λ_ (1 _− p_ ), and Cov( _N, N − SN_ ) = Var[ _N − SN_ ] _̸_ = 0 in general. 

_CHAPTER 2. THE DISCRETE CASE: FROM FINITE TO COUNTABLE_ 

78 

Exercise 6 

Consider a sequence of tosses of a coin labeled on _{_ 0 _,_ 1 _}_ such that the probability of getting 1 at each toss is _p ∈_ (0 _,_ 1). Assume that a dealer accepts bettings according to the following rule: at each toss, the player wins the amount bet if 1 occurs in the toss, otherwise she loses such amount. 

Imagine now that a player, endowed with an initial amount of 1023 Euro, employs the following betting strategy: in the first toss, she will bet 1 Euro; if she wins, she will leave the game, otherwise, she will double the betting (2 Euro) in the second toss; and so on, until, possibly, she loses all the capital. 

- (a) Verify that the wealth of the gamer is 0 after 10 (unlucky) tosses all giving outcome 0; otherwise it will be 1024 Euro. 

- (b) Compute the expected value of the duration of the game. 

##### **Solution.** 

- (a) The player bets according to the doubling strategy. Let _Bn_ = 2<sup>_n−_1</sup> be the bet at toss _n_ , for _n_ = 1 _,_ 2 _, . . . ,_ 10. The total capital used after _n_ consecutive losses is 



After 10 consecutive losses, the total loss is 2<sup>10</sup> _−_ 1 = 1023 Euro, exhausting the initial capital. If the player wins at toss _n ≤_ 10, her net gain is 



Thus her final wealth becomes 1023 + 1 = 1024 Euro. If she never wins within the first 10 tosses, she is ruined. 

- (b) Let _T_ be the duration of the game. The player stops either at the first success or after 10 consecutive failures. Thus _T_ takes values in _{_ 1 _,_ 2 _, . . . ,_ 10 _}_ . For 1 _≤ n ≤_ 9, 



For _n_ = 10, 



Hence 



where we used the formula 



with _q_ = 1 _− p_ , _N_ = 9. The expression simplifies to 



## **Chapter 3** 

# **Stochastic processes in discrete time** 

Let us introduce the concept of stochastic process in discrete time. Stochastic processes are mathematical objects aiming at describing the evolution (in time) of random phenomena. First of all, one needs to specify the set of times one deals with. As anticipated, we will deal with discrete time sets. Without loss of generality, the running index of time can be identified by a subset of the natural numbers. Also, it is natural to start from the very first natural number _n_ = 0 as first index and do not skip any natural number in the list. In other term it is natural to consider as set of times 



or 

_N_ = N (infinite horizon case) _._ 

We set 



With this notation, we read the index _n ∈N_ as a discrete time index. 

### **3.1 Notion of stochastic process** 

In what follows, (Ω _, F,_ P) will be a given and fixed probability space. As for the arrival spaces _E_ of the random maps, they will be considered at most countable and endowed with the discrete _σ_ -algebra _E_ = 2<sup>_E_</sup> . 

**Definition 3.1.1.** _An E-valued stochastic process (indexed in n ∈N ) is a family X_ = ( _Xn_ ) _n∈N of random variables Xn_ : Ω _→ E._ 

If _X_ = ( _Xn_ ) _n∈N_ is an _E_ -valued stochastic process, we should think of the sequence _X_ = ( _Xn_ ) _n∈N_ as the random realization of subsequent random variables in time. Then, for a fixed _ω ∈_ Ω, the object 



is called a _trajectory of the stochastic process X_ . 

### **3.2 Filtration as information structure** 

We want to endow the model above with an information structure reflecting the fact that, when time goes on, the individual reads what happens. To be a bit more precise, we have to imagine that the individual “reads” the realizations of an _E_<sup>_′_</sup> -values stochastic process _ξ_ = ( _ξn_ ) _n∈N_ when time goes on: i.e., at time _n ∈N_<sup>0</sup> , she/he knows the values of _ξ_ 0( _ω_ ) _, ..., ξn_ ( _ω_ ). Then, letting _X_ be 

79 

_CHAPTER 3. STOCHASTIC PROCESSES IN DISCRETE TIME_ 

80 

another random variable defined on the same probability space, the knowledge of _ξ_ 0( _ω_ ) _, ..., ξn_ ( _ω_ ) may modify the individual confidence on the outcomes of _X_ . To formalise this idea, we introduce the notion of filtration generated by _ξ_ on the probability space. We define 



where the right handside denotes the _σ_ -algebra generated by the random variables _ξ_ 0 _, ..., ξn_ — i.e., the minimal _σ_ -algebra making the random variables _ξ_ 0 _, ..., ξn_ measurable. Clearly, this is an increasing sequence of _σ_ -algebra, in the sense that, for each _n ∈N_<sup>_o_</sup> , 



If _N_ = N, we set also 



In this case, we have 



**Definition 3.2.1** (Filtration generated by a stochastic process) **.** _The sequence of σ-algebra defined in_ (3.2.1) _is denoted in a compact way by_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_,andcalledthe_filtrationgeneratedby</sup> the stochastic process _ξ or_ the natural filtration of the stochastic process _ξ._ □ 

**Remark 3.2.2.** _In our setting, we deal with filtrations_ generated by stochastic processes _. One can disengage the notion of filtration from stochastic processes and just define it as an increasing sequence of σ-algebra. This turns out to be useful, but we skip this approach as it is not needed for our scopes._ 

**Definition 3.2.3** (Adapted process) **.** _Let X_ = ( _Xn_ ) _n∈N be stochastic process and let ξ_ = ( _ξn_ ) _n∈N be another stochastic process. We say that X is adapted with respect to the filtration generated by ξ if Xn is Fn_<sup>_ξ-measurableforalln ∈N._</sup> □ 

Very often, as underlying reference filtration one considers the filtration generated by the process _X_ under study itself, i.e. _F_<sup>_X_</sup> ; this is the so called _natural filtration of the process X_ . Clearly, the process is adapted to its natural filtration by construction. 

### **3.3 Stopping times and hitting times** 

In the framework of stochastic processes, an important notion is the one of _stopping time_ . It encodes the idea of random times that whose occurrence can be established without forward looking in the future. 

**Definition 3.3.1** (Stopping time) **.** _Let ξ_ = ( _ξn_ ) _n∈N be a stochastic process valued in some discrete space. A random variable τ_ : Ω _→N ∪{∞} is called a_ stopping time _(with respect to the filtration_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_)if_</sup> 



Interpreting _Fn_<sup>_ξ_astheinformationavailabletilltime</sup><sup>_n_and</sup><sup>_τ_asthetimeoftheoccurrence</sup> of some phenomenon (within the given probabilistic framework), saying that _τ_ is a stopping time means that at each time _n_ an individual who read the current information _Fn_<sup>_ξ_cansayifeither</sup> this phenomenon has already occurred or not. Notice that the definition refers to a given filtration. 

**Exercise 3.3.2.** _Show that τ is a stopping time if and only if {τ_ = _n} ∈Fn_<sup>_ξforalln ∈N._</sup> 

Typical examples of stopping times are so called entry or hitting times. 

_3.4. EXERCISES_ 

81 

**Definition 3.3.3.** _Let ξ_ = ( _ξn_ ) _n∈N be a stochastic process valued in some discrete space and let X_ = ( _Xn_ ) _n∈N be a stochastic process valued in some discrete space E and adapted to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_._</sup> _Given A ⊆ E, the_ hitting time _or the_ entry time _of the process in the set A is the random variable_ 



_with the convention_ inf _∅_ = _∞._ 

Entry times are stopping times (check it!). Let us see in an example what is not a stopping time. 

**Example 3.3.4.** _Let N < ∞ and let X_ = ( _Xn_ ) _n∈N be a stochastic process valued in a discrete set E ⊂_ R _and adapted to a reference filtration_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_.Considertherandomvariable_</sup> 



_and define_ 



_Then, τ is not (in general), a stopping time with respect to the filtration generated by X. Indeed_<sup>1</sup> _, to determine whether the current time n is the instant at which the process attains its global maximum over the entire horizon {_ 0 _, . . . , N }, one would require knowledge of the future realizations of the process. Consequently, the decision depends on future information, and thus τ cannot be a stopping time._ 

**Definition 3.3.5** (Stopped process) **.** _Let ξ_ = ( _ξn_ ) _n∈N be a stochastic process valued in some discrete space and let X_ = ( _Xn_ ) _n∈N be a stochastic process valued in some discrete space E and adapted to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_andletτbeastoppingtime.TheprocessXstoppedatτistheprocess_</sup> 







**Proposition 3.3.6.** _If X is adapted to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_,alsoXτisadaptedto_(</sup><sup>_F_</sup> _n_<sup>_ξ_)</sup> _n∈N_<sup>_._</sup> 

_Proof._ For _n ∈N_ and _A ∈Fn_<sup>_ξ_,</sup> 



the claim. 

### **3.4 Exercises** 

**Exercise 3.4.1** (Minimum of stopping times) **.** _Let τ_ 1 _and τ_ 2 _be two stopping times with respect to the same filtration_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_.Provethatτ_= min(</sup><sup>_τ_</sup> 1<sup>_, τ_</sup> 2<sup>)</sup><sup>_isalsoastoppingtime._</sup> 

> 1This is only a heuristic explanation. 

> 2The space _E_ does not have an algebraic structure; so the expression _Xn_ **1** _{τ>n}_ + _Xτ_ **1** _{τ ≤n}_ should be read as 



_CHAPTER 3. STOCHASTIC PROCESSES IN DISCRETE TIME_ 

82 

_Solution._ By definition, _τ_ is a stopping time if _{τ ≤ n} ∈Fn_<sup>_ξ_forevery</sup><sup>_n ∈N_.Observethatthe</sup> minimum of two numbers is less than or equal to _n_ if and only if at least one of them is less than or equal to _n_ . Formally: 



Since _τ_ 1 and _τ_ 2 are stopping times, we know that _{τ_ 1 _≤ n} ∈Fn_<sup>_ξ_and</sup><sup>_{τ_</sup> 2<sup>_≤n}∈F_</sup> _n_<sup>_ξ_.Given</sup> that the _σ_ -algebra _Fn_<sup>_ξ_isclosedunderfiniteunions,itfollowsthat</sup><sup>_{τ≤n}∈F_</sup> _n_<sup>_ξ_.Thus,</sup><sup>_τ_isa</sup> stopping time. 

**Exercise 3.4.2** (Last exit time) **.** _Let X be an adapted process and let A ⊂ E. We define LA_ = sup _{n ∈N_ : _Xn ∈ A} as the last time the process visits the set A (with the convention_ sup _∅_ = 0 _). Explain why, in general, LA is not a stopping time._ 

_Solution._ To determine whether the event _{LA_ = _n}_ has occurred, we would need to know not only that _Xn ∈ A_ , but also that for all future times _k > n_ , the process _Xk_ does not return to _A_ . Mathematically: 



The event _{Xn_ +1 _∈/ A, Xn_ +2 _∈/ A, . . . }_ depends on future realizations of the process, which are not contained in the _σ_ -algebra _Fn_<sup>_ξ_(which only contains information up to time</sup><sup>_n_).Consequently,</sup> _LA_ requires “looking into the future” and cannot be a stopping time. 

**Exercise 3.4.3** (Atoms of a filtration) **.** _Let ξ_ = ( _ξn_ ) _n∈_ N _be a sequence of independent and identically distributed (i.i.d.) random variables representing a coin toss, i.e., ξn ∈{_ 0 _,_ 1 _} with_ P( _ξn_ = 1) = _p. Explicitly describe the atoms of the σ-algebra F_ 1<sup>_ξ_=</sup><sup>_σ_(</sup><sup>_ξ_0</sup><sup>_, ξ_1)</sup><sup>_._</sup> 

_Solution._ The atoms of a _σ_ -algebra generated by discrete random variables are the elementary events that provide the maximum possible information. In this case, _F_ 1<sup>_ξ_isgeneratedby</sup><sup>_ξ_0and</sup> _ξ_ 1. Since each _ξi_ can take 2 values, the sample space can be partitioned into 2<sup>2</sup> = 4 disjoint elementary events (atoms): 







Every element of _F_ 1<sup>_ξ_isaunionoftheseatoms.</sup> 

**Exercise 3.4.4** (Algebra of Stopping Times) **.** _Let τ_ 1 _and τ_ 2 _be two stopping times with respect to a filtration_ ( _Fn_ ) _n∈N . Prove that τ_ = _τ_ 1 + _τ_ 2 _is also a stopping time._ 

_Solution._ We need to show that _{τ_ 1 + _τ_ 2 = _n} ∈Fn_ for every _n ∈N_ . We can decompose the event as follows: 



For each _k ∈{_ 0 _, . . . , n}_ , we have: 





The intersection of two events in _Fn_ is still in _Fn_ , and their finite union across _k_ remains in _Fn_ . Therefore, _τ_ 1 + _τ_ 2 is a stopping time. 

## **Chapter 4** 

# **Martingales** 

In this chapter (Ω _, F,_ P) is a given and fixed reference probability space. When not explicitly stated, _ξ_ = ( _ξ_ ) _n∈N_ will be a stochastic process defined on this probability space and ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>the</sup> filtration generated by _ξ_ . 

### **4.1 Notion of martingale** 

We introduce a very important notion in the theory of stochastic processes, i.e., the notion of _martingale_ . 

**Definition 4.1.1.** _Let X_ = ( _Xn_ ) _n∈N be a real valued stochastic process X adapted to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_._</sup> _We say that X_ submartingale _(resp., a_ supermartingale _) with respect to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_if_</sup> 

- _(i) Xn ∈ L_<sup>1</sup> _for all n ∈N ;_ 

_(ii) the following ineequality holds true:_ 



_It is said a_ martingale _if the equality holds, i.e._ 



Let us give an interpretation to the definition above. Assume that _X_ = ( _Xn_ ) _n∈N_ represents the position of an individual position in a game<sup>1</sup> . Recalling the interpretation of conditional expected value and that the fact that _X_ is a submartingale martingale says that, sitting at time _n ∈N_<sup>0</sup> and asking ourselves what we expect about our position _Xn_ +1 at the next date _n_ + 1 _given the available knowledge Fn_<sup>_ξ_theresultismorethan</sup><sup>_X_</sup> _n_<sup>,soweareplayingafavorablegame.</sup> Similarly, in the supermartingale case, we are playing an unfavorable game and in the martingale case, we are playing a fair game. 

##### **Remark 4.1.2.** 

- _(i) Notice that the definitions depend on the filtration and on the probability_ P _: both them play a role in the definition. In particular, to stress the dependence on the probability, when needed (and it will be in the next chapters), we will say that the process is a_ P _-martingale._ □ 

- _(ii) According to Remark 3.2.2, one may define the concept of (sub/super)martingale_ with respect to a given reference filtration _, not necessarily generated by a stochastic process. However, as we said in the previous chapter, for our purposes we can always restrict ourselves to consider a filtration generated by the stochastic process ξ. Often ξ_ = _X and we just say that X is a (sub/super)martingale (meaning: with respect to the natural filtration)._ □ 

> 1Where, by game, here we may mean whatever: cards game, lotteries, roulette, financial trading, etc.. 

83 

_CHAPTER 4. MARTINGALES_ 

84 

Let us see three important examples of martingales. 

**Example 4.1.3** (Random walks with independent increments) **.** _Let ξ_ = ( _ξn_ ) _n∈N ⊂ L_<sup>1</sup> _be a sequence of independent random variables such that_ E[ _ξn_ ] = 0 _for every n_ = 1 _, ..., N . Let X_ 0 _∈ L_<sup>1</sup> _be an assigned F_ 0<sup>_ξ-measurablerandomvariableanddefine,byrecurrence,_</sup> 



_Given n ∈N_<sup>0</sup> _, we have_ 



_showing that X is a martingale with respect to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_._</sup> 

Let us see another example of martingale that will be play an important role in financial modeling. 

**Example 4.1.4** (Geometric martingale) **.** _Let the process ξ_ = ( _ξn_ ) _n∈N be a sequence of independent real valued bounded random variables such that_ E[ _ξn_ ] = 1 _for every n ∈N . Let X_ 0 _be a F_ 0<sup>_ξ_</sup> _measurable real valued random variable and define, by recurrence,_ 



_Given n ∈N_<sup>0</sup> _, we have_ 



_showing that X is a martingale with respect to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_._</sup> 



**Example 4.1.5** (Closed martingale) **.** _Let Z ∈ L_<sup>1</sup> _. Define_ 



_Then, by the tower property, for every n ∈N_<sup>_o_</sup> _,_ 



_so that X_ = ( _Xn_ ) _n∈N is a martingale. It can be seen as the updated information on the random variable Z over time. When N_ = N _an interesting question is: does_ lim _n→∞ Xn exists (a.s.); and in case, does it coincide with Z?_ 

The proposition below says that a necessary condition for a stochastic process to be a martingale is that its expected value is constant over time. We warn that this condition is far to be sufficient for the notion of martingale, as shown in Example 4.1.7. 

**Proposition 4.1.6.** _Let X_ = ( _Xn_ ) _n∈N be a submartingale (rest., supermartingale) with respect to the filtration generated by a process ξ_ = ( _ξn_ ) _n∈N . Then, the map n �→_ E[ _Xn_ ] _is nondecreasing (resp. nonincreasing)._ 

_4.2. SOME USEFUL RESULTS ON MARTINGALES_ 

85 

_Proof._ By Proposition 1.7.3(iv) and by definition of submartingale, we have 



The claim follows by recurrence. 

The converse is not true, as shown below. 

**Example 4.1.7.** _Let_ Ω= _{ω, ω_<sup>_′_</sup> _}, F_ = 2<sup>Ω</sup> _, and let_ P _be the uniform distribution on_ Ω _:_ 



_Consider the random variable X_ 0 : Ω _→{−_ 2 _,_ 2 _} defined by_ 



_Then, define_ 



_Then_ E[ _X_ 0] = E[ _X_ 1] = 0 _. On the other hand,_ 



_hence, the process X_ = ( _X_ 0 _, X_ 1) _is not a martingale._ 

### **4.2 Some useful results on martingales** 

In this section, we state and prove some important results on martingales that will be employed afterwards. We start with the following, containing also the notion of predictable compensator. **Proposition 4.2.1.** _Let X_ = ( _Xn_ ) _n∈N be a square integrable martingale (that is,_ E[ _Xn_<sup>2]</sup><sup>_< ∞for_</sup> _each n ∈N ) with respect to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_.Then_</sup> 

_(i) X_<sup>2</sup> = ( _Xn_<sup>2)</sup><sup>_n∈Nisasubmartingalewithrespectto_(</sup><sup>_F_</sup> _n_<sup>_ξ_)</sup> _n∈N_<sup>_.;_</sup> 

_(ii) Define the process_ 



_Then the process_ 



_is a martingale with respect to_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_.TheprocessC_=(</sup><sup>_C_</sup> _n_<sup>)</sup> _n∈N\{_ 0 _}_<sup>_iscalledthe_pre-</sup> dictable<sup>2</sup> compensator _of X_<sup>2</sup> _._ 

_Proof._ (i) We have 

Hence 



showing the first claim. 

> 2Predictable means that _Cn_ is _Fn−_ 1-measurable, hence, its value is known at time _n −_ 1. 

_CHAPTER 4. MARTINGALES_ 

86 

(ii) Notice that 



Hence, taking into account the chain of equalities performed in the proof of item (i), we have, for every _n ∈N_<sup>_o_</sup> , 



and the claim follows. 

**Remark 4.2.2.** _Notice that, when X is as in Example 4.1.3, the compensator C of X_<sup>2</sup> _is given by_ 



The following result is a key result in financial application in the arbitrage theory. 

**Proposition 4.2.3.** _Let X_ = ( _Xn_ ) _n∈N be a martingale and let h_ = ( _hn_ ) _n∈N be a_ _<u>bounded</u> real valued stochastic process, both adapted to the filtration_ ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>_.LetY_</sup> 0<sup>_∈L_1</sup><sup>_beF_</sup> 0<sup>_ξ-measurable_</sup> _and define the real valued stochastic process Y_ = ( _Yn_ ) _n∈N by_ 



##### _i.e., recursively on n,_ 



_Then Y is a martingale with respect to the filtration generated by ξ_ = ( _ξn_ ) _n∈N ._ 

_Proof._ Clearly, _Y_ is adapted with respect to ( _Fn_<sup>_ξ_)</sup> _n∈N_<sup>.</sup> Then, using several properties of the conditional expected value and the martingale property of _X_ , 



the claim. 

**Corollary 4.2.4** (Stopped martingales) **.** _Let X_ = ( _Xn_ ) _n∈N be a martingale and let τ be a stopping time, both with respect to the filtration generated by a process ξ_ = ( _ξn_ ) _n∈N . Then the stopped process X_<sup>_τ_</sup> _is a martingale with respect to the same filtration._ 

_Proof._ Consider the stopping strategy 



Applying Proposition (4.2.3) with _hn_ as above, we get the claim. 

**Remark 4.2.5.** _The statements above still hold when replacing “martingale” with “submartingale” or “supermartingale” and hn ≥_ 0 _._ 

## **Chapter 5** 

# **Random walks** 

Let _ξ_ = ( _ξn_ ) _n∈_ N be a sequence of real valued discrete random variables and set 



Let 



Clearly, _X_ is a real valued stochastic process adapted to ( _Fn_<sup>_ξ_)</sup> _n∈_ N<sup>.Itrepresentsa</sup><sup>_randomwalk_</sup> on the real line with starting point _X_ 0 = _ξ_ 0 and steps of amplitude (possibly negative) ( _ξn_ ) _n∈_ N0; that is, _Xn_ represents the position after _n_ steps. We want to study the long run behavior of this process under proper assumptions. 

### **5.1 Kolmogorov’s** 0 **-** 1 **law and Borel-Cantelli lemmas** 

Let us introduce the notion of _tail σ-algebra_ . 

**Definition 5.1.1** (Tail _σ_ -algebra generated by a sequence of random variables) **.** _Let ξ_ = ( _ξn_ ) _n∈_ N _be a sequence of discrete E-valued random variables. The_ tail _σ_ -algebra _generated the sequence ξ is the σ-algebra_ 



_where_ 



Roughly speaking, the tail _σ_ -algebra represents the information brought by the queue of the sequence. Many events and important random variables defined as limits are measurable with respect to this _σ_ -algebra. For instance, the events 

or the random variables 



We have the following notable results. 

**Theorem 5.1.2** (Kolmogorov’s 0-1 law) **.** _Let ξ_ = ( _ξn_ ) _n∈_ N _be a sequence of discrete independent random variables and let T_<sup>_ξ_</sup> _be the tail σ-algebra generated by this sequence. If X is a discrete T_<sup>_ξ_</sup> _-measurable random variable, then it is equal to a constant (a.s.)._ 

_In particular, applying the claim to X_ = **1** _A with A ∈T_<sup>_ξ_</sup> _shows that_ 

_A ∈T_<sup>_ξ_</sup> _⇒ either_ P( _A_ ) = 0 _or_ P( _A_ ) = 1 _._ 

87 

_CHAPTER 5. RANDOM WALKS_ 

88 

_Proof._ Let _E, E_<sup>_′_</sup> be, repectively, the state space of _X_ and of _ξ_ . Since _X_ is _T_<sup>_ξ_</sup> -measurable, by Doob’s measurability criterion, for every _M ⊂_ N with _|M | < ∞_ , it can be written as 



for some function _fM_ : _E_<sup>_Mc_</sup> _→ E_<sup>_′_</sup> . Since the sequence of random variables ( _ξn_ ) _n∈_ N is an independent sequence, we must have that _X_ is independent of ( _ξn_ ) _n∈M_ . But since this holds for any arbitrary finite set _M ⊂_ N, we deduce that _X_ is independent of the entire sequence ( _ξn_ ) _n∈_ N. Hence, it must be independent of itself. The only random variables which are independent of themselves are the random variables which are (a.s.) constant, and the proof is complete. 

Let us see how the above result can be applied to “limsup of events”. Let ( _An_ ) _n∈_ N _⊆F_ and define 



Clearly 



**Lemma 5.1.3** (First Lemma of Borel-Cantelli) **.** _Let_ ( _An_ ) _n∈_ N _⊆F._ 



_Proof._ Set 



Clearly, the sequence of _Bn_ ’s is decreasing and 



Therefore, 



By subadditivity 



Since by assumption<sup>�</sup> _n∈_ N<sup>P(</sup><sup>_An_)</sup><sup>_< ∞_,therighthandsideintheinequalityaboveconvergesto</sup> 0 and the claim follows. 

Assume now that the events ( _An_ ) _n∈_ N are independent. In this case, by the Kolmogorov’s 0-1 law, we must have 



**Lemma 5.1.4** (Second Lemma of Borel-Cantelli) **.** _Let_ ( _An_ ) _n∈_ N _⊆F be independent_<sup>1</sup> _. Then,_ 



> 1Actually, it suffices that they are independent by pairs; i.e., _An_ is independent by _Am_ for every _n̸_ = _m_ . 

_5.1. KOLMOGOROV’S_ 0 _-_ 1 _LAW AND BOREL-CANTELLI LEMMAS_ 

89 

**Remark 5.1.5.** _Note that, by combining Lemma 5.1.3 and Lemma 5.1.4, in the case when the events_ ( _An_ ) _n∈_ N _are independent, the dichotomy_ (5.1.3) _is “solved” by_ 



To prove Lemma 5.1.4, we first show the following. 

**Lemma 5.1.6.** _Let_ ( _ξn_ ) _n≥_ 0 _be a sequence of real valued independent random variables such that_ 0 _≤ ξn ≤_ 1 _and set_ 



_Assume that_ E[ _Xn_ ] _↑∞. Then,_ 

_Xn →∞ a.s.._ 



_Proof._ We have 



Now, by a result of measure theory, one can extract a subsequence _Xnk_ such that 



so that 

_Xnk →∞_ a.s.. 

But, since _Xn_ is increasing, we may conclude that actually the stronger (5.1.4) holds. 

_Proof of Lemma 5.1.4._ Let us apply Lemma 5.1.6 with _ξn_ = **1** _An_ . We may do that, since the events ( _An_ ) _n∈_ N are independent and moreover, with this specification, we have by assumption 



so all the assumptions of Lemma 5.1.6 are fulfilled. Then, 



hence 

that is, recalling (5.1.2), 



_CHAPTER 5. RANDOM WALKS_ 

90 

**Example 5.1.7** (A sequence converging in probability not converging almost surely) **.** _We show an application of the second Borel-Cantelli Lemma exhibiting a sequence of random variables converging in probability but not converging_ P _-almost surely._ 

_Let_ (Ω _, F,_ P) _be a suitable probability space supporting an independent sequence_ ( _Xn_ ) _n∈_ N _of Bernoulli random variables valued in {_ 0 _,_ 1 _} such that_ P _{Xn_ = 1 _}_ = 1 _/n. Then, given ε ∈_ (0 _,_ 1) _, we have_ 



_so Xn converges to_ 0 _in probability. On the other hand, we have_ 



_Since the events {Xn_ = 1 _} are independent, by the second Borel-Cantelli lemma, we have_ 



_This means that, a.s. Xn does not converge to_ 0 _._<sup>2</sup> 

### **5.2 Limit behavior of symmetric random walks** 

Let us come back to our random walk framework. From now on, we consider a special symmetric case: ( _ξn_ ) _n∈_ N is a sequence of independent random variable valued in _{−_ 1 _,_ 0 _,_ 1 _}_ , with distribution possibly depending on _n_ , of the following type 



We are interested in the limiting behavior of _Xn_ . Let 



Clearly, _A∞ ∈T_<sup>_ξ_</sup> . Since the sequence ( _ξn_ ) _n∈_ N is a sequence of independent random variables, it follows, by the Kolmogorov 0 _−_ 1 law that 



We have the following characterization. 

**Proposition 5.2.1.** _We have_ 



_Proof._ Set _An_ := _{|ξn|_ = 1 _}_ . We have 



The claim follows from Remark 5.1.5. 

The above result says, in particular, that when<sup>�</sup><sup>_∞_</sup> _n_ =0<sup>_pn<∞_,therandomwalkbecomes</sup> definitively constant a.s. (<sup>3</sup> ). What cab be said about the long run behavior when<sup>�</sup><sup>_∞_</sup> _n_ =0<sup>_pn_=</sup><sup>_∞_?</sup> The following theorem provides a first answer. 

> 2Not only it is not true that _Xn_ converges to 0 almost surely; much more: almost surely _Xn_ does not converge to 0. 

> 3But be careful: the time step at which it becomes constant depends on _ω_ . 

_5.2. LIMIT BEHAVIOR OF SYMMETRIC RANDOM WALKS_ 

91 

**Theorem 5.2.2.** _We have_ 



_Proof._ Let _a ∈_ N0 and set 



with the usual convention inf _∅_ = _∞_ . The latter is a stopping time with respect to the reference filtration ( _Fn_<sup>_ξ_).Wehave</sup> 

so that 



Since 

we have 



To show the claim it thus suffices to prove that 



The rest of the proof is devoted to achieve that. 

So, let _a ≥_ 1 and consider the martingale 



where _C_ is provided by Remark 4.2.2 and notice that, in the present case, 



By Corollary 4.2.4, ( _Mn_<sup>_τa_)</sup><sup>_n≥_0isamartingaletoo,sothat</sup> 



that is 

Clearly, 



Therefore, by (5.2.4), 



Since _C_ is nonnegative, we have _Cτa∧n ≥ Cn_ **1** _{τa_ = _∞}_ , hence we also have 



Recalling that 



_CHAPTER 5. RANDOM WALKS_ 

92 

we get 



and taking the limit as _n →∞_ , 

Since, by assumption,<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>_pn_=</sup><sup>_∞_,weneedtohaveP</sup><sup>_{τa_=</sup><sup>_∞}_= 0.Byarbitrarinessof</sup><sup>_a_,we</sup> obtain (5.2.3) and therefore conclude the proof. 

### **5.3 An interlude: Gambler’s ruin in the fair case** 

Assume that two players, say (A) and (B), play the following game. They play an indefinite number of stakes. At each stake, there are three possibilities: 

1. (A) wins with probability _p ∈_ (0 _,_ 1 _/_ 2] and receive a unit of money by (B); 

2. (B) wins with the same probability _p_ and receive a unit of money by (A); 

3. the stake results in a draw and no one pays the other one. 

The initial endowment of (A) is _a ∈_ N0 and the initial endowment of (B) is _b ∈_ N0. The game ends when one of the two players loose all the money (ruin). We may model the overall game by a random walk _X_ = ( _Xn_ ) _n∈_ N as before, with _ξ_ = ( _ξn_ ) _n≥_ 0 an i.i.d. sequence of random variables with _pn ≡ p_ . Associating the outcome 1 to the winning of (A) in the single stake and the outcome _−_ 1 to the winning of (B) in a single stake, we set 



They are stopping times. The events 



represent, respectively, the ruin of (A) and the ruin of (B). The terminal time of the game is the stopping time 



Since<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>_p_=</sup><sup>_∞_,fromTheorem5.2.2weknowthat</sup><sup>_τ< ∞_a.s.,sothat</sup> 



We are interested in computing P( _RA_ ) and P( _RB_ ). By the martingale property of _X_ and by Corollary 4.2.4, we have 



On the other hand, since _τ < ∞_ a.s., we have 



Since _−a ≤ Xτ ∧n ≤ b_ , we may apply dominated convergence theorem, to get, also using (5.3.2), 

0 = _n_ lim _→∞_<sup>E[</sup><sup>_Xτ∧n_] = E[</sup><sup>_b_</sup><sup>**1**</sup><sup>_RB−a_</sup><sup>**1**</sup><sup>_RA_] =</sup><sup>_b_P(</sup><sup>_RB_)</sup><sup>_−a_P(</sup><sup>_RA_)</sup><sup>_._</sup> 

Combining with (5.3.1), we get the following expressions: 



_5.4. STILL ON THE LIMIT BEHAVIOR OF SYMMETRIC RANDOM WALKS_ 

93 

### **5.4 Still on the limit behavior of symmetric random walks** 

We can get a consequence from (5.3.3), by a limiting argument: the fact that the random walk reaches any prescribed target _α ∈_ Z. 

Set 



With the notations used above, assuming without loss of generality that _α <_ 0 and setting _a_ := _−α_ , we have 



and 



Hence, 



This shows that the random walks reaches any state in Z a.s. in finite time. As a consequence, we have, a.s., 



94 _CHAPTER 5. RANDOM WALKS_ 

## **Chapter 6** 

# **Financial models in finite probability spaces** 

We are going to describe simple financial models in discrete time, where the martingale theory shows, in a nutshell, its relevance as a tool to describe the main notions of the field. We start from the one period model and then move on the multi-period model. 

### **6.1 One period models** 

In this section (Ω _, F,_ P) will be a finite probability space: 



where 



#### **6.1.1 Market model: one single risky asset** 

The financial model we are going to build consist only of two dates, _n_ = 0 (say, today) and _n_ = _N_ = 1 (say, tomorrow); the generic _ω ∈_ Ωcan be interpreted as a parameter representing the “state of the (financial) world” at time _n_ = 1. We consider a very simple financial marked composed only by two asset: a riskless asset ( **bond** ) denoted by _B_ ; a risky asset ( **stock** ) denoted by _S_ . The values of these two assets at time _n_ = 0 _,_ 1 are denoted, respectively, by _B_ 0 _, B_ 1 and by _S_ 0 _, S_ 1. We assume that 



We assume, without loss of generality<sup>1</sup> , that 



Notice that _B_ 0 _, S_ 0 are some given constant, so they are _deterministic_ . Also the value _B_ 1 is a deterministic object, whereas _S_ 1 is random: it is a real valued random variable defined on (Ω _, F, P_ ) depending on _ω ∈_ Ω. The returns of the riskless and of the risky arrest are, respectively, 



> 1One may restrict the probability space to fulfill (6.1.1) if needed. 

95 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

96 

It is usual and useful, in a financial context, to take the riskless asset as “numeraire” and to consider the risky asset(s) with respect to it by defining its discounted value: 



**Remark 6.1.1.** _Typically, r >_ 0 _. However, the mathematical model we are building does not have any reason to require this assumption, which turns out to be restrictive nowadays — given the fact that negative interest rates are observed in the real world._ □ 

**Remark 6.1.2.** _The probability measure_ P _is sometimes referred to as the_ real _or_ physical _probability, in contrast to another measure that we will introduce shortly and which will play a fundamental role in the remainder of this work. However, this terminology is often considered inadequate from a mathematical perspective, which typically views probability through a_ subjective _lens. We therefore prefer to avoid such terms:_ P _is, more simply, the probability that a market agent chooses to associate with her/his degree of belief regarding future “states of the world.”_ □ 

#### **6.1.2 Portfolio, arbitrage, and martingale measures** 

In the market model above we define a _portfolio strategy_ simply as a vector _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) _∈_ R<sup>2</sup> , where _h_<sup>_B_</sup> _, h_<sup>_S_</sup> are, respectively, the number of shares in the bond and in the stock held in the portfolio. Negative values of _h_<sup>_B_</sup> _, h_<sup>_S_</sup> are interpreted as “short selling” of the asset. Denoting by _V_ 0<sup>_h, V_</sup> 1<sup>_h_,respectively,thevalueoftheportfolioattime</sup><sup>_n_= 0and</sup><sup>_n_= 1,wehave</sup> 

_V_ 0<sup>_h_=</sup><sup>_hBB_0+</sup><sup>_hSS_0=</sup><sup>_hB_+</sup><sup>_hSs,_</sup> _V_ 1<sup>_h_=</sup><sup>_hBB_1+</sup><sup>_hSS_1=</sup><sup>_hB_(1 +</sup><sup>_r_) +</sup><sup>_hSS_1</sup><sup>_._</sup> Clearly, _V_ 0<sup>_h_is a deterministic object, whereas</sup><sup>_V_</sup> 1<sup>_h_is, in general, a random variable truly depending</sup> on _ω ∈_ Ω. 



The interpretation of the above concept is clear: an arbitrage is a “money machine” allowing to do money with positive probability for free. Indeed, it is an investment strategy in the market which guarantees, starting without money at time _n_ = 0 (property (i)), to make money with positive probability at time _n_ = 1 (property (iii)), without incurring in any risk to loose money (property (ii)). If there are no arbitrage opportunities in the market, the latter is said _arbitrage free_ . 

As for the stock, we can define the discounted value of the portfolio: 



In terms of this more convenient object, the definition above can be reformulated as follows. 









_6.1. ONE PERIOD MODELS_ 

97 

The existence of arbitrage opportunities in the market is related, as we will see, to the existence of a _martingale measure_ for the model. 

**Definition 6.1.5.** _A probability measure_ Q : _F →_ [0 _,_ 1] _is said equivalent to_ P _if_ Q( _A_ ) = 0 _if and only if_ P( _A_ ) = 0<sup>2</sup> _. In this case, we write_ Q _∼_ P _._ □ 

In our framework, clearly Q _∼_ P if and only if _qk_ := Q _{ωk} >_ 0 for all _k_ = 1 _, ..., M_ . Definition 6.1.6 then turns out to be equivalent to the following. 

**Definition 6.1.6** (Arbitrage - III) **.** _Let_ Q _∼_ P _. An_ arbitrage _is a portfolio strategy h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) _such that:_ 





**Definition 6.1.7** (Equivalent martingale measure) **.** _An_ equivalent martingale measure _for the financial model above is a probability measure_ Q _∼_ P _such that the stochastic process S_<sup>�</sup> = ( _S_<sup>�</sup> 0 _, S_<sup>�</sup> 1) _is a martingale with respect to_ Q _; that is_<sup>3</sup> _,_ 



**Theorem 6.1.8** (First fundamental theorem of asset pricing) **.** _The market model above is arbitrage free if and only if there exists an equivalent martingale measure._ 

_Proof._ (Proof of _⇐_ ). Let Q _∼_ P be an equivalent martingale measure. Given _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ), we have 



A logical argument shows that the absence of arbitrage is equivalent to the implication 



i.e., whenever (i) and (ii) of Definition 6.1.6 hold, (iii) does not. Let _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) be a portfolio strategy such that _V_<sup>�</sup> 0<sup>_h_= 0andQ</sup><sup>_{V_�</sup> 1<sup>_h≥_0</sup><sup>_}_= 1.Then,by(6.1.2),</sup> 



Hence, by Proposition 1.6.2(v), we have to conclude that _V_<sup>�</sup> 1<sup>_h≡_0andtheimplication(6.1.3)is</sup> proved. 

(Alternative proof of _⇐_ ). Assume, by contradiction, that the market is not arbitrage free. This means that there exists a portfolio _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) such that 







> 2Equivalently, if Q( _A_ ) _>_ 0 if and only if P( _A_ ) _>_ 0. 

> the3naturalWe are filtration.in a one periodTherefore,framework _F_ 0 _S_ �<sup>=</sup><sup>_σ_</sup> and<sup>(</sup><sup>_S_�</sup> 0we<sup>) =</sup> are<sup>_{∅,_</sup> implicitly<sup>Ω</sup><sup>_}_,since</sup><sup>_S_</sup> assuming<sup>�</sup> 0<sup>isaconstant.</sup> to speak<sup>Hence</sup> about<sup>EQ</sup> martingale<sup>[</sup><sup>_S_�</sup> 1<sup>_| F_</sup> 0 _S_ �<sup>] =</sup> with<sup>EQ[</sup><sup>_S_�</sup> respect1<sup>]</sup><sup>_._</sup> to 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

98 

Then, letting Q be an arbitrary probability measure equivalent to P, we should have 

_h_<sup>_B_</sup> + _h_<sup>_S_</sup> _s_ = 0 _<_ E<sup>Q</sup> [ _V_<sup>�</sup> 1<sup>_h_] = EQ[</sup><sup>_hB_+</sup><sup>_hS_�</sup><sup>_S_1] =</sup><sup>_hB_+</sup><sup>_hS_EQ[</sup><sup>_S_�1] =</sup><sup>_hB_+</sup><sup>_hSs,_</sup> 

a contradiction. 

(Proof of _⇒_ ) Let the market model above be arbitrage free. We prove the claim in the case _M_ = 2 and _M_ = 3; then, in Remark 6.1.9, we comment on the extension in the general case. 

( _M_ = 2) In this case, we will prove that there exists a _unique_ equivalent martingale measure Q _∼_ P. Assume, without loss of generality, that _s_ 1 _< s_ 2. Let us show first that it must be 



Indeed, assume first, by contradiction, that 



and consider the portfolio strategy _h_ = ( _−s,_ 1). Concretely, this correspond to borrow the amount _s_ from the bank (short sell of _s_ shares of bond) and use it to buy 1 share of stock. We have 



By (6.1.5), we have 



showing that _h_ is an arbitrage portfolio. So, we have proved that the absence of arbitrage is not consistent with the inequality<sup>_<u>s</u>_</sup> _S_<sup><u>1</u></sup><sup>_≥_1 +</sup><sup>_r_,i.e.that</sup> 



A symmetric argument shows that 



Putting together these two conclusions, we have shown (6.1.4). Let us construct the unique equivalent martingale measure. Indeed, let Q _∼_ P and set _q_ 1 := Q _{ω_ 1 _}_ , _q_ 2 := Q _{ω_ 2 _}_ . Then, in order to be Q a martingale measure, it must hold 



Combining the latter with the condition _q_ 1 + _q_ 2 = 1, we get the linear system in the unknowns _q_ 1 _, q_ 2 



This linear system admits a (unique) solution 



Because of (6.1.4), the latter expressions of _q_ 1 _, q_ 2 belong to (0 _,_ 1), so they really define a probability measure equivalent to P. This is the (unique) equivalent martingale measure we were looking for. 

_6.1. ONE PERIOD MODELS_ 

99 

- ( _M_ = 3) We only sketch the proof, which proceeds along the same line of the case _M_ = 2. Indeed, assuming without loss of generality that _s_ 1 _< s_ 2 _< s_ 3, as in the case _M_ = 2 one shows that the absence of arbitrage implies 



Then, arguing again as in the case _M_ = 3, we end up with the system 



for the search of an equivalent martingale measure Q. It is possible to show that, by (6.1.7), this linear system admits a whole family of solutions ( _q_ 1<sup>_λ, q_</sup> 2<sup>_λ, q_</sup> 3<sup>_λ_)</sup><sup>_∈_(0</sup><sup>_,_1)3parametrizedin</sup> _λ ∈_ Λ, with Λ an infinite set. □ 

**Remark 6.1.9.** _(i)_ (6.1.2) _says that, if_ Q _∼_ P _is an equivalent martingale measure, then_ ( _V_<sup>�</sup> 0<sup>_h,_�</sup><sup>_V_</sup> 1<sup>_h_)</sup><sup>_isa_Q</sup><sup>_-martingaleforeachchoiceoftheportfoliostrategyh._</sup> 

- _(ii) The argument used to prove the second part of Proposition 6.1.8 for the case M_ = 2 _and M_ = 3 _can be easily generalized to generic M ≥_ 2 _to prove the following: letting s_ 1 _< ... < sM , t_ 



_and the latter leads to the construction of a family of equivalent martingale measures. Notice that_ (6.1.8) _is equivalent to_ 



_i.e., in an arbitrage free market the minimal return of the risky asset,_<sup>_<u>s</u>_</sup><sup><u>1</u></sup> _S_<sup>_−s,islowerthan_</sup> _the return of the riskless asset and the maximal return of the risky asset,_<sup>_<u>sM</u>_</sup> _S_<sup>_−s_</sup> _, is larger than the return of the riskless asset._ 

- _(iii) Since we have already proved that the existence of an equivalent martingale measure implies that the market is arbitrage free (Theorem 6.1.8), we have the following chain of implications:_ 



_Hence, the following facts are equivalent:_ 



- _(iv) The cases M_ = 2 _and M >_ 2 _are structurally different. In the former, there exists a_ unique _equivalent martingale measure; in the latter, there exists a whole family of equivalent martingale measures. This difference will play a role when we will address the issue of_ completeness _of the market._ 

- _(v) For the sake of simplicity, we are just considering a market model composed by one single risky asset and we will just briefly comment about the extension to (one-period) market model composed by several risky assets in Section 6.1.4. Here, we comment about the extension of the First Fundamental Theorem of Asset Pricing to the case of several risky assets. Consider_ 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

100 

_then a market model composed by a riskless asset B as the one introduced above and by d >_ 1 _risky assets S_<sup>1</sup> _, S_<sup>2</sup> _, ..., S_<sup>_d_</sup> _with prices_<sup>4</sup> 



_being S_ 1<sup>1</sup><sup>_, ..., S_</sup> 1<sup>_drandomvariablesvaluedin_(0</sup><sup>_, ∞_)</sup><sup>_.Withclearextensionofthenotionof_</sup> _portfolio strategy, which is now a vector h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_1</sup> _, ..., h_<sup>_Sd_</sup> ) _∈_ R<sup>_d_+1</sup> _, of portfolio value, and of arbitrage, we have that the market is arbitrage free if and only there exists an equivalent martingale measure for the discounted price processes_ 



_where_ 



_i.e., if and only if there exists_ Q _∼_ P _such that_ 



_As we will see, this extension allows to employ the so-called martingale method for pricing contingent claims._ □ 

#### **6.1.3 Contingent claims: pricing, hedging, and completeness** 

Two fundamental issues of mathematical finance concerns _pricing_ and _hedging_ of financial instruments based on underlying stock asset(s). Let us give a formal definition of such instruments, that we will call _contingent claims_ , in our market model framework. 

**Definition 6.1.10** (Contingent claim) **.** _A_ contingent claim _with payoff ϕ_ ( _S_ 1) _, where ϕ_ : (0 _, ∞_ ) _→_ R _, is a contract subscribed at time n_ = 0 _which pays to the holder at time n_ = 1 _the amount ϕ_ ( _S_ 1) _._ □ 

The most common contingent claim traded on the real market are the _call_ and the _put_ option with a given strike price _K >_ 0. These contracts are structured as follows: 

- (i) In the case of the call option with strike price _K_ , the holder has the right, but not the obligation, to buy at the date _n_ = 1 the stock _S_ at the price _K_ ; 

- (ii) In the case of the put option with strike price _K_ , the holder has the right, but not the obligation, to sell at the date _n_ = 1 the stock _S_ at the price _K_ . 

Hence, the payoffs are, respectively, 



> 4The subscripts 0 and 1, as in the case of a single risky asset, here refer to time, _n_ = 0 and _n_ = 1. 

Other common contingent claims are digital options with strike price _K >_ 0; they are in the form 

_ϕ_ ( _S_ 1) = **1** [ _K,∞_ )( _S_ 1) or _ϕ_ ( _S_ 1) = **1** (0 _,K_ ]( _S_ 1) _._ 

_6.1. ONE PERIOD MODELS_ 

101 



<!-- Start of picture text -->
—<br>C<br>Here •Stock Stock priceS, priceSt<br>K K<br><!-- End of picture text -->

Introducing a financial product in a free arbitrage market, the natural question which arises is: “Which is a fair price for it?”. The most natural answer, relying on a _no-arbitrage principle_ , should be: “A fair price is a price which does not introduce arbitrage opportunities”. One can address the last sentence in two ways: 

1. Through a _hedging_ argument; 

2. Through a _martingale measure_ argument. 

Let us illustrate these two methods and their connection. In the following we assume that the market model above is arbitrage free. 

##### **Pricing** **_via_ hedging** 

The method we are going to illustrate here only works when the contingent claim is _reachable_ or _hedgeable_ (in the sense of the definition given below) and gives rise to a _unique_ possible price not introducing arbitrage opportunities in the market. First let us clarify more formally the latter concept. Set _X_ 1 := _ϕ_ ( _S_ 1). The price _x_ for the contingent claim does not introduce arbitrage if the _extended market_ composed by the three assets 



is still arbitrage free, i.e. there is no “extended” portfolio strategy _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> _, h_<sup>_X_</sup> ) _∈_ R<sup>3</sup> producing an arbitrage in a sense exactly analogous to the one of Definition 6.1.3. 

**Definition 6.1.11** (Reachable or hedgeable claim) **.** _A contingent claim ϕ_ ( _S_ 1) _is said_ reachable _or_ hedgeable _if there exists a portfolio h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) _such that V_ 1<sup>_h_=</sup><sup>_ϕ_(</sup><sup>_S_1)</sup><sup>_.Inthiscase,hissaid_</sup> _a_ replicating _or_ hedging _investment strategy for the contingent claim ϕ_ ( _S_ 1) _._ □ 

The following proposition points out the basic facts concerning pricing and hedging of reachable claims. 

**Proposition 6.1.12.** _Let ϕ_ ( _S_ 1) _be a reachable contingent claim._ 

- _(i) The replicating portfolio is unique._ 

- _(ii) The unique price which does not introduce arbitrage in the market is given by V_ 0<sup>_h,whereh_</sup> _is the replicating portfolio._ 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

102 

**Proof.** (i) Let _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) and _h_ = ( _h_ _~~B~~ , hS_ ) be two portfolios replicating _ϕ_ ( _S_ 1). Since _V_ 1<sup>_h_=</sup><sup>_ϕ_(</sup><sup>_S_1) =</sup><sup>_V_</sup> 1 _h_<sup>,wealsohave</sup><sup>_V_�</sup> 1<sup>_h_=</sup><sup>_V_�</sup> 1 _h_<sup>,i.e.</sup> 



We can rewrite it as 



Now, notice that _S_<sup>�</sup> 1 is truly random, whereas _hB − hB_ is a deterministic object. So, to have the above equality it must hold _h_<sup>_S_</sup> _− h_ _~~S~~_ = 0, i.e. _hS_ = _h_ _~~S~~_ . It follows that it must be also _hB_ = _hB_ , concluding the proof of this item. 

(ii) Let _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) be the replicating portfolio and set _p_ := _V_ 0<sup>_h_=</sup><sup>_hB_+</sup><sup>_hSs_.Letusshow</sup> that a price _x > p_ introduces arbitrage. Indeed, consider the extended portfolio 



It consists in the following financial actions at time _n_ = 0: 

- Sell the contingent claim at price _x_ ; 

- Use the amount _p_ = _h_<sup>_B_</sup> + _h_<sup>_S_</sup> _s < x_ to replicate the contingent claim _X_ 1 = _ϕ_ ( _S_ 1); 

- Invest the amount _x − p >_ 0 in the bond. 

The cost of these financial operations is _x −_ ( _h_<sup>_B_</sup> + _h_<sup>_S_</sup> _s_ ) _−_ ( _x − p_ ) = 0. In other terms, the initial value of the portfolio is 



On the other hand, the value of the final portfolio is 



showing the arbitrage property of this portfolio. With a symmetric argument, one may show that also a price _x < p_ gives rise to arbitrage opportunities. 

Let now _x_ = _p_ . We aim at showing that this price does not introduce arbitrage opportunities. To prove this<sup>5</sup> , let us ask ourselves: What are we doing? Are we introducing something new in the market? Actually not, we are just duplicating something that already exists. Indeed, ( _p, X_ ) is the same as ( _p, V_ 1<sup>_h_), where</sup><sup>_h_= (</sup><sup>_hB, hS_) is the replicating portfolio of</sup><sup>_X_1.So, the portfolios</sup><sup>_Vk_,</sup> _k_ = ( _k_<sup>_B_</sup> _, k_<sup>_S_</sup> _, k_<sup>_X_</sup> ) _∈_ R<sup>3</sup> , that an agent may construct with the three assets (1 _, B_ 1) _,_ ( _s, S_ 1) _,_ ( _p, X_ 1) are the same as the portfolios that an agent may construct by the following financial instruments: 

- the two assets (1 _, B_ 1) _,_ ( _s, S_ 1); 



Clearly, the latter asset is redundant, as contained already as combinations of the former ones. In other terms, all the portfolios which can be constructed in the extended market can be constructed already as portfolios investing only in the original market ( _B, S_ ). Since the latter market is arbitrage free, the claim follows. □ 

> 5We will not be very rigorous in the proof. 

_6.1. ONE PERIOD MODELS_ 

103 

##### **Pricing through martingale measures** 

Differently from the previous method, this martingale method does not requires that the contingent claim is reachable. The martingale method relies on the first fundamental theorem of the asset pricing. Indeed, let _x_ be a price at time _n_ = 0 for the contingent claim _X_ 1 = _ϕ_ ( _S_ 1), and consider the extended market ( _B, S, X_ ), with _X_ = ( _x, X_ 1). In order to be this extended market arbitrage free, by the first fundamental theorem of asset pricing (notably, its version illustrated in Remark 6.1.9) the discounted values of the assets _S, X_ must be martingales under some martingale measure. Then, taking _any_ martingale measure Q _∼_ P for the original market, the fact that also the remaining asset _X_ is a martingale under this martingale measure corresponds simply to set 



Notice that we do not have a priori a unique possible fair price. Indeed, if we have more than one martingale measure for the original market, say two different martingale measures Q _,_ Q<sup>_′_</sup> both the values/prices 



let the extended market arbitrage free. Actually, it is true, even if we do not prove it, that, if more than one fair price exists, then there is a _whole interval_ ( _xmin, xmax_ ) of fair prices. However, consistently with what stated in the previous subsection, if the contingent claim is hedgeable, even if there exist several martingale measures, the fair price is unique. Indeed, letting _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) be the replicating portfolio and letting Q be _any arbitrary_ martingale measure, we have 



and the last term does not depend on Q. 

**Example 6.1.13.** _[Bjork, Ch. 2, Example 2.12] In the setting above with M_ = 2 _, consider the following example:_ 









_If we compute the expected value of the the stock price at time n_ = 1 _under_ P _, we get_ 



_Since r_ = 0 _this means that the average return of the risky asset is higher than the return of the riskless asset: this fact is expressed by saying that the market is_ risk averse _— a risk premium is “paid from the market” to investors in the risky asset. Clearly, since_ 80 _<_ 100 _<_ 120 _, we have_ 



_hence the market is arbitrage free. Consider a European call option with strike price K_ = 110 _on this market, i.e. the claim_ 



_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

104 

_If we used the method of pricing the claim as discounted expected value under the_ objective probability P _, we would get as price_ 



_But, if we use the martingale method (the correct one in the sense of the no-arbitrage principle!) to price the claim, we get a different result. Indeed, it is easily seen that the martingale measure in this example is just the equi-distributed one:_ 



_Notice that If we compute the expected value of the the stock price at time n_ = 1 _under_ Q _we get_ 



_i.e., if “we look at the world with the glasses_ Q _”, there is no convenience, in average, in the investment in the risky asset with respect to the investment in the riskless one — this is why the martingale measure is also called “risk neutral” measure. Now let us price the claim according to the martingale method. We get_ 



_which is different from the price obtained pricing under_ P _._ 

_Now, we try to replicate the option with an initial endowment V_ 0<sup>_h_</sup> = 5 _. We need to find h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) _∈_ R<sup>2</sup> _such that h_<sup>_B_</sup> (1 + _r_ ) + _h_<sup>_S_</sup> _S_ 1 = ( _S_ 1 _−_ 110)<sup>+</sup> _. With our data this leads to_ 







_which has the unique solution h_<sup>_B_</sup> = _−_ 20 _, h_<sup>_S_</sup> = 1 _/_ 4 _. Notice that the initial value of the replicating portfolio is_ 



_Hence, if someone is foolish enough to buy from us the option at the price_ 6 _produced by the first method (pricing under the objective probability), we may make money for free (arbitrage). We use the amount_ 5 _to replicate the option repaying the buyer at time n_ = 1 _and put the remaining amount_ 1 _in the bank account. We did not spend anything and tomorrow (n_ = 1 _) we have the amount_ 1 _in our pocket money._ □ 

**Exercise 6.1.14.** _Discuss the same questions of Example_ (6.1.13) _in the following cases._ 

- _(i) Same structure as in the example, but d_ = 100 _, u_ = 120 _._ 

_(ii) Same structure as in the example, but with the Put option: X_ 1 = (110 _− S_ 1)<sup>+</sup> _._ 



_(iv) The probability space is changed in_ Ω= _{ωd, ωm, ωu} and_ 





_Discuss the cases X_ 1 = **1** [0 _,_ 100]( _S_ 1) _, X_ 1 = ( _S_ 1 _−_ 110)<sup>+</sup> _, X_ 1 = (110 _− S_ 1)<sup>+</sup> _._ 

_6.1. ONE PERIOD MODELS_ 

105 

#### **6.1.4 Completeness of the market** 

Let us come back to the extension to the case of several risky asset mentioned in Remark 6.1.9(v), exposing and commenting some facts without providing the proofs. 

We therefore consider a market model composed by a riskless asset _B_ and by _d >_ 1 risky assets _S_<sup>1</sup> _, S_<sup>2</sup> _, ..., S_<sup>_d_</sup> with prices 



being _S_ 1<sup>1</sup><sup>_, ..., S_</sup> 1<sup>_d_random variables valued in (0</sup><sup>_, ∞_).We have seen in Remark 6.1.9(v) that — with</sup> clear extension of the notion of portfolio strategy, which is now a vector _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_1</sup> _, ..., h_<sup>_Sd_</sup> ) _∈_ R<sup>_d_+1</sup> , of portfolio value, and of arbitrage — the market is arbitrage free if and only there exists a martingale measures for the discounted price processes 

where 



i.e., if and only if there exists Q _∼_ P such that 



In this context one naturally considered contingent claims depending on the final values of _all_ the risky assets, i.e. financial payoffs in the form 



where _ϕ_ : (0 _, ∞_ )<sup>_d_</sup> _→_ R+. Similarly to the case of one risky asset one says that a contingent claim is reachable if there exists a portfolio strategy _h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_1</sup> _, ..., h_<sup>_Sd_</sup> ) such that _V_ 1<sup>_h_=</sup><sup>_ϕ_(</sup><sup>_S_</sup> 1<sup>1</sup><sup>_, ..., S_</sup> 1<sup>_d_).</sup> **Definition 6.1.15** (Completeness of the market) **.** _The market model is said_ complete _if each contingent claim in the form ϕ_ ( _S_ 1<sup>1</sup><sup>_, ..., S_</sup> 1<sup>_d_)</sup><sup>_,whereϕ_: (0</sup><sup>_, ∞_)</sup><sup>_d→_R+</sup><sup>_isreachable._</sup> 

Define the matrix _D ∈_ R<sup>(</sup><sup>_d_+1)</sup><sup>_×M_</sup> 



it is possible to show that 

The market is complete _⇐⇒_ Rank( _D_ ) = _M._ (6.1.10) 

In particular, in the case of one single risky asset, we see that, under the assumption 6.1.1, the market is complete if and only if _M_ = 2, i.e. only in the case when _S_ 1 is binary, that is, basically, it is a Bernoulli random variable. The following result is the Second Fundamental Theorem of Asset Pricing; it can be proved by means of (6.1.10). 

**Theorem 6.1.16** (Second Fundamental Theorem of Asset Pricing) **.** _The market model above is complete if and only if there exists_ at most one _martingale measure on σ_ ( _S_<sup>1</sup> _, ..., S_<sup>_d_</sup> ) _._ □ 

Joining the statement of the First and Second Theorem of Asset Pricing we conclude that 

Market arbitrage free and complete _⇐⇒∃_ ! martingale measure _._ 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

106 

### **6.2 Multi-period financial models** 

In this section, (Ω _, F,_ P) will be a (finite) reference probability space. 

#### **6.2.1 The market model** 

The financial model we are going to build consists of _N_ + 1 dates, _n_ = 0 _,_ 1 _, ..., N_ , with _N < ∞_ . We consider a very simple financial marked composed only by two assets: a riskless asset ( **bond** ) denoted by _B_ ; a risky asset ( **stock** ) denoted by _S_ . The values of these two assets at time _n_ , where _n_ = 0 _,_ 1 _, .., N_ , are denoted, respectively, by _Bn_ and by _Sn_ . We assume that, for some _r > −_ 1, 







and 



is a stochastic process supported by the probability space (Ω _, F,_ P). We assume that _S_ 0 = _s >_ 0 is a given constant (not a random variable), i.e. that the price of the stock at time _n_ = 0 is known. We consider the filtration ( _Fn_ ) _n∈N_ = ( _Fn_<sup>_S_)</sup><sup>_n∈N_generatedbythisprocessandinterpret</sup> the algebra _Fn_ = _σ_ ( _S_ 0 _, ..., Sn_ ) as the set of information collected by the observation of the market till time _n_ . We assume that 



i.e. that _Sn_ +1 is really unknown at time _n_ . Since _S_ 0 is a constant, the information brought by it is the trivial one, i.e., _F_ 0<sup>_S_=</sup><sup>_{∅,_Ω</sup><sup>_}_.Wethentaketherisklessassetas“numeraire”andto</sup> consider the price of the risky asset with respect to the former, by defining the discounted prices: 



Notice that the filtration generated by _S_ is the same as the one generated by _S_<sup>�</sup> . It is convenient also to define the stochastic process “return of the risky asset”, i.e. the process 



**Remark 6.2.1.** _To model the price process S, one typically follows the other way around; that is, one starts by modeling the return process ϱ_ = ( _ϱn_ ) _n_ =1 _,...,N and then define the price process S_ = ( _Sn_ ) _n∈N recursively as_ 



#### **6.2.2 Self-financed portfolios, arbitrage, and martingale measures** 

In the market model above, a _portfolio investment strategy_ is a couple of real valued ( _Fn_<sup>_S_)</sup><sup>_n∈N_-</sup> adapted stochastic processes 



where, for _n ∈N_<sup>0</sup> , the random variables _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>are,respectively,thenumberofsharesinthe</sup> bond and in the stock held in the portfolio in the period _n → n_ +1. The fact that the processes are adapted to ( _Fn_<sup>_S_)</sup><sup>_n∈N_accounts for the non-anticipativity of the strategy:the information available</sup> to the investor at time _n_ to choose the allocation of the portfolio is the history of the stock price process up to current time. Negative values of _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>areinterpreted,asusual,as“shortselling”</sup> of the asset at the date _n_ . Notice that _h_<sup>_B_</sup> 0<sup>_, hS_</sup> 0<sup>areconstant(deterministicobject,notrandom</sup> 

_6.2. MULTI-PERIOD FINANCIAL MODELS_ 

107 

variables), as _F_ 0<sup>_S_=</sup><sup>_{∅,_Ω</sup><sup>_}_andtheonlyrandomvariablesmeasurablewithrespecttothetrivial</sup> algebra are the constants ones. We denote by _V_<sup>_h_</sup> = ( _Vn_<sup>_h_)</sup><sup>_n∈N_the value of the portfolio over time,</sup> defined as 



**Definition 6.2.2.** _We say that a portfolio investment strategy h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_</sup> ) = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0</sup><sup>_is_</sup> self-financing _and that the portfolio is_ self-financed _if_ 



_i.e., if the variation of the portfolio value in the period n → n_ + 1 _is only due to the return on investments_<sup>6</sup> _._ □ 

Since 



the requirement (6.2.2) is a constraint on the choice of ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>).Indeed,itmusthold</sup> 

_h_<sup>_B_</sup> _n_ +1<sup>_Bn_+1+</sup><sup>_h_</sup> _n_<sup>_S_</sup> +1<sup>_Sn_+1=:</sup><sup>_V_</sup> _n_<sup>_h_</sup> +1<sup>=</sup><sup>_V_</sup> _n_<sup>_h_+</sup><sup>_h_</sup> _n_<sup>_B_(</sup><sup>_Bn_+1</sup><sup>_−Bn_) +</sup><sup>_h_</sup> _n_<sup>_S_(</sup><sup>_Sn_+1</sup><sup>_−Sn_) :=</sup><sup>_h_</sup> _n_<sup>_BBn_+1+</sup><sup>_h_</sup> _n_<sup>_SSn_+1</sup><sup>_._</sup> Hence, at time _n_ + 1, the number _h_<sup>_B_</sup> _n_ +1<sup>isfixedonce</sup><sup>_hS_</sup> _n_ +1<sup>isdecided:</sup> 



It is easier to deal with discounted values: indeed, defining 



under the assumption that the portfolio is self-financed, we have for every, _n ∈N_<sup>0</sup> , 



Let us rewrite the previous equation emphasizing the first and the last term: 



This form is particularly convenient: it expresses, under the assumption of self-financing investment strategy, the dynamics of the discounted portfolio value over time given the only choice of the investment strategy in the stock asset _h_<sup>_S_</sup> = ( _h_<sup>_S_</sup> _n_<sup>)</sup> _n∈N_<sup>0;7thechoiceoftheinvestmentstrat-</sup> egy in the bond market _h_<sup>_B_</sup> = ( _h_<sup>_B_</sup> _n_<sup>)</sup> _n∈N_<sup>0isthenobligedandmaybederivedbytheconstraint</sup> (6.2.3). The notion of arbitrage, that we give already in terms of discounted portfolio value, can be generalized to this dynamic context as follows. 

**Definition 6.2.3** (Arbitrage - I) **.** _An_ arbitrage _is a self-financing portfolio strategy h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0</sup> _such that:_ 

> 6No extra cashflows such as consumption or money injection contributes to the variation of the portfolio value. 

> 7In the language of control theory, this is a _state equation_ : _V_ � is the _state variable_ and _h_ is the _control variable_ . 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

108 



Also in this case, the existence of arbitrage opportunities in the market is related, as we will see, to the existence of a _martingale measure_ for the model. Clearly, the notion of arbitrage can be reformulated in terms of _any_ equivalent probability measure as follows. 

**Definition 6.2.4** (Arbitrage - II) **.** _Let_ Q _∼_ P _. An_ arbitrage _is a self-financing portfolio strategy h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0</sup><sup>_suchthat:_</sup> 





Let us give the definition of _martingale measure_ in our dynamic context. 

**Definition 6.2.5** (Equivalent martingale measure) **.** _An_ equivalent martingale measure _for the financial model above is a probability measure_ Q _∼_ P _such that the stochastic process S_<sup>�</sup> = ( _S_<sup>�</sup> _n_ ) _n∈N is a martingale with respect to_ Q _._ □ 

Notice that, if Q _∼_ P is an equivalent martingale measure, then, by Proposition 4.2.3, also the discounted portfolio value process 



is a Q-martingale for all portfolio strategies _h_<sup>_S_</sup> = ( _h_<sup>_S_</sup> _n_<sup>)</sup> _n∈N_<sup>0.Acharacterizationoftheabsence</sup> of arbitrage holds in this dynamic context similarly to the one we have seen in the one period model. 

**Theorem 6.2.6** (First fundamental theorem of asset pricing) **.** _The market model above is arbitrage free if and only if there exists an equivalent martingale measure._ 

**Proof.** We only show one of the implications, i.e. the fact that the existence of an equivalent martingale measure implies absence of arbitrage. Let Q _∼_ P be an equivalent martingale measure and let _h_<sup>_S_</sup> = ( _h_<sup>_S_</sup> _n_<sup>)</sup> _n∈N_<sup>0beaself-financingportfoliostrategysuchthat(i)–(ii)ofDefinition6.2.4</sup> hold. As observed, also _V_<sup>�</sup><sup>_h_</sup> = ( _V_<sup>�</sup> _n_<sup>_h_)</sup><sup>_n∈N_isaQ-martingale.ByProposition4.1.6,</sup> 



Hence, by Proposition 1.6.2(v), if (i)–(ii) of Definition 6.2.4 hold, then (iii) of Definition 6.2.4 cannot hold. It follows that no arbitrage may exist. □ 

**Remark 6.2.7.** _For the sake of simplicity, we are just considering a market model composed by one single risky asset and we will just briefly comment about the extension to (one-period) market model composed by several risky assets in Section 6.1.4. Here, we comment about the extension of the First Fundamental Theorem of Asset Pricing to the case of several risky assets. Consider then a market model composed by a riskless asset B as the one introduced above and by d >_ 1 _risky assets S_<sup>1</sup> _, S_<sup>2</sup> _, ..., S_<sup>_d_</sup> _with price processes_ 



_6.2. MULTI-PERIOD FINANCIAL MODELS_ 

109 

_With clear extension of the notion of portfolio strategy, which is now a vector of adapted stochastic processes h_ = ( _h_<sup>_B_</sup> _, h_<sup>_S_1</sup> _, ..., h_<sup>_Sd_</sup> ) _, of portfolio value, and of arbitrage, we have that the market is arbitrage free if and only there exists an equivalent martingale measure for the discounted price processes_ 

_where_ 



_i.e., if and only if there exists_ Q _∼_ P _such that_ 



_This extension allows to employ the martingale method for pricing contingent claims._ 

□ 

#### **6.2.3 Contingent claims: pricing, hedging, and completeness** 

As for the static (one period) case, we can consider the problems of _pricing_ and _hedging_ of financial instruments based on underlying stock asset(s). In our dynamic framework the definition of contingent claim is the following. 

**Definition 6.2.8** (Contingent claim) **.** _A_ contingent claim _with payoff ϕ_ ( _SN_ ) _, where ϕ_ : R _→_ R _, is a contract subscribed at time n_ = 0 _which pays to the holder at time n_ = _N the amount ϕ_ ( _SN_ ) _._ □ 

In this dynamic context, the payoffs of the call and put options are 



**Remark 6.2.9.** _The terminology “European” refers to the fact that the option can be exercised only at the expiration date n_ = _N . We mention that more complex contracts may be considered in this dynamic context._ 

- _Asian options: They are contracts whose payoff depends on the whole path_ ( _Sn_ ) _n∈N of the stock price, not only on its price SN at the terminal date n_ = _N ; for instance_ 



- _American options: The owners of this kind of contracts have the right to exercise the option at any date n ∈N ; that is, to ask, at any time n_ = 0 _, ..., N , to get paid ϕ_ ( _n, Sn_ ) _where_ 



_is a payoff function defining the contract._ 

_The mathematical issues of pricing and hedging these kinds of contracts may be much harder. For the last type of options, mathematically speaking one has to solve an optimal stopping problem._ □ 

Again relying on a _no-arbitrage principle_ , we address the problem of pricing the contingent claims in this dynamic context 

1. through a _hedging_ argument; 

2. through an _equivalent martingale measure_ argument. 

We assume, hereafter in this section, that the market ( _B, S_ ) is arbitrage free. 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

110 

##### **Pricing** **_via_ hedging** 

The method we are going to illustrate here only works when the contingent claim is _reachable_ or _hedgeable_ and gives rise to a _unique_ possible price not introducing arbitrage opportunities in the market, according to the following definition. 

**Definition 6.2.10.** _In the market model_ ( _B, S_ ) _above, assume to introduce the contingent claim ϕ_ ( _SN_ ) _at price x at time n_ = 0 _. We say that the price x introduces arbitrage in the market if there exists a dynamic-static investment strategy_ 



_in the extended market_ ( _B, S, ϕ_ ( _SN_ )) _such that_ 

_(a)_ ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0</sup><sup>_isaself-financinginvestmentportfoliostrategyinthe_(</sup><sup>_B, S_)</sup><sup>_market;_</sup> _(b) h_<sup>_ϕ_</sup> 0<sup>_∈_R</sup><sup>_;_</sup> 

_(c) Defining_ 



_one has_ 



**Definition 6.2.11** (Reachable or hedgeable claim) **.** _A contingent claim ϕ_ ( _SN_ ) _is said_ reachable _or_ hedgeable _if there exists a self-financing investment strategy h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup><sup>_n∈N osuchthat_</sup> _VN_<sup>_h_=</sup><sup>_ϕ_(</sup><sup>_SN_)</sup><sup>_.In this case, h is said a_replicating</sup><sup>_or_hedging</sup><sup>_investment strategy of the contingent_</sup> _claim ϕ_ ( _SN_ ) _and V_<sup>_h_</sup> _is called a_ replicating _portfolio of the contingent claim ϕ_ ( _SN_ ) _._ □ 

**Proposition 6.2.12.** _Let ϕ_ ( _SN_ ) _be a reachable contingent claim._ 

- _(i) The replicating investment strategy is unique._ 

- _(ii) The unique price which does not introduce arbitrage in the market is given by V_ 0<sup>_h,whereh_</sup> _is the replicating investment strategy._ 

_~~B S~~_ **Proof.** (i) Let _h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0and</sup> _h_ = ( _hn_<sup>_,_</sup> _hn_<sup>)</sup> _n∈N_<sup>0betwoself-financinginvestment</sup> portfolio strategies replicating _ϕ_ ( _SN_ ). Since _VN_<sup>_h_=</sup><sup>_ϕ_(</sup><sup>_SN_) =</sup><sup>_V_</sup> _Nh_<sup>,wealsohave</sup> 





The left hand side is _FN −_ 1-measurable whereas _S_<sup>�</sup> _N_ is not (cf. (6.2.1)). So, arguing similarly to the one period case one concludes that 



Iterating backward the argument one gets 



_6.2. MULTI-PERIOD FINANCIAL MODELS_ 

111 

The self-financing constraint (6.2.3) then provides 



concluding the proof of this item. 

(ii) Let _h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0)bethereplicatingportfolioandset</sup><sup>_p_:=</sup><sup>_V_</sup> 0<sup>_h_.Letusshowthata</sup> price _x > p_ introduces arbitrage. Indeed, consider the extended portfolio 



It consists in the following financial actions: 

- At time _n_ = 0 sell the contingent claim at price _x_ ; 

- Use the amount _p < x_ to replicate the contingent claim _ϕ_ ( _SN_ ) with the dynamic strategy _h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>)</sup> _n∈N_<sup>0);</sup> 

- Invest at time _n_ = 0 the remaining amount _x − p >_ 0 in the bond and keep this position till time _N_ . 

The initial value of the portfolio is _V_ 0<sup>_k_= (</sup><sup>_x −p_) +</sup><sup>_V_</sup> 0<sup>_h−x_= 0.Ontheotherhand,thevalueof</sup> the final portfolio is 



showing the arbitrage property of this portfolio. With a symmetric argument, one may show that also a price _x < p_ gives rise to arbitrage opportunities. Finally, the fact that the price _x_ = _p_ does not introduce arbitrage follows from an argument similar to the one used to prove this fact in the one period case (Proposition 6.1.12(ii)). □ 

##### **Pricing through equivalent martingale measures** 

Differently from the previous method, this martingale method does not requires that the contingent claim is reachable. In this case we give a more relaxed (at least in principle) notion of arbitrage price, based on the price process for the claim and on the possibility of investing to trade the claim at any date _n ∈N_ . 

**Definition 6.2.13.** _In the market model_ ( _B, S_ ) _above, assume to introduce the contingent claim ϕ_ ( _SN_ ) _allowing to trade it at any date with price process_ 



_We say that the price process_ ( _Xn_ ) _n∈N introduces arbitrage in the market if there exists a selffinancing investment strategy_ 



The argument to define the price is the same as in the one period case. The martingale method relies on the first fundamental theorem of the asset pricing. Indeed, consider the extended market ( _B, S, X_ ), with _X_ = ( _Xn_ ) _n∈N_ , looking at it as at a new risky asset. In order to be this extended market arbitrage free, by the first fundamental theorem of asset pricing (notably, its version illustrated in Remark 6.2.7) the discounted values of the assets _S, X_ must be martingales under some equivalent martingale measure. Then, taking _any_ equivalent martingale measure Q _∼_ P 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

112 

for the original market, the fact that also the discounted value of the remaining asset _X_ is a martingale under this equivalent martingale measure corresponds simply to the condition 



which provides, imposing _XN_ = _ϕ_ ( _SN_ ), 







The latter is the so called _risk-neutral valuation formula_ . Notice that, as in the one period case, we do not have a priori a unique possible price process not introducing arbitrage, as different martingale measures (if more than one martingale measure exist) may lead to different pricing. But again, if the contingent claim is hedgeable, all the risk-neutral valuation done under different martingale measures produce the same price process. 

#### **6.2.4 Completeness of the market** 

Let us come back to the extension to the case of several risky asset mentioned in Remark 6.1.9(v), exposing and commenting some facts without providing the proofs. 

We therefore consider a market model composed by a riskless asset _B_ = ( _Bn_ ) _n∈N_ given by _Bn_ = (1 + _r_ )<sup>_n_</sup> and by _d >_ 1 risky assets _S_<sup>1</sup> _, S_<sup>2</sup> _, ..., S_<sup>_d_</sup> with price processes 



We have seen in Remark 6.2.7(v) that — with suitable extension of the notion of self-financing portfolio strategy, which is now a vector of stochastic processes, of portfolio value, and of arbitrage — the market is arbitrage free if and only there exists a martingale measures for the discounted price processes 



where 



i.e., if and only if there exists Q _∼_ P such that 



where now 



In this context one naturally considered contingent claims depending on the final values of _all_ the risky assets, i.e. financial payoffs in the form 



where _ϕ_ : (0 _, ∞_ )<sup>_d_</sup> _→_ R+. Similarly to the case of one risky asset, one says that a contingent claim is reachable if there exists a self-financing portfolio strategy _h_ = ( _h_<sup>_B_</sup> _n_<sup>_, hS_</sup> _n_<sup>1</sup><sup>_, ..., hS_</sup> _n_<sup>_d_)</sup> _n∈N_<sup>0suchthat</sup> _VN_<sup>_h_=</sup><sup>_ϕ_(</sup><sup>_S_</sup> _N_<sup>1</sup><sup>_, ..., S_</sup> _N_<sup>_d_).</sup> 

**Definition 6.2.14** (Completeness of the market) **.** _The market model is said_ complete _if each contingent claim in the form ϕ_ ( _SN_<sup>1</sup><sup>_, ..., S_</sup> _N_<sup>_d_)</sup><sup>_,whereϕ_: (0</sup><sup>_, ∞_)</sup><sup>_d→_R+</sup><sup>_,isreachable._</sup> 

The Second Fundamental Theorem of Asset Pricing still holds. 

_6.2. MULTI-PERIOD FINANCIAL MODELS_ 

113 

**Theorem 6.2.15** (Second Fundamental Theorem of Asset Pricing) **.** _The market model above is complete if and only if there exists_ at most one _martingale measure on FN_<sup>_S._</sup> □ 

Joining the statements of the First and Second Theorem of Asset Pricing we conclude that 

Market arbitrage free and complete _⇐⇒∃_ ! martingale measure _._ 

#### **6.2.5 The binomial model** 

We illustrate more in detail the so called _binomial model_ . We model it by modeling (cf. Remark 6.2.1) as primary object a process _Z_ = ( _Zn_ ) _n_ =1 _,...,N_ and then defining the price process _S_ = ( _Sn_ ) _n∈N_ recursively as<sup>8</sup> 



The strong — but still meaningful — assumption that we do is that the process 



is done by a family of independent Bernoulli random variables, defined on the probability space (Ω _, F,_ P) and valued in the set _{d, u}_ , where _d, u_ are real numbers such that 0 _< d < u_ ; here, _d_ represents the “low return” case, _u_ represents the “high return” case for the risky asset _S_ . We set 



The binomial tree illustrating the evolution of the stock price is the following: 



<!-- Start of picture text -->
su 3<br>u<br>su 2<br>u<br>d<br>su su 2 d<br>u u<br>d<br>s sud<br>u<br>d d<br>sd sud 2<br>u<br>d<br>sd 2<br>d<br>sd 3<br><!-- End of picture text -->

**Proposition 6.2.16.** _Assume that_ 



_Then, there exists a unique martingale measure_ Q _for the model_<sup>9</sup> _and under this measure the sequence_ ( _Z_ 1 _, ..., ZN_ ) _is an i.i.d. sequence of Bernoulli random variables, valued in {u, d}, with common law, for j_ = 1 _, ..., N , characterized by_ 



> 8We can imagine that _Zn_ = 1 + _ρn_ where _ρn_ is the return of the risky asset in the time period _n → n_ + 1. 

> 9Hence, by the First and the Second Fundamental Theorems of Asset Pricing, the market is arbitrage free and complete. 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

114 

_Proof._ Let Q _∼_ P. By definition, Q is a martingale measure if and only if 



i.e. 



Since _Sn_ is _Fn_ -measurable, using the properties of the conditional expected value, we have 



Hence, combining the two equations above, we get that Q is a martingale measure if and only if 



Let us exploit this relation for _n_ = 0. It reads as 



which, combined with the relation Q _{Z_ 1 = _d}_ + Q _{Z_ 1 = _u}_ = 1, provides 



Let us exploit now (6.2.6) in the case _n_ = 1. It provides, splitting on the atoms _{Z_ 1 = _u}_ and _{Z_ 1 = _d}_ of _F_ 1, 



i.e., 



Combining with the clear relations 



we get, for all _k_ 1 _, k_ 2 _∈{u, d}_ , 



From the relations above, using the law of total probabilities, we deduce that 



Iterating the argument, we get 



It follows that the probability Q is uniquely determined. Under it, the sequence of random variables ( _Z_ 1 _, ..., ZN_ ) is an i.i.d. sequence with common law as in the statement. 

_6.2. MULTI-PERIOD FINANCIAL MODELS_ 

115 

Let us implement this model for pricing a contingent claim _ϕ_ ( _SN_ ). First, we notice that the distribution under Q of _Sn_ is (up to a one-to-one correspondence) the binomial one: indeed, letting _i ∈{_ 0 _, ..., n}_ be the number of “ _u_ movements” of the stock in the time periods 0 _→_ 1, ..., _n −_ 1 _→ n_ , we have 



Then, we can compute backward the price process _X_ = ( _Xn_ ) _n∈N_ as follows. 

- First, we set _XN_ = _ϕ_ ( _SN_ ) (the price at time _N_ must coincide with the payoff); 

- Then, we use the risk valuation formula to compute _XN −_ 1<sup>10</sup> : 



hence, multiplying by (1 + _r_ )<sup>_N−_1</sup> , 



• For _N −_ 2 we get 



• In general, we get 





**Remark 6.2.17.** _Notice that_ (6.2.5) _is essential for guaranteeing_ ( _qu, qd_ ) _∈_ (0 _,_ 1)<sup>2</sup> _, i.e. to get the existence of a martingale measure for the model._ □ 

**Example 6.2.18** (Bjork’s book, Ch. 2, Example 2.23) **.** _In the setting above we take_ 

- _N_ = 3 _,_ 







> 10In the third equality below we use a property of conditional expected value known as “freezing lemma”. 

_CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

116 





_Since d <_ 1 + _r < u the market is arbitrage free (and complete). The binomial tree describing the evolution of the stock is illustrated below._ 



<!-- Start of picture text -->
270<br>180<br>120 90<br>80 60<br>40 30<br>20<br>10<br><!-- End of picture text -->

_We consider the problem of pricing, through the martingale method described above, a European call option with delivery time N_ = 3 _and strike price K_ = 80 _, i.e. the contingent claim_ 



_The unique martingale measure_ Q _∼_ P _for the model is such that for each n_ = 1 _,_ 2 _,_ 3 



_We need to find the process_ ( _Xn_ ) _n_ =0 _,_ 1 _,_ 2 _,_ 3 _with the method illustrated above. First, we start from the value of the option at time N_ = 3 _: we have_ 



_and the value X_ 3 _is represented in the boxes below according to the possible occurrences of S_ 3 _._ 



<!-- Start of picture text -->
270 190<br>180<br>120 90 10<br>80 60<br>40 30 0<br>20<br>10 0<br><!-- End of picture text -->

_Now we compute X_ 2 _using_ (6.2.8) _:_ 



_6.2. MULTI-PERIOD FINANCIAL MODELS_ 

117 

_For S_ 2 _we have three occurrences: S_ 2 = 180 _, S_ 2 = 60 _, S_ 2 = 20 _. Depending on them, we have_ 



_The picture representing this stage of the algorithm is the following one:_ 



<!-- Start of picture text -->
270 190<br>180 100<br>120 90 10<br>80 60 5<br>40 30 0<br>20 0<br>10 0<br><!-- End of picture text -->

_Using_ (6.2.9) _we have the valuation at n_ = 1 _:_ 



_Finally, we have the valuation at n_ = 0 _:_ 



_Below the picture of the final stage:_ 



<!-- Start of picture text -->
270 190<br>180 100<br>120 52.5 90 10<br>80 27.5 60 5<br>40 2.5 30 0<br>20 0<br>10 0<br><!-- End of picture text -->

118 _CHAPTER 6. FINANCIAL MODELS IN FINITE PROBABILITY SPACES_ 

## **Chapter 7** 

# **An introduction to Markov chains** 

We introduce and discuss some topics for another very important class of stochastic processes, whose range of applications is huge and far to be exhausted by this chapter. It is the concept of Markov chain, relying on the idea of a stochastic process _X_ whose evolution occurs “without memory of the past”. 

### **7.1 A heuristic introduction** 

Let us illustrate heuristically the concept of Markov chain by some examples taken by [14] and [12]. 

**Example 7.1.1** (Salisburg’s weather) **.** _In Salisburg the weather is very variable. There are three states for the weather: Sunny (S), Raining (P), Snowing (N). Never there are two subsequent sunny days. If it is sunny in a day, the day after there will be snow or rain with equal probability. It it is raining or snowing, the day after there will be, with the same probability, the same weather or another weather. In the latter case, the change will occur with the same probability. The described phenomenon is represented by the following graph and by the following matrix._ 



<!-- Start of picture text -->
1/2<br>s/0 1/2 1/2<br>‘pa TSS<br>n\i/a 1/4 1/2<br>10; 1/2 8) dee Se<br>1201")<br><!-- End of picture text -->

_Interesting questions might be questions like the following ones:_ 

_1. If today is sunny, what is the probability that in two weeks it is raining?_ 

_2. What is the average number of sunny days in a year?_ 

**Example 7.1.2** (Drunk’s walking) **.** _A drunk guy exits from the pub and has to come back to home. The home is 200 meters on his right. On the other hand, 100 meters on his left there is a lake. The guy does steps of length 1 meter towards the left and towards the right with the same probability._<sup>1</sup> 

> 1The probabilistic model is something that we bave already seen: a random walk with steps valued in _{−_ 1 _,_ 1 _}_ with equal probability 1 _/_ 2. 

119 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

120 



<!-- Start of picture text -->
a<br><!-- End of picture text -->

_An interesting question might be: what is the probability that the guy will reach eventually his home?_<sup>2</sup> 

We are going to provide a probabilistic framework for this kind of phenomena and for this kind of questions. 

### **7.2 The concept of Markov chain** 

In this section we will adopt the following convention concerning conditional probabilities (if not differently specified): when an expression of the form P( _· | H_ ) appears in some statement, it is implicitly assumed to come with the sentence _“whenever_ P( _H_ ) _>_ 0 _”_ . Moreover, 

- (i) the set of times is _N_ = N; 

- (ii) the reference filtration, generated by an underlying process _ξ_ , will be simply denoted by ( _Fn_ ) _n∈_ N; unless differently specified, the various notions possibly depending on the filtration will be referred to this filtration. 

**Definition 7.2.1** (Time-homogeneous Markov chain) **.** _Let_ (Ω _, F,_ P) _be a probability space. A_ time homogeneous Markov chain _with respect to the filtration_ ( _Fn_ ) _n∈N and valued in the (discrete) state space E is an adapted stochastic process {Xn_ : Ω _→ E}n∈_ N _such that_ 



From now on, the attribute _time-homogeneous_ will be skipped. The space of trajectories of a Markov chain having _E_ as state space is _E_<sup>N</sup> . 

Let us try to understand what are, given a Markov chain, the “relevant ingredients”. We may individuate three of them: 

1. The state space _E_ . 

2. The initial distribution, i.e, the law of _X_ 0 under P, that we denote by _µ_ 0. If _µ_ 0 is concentrated at _x ∈ E_ , i.e. 



we say that the Markov chain is exiting from the state _x_ . 

> 2A question that actually we already discussed: see the gambler’s ruin. But this is a very special model of the type of processes that we are going to describe. 

_7.3. QUESTIONS OF EXISTENCE: CONSTRUCTION OF MARKOV CHAINS_ 

121 

3. The transition of the Markov chain in one time step, represented by the _transition probabilities p_ ( _x, y_ ) for _x, y ∈ E_ . Clearly, 





<!-- Start of picture text -->
y 1<br>y 2<br>� p ( x, y ) = 1<br>x ... Spazio E<br>y∈E<br>yi<br>yN<br>p ( x, yi )<br>p ( x, y 2)<br>p ( x, y 1)<br>p ( x, yN )<br><!-- End of picture text -->

To these family is associated the family of probability measures **T** = ( **T** _x_ ) _x∈E_ on _E_ defined as 



This family of probability measures in ( _E, E_ ), indexed in _E_ , is called the _transition kernel_ of the Markov chain. 

A special relevant case is when _N_ := _|E| < ∞_ . In this case, we may conveniently “order” the elements of _E_ with a bijection _{_ 1 _, ..., N } → E_ and organize the numbers _p_ ( _x, y_ ) in a matrix **M** _∈_ R<sup>_N×N_</sup> : 



The transition kernel is then represented by the matrix _M_ , which is called the _transition matrix_ associated to the Markov chain _X_ . Such matrix **M** = ( _mij_ ) _i,j_ =1 _,...,N_ then satisfies 



Matrices satisfying (7.2.4) are called _stochastic matrices_<sup>3</sup> . 

### **7.3 Questions of existence: construction of Markov chains** 

Now we work in the opposite direction, by posing the following questions concerning existence and uniqueness of Markov chains. We pose the question following questions. Let ( _E, µ_ 0 _,_ **T** ) be a triple where: 

1. _E_ a discrete space; 

2. _µ_ 0 a probability law on _E_ ; 

3. **T** = ( **T** _x_ ) _x∈E_ a transition kernel in the space _E_ ; that is, a family of probability measures ( **T** _x_ ) _x∈E_ on _E_ . 

We address the following questions: 

> 3To avoid misunderstanding: _the entries of stochastic matrices are not random_ . 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

122 

1. Does it exist a Markov chain admitting _E_ as state space, _µ_ 0 as initial distribution, and **T** as transition kernel? 

2. If the answer to the question above is positive, can we state “somehow uniqueness” of such Markov chain? 

**Theorem 7.3.1** (Existence and uniqueness in law of Markov chains) **.** _Let_ ( _E, µ_ 0 _,_ **T** ) _be a triple with E a discrete space, µ_ 0 _a probability law on E, and_ **T** _a transition kernel. Then, we have the following statements._ 

_1. (Existence) There exists a Markov chain admitting E as state space, µ_ 0 _as initial distribution, and_ **T** _as transition kernel._ 

_2. (Uniqueness in law) If X, X_<sup>ˆ</sup> _are two Markov chains defined on_ (Ω _, F,_ **P** ) _and_ (Ω<sup>ˆ</sup> _, F_<sup>ˆ</sup> _,_ P<sup>ˆ</sup> ) _respectively, admitting E as state space, µ_ 0 _as initial distribution, and T as transition kernel, then they have the same law on the space of trajectories E_<sup>N</sup> _; that is, for each finite set of indices_ ( _i_ 1 _, ..., ik_ ) _and each B ⊆ E_<sup>_k_</sup> _, we have_ 



_Proof._ See [14, Ch. 1, Theorems 1.1 and 1.2]. The construction for the existence is done over the so called canonical space, i.e. the space of trajectories 



Then, the process _X_ is represented just by the canonical projections: _Xn_ ( _ω_ ) = _ω_ ( _n_ ) _._ 

Actually a strong statement is possible: given ( _E,_ **T** ) with _E_ a discrete space and **T** a transition kernel, there exist a couple (Ω _, F_ ), a family (P _x_ ) _x∈E_ of probability measures on (Ω _, F_ ), and an _E_ -valued stochastic process _X_ = ( _Xn_ ) _n∈_ N such that _Xn_ is a Markov chain exiting from _x_ with transition kernel **T** under P _x_ . Given that, the statement of Proposition 7.3.1 is a consequence. It suffices to take as probability on the same space (Ω _, F_ ) the convex envelope of the probabilities P _x_ according to _µ_ 0; that is 



We will make use of this construction based on the family (P _x_ ) _x∈E_ . More precisely, in the remainder of this chapter, typically: 

- (i) _X_ will be a stochastic precess on (Ω _, F_ ) adapted to a reference filtration and valued in _E_ ; 

- (ii) for every _x ∈ E_ , under P _x_ , the process _X_ is a Markov chain with transition kernel **T** exiting from _x_ ; that is, such that P _x{X_ 0 = _x}_ = 1 (equivalently, _L_<sup>P</sup><sup>_x_</sup> ( _X_ 0) = _δ{x}_ ); 

- (iii) when we will use P, this will generically denote a probability on (Ω _, F_ ) such that _X_ is still a Markov chain with transition kernel **T** , but with generic initial law _µ_ 0 = _L_<sup>P</sup> ( _X_ 0) under it; 

- (iv) the expected value under P _x_ will be denoted by E _x_ . 

**Remark 7.3.2.** _Clearly, given what said above, we can generalize further the result above. Given_ ( _E,_ **T** ) _with E a discrete space and_ **T** _a transition kernel, there exists a couple_ (Ω _, F_ ) _, a family_ (P _µ_ 0) _µ_ 0 _∈P_ ( _E_ ) _of probability measures on_ (Ω _, F_ ) _, and an E-valued stochastic process X_ = ( _Xn_ ) _n∈_ N _such that X is a Markov chain with initial distribution µ_ 0 _._ 

_7.4. MARKOV CHAINS AND STOCHASTIC DIFFERENCE EQUATIONS_ 

123 

### **7.4 Markov chains and stochastic difference equations** 

Stochastic difference equations are natural and very convenient models for Markov chains. Let (Ω _, F,_ P) be a probability space and let ( _ξn_ ) _n∈_ N be a sequence of i.i.d. random variables valued in a discrete space _F_ . Let _X_ 0 be another _F_ 0-measurable random variable valued in the discrete space _E_ independent of the sequence ( _ξn_ ) _n∈_ N0, and let _f_ : _E × F → E_ be a given function. We define recursively the process 



Clearly, _Xn_ only depends on _ξ_ 0 _, ξ_ 1 _, ..., ξn_ , hence is independent of _ξn_ +1. For the same reason, for each _n ∈_ N and _A ∈Fn_ , we need to have _A_ independent of _ξn_ +1 as well. Hence, 



So, setting 



we see that the process ( _Xn_ ) _n∈_ N is a Markov chain with transition probabilities given above. 

The following question is relevant: given a Markov chain, is it representable as a stochastic difference equation? We provide a result in this sense. 

**Theorem 7.4.1.** _Let_ ( _E, µ_ 0 _,_ **T** ) _be a triple with E a finite space, µ_ 0 _a probability law on E, and_ **T** = ( **T** _x_ ) _x∈E a transition kernel on E satisfying under the (strong) assumption_ 



_Then, there exists a probability space_ (Ω _, F,_ P) _supporting a random variable X_ 0 _with law µ_ 0 _and an i.i.d. sequence of random variables ξ_ = ( _ξn_ ) _n∈_ N0 _valued in {_ 1 _, ..., M }, and a function f_ : _E × {_ 1 _, .., M } → E such that the stochastic difference equation_ 



_defines a Markov chain valued in E, with initial distribution µ_ 0 _and transition kernel_ **T** _._ 

_Proof._ Consider, on _{_ 1 _, ...., M }_ , the uniform distribution 



For each _x ∈ E_ , we can find a partition ( _By_<sup>_x_)</sup><sup>_y∈E_of</sup><sup>_{_1</sup><sup>_, ..., M}_suchthat</sup> 

_µ_ ( _By_<sup>_x_) =</sup><sup>**T**</sup><sup>_x_(</sup><sup>_y_) =</sup><sup>_p_(</sup><sup>_x, y_)</sup><sup>_._</sup> 

Define 



Let (Ω _, F,_ P) be a probability space supporting a random variable _X_ 0 with law _µ_ 0 and an i.i.d. sequence of random variables _ξ_ = ( _ξn_ ) _n∈_ N0, valued in _{_ 1 _, ..., M }_ and with common law _µ_ , independent of _X_ 0. Define by recurrence 



_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

124 



<!-- Start of picture text -->
x<br>f<br>y 1 y 2 =  f ( x, α ) . . . yN<br>B x B x B x . . . B x<br>y 1 y 2 y 3 yN<br>0 1<br>α<br>p ( x, y 1) p ( x, y 2) p ( x, yN )<br><!-- End of picture text -->

Then 



The claim follows. 

**Example 7.4.2.** _In the setting above, consider the process defined, let {ξn}n≥_ 0 _be an i.i.d. sequence of Bernoulli random variables of parameter_ 2 _/_ 3 _valued in {−_ 1 _,_ 1 _} (i.e._ P _{ξn_ = 1 _}_ = 2 _/_ 3 _). Define, recursively on n ≥_ 0 _,_ 



_Then, X is not a Markov process. We clearly have Xn ∈{−_ 1 _,_ 1 _}, X_ 2 = _ξ_ 2 _, and_ 



_Then,_ 

_whereas_ 





Figure 7.1: Grafico delle dipendenze: _X_ 4 “guarda indietro” di due passi. 

_7.5. TRANSITION OF MARKOV CHAINS: THREE POINTS OF VIEW_ 

125 

### **7.5 Transition of Markov chains: three points of view** 

Let _X_ be a Markov chain valued in _E_ with a transition kernel **T** assigned. Given an initial distribution of _X_ 0, the distribution of _Xn_ is uniquely determined. We may look at this evolution from three distinct points of view: microscopic, macroscopic, and functional. 

##### **Transition probabilities** 

We have already described by the numbers _{p_ ( _x, y_ ) _}x,y∈E_ the transition of the Markov chain in one step. What is the probability of passing from the state _x_ to the state _y_ in _exactly n_ steps? That is, what is the value of 



By time homogeneity, this corresponds to asking: what is the value of 



We know that: 



By the law of total probability, the following recursive relation holds: 



This is a specific case of the more general _Chapman-Kolmogorov_ equation: 





<!-- Start of picture text -->
Intermediate states z ∈ E<br>z 1<br>Start z 2 Destination<br>x y<br>...<br>zi<br>zN<br>p ( n + m ) ( x, y ) = � zi∈E p ( m )( x, zi )  · p ( n )( zi, y )<br>p ( m )( x, zi ) p ( n )( zi, y )<br>p ( m )( x, z 1) p ( n )( z 1 , y )<br><!-- End of picture text -->

Figure 7.2: Visual representation of the Chapman-Kolmogorov equation. 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

126 

##### **Law transition** 

A second and more abstract view looks at how the probability law evolves. Let _P_ ( _E_ ) be the space of probability distributions on _E_ and define the operator 



To gain an intuition, we can compare the individual and global perspectives: 

- _Individual (p_ ( _x, y_ ) _):_ Tracks a single particle starting at _x_ ; it tells us where it is likely to be tomorrow. 

- _Population (T ):_ Tracks the entire probability mass. If _E_ represents a set of cities and _µ_ 0( _x_ ) the population percentage in city _x_ , then ( _T µ_ 0)( _y_ ) is the population percentage in city _y_ tomorrow, after redistribution. 

Then, the evolution of the law of the Markov chain is given by the rule 

_µn_ +1 = _T µn._ 



<!-- Start of picture text -->
µn +1( x 3)<br>µn ( x 3)<br>T µn +1( x 2)<br>µn ( x 2)<br>µn +1( x 1)<br>µn ( x 1)<br>µn µn +1 =  T µn<br><!-- End of picture text -->

By induction, letting _µn_ = _L_ ( _Xn_ ), we have _µn_ = _T_<sup>_n_</sup> _µ_ 0. This view leads to two fundamental questions: 

1. **Existence of a limit:** Is it guaranteed that _µ∞_ := lim _n→∞ T_<sup>_n_</sup> _µ_ 0 exists? 

2. **Invariant distribution:** Does there exist _µ_ � _∈P_ ( _E_ ) such that _T µ_ � = _µ_ �? This represents a _dynamic equilibrium_ : flows between states are perfectly balanced. 

##### **Transition operator** 

A third way of looking at the transition is to observe how it transforms real-valued bounded functions _B_ ( _E_ ) defined on the state space. We define the operator: 



_L_ is a linear operator such that _L_ **1** _E_ = **1** _E_ . By induction, E _x_ [ _f_ ( _Xn_ )] = ( _L_<sup>_n_</sup> _f_ )( _x_ ). The Markov property implies: 



In the modern theory of Markov chains the equality 



_7.6. THE STRONG MARKOV PROPERTY_ 

127 

is taken as definition of (time-homogenous) Markov chain; that is, given an operator _L_ on _B_ ( _E_ ) satisfying the properties 1 and 2 listed above, a process _X_ is said to be a (time homogeneous) Markov chain with transition operator _L_ if (7.5.4) holds for every _f_ : _E →_ R bounded. This view allows more natural generalization to the case of uncountable state spaces and continuous time. The definitions turn out to be equivalent. Indeed, taking (7.5.4) as definition of Markov chain and applying it to _f_ = **1** _{y}_ , we get 



Hence, 



coming back to original definition of Markov chain. 

### **7.6 The strong Markov property** 

Let _τ_ be a a stopping time with respect to the reference filtration ( _Fn_ ) _n∈_ N. We define the _σ_ -algebra of the events prior to _τ_ as 



Intuitively, the event in _Fτ_ are the events which are observable before _τ_ . Let us illustrate this by an example. 

**Example 7.6.1.** _Let X_ = ( _Xn_ ) _n∈_ N _be a random walk valued in_ Z _with steps valued in {−_ 1 _,_ 1 _} and starting at X_ 0 = 0 _. Let_ 



_This is a stopping time. Clearly τ ≥_ 2 _._ 

_(i) The event_ 



_belongs to Fτ . Indeed, A ∈F_ 2 _. For n <_ 2 _, A ∩{τ ≤ n}_ = _∅∈Fn. For n ≥_ 2 _, A ∈F_ 2 _⊆Fn and {τ ≤ n} ∈Fn, thus A ∩{τ ≤ n} ∈Fn._ 

_(ii) The event_ 



_belongs to Fτ . Indeed, for any n ∈_ N _:_ 



_Since {_ min _k≤j Xk ≤−_ 1 _} ∈Fj and {τ_ = _j} ∈Fj, each term of the union is in Fj ⊆Fn. (iii) The event_ 



_does not belong to Fτ . Indeed, for n_ = 2 _:_ 



_Clearly A ∩{τ ≤_ 2 _} ∈F/_ 2 _because it depends on X_ 3 _._ 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

128 

**_Intuition._** _The σ-algebra Fτ represents the information accumulated by the process up to the (random) stopping time τ . An event A belongs to Fτ if, at the moment we observe τ , we are able to determine whether A has occurred or not without having to look at the future of the chain._ 

- **_Event (i):_** _A_ = _{_ sup _n_ =0 _,_ 1 _,_ 2 _Xn ≤_ 1 _}. Since we know that τ ≥_ 2 _almost surely, the stopping time always occurs ”after” or ”at the same time” as n_ = 2 _. Consequently, when we stop at τ , we have already observed the entire trajectory necessary to determine the maximum of the first three steps. The information is already part of our ”past”._ 

- **_Event (ii):_** _A_ = _{_ inf _n_ =0 _,...,τ Xn ≤−_ 1 _}. This event concerns the history of the trajectory covered exactly up to the instant of stopping. Imagine recording the minimum value reached during the walk; the moment the process hits the threshold (i.e., at τ ), the value of the infimum is a fact already acquired and observable. No information subsequent to τ is needed._ 

- **_Event (iii):_** _A_ = _{X_ 3 _≥_ 2 _}. This event_ **_does not_** _belong to Fτ because it violates the principle of causality. If the chain reaches the threshold quickly, for example with τ_ = 2 _(meaning X_ 0 = 0 _, X_ 1 = 1 _, X_ 2 = 2 _), the stopping time forces us to stop before we have been able to observe X_ 3 _. To determine if A is true, we would have to look into the future beyond the stopping time, which is forbidden by the structure of Fτ ._ 



<!-- Start of picture text -->
Xn<br>Past (In Fτ ) Future (Not in Fτ )<br>τ<br>X 4 = 4<br>Is X 3 ≥ 2 ?<br>Xτ = 2 Possible: X 3 ∈{ 1 ,  3 }<br>Unobservable in Fτ<br>X 1 = 1<br>n<br>X 0 = 0 3<br><!-- End of picture text -->

**Lemma 7.6.2.** _Let k ∈_ N _. If τ is a stopping time, then σ_ := _τ_ + _k is a stopping time. Proof._ Notice that _σ ≥ k_ . So, for all _n < k_ we have 



On the other hand, given _n ≥ k_ , we have 



proving the claim. 

**Theorem 7.6.3** (Strong Markov property) **.** _Let_ (Ω _, F,_ P) _be a probability space, let X be a Markov chain with transition kernel_ **T** _defined on it, and let τ be a stopping time. Let H_ := _{τ < ∞} and assume that_ P( _H_ ) _>_ 0 _. Consider on_ (Ω _, F,_ P _H_ ) _the process_ 



_7.6. THE STRONG MARKOV PROPERTY_ 

129 

_and the filtration_ 



_Then, Y is a Markov chain with respect to_ ( _Gn_ ) _n∈_ N _with transition operator_ **T** _(and state space E) under_ P _H ._ 

_Proof._ (i) First we prove that _Y_ is adapted to ( _Gn_ ) _n∈_ N. For that, given _B ∈E_ and _n ∈_ N, we need to show that 

_{Yn ∈ B} ∈Gn ∀n ∈_ N _._ 

We will prove that 



then, by Lemma 7.6.2, up to substituting _τ_ with _σ_ := _τ_ + _n_ , the general claim follows. We have 



Now, notice that, since _X_ is adapted and _τ_ is a stopping time, 



The condition _{Y_ 0 _∈ B} ∈Fτ_ corresponds to 



Now, by (7.6.2), 



In any case 



Hence, by (7.6.1), we get (7.6.3). 

(ii) We have to check that, for every _n ∈_ N, we have 



We will prove that 



then, since _{τ < ∞}_ = _{σ < ∞}_ , up to substituting _τ_ with _σ_ := _τ_ + _n_ , the general claim follows. 

Set 



and notice that 



by definition of _Fτ_ . We have, given _A ∈G_ 0 = _Fτ_ , 



_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

130 

Since _X_ is a Markov chain with transition operator **T** , we then have 



Hence, combining the equalities above we get 

the claim. 

### **7.7 Visits and state classification** 

Given a Markov chain, we want to distinguish their states according to their nature with respect to the overall chain. To introduce the concepts, consider the following graph representing a Markov chain. 



<!-- Start of picture text -->
Q——®<br>=| oO:<br>® ®<br>"i So)<br>1)<br><!-- End of picture text -->

Notice that we have only (directed) arrows, the transition probabilities are not reported in the graph. If a directed arrow from state _x_ to state _y_ is in the graph, this means that the transition probability _p_ ( _x, y_ ) is strictly positive. We are interested in describing the possibility of reaching a state from another one. We start with some definitions. 

**Definition 7.7.1.** _Given x, y ∈ E, we write:_ 

_(i) x →_<sup>_n_</sup> _y, if p_<sup>(</sup><sup>_n_)</sup> ( _x, y_ ) _>_ 0 _; (ii) x → y, if there exists n ∈_ N _such that x →_<sup>_n_</sup> _y; we say that y_ is accessible form _x;_ 

_7.7. VISITS AND STATE CLASSIFICATION_ 

131 

_(iii) x̸ → y, if there is no n ∈_ N _such that x →_<sup>_n_</sup> _y; we say that y_ is not accessible form _x;_ 

_(iv) x ↔ y, if x → y and y → x; we say that x_ and _y_ communicate (each other) _._ 

Clearly, the relation _→_ is transitive: 



More precisely, 



As a matter of fact, the relation _↔_ is reflexive, symmetric, and transitive. Hence, it is an equivalence relation on _E_ . In particular, the subsets _C ⊆ E_ such that _x ↔ y_ for every _x, y ∈ C_ are disjoint. Naturally, we are led to give the following. 

##### **Definition 7.7.2.** 

- _(i) The equivalence classes with respect to the relation ↔ are called called_ irreducible classes _of the Markov chain._ 

- _(ii) If there is only E as irreducible class, the Markov chain is said_ irreducible _._ 

With respect to the graph above, we have this representation of the irreducible classes. 



<!-- Start of picture text -->
2)<br><!-- End of picture text -->

A main question in the theory of Markov chains, related to the characterization of the irreducible classes, is if and how many times the chain visits a given subset _A_ of the state space _E_ — typically, a given state _x_ . So, given _x ∈ E_ , define the first time of visit of the chain to the state _x_ after time 0; that is, the stopping times 



The following quantities are of interest: 



Notice that _F_ ( _x, x_ ) represents the probability of return to the state _x_ for a Markov chain with transition kernel **T** exiting from _x_ . We classify the states of the Markov chain according to _F_ . 

**Definition 7.7.3.** _We say that x ∈ E is_ 

_(i)_ transient _if F_ ( _x, x_ ) _<_ 1 _;_ 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

132 

_(ii)_ recurrent _if F_ ( _x, x_ ) = 1 _;_ 

Notice that, if _p_ ( _x, x_ ) = 1, then _F_ ( _x, x_ ) = 1. In this case, the state _x_ is said _absorbing_ . The reason of the terminology _absorbing_ is clear: if a Markov chain enters into an absorbing state, it remains there forever. The terminology _recurrent_ and _transient_ is obscure so far. To motivate it, let us consider the following objects. Define, recursively, the random times “times of visits to _x_ after _n_ = 0”, 



**Theorem 7.7.4.** _We have_ 



_Proof._ Given _k ∈_ N0, let _H_ := _{τx,k < ∞}_ . 







Let us consider the process 



By Theorem 7.6.3, the process _Y_ is a Markov chain with transition kernel **T** under P<sup>_H_</sup> _x_ exiting from _x_ . Then 

P<sup>_H_</sup> _x_<sup>_{τx,k_+1</sup><sup>_< ∞}_=</sup><sup>_F_(</sup><sup>_x, x_)</sup><sup>_,_</sup> 

and the claim follows. 

Define the random variable “number of visits at _x_ after _n_ = 0” 



We have 

_{Vx_ = _∞}_ = lim sup _n→∞_<sup>_{Xn_=</sup><sup>_x}._</sup> 

The following result gives reason of the adopted terminology. 

**Corollary 7.7.5.** _We have the following._ 

_(i) If x is transient, then_ 







_Proof._ (i) By Theorem 7.7.4, we have 



Then, _Vx_ must be finite **P** _x−_ a.s., i.e. (7.7.2). 

_7.7. VISITS AND STATE CLASSIFICATION_ 

133 

(ii) By Theorem 7.7.4, 





**Remark 7.7.6.** _Actually, we have the following more general claims:_ 

_(i) If x is transient, then_ 



_(ii) If x is recurrent, then_ 



_precisely:_ 



We also deduce this other characterization of the recurrent and transient states. 

**Corollary 7.7.7.** _Let x ∈ E._ 



_Proof._ Let _x ∈ E_ . We have 



We conclude by Corollary 7.7.5. 

Given a sequence ( _An_ ) _n∈_ N, define 



The chain does visit a finite number or transient states only a finite number of times. 

**Proposition 7.7.8.** _Let A ⊆ E be a finite set of transient states. Then,_ 



_that is the set A is a.s. visited only a finite number of times by the Markov chain. In other terms, the chain leaves the set A definitively a.s._ 

_Proof._ Let _A_ = _{x_ 1 _, ..., xM }_ . For all _xi ∈ A_ , _i_ = 1 _, ..., M_ , denoting by _Vi_ the random variable “number of visits at _xi_ ”, we have _Vi < ∞_ P-a.s.. Therefore, for P-a.e. _ω ∈_ Ω, and all _i_ = 1 _, ..., M_ , there exists _ni_ ( _ω_ ) _∈_ N such that 



which says 



We have therefore proved (7.7.7). 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

134 

**Remark 7.7.9.** _By virtue of Proposition 7.7.8, if E is finite, then the chain admits a recurrent state. Indeed, if E is finite and is done only by transient states, we have E_<sup>_c_</sup> = _∅ and_ (7.7.7) _with A_ = _E would provide_ 



_which is clearly absurde._ 

The recurrence is “contagious”, as shown by the following. 

**Theorem 7.7.10.** _Let x be recurrent and let x → y. Then y is recurrent._ 

_Proof._ If _y_ = _x_ , there is noting to prove. Let then _y̸_ = _x_ . Set 



and _H_ = _{ρy < ∞}_ . Since _x → y_ , we have P _x_ ( _H_ ) _>_ 0. Consider the process 



Then, by strong Markov property, _Y_ is a Markov chain under P<sup>_H_</sup> _x_<sup>exitingfrom</sup><sup>_y_.Ontheother</sup> hand, the chain _X_ will visit the state _x_ infinitely many times P _x_ -a.s., hence also P<sup>_H_</sup> _x_<sup>-a.s..So,also</sup> _Y_ will visit _x_ infinitely many times P<sup>_H_</sup> _x_<sup>-a.s.,showingthat</sup><sup>_y→x_.Since,byassumption,</sup><sup>_x→y_,</sup> it follows that _x ↔ y_ . Therefore, there exist _h, k ∈_ N0 such that 



Notice now that 

Hence 



Since _x_ is recurrent, the right hand side is equal to _∞_ by Corollary 7.7.7. Therefore, 



which also implies 



Again by Corollary 7.7.7, we conclude that _y_ is recurrent. 

**Definition 7.7.11.** _Let X be an irreducible Markov chain valued in E. We say that_ 

- _(i) X is_ irreducible recurrent _if any x ∈ E is recurrent;_ 

- _(ii) X is_ irreducible transient _if any x ∈ E is transient._ 

By virtue of the Theorem 7.7.10, we have the following dichotomy. 

**Corollary 7.7.12.** _An irreducible Markov chain is either irreducible recurrent or irreducible transient._ 

**Remark 7.7.13.** _If E is finite, then an irreducible chain is recurrent (cf. Remark 7.7.9 and Theorem 7.7.10)._ 

**Example 7.7.14.** _Baldi, Esempio 5.3, 5.5. Grafi di Woess, p.1, 23, 24, 25, 30 con discussione. Qualche esempio da Bremaud._ 

_7.8. INVARIANT MEASURES_ 

135 

#### **Summary tables:** 

The following tables synthesize the criteria for classifying individual states and the global behavior of irreducible Markov chains. 

**Table 1: Classification of a single state (Definition 7.7.3)** 

This table summarizes the criteria used to determine the nature of a state _x ∈ E_ . 

||**Transient State**|**Recurrent State**|
|---|---|---|
|**Return Probability**|_F_(_x, x_)_<_1|_F_(_x, x_) = 1|
|**Number of Visits**|_Vx < ∞_P_x_-a.s. (Cor. 7.7.5)|_Vx_ =_∞_P_x_-a.s. (Cor. 7.7.5)|
|**Analytical Criterion**|~~�~~<br>_n≥_1 <sup>_p_(</sup><sup>_n_)(</sup><sup>_x, x_)</sup><sup>_< ∞_(Cor. 7.7.7)</sup>|~~�~~<br>_n≥_1 <sup>_p_(</sup><sup>_n_)(</sup><sup>_x, x_) =</sup><sup>_∞_(Cor. 7.7.7)</sup>|



##### **Table 2: Key results** 

Key results governing the long-term behavior and the nature of states. 

||**Result**|**Reference**|
|---|---|---|
|**Finite space** _E_|A finite state space must contain at least one<br>recurrent state.|Remark 7.7.9|
|**Transient sets**|A finite set of transient states is visited only<br>finitely often; the chain leaves it definitively a.s.|Prop. 7.7.8|
|**Contagion**|If_x_is recurrent and_x →y_, then_y_ is also recur-<br>rent.|Theorem 7.7.10|



##### **Table 3: Nature of irreducible Markov chains** 

This table summarizes the global classification when the chain is irreducible (i.e., it consists of a single irreducible class). 

||**Condition**|
|---|---|
|**Irreducible Recurrent**|Every state _x ∈E_ is recurrent.|
|**Irreducible Transient**|Every state _x ∈E_ is transient.|
|**Dichotomy**|An irreducible Markov chain is either irreducible recur-<br>rent or irreducible transient (Cor. 7.7.12).|



### **7.8 Invariant measures** 

In this section we address questions of existence and uniqueness of invariant probability measures of a Markov chain. We limit ourselves just to some results, warning that such results can be extended and streghtened. 

We recall the transition operator _T_ acting on the space of probability measures _P_ ( _E_ ): 



_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

136 

It can be extended to the space of (positive ) measure _M_<sup>+</sup> ( _E_ ): 



**Definition 7.8.1** (Invariant probability measure) **.** _An_ invariant probability measure _(or_ stationary distribution _) for the Markov chain X is a probability distribution µ_ � _∈P_ ( _E_ ) _such that_ 



We are interested in the existence and uniqueness of such a � _µ_ . When _|E| < ∞_ , this corresponds to a problem of linear algebra. Letting _M_ be the transition matrix associated to the Markov chain, one seeks a non-negative vector _π_ with components summing up to 1 such that 



which corresponds to finding a non-negative left eigenvector of _M_ with eigenvalue 1. 

**Example 7.8.2.** _The symmetric random walk on_ Z _(with p_ = 1 _/_ 2 _) does not admit any invariant probability measure. To see that, assume, by contradiction, that µ_ � _is an invariant probability measure. Then:_ 



_Since_<sup>�</sup> _k∈_ Z<sup>_µ_�</sup><sup>_{k}_=1</sup><sup>_,wemusthave_lim</sup><sup>_k→±∞µ_�</sup><sup>_{k}_=0</sup><sup>_.Thisimpliesthatthereexistsk∗∈_Z</sup> _where the measure attains its maximum: µ_ � _{k_<sup>_∗_</sup> _}_ = sup _k∈_ Z � _µ{k}. From_ (7.8.3) _, we get:_ 



_which holds only if µ_ � _{k_<sup>_∗_</sup> _−_ 1 _}_ = _µ_ � _{k_<sup>_∗_</sup> + 1 _}_ = _µ_ � _{k_<sup>_∗_</sup> _}. By induction, µ_ � _{k} must be constant for all k, which contradicts the fact that its sum is_ 1 _._ 

**Proposition 7.8.3.** _Let µ_ � _be an invariant probability measure for X. If x is transient, then µ_ � _{x}_ = 0 _._ 

_Proof._ Let _X_ 0 _∼ µ_ �. Since _µ_ � is invariant, P( _Xn_ = _x_ ) = _µ_ � _{x}_ for all _n ≥_ 0. By Proposition 7.7.8, if _x_ is transient, the number of visits _Vx_ is finite a.s., hence P(lim sup _n→∞{Xn_ = _x}_ ) = 0. Using the property of the limit of measures: 



**Proposition 7.8.4.** _Let X be an irreducible Markov chain. If µ_ � _is an invariant probability measure for X, then µ_ � _{x} >_ 0 _for every x ∈ E._ 

_Proof._ Since _µ_ � is a probability measure, there must exist at least one state _x_ 0 _∈ E_ such that _µ_ � _{x_ 0 _} >_ 0 (otherwise the total mass<sup>�</sup> _z∈E_<sup>_µ_�</sup><sup>_{z}_wouldbe0).</sup> 

Let _y_ be any state in _E_ . By the irreducibility of the chain, there exists an integer _m ≥_ 1 such that _p_<sup>(</sup><sup>_m_)</sup> ( _x_ 0 _, y_ ) _>_ 0. Using the invariance property _µ_ � = _T_<sup>_m_</sup> _µ_ �, we have: 



Since both _µ_ � _{x_ 0 _}_ and _p_<sup>(</sup><sup>_m_)</sup> ( _x_ 0 _, y_ ) are strictly positive, it follows that _µ_ � _{y} >_ 0. 

_7.8. INVARIANT MEASURES_ 

137 

#### **7.8.1 Existence and uniqueness** 

To address the question of existence and uniqueness of invariant probability measures, we first introduce a fundamental construction based on the regenerative properties of recurrent states. For a recurrent state _x_ , we define a measure that counts the expected number of visits to any state _y_ during a single “cycle” (the time between two consecutive visits to _x_ ). 

**Definition 7.8.5.** _Let x ∈ E be a recurrent state. We say that:_ 

- _(i) x is_ positive recurrent _if_ E _x_ [ _ρx_ ] _< ∞;_ 

- _(ii) x is_ null recurrent _if_ E _x_ [ _ρx_ ] = _∞._ 

To address existence and uniqueness, we define the measure _νx_ associated with a recurrent state _x_ , which counts the expected time spent in each state during a single regenerative cycle. 

**Definition 7.8.6.** _Let x ∈ E be a recurrent state. We define the measure νx as:_ 



**Proposition 7.8.7.** _If x is a recurrent state, then the measure νx is invariant for T ; that is,_ 

_T νx_ = _νx._ 

_Proof._ For any _y ∈ E_ , we compute: 



We split the sum considering whether the return to _x_ occurs at time _n_ + 1: 



- If _y̸_ = _x_ , then P _x_ ( _Xρx_ = _y_ ) = 0. Since P _x_ ( _X_ 0 = _y, ρx >_ 0) = 0, the sum is exactly _νx{y}_ . 

- If _y_ = _x_ , the first sum is 0 (since _Xm_ = _x_ contradicts _ρx > m_ ). The second term is P _x_ ( _Xρx_ = _x_ ) = 1 because _x_ is recurrent. Since _νx{x}_ = 1, the equality holds. 

**Proposition 7.8.8.** _Let X be an irreducible recurrent Markov chain. For a fixed x ∈ E:_ 

_(i) νx{x}_ = 1 _._ 

- _(ii) For any y ∈ E, νx{y} < ∞._ 

_(iii) νx_ ( _E_ ) = E _x_ [ _ρx_ ] _._ 

_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

138 

_Proof._ **(i)** Immediate from definition: for _n_ = 0, **1** _{X_ 0= _x}_ = 1. For _n ≥_ 1, **1** _{Xn_ = _x,ρx>n}_ = 0. **(ii)** By irreducibility, there exists _m ≥_ 1 such that _p_<sup>(</sup><sup>_m_)</sup> ( _y, x_ ) _>_ 0. Using the invariance _νx_ = _T_<sup>_m_</sup> _νx_ : 



Thus _νx{y} < ∞_ . 

**(iii)** By linearity of expectation and monotone convergence: 



To prove that existence of an invariant probability implies positive recurrence, we first establish that any invariant measure must be a multiple of the measure _νx_ . 

**Theorem 7.8.9.** _Let X be an irreducible recurrent Markov chain. If µ is an invariant measure, then for any x ∈ E there exists a constant cx ≥_ 0 _such that µ_ = _cxνx. In particular, if an invariant probability exists, then it is unique._ 

_Proof._ Fix _x ∈ E_ . We first show that any invariant measure _µ_ satisfies _µ{y} ≥ µ{x}νx{y}_ for all _y ∈ E_ . By expanding the invariance equation _µ_ = _µP_ and isolating state _x_ : 



Iterating this substitution for all _z̸_ = _x_ yields: 



Since _µ_ is non-negative, the second term is non-negative. Letting _k →∞_ , we obtain: 



Define _η_ = _λ−λ{x}νx_ . We know that _η_ is a non-negative invariant measure and, by construction, _η{x}_ = 0. We now show that _η_ must be identically zero. Suppose, for sake of contradiction, that there exists some state _y ∈ E_ such that _η{y} >_ 0. By the irreducibility of the chain, there exists an integer _m ≥_ 1 such that _p_<sup>(</sup><sup>_m_)</sup> ( _y, x_ ) _>_ 0. Using the invariance of _η_ (following the same logic as in Proposition 7.8.4): 



Since _η{y} >_ 0 and _p_<sup>(</sup><sup>_m_)</sup> ( _y, x_ ) _>_ 0, it follows that _η{x} >_ 0. This directly contradicts the fact that _η{x}_ = 0. Therefore, no such _y_ can exist, and _η_ must be the zero measure, implying _λ_ = _λ{x}νx_ . 

**Theorem 7.8.10.** _Let X be an irreducible Markov chain. The following are equivalent:_ 

- _(i) There exists at least one state x ∈ E which is positive recurrent._ 

- _(ii) The chain admits an invariant probability measure µ_ � _._ 

- _(iii) Every state y ∈ E is positive recurrent._ 

_7.9. THE ERGODIC THEOREM_ 

139 

_Proof._ We prove the logical cycle (i) = _⇒_ (ii) = _⇒_ (iii) = _⇒_ (i). 

**(i)** = _⇒_ **(ii).** Assume state _x_ is positive recurrent, meaning E _x_ [ _ρx_ ] _< ∞_ . By Proposition 7.8.7, the Kac measure _νx_ is invariant ( _T νx_ = _νx_ ). We can define a normalized measure: 



Since<sup>�</sup> _y_<sup>_νx{y}_= E</sup><sup>_x_[</sup><sup>_ρx_],thetotalmassof</sup><sup>_µ_�is1.Thus,</sup><sup>_µ_�isaninvariantprobabilitymeasure.</sup> **(ii)** = _⇒_ **(iii).** Let _µ_ � be an invariant probability measure. By Proposition 7.8.4, we have _µ_ � _{x} >_ 0 for all _x ∈ E_ . Now, we use Proposition 7.8.9, which says that there exists a constant _c_ such that: 



Specifically, evaluating at state _x_ (where _νx{x}_ = 1), we find _c_ = _µ_ � _{x}_ . Therefore, _µ_ � = _µ_ � _{x}νx_ . Summing over all states _y ∈ E_ : 



Substituting the known values (1 for the probability mass and E _x_ [ _ρx_ ] for the Kac measure mass): 



Since _µ_ � _{x} >_ 0, this identity implies E _x_ [ _ρx_ ] = 1 _/µ_ � _{x} < ∞_ . Thus, _x_ is positive recurrent. Since _x_ was arbitrary, all states are positive recurrent. 

**(iii)** = _⇒_ **(i).** Trivial. 

The following table summarizes the relationship between the nature of an irreducible Markov chain, the expected return time, and the existence of a stationary distribution _µ_ �. 

|**State Nature**|**Exp. Return Time** E_x_[_ρx_]|**Invariant Prob. Measure** �_µ_|
|---|---|---|
|**Transient**|_∞_(return not guaranteed)|**None**exists. Any invariant measure must<br>satisfy �_µ{x}_= 0 (Prop. 7.8.3).|
|**Null Recurrent**|_∞_(guaranteed but “slow”)|**None** exists.<br>The invariant measure _νx_<br>exists but has infinite total mass.|
|**Positive Recurrent**|_< ∞_(guaranteed and “fast”)|**Unique**<br>measure<br>exists,<br>defined<br>by:<br>�_µ{x}_=<br>1<br>E_x_[_ρx_]<sup>.</sup>|



Table 7.1: Classification of irreducible chains in relation to invariant probability measures. 

### **7.9 The Ergodic Theorem** 

Through the previous analysis, we have defined the conditions for the existence of an invariant measure. Now, we address the bridge between theoretical expectations and empirical observations. The Ergodic Theorem explains why the long-term behavior of a single realization of a Markov chain is representative of the entire system’s equilibrium. 

**Theorem 7.9.1** (Ergodic theorem) **.** _Let X be an irreducible positive recurrent Markov chain with invariant measure µ_ � _. Let f_ : _E →_ R _be such that_<sup>�</sup> _x∈E_<sup>_|f_(</sup><sup>_x_)</sup><sup>_|µ_�</sup><sup>_{x} < ∞.Then_</sup> 



_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

140 

_Proof._ (Sketch.) Fix _x ∈ E_ and let _τx,k_ be the time of the _k_ -th visit to _x_ . Let _Zk_ =<sup>�</sup><sup>_τ_</sup> _j_<sup>_x,k_</sup> = _τx,k_<sup>+1</sup><sup>_−_1</sup> _f_ ( _Xj_ ). By the strong Markov property, the variables ( _Zk_ ) _k≥_ 1 are i.i.d. because each “cycle” between visits to _x_ is independent of the previous ones. By the strong law of large numbers: 



Substituting the identity E _x_ [ _τx,_ 1] = 1 _/µ_ � _{x}_ and the construction of _Z_ 1, the empirical average converges to the weighted average of _f_ over the state space. 

#### **7.9.1 The ergodic theorem and the law of large numbers** 

The ergodic theorem can be viewed as a generalization of the _strong law of large numbers_ (SLLN). While the classical SLLN requires the random variables to be independent, the ergodic theorem allows for a structure of dependence, provided the chain is sufficiently “mixed” (i.e., irreducible and positive recurrent). 

To see how one can fit the law of large numbers with the previous theorem, let ( _Xn_ ) _n≥_ 1 be a sequence of i.i.d. random variables taking values in _E_ with a common distribution _π_ . This process is a Markov chain with transition kernel _p_ ( _x, y_ ) = _π{y}_ . In this “zero-memory” scenario, the distribution _π_ is the unique invariant measure _µ_ �. Indeed: 



Applying Theorem 7.9.1 with _f_ ( _x_ ) = _x_ yields: 



This demonstrates that the SLLN is a special case of ergodicity where transitions are independent of the current state. 

**Remark 7.9.2.** _The significance of the ergodic theorem lies in the fact that even when there is active dependence, the empirical (time) average still converges to the theoretical (space) average, when the latter is computed with the stationary distribution µ_ � _._ 

### **7.10 Selected exercises** 

(DA CONTROLLARE) 

**Exercise 7.10.1** (The i.i.d. Model) **.** _Let E be a discrete state space and π be a probability distribution on E. Consider a Markov chain with transition probabilities p_ ( _x, y_ ) = _π{y} for all x, y ∈ E._ 

- _a) Analytically prove that π is an invariant measure for this chain._ 

- _b) Calculate the expected first return time_ E _x_ [ _ρx_ ] _for a generic state x ∈ E using the properties of stationary distributions._ 

**Exercise 7.10.2** (Invariant Measures and Transience) **.** _Let X be an irreducible Markov chain on an infinite state space E. Suppose the chain admits an invariant probability measure µ_ � _._ 

- _a) Is it possible for this chain to be transient? Justify your answer using Proposition 5.1 (regarding the limit of the probability of being in a transient state)._ 

_7.10. SELECTED EXERCISES_ 

141 

_b) According to the Ergodic Theorem, what is the almost sure limit of the time average n_<sup><u>1</u></sup> � _nk_ =1<sup>**1**</sup><sup>_{X_</sup> _k_<sup>=</sup><sup>_x}?_</sup> **Exercise 7.10.3** (Kac’s Measure and Return Times) **.** _Consider an irreducible Markov chain with three states E_ = _{_ 1 _,_ 2 _,_ 3 _}. The Kac’s measure relative to state_ 1 _is given by:_ 



_a) Calculate the expected return time to state_ 1 _, i.e.,_ E1[ _ρ_ 1] _._ 

_b) Determine the unique stationary distribution µ_ � _of the chain._ 

_c) Using the result from (b), determine the expected return time to state_ 2 _, i.e.,_ E2[ _ρ_ 2] _._ 

**Exercise 7.10.4** (Application of the Ergodic Theorem) **.** _A positive recurrent Markov chain has a stationary distribution µ_ � = ( 2<sup><u>1</u></sup><sup>_,_</sup><sup><u>1</u></sup> 3<sup>_,_</sup> 6<sup><u>1</u>)</sup><sup>_onstatesE_=</sup><sup>_{_1</sup><sup>_,_2</sup><sup>_,_3</sup><sup>_}.Letf_(</sup><sup>_x_) =</sup><sup>_x_2</sup><sup>_beafunctiononthe_</sup> _state space. Calculate the value of the almost sure limit:_ 



_CHAPTER 7. AN INTRODUCTION TO MARKOV CHAINS_ 

142 

### **Solutions** 

#### **Solution to Exercise 7.10.1** 



Since the sum equals _π{y}_ , _π_ is invariant. 

b) From the fundamental relation _µ_ � _{x}_ = 1 _/_ E _x_ [ _ρx_ ], and knowing _µ_ � = _π_ , we have: 



#### **Solution to Exercise 7.10.2** 

- a) No, it is not possible. If the chain were transient, Proposition 5.1 implies _µ_ � _{x}_ = 0 for every _x ∈ E_ . However, since _µ_ � is a probability measure, it must satisfy<sup>�</sup> _x∈E_<sup>_µ_�</sup><sup>_{x}_=1.Asumof</sup> zeros cannot equal 1; therefore, the chain must be recurrent (specifically, positive recurrent). 

b) By the Ergodic Theorem, choosing _f_ = **1** _{x}_ , the time average converges to the spatial average: 



#### **Solution to Exercise 7.10.3** 

a) The total mass of Kac’s measure is the expected return time to the reference state: 



b) The stationary distribution is the normalized Kac’s measure: 



c) Using the relation E2[ _ρ_ 2] = 1 _/µ_ � _{_ 2 _}_ : 



#### **Solution to Exercise 7.10.4** 

According to the Ergodic Theorem, the limit is the expectation of the function _f_ with respect to the stationary measure _µ_ �: 



## **Chapter 8** 

# **Discrete time stochastic optimal control** 

This chapter is devoted to introduce the reader to stochastic optimal control in discrete time and to the illustration of the dynamic programming method for their solution. Some specific problems motivated by economic and financial applications will be provided. As for the set of times, we will use the notations introduced in Chapter 3. 

### **8.1 A class of stochastic control problems in discrete time** 

We are going to provide a quite general framework to set up stochastic dynamic optimization problem in discrete time. We’ll consider time homogeneous dynamics and constraints for simplicity of notations. Many applied problems fall into this setting. Consider the following objects. 

- (i) A set _S_ , called _state space_ ; typically, _S ⊂_ R<sup>_k_</sup> . 

- (ii) A set _C_ , called _control space_ ; typically, _C ⊂_ R<sup>_d_</sup> . 

- (iii) A probability space (Ω _, F,_ P) and, defined on it, an i.i.d. sequence of discrete random variables _{ξn}n∈N\{_ 0 _}_ valued in ( _E, E_ ). 

- (iv) The filtration _{Fn_<sup>_ξ}_</sup> _n∈N_<sup>definedas</sup> 



- (v) A function 

_f_ : _S × C × E → S,_ 

stating the (stochastic) dynamics of the system. 

(vi) (Possibly) An aggregated running control-state constraint function 



(vii) (Possibly) A final state constraint function (if _N < ∞_ ) 



(viii) A running payoff function 

_g_ : _S × C →_ R 

and a discount factor _β ∈_ (0 _,_ 1]. 

143 

_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

144 

(ix) (If _N < ∞_ ) A terminal payoff function 



Denote 



We call an element in the set above a _control process_ . Given an initial state _x ∈ S_ and a control process _c ∈ A_<sup>ˆ</sup> , the dynamics of the system is established recursively by the _state equation_ 



Here, _X_ = ( _Xn_ ) _n∈N_ is the stochastic process representing the state of the system over time. Clearly _X_ depends on _x_ and _c ∈ A_<sup>ˆ</sup> . To stress this dependence, we often write 



**Remark 8.1.1.** _Note that, due to the fact that the control process c ∈ A_<sup>ˆ</sup> _is {Fn_<sup>_ξ}_</sup> _n∈N_<sup>_-adapted_</sup> _and that the family of random variables {ξn}n∈N\{_ 0 _} generating Fn_<sup>_ξtakesvaluesinadiscreteset,_</sup> _then cn itself takes values in a discrete subset of the control space C. Consequently, also X_<sup>_x,c_</sup> _is {Fn_<sup>_ξ}_</sup> _n∈N_<sup>_-adaptedandtakesvaluesindiscretesubsetofthestatespaceS._</sup> 

If one wants to consider (time-homogenoeous) constraints<sup>1</sup> on the control and state processes represented by the vector-valued functions _G, H_ , the set of _admissible control strategies_ is restricted to 



or 



where **0** _m_ and **0** _j_ denote, respectively, the null vector of R<sup>_m_</sup> and of R<sup>_j_</sup> (<sup>2</sup> ). Given _x ∈ S_ , the stochastic optimal control problem is 



where _J_ ( _x_ ; _·_ ) is the _objective functional_ 



or 



assuming that the expressions above are well-defined for all _c ∈A_ ( _x_ ). 

> 1In this formulation we consider constraints expressed by large inequalities; of course some or all the inequalities could be strict depending on the problem. 

> 2Clearly, by _G_ ( _·, ·_ ) _≤_ **0** _m_ and _H_ ( _·_ ) _≤_ **0** _j_ here we intend, respectively, 



_8.2. EXAMPLES OF STOCHASTIC OPTIMAL CONTROL PROBLEMS_ 

145 

**Remark 8.1.2.** _The filtration used to define adapted control is the one generated by the_ primary _random sources_ ( _ξn_ ) _n∈N . By Doob’s measurability criterion, for each n ∈N_<sup>0</sup> _, we have_ 



_for some Yn_ : _E_<sup>_n_+1</sup> _→ C. Hence, the control processes may be identified with the family of maps_ 



_This choice may be arguable: indeed, it means that we are able to observe the process {ξn}n∈N\{_ 0 _} over time. However, in principle, we should think of the latter random variables just as mathematical objects that are not observable by the agent. The advantage of this choice is that the observation filtration is fixed from the beginning in the formulation. On the other hand, it would be more realistic to assume that the control process is adapted with respect to the filtration {Fn_<sup>_X}n∈N_</sup> _generated by X, the state process — assuming that we have perfect information on it as times go on — and, in general, we only have Fn_<sup>_X⊂F_</sup> _n_<sup>_ξ.ThedrawbackofthelatterviewpointisthatX_</sup> _itself is defined in terms of c and the formulation would be more cumbersome. A solution would be (see [3, 4, 15]) to identify the control processes with maps_ 







_In this way the control is seen just as a feedback map on the past values of the system. This is the passage from the so called_ open loop _form of the control to the so called_ closed loop _form of the control. In particular, when Yn depends only on Xn, i.e. cn_ = _Yn_ ( _Xn_ ) _, the feedback map is said a_ Markovian _feedback map._ 

### **8.2 Examples of stochastic optimal control problems** 

In this section, we provide some examples motivated by economic and financial applications. For each of them, we first give an informal description and then frame it within the general formulation described in the previous section by setting the specifcation 

#### **8.2.1 Optimal stochastic growth** 

This problem of optimal stochastic growth is taken from Example 16.1 in [1] (see also [1, Sec. 17.1] and the references therein). Consider the following objects. 

- (i) _Q_ = _{Qn}n∈_ N, an R<sup>+</sup> -valued stochastic process representing capital over time. 

- (ii) _c_ = _{cn}n∈_ N, an R<sup>+</sup> -valued stochastic process representing consumption over time. 

- (iii) A Markov chain _Z_ = _{Zn}n∈_ N valued in a discrete set _Z_ defined on some probability space (Ω _, F,_ P); it represents some stochastic factor affecting the production (e.g., the technological progress). 

- (iv) A _production function_ (concave and increasing in the first argument) 



- (v) A depreciation factor _δ ∈_ [0 _,_ 1). 

_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

146 

Given an initial capital value _q ∈_ R<sup>+</sup> , we consider the controlled dynamical system 



Such dynamical system is recursively well defined if 



Assume that at each time _n ∈_ N the agent may choose the consumption _cn_ based upon to the information brought by the random variables _Q_ 0 _, ..., Qn_ and _Z_ 0 _, ..., Zn_ . In other terms assume that we can read the realizations of the latter random variables at time _n ∈_ N and, accordingly, decide _cn_ . Then the agent aims at maximize the expected value of intertemporal utility from consumption: 



where _β ∈_ (0 _,_ 1) is a discount factor and _U_ : R<sup>+</sup> _→_ R is a utility function. 

**Formal setting.** We assume that _Z_ is a Markov chain valued in some discrete space _Z_ and evolving according to some dynamics 



for some _fZ_ : _Z × E →Z_ , where _ξ_ = ( _ξn_ ) _n∈N_ is an i.i.d. sequence valued in a discrete space _E_ representing the source of randomness of the system. 

Then, the problem above can be rigorously formulated within the general setting provided in Subsection 8.1, using the following specifications. 

(i) _N_ = N. 

(ii) _S_ = R _× Z_ . We denote by _x_ = ( _q, z_ ) the elements of _S_ and set 



(iii) _C_ = R<sup>+</sup> . 

(iv) The function stating the dynamics is 



where 



(v) The real valued running state constraint function is 



(vi) The running payoff function is 



(vii) The initial datum is _x_ = ( _q, z_ ). 

(viii) The optimization problem is then 



_8.2. EXAMPLES OF STOCHASTIC OPTIMAL CONTROL PROBLEMS_ 

147 

#### **8.2.2 Optimal portfolio allocation over finite horizon** 

This is a classical problem of modern financial theory, where it appears in several variants (see also [13, Ch. 2] and [3, Ch. 4, Sec. 3]). Let _N < ∞_ and consider a market composed by a riskless asset with price _B_ = _{Bn}n∈N_ and a risky asset with price _S_ = _{Sn}n∈N_ . 

The dynamics of _B_ is 



where _r ∈_ ( _−_ 1 _,_ + _∞_ ) is the risk-free interest rates, which is assumed to be deterministic. The deterministic process _B_ can be seen as the evolution of a bank account with initial unitary investment over time. 

The dynamics of _S_ is stochastic and constructed over a probability space (Ω _, F,_ P): 



where _µ_ = ( _µn_ ) _n∈N\{_ 0 _}_ is a stochastic processes taking values in ( _−_ 1 _,_ + _∞_ ) and represents the stream of random returns of the asset _S_ over time; i.e., _µn_ +1 is the random return of the asset _S_ in the time period _n → n_ + 1. 

Assume that an agent can invest on this market (model). We want to define portfolio strategies and perform an optimization problem. Denote by _W_ = _{Wn}n∈N_ the stochastic process representing the value of the agent’s portfolio (the overall money which the agent owns over time in terms of shares of riskless and risky asset). Assume (for the moment) that the portfolio is _self-financed_ in the sense that no extra cash-flow takes place in our investment: money is not added nor subtracted from our portfolio at any time. Hence, the only variations in the portfolio process are due to the variation of the prices of the two assets. With this (informal) assumption in mind, we construct an investment strategy as follows: denote by _π_ = _{πn}n∈N o_ the (control) process, representing the fraction of portfolio which at each time is (re)invested in the risky asset and consider this as decision (control) process. To be more precise, recursively over _n ∈N_<sup>_o_</sup> , 

1. At time _n_ = 0 the value of the portfolio _W_ = _w ∈_ R<sup>+</sup> (initial endowment) is given; 

2. At time _n ∈N_<sup>_o_</sup> the agent (re)allocates her/his position deciding the fraction _πn ∈_ R of _Wn_ to be (re)invested in the risky asset<sup>3</sup> ; 

3. The remaining part of the portfolio (1 _− πn_ ) _Wn_ is (re)invested in the riskless asset; 

4. The value of _Wn_ +1 is then determined by the assumption of self-financing: 



The last relation expresses formally the fact that the portfolio is self-financed and can be also rewritten in more compact and convenient way: 



where 



> 3We intend here fraction in a generalized sense: in the financial language, _πn <_ 0 means short selling of the riskless asset _B_ ; _πn_ means short selling of the risky asset _S_ . 

_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

148 

is the stochastic process representing the excess of return rate<sup>4</sup> of the risky asset with respect to the riskless one. 

At time _n_ the agent reads the stream of realizations _{µ_ 1 _, ..., µn}_ , hence of _{_ Λ1 _, ...,_ Λ _n}_ , and (consequently) the current value _Wn_ value of its portfolio; based upon this information decide how to reallocate its portfolio choosing _πn_ . 

The optimization problem of the agent consists in maximizing the expected utility from the terminal wealth 



for each control strategy which guarantees _WN ≥_ 0. 

**Formal setting.** Assume that 



for some _f_ Λ : R _× E →_ R, and _ξ_ = ( _ξn_ ) _n∈N\{_ 0 _},_ sequence of i.i.d. random variables taking values in some discrete space _E_ , which we take as the primary source of randomness of the system. 

Then, the portfolio problem can be rigorously formulated within the general setting provided by Subsection 8.1, using the following specifications. 







(iii) _C_ = R. 

(iv) The function stating the dynamics is 



where 

_fW_ ( _x, c_ ) = _w_ [(1 + _r_ ) + _cλ_ ] _, x_ = ( _w, λ_ ) _._ 

(v) The terminal constraint function is 



(vi) The current payoff function is _g_ ( _x, c_ ) _≡_ 0. 

(vii) The terminal payoff function is 



(viii) The initial datum is _x_ = ( _w, λ_ ) _∈ S_<sup>+</sup> . 

(ix) The optimization problem is then 



> 4It may be negative for some _ω ∈_ Ω. 

_8.2. EXAMPLES OF STOCHASTIC OPTIMAL CONTROL PROBLEMS_ 

149 

**Remark 8.2.1.** _Clearly, the structure of the set A_ ( _x_ ) _in the example above strongly depends on the ranges of {µn}n∈N and on r._ 

_However, if πn ∈_ [0 _,_ 1] _for each n ∈N_<sup>_o_</sup> _— which corresponds to exclude short selling of the assets in our portfolio allocation — then, whatever the ranges of {µn}n∈N and r are, we have_ 

(1 + _r_ ) + _πn_ ( _µn_ +1 _− r_ ) _≥_ 0 _, ∀n ∈N ._ 

_Hence, starting for nonnegative W_ 0 = _w, the component Wn of the state process Xn_ = ( _Wn,_ Λ _n_ ) _is automatically nonnegative for each n ∈N . This means that, if we restrict the control set to C_ = [0 _,_ 1] _, then the use of the constraint function H in_ (8.2.2) _to define the admissible controls is redundant. In other terms, if C_ = [0 _,_ 1] _, then one can take as state space S_<sup>+</sup> _and the set of admissible control strategies is simply the set, independent of x,_ 



#### **8.2.3 Optimal inventory** 

This example is a generalization of the problem illustrated in [3, Ch. 1, Sec. 1-2, and Ch. 4, Sec. 2]. Let _N < ∞_ . Assume that a shop faces the problem of ordering, at each time _n ∈N_ , a quantity of stock, so as to meet a random demand. Consider the following objects. 

- (i) _Q_ = ( _Qn_ ) _n∈N_ , a real valued stochastic process, representing the quantity of stock of some good stored by the shop<sup>5</sup> . 

- (ii) _c_ = ( _cn_ ) _n∈N o_ , a real valued nonnegative stochastic process, where _cn_ represents the quantity of stock of new good ordered by the firm; it is delivered and becomes available for selling at time _n_ + 1 _∈N_ . 

- (iii) _D_ = ( _Dn_ ) _n∈N o_ , a real valued nonnegative stochastic process, representing the demand of the good over time. 

The dynamics of the system is linear: 



where _q ∈_ R is the initial stock. We want to penalize deviation of the current available stock by the current demand by a cost represented by a convex function _g_ 0 : R _→_ R<sup>+</sup> such that _g_ 0(0) = 0 and _g_ 0 _≥_ 0. Also, we want to consider the (linear) cost _αcn_ of purchasing the quantity _cn_ at time _n_ . Here, _α >_ 0 is the cost per unit of the good, and the final inventory at time _N_ by a convex function Φ0 : R _→_ R<sup>+</sup> such that Φ0 _≡_ 0 on ( _−∞,_ 0] and Φ0 _≥_ 0 on (0 _,_ + _∞_ ). So, considering a discount factor _β ∈_ (0 _,_ 1), the agent aims at minimizing 



**Formal setting.** Assume that 



for some _fD_ : R<sup>+</sup> _× E →_ R<sup>+</sup> , where _E_ is a discrete space, and for an independent sequence of _E_ -valued random variables _ξ_ = ( _ξn_ ) _n∈N\{_ 0 _}_ , which we take as the random source of the system. This problem can be rigorously formulated within the general setting provided by Subsection 8.1 with the following specifications. 

> 5 _Q_ can be also negative: positive values have to be interpreted as an excess of inventory; negative values have to be interpreted as backlogged demand. 

_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

150 

(i) _N_ = _{_ 0 _, ..., N }._ 

(ii) _S_ = R _×_ R<sup>+</sup> . We denote _x_ = ( _q, d_ ) the elements of _S_ . 

(iii) _C_ = R<sup>+</sup> . 

(iv) The function stating the dynamics is 



where 



(v) The running payoff function is 



(vi) The terminal payoff function is 



(vii) The initial datum is _x_ = ( _q, d_ ) _∈ S_ . 

(viii) The optimization problem is then 



### **8.3 Dynamic Programming** 

We are going to introduce and describe one of the most employed methods to tackle dynamic optimization problems like the ones described in the previous chapter. It is the so called _Dynamic Programming_ (DP) method, based on the so called _Bellman’s optimality principle_ . The idea behind is to split the optimization step-by-step ( _time_ step), considering at each step, as exit functional, the optimal value of the problem starting at next step. It is therefore clear that the first passage in this respect is to define the problem for generic initial data ( _k, x_ ) _∈N × E_ . 

#### **8.3.1 Value function** 

Let _k ∈N_ and set the following objects. 



(iii) The filtration _{Fn_<sup>_k,ξ}_</sup> _n∈Nk_<sup>over</sup><sup>_N_</sup> _k_<sup>definedas</sup> 



(iv) The set 



We call an element in the set above a _control process starting at time k ∈N_<sup>_o_</sup> . Given an initial state _x ∈ S_ at time _k ∈N_<sup>_o_</sup> and a control process _c ∈ A_<sup>ˆ</sup> _k_ , the dynamics of the system is established recursively by the _state equation_ 



_8.3. DYNAMIC PROGRAMMING_ 

151 

where 

_X_ = _{Xn}n∈Nk_ 

is the stochastic process representing the state of the system over the time set _Nk_ . Clearly _X_ depends on _k ∈N_<sup>_o_</sup> , _x ∈ S_ , and _c ∈ A_<sup>ˆ</sup> _k_ . To stress this dependence, we write 



(v) Given functions _G, H_ as in the formulation of Section 8.1, we define 

or 



(vi) Given _x ∈ S_ and functions _g, h_ as in Section 8.1, we consider the _objective functional_ 



or 



(vii) We finally consider the dynamic optimization problem 



From now on, in the rest of this section, with the exception of Subsection 8.4.3 where the optimal inventory problem is discussed, we consider _maximization problems_ and state the results for them. Let ( _k, x_ ) _∈N_<sup>_o_</sup> _× S_ . Assuming that _Jk_ ( _x_ ; _c_ ) is well defined for each _c ∈Ak_ ( _x_ ) :, we define, with the convention sup _∅_ = _−∞_ , its optimal value, possibly infinite: 



If _N < ∞_ , we set 



**Definition 8.3.1.** _An_ optimal control starting from ( _k, x_ ) _∈N_<sup>_o_</sup> _× S is a control process c_<sup>_∗_</sup> _∈ Ak_ ( _x_ ) : _such that_ 



Letting the initial data ( _k, x_ ) vary in the set _N × S_ , we can look at _V_ as at a function defined on this subset and taking values in R. The function _V_ is called the _value function_ of the optimization problem. The dynamic programming method consists in the following steps. 

1. Associate an equation to _V_ ; this is done showing that _V_ satisfies an equality called _Bellman’s optimality principle_ . 

2. Characterize _V_ as unique solution of such equation with 

   - (i) a suitable terminal condition if _N < ∞_ ; this is done just by a backward recursive algorithm; 

   - (ii) a suitable growth condition (when _N_ = _∞_ ); this is done through a so called verification theorem. 

3. Obtain optimal controls in special form ( _Markovian_ ), relying on the solution of the step above. 

_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

152 

#### **8.3.2 Bellman’s equation** 

We are going to prove the key result on which the solution of the optimization problem relies. Consider the setting of Section 8.3.1. We shall make use of the following assumption, that will be standing form now on. 

**Assumption 8.3.2.** _For every k ∈N_<sup>_o_</sup> _and x ∈ S,_ 

- _(i) Jk_ ( _x_ ; _c_ ) _is well defined and finite for every c ∈Ak_ ( _x_ ) _;_ 

- _(ii) |Vk_ ( _x_ ) _| < ∞._ 

**Remark 8.3.3.** _Notice that Assumption 8.3.2 implies that, for every k ∈N_<sup>_o_</sup> _and x ∈ S, we have Ak_ ( _x_ ) := _̸ ∅._ 

Introduce the set 



This sets represents the feasible choices at time _k_ if the system starts from the state _x_ at that time. By time homogeneity of the system and of the constraints, this set does not depend on _k_ , i.e. 



From here on, we simply write Γ( _x_ ). 

**Theorem 8.3.4** (Bellman’s optimality principle) **.** _Let_ ( _k, x_ ) _∈N_<sup>_o_</sup> _× S (with N finite or not). We have_ 



_Proof._<sup>6</sup> We show the two inequalities separately. For simplicity we consider the case _N < ∞_ . The same holds in the case _N_ = _∞_ . 

_First step._ We show that 



Let _c ∈Ak_ ( _x_ ). We have 



Taking the supremum over _c ∈Ak_ ( _x_ ), we get 

where the last equality follows from definition of Γ( _x_ ). 

> 6Some passages of the proof are heuristic; a rigorous prove should involve conditioning on _Fk_ +1. 

_8.3. DYNAMIC PROGRAMMING_ 

153 

_Second step._ We show that 



Let _ε >_ 0. For each _x_<sup>_′_</sup> _∈ S_ , we consider a _ε_ -optimal control _c_<sup>_x′_</sup> _∈A_ ( _k_ + 1 _, x_<sup>_′_</sup> ) for the problem starting from _x_<sup>_′_</sup> at time _k_ + 1; that is, such that 



Define the control 



Then _c_ ¯ _∈Ak_ ( _x_ ) : and 



Taking the supremum over _γ ∈_ Γ( _x_ ) and by arbitrariness of _ε_ , we get the claim. 

#### **8.3.3 The DP algorithm in the finite horizon case** 

In this section, we show how the Bellman equation can be employed to solve the problem in the finite horizon case ( _N < ∞_ ). In other terms, _V_ solves a functional equation. Define the transition operator of the controlled Markov process _X_ under the control action _γ ∈ C_ : 



By (8.3.3), the value function _V_ can be constructed by backward recursion with the algorithm 



Assuming existence and uniqueness of the maximizer for _n ∈N_<sup>_o_</sup> , define the so called _optimal feedback map_ : 



Then, fixing ( _k, x_ ) _∈N_<sup>_o_</sup> _× S_ , consider the Markov chain _X_<sup>_∗_</sup> = _{Xn_<sup>_∗}_</sup> _n∈N_<sup>_k_definedrecursivelyby</sup> 



The equation above, which is nothing but the state equation when the input _γn_<sup>_∗_(</sup><sup>_Xn_) is plugged in</sup> place of _cn_ , is called _closed loop equation_ . Consider the _Markovian_ control process _c_<sup>_∗_</sup> = _{c_<sup>_∗_</sup> _n_<sup>_}_</sup> _n∈N_<sup>_k_,</sup> defined by 



_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

154 

Then, by construction, _c_<sup>_∗_</sup> _∈Ak_ ( _x_ ) : and 



It is then immediate to see, by recursion, that _Vk_ ( _x_ ) = _Jk_ ( _x_ ; _c_<sup>_∗_</sup> ), that is that _c_<sup>_∗_</sup> is optimal starting at ( _k, x_ ). 

#### **8.3.4 The DP algorithm in the infinite horizon stationary case** 

We consider the case of infinite horizon stochastic optimal control problems. Since we are assuming time homogeneity of the data, in this case the problem has a ststionary nature allowing to get rid of the time variable as we are going to show. So, let _N_ = N, _β ∈_ (0 _,_ 1), and let _{ξn_ +1 _}n∈N_ be an i.i.d. sequence of random variables valued in a discrete space _E_ . We then have the following result, whose content is quite intuitive. We skip the proof for the sake of brevity. 

**Lemma 8.3.5.** _Let_ ( _k, x_ ) _∈N × S._ 

_(i) There is a one-to-one correspondence_ 



_such that_ 



_(ii) We have_ 



Consider the counterpart of Assumption 8.3.2 in this context; that is, for every _x ∈ S_ , 

(i) _J_ 0( _x_ ; _c_ ) is well defined and finite for every _c ∈A_ 0( _x_ ); 

(ii) _|V_ 0( _x_ ) _| < ∞_ . 

We assume that this is a standing assumption hereafter in this subsection. Looking at the original Bellman’s equation at time _k_ = 0, we obtain the Bellman equation solved by _V_ 0: 



The main problem, with respect to the finite horizon case, is that here we do not have a terminal condition to characterize _V_ as unique solution of the Bellman equation. The counterpart of such terminal condition is typically a growth condition at infinity, the so called _transversality condition_ , which allows to prove the following so called _verification theorem_ . 

**Theorem 8.3.6** (Verification theorem) **.** _Let g_ : _S × C →_ R<sup>+</sup> _and let v_ 0 : _S →_ R _be a solution to_ 



_Assume that for each x ∈ S there exists a unique maximizer γ_<sup>_∗_</sup> ( _x_ ) _for the map_ 



_Now, fix x ∈ S and assume that_ 



_We have the following._ 

_8.3. DYNAMIC PROGRAMMING_ 

155 

_(i) v_ 0( _x_ ) _≥ V_ 0( _x_ ) _._ 

_(ii) If the feedback relation_ 



_holds for each n ∈N , then v_ 0( _x_ ) = _V_ 0( _x_ ) _and c_<sup>_∗_</sup> _∈A_ 0( _x_ ) _is optimal starting at x, i.e. J_ 0( _x_ ; _c_<sup>_∗_</sup> ) = _V_ 0( _x_ ) _._ 

_Proof._ (i) Let _c ∈A_ 0( _x_ ). Note that 



Using the fact that _v_ 0 solves the Bellman equation and arguing recursively we obtain for each _N ∈_ N 



Taking the limit for _N →∞_ and using Corollary 2.7.8 (as _g_ 0 is nonnegative) and (8.3.14) we get 



We conclude by taking the supremum over _c ∈A_ 0( _x_ ). 

- (ii) Using the fact that _v_ 0 solves the Bellman equation (8.3.13) and that _c_<sup>_∗_</sup> _∈A_ 0( _x_ ) satisfy (8.3.15), and arguing recursively, we get for each _N ∈_ N, 



Taking the limit for _N →∞_ and using Corollary 2.7.8 (as _g_ is nonnegative) and (8.3.14), we get 



As we have already proved in part (i) that _v_ 0( _x_ ) _≥ V_ 0( _x_ ), we get, at once, _v_ 0( _x_ ) = _V_ 0( _x_ ) and the optimality of _c_<sup>_∗_</sup> . 

In view of Theorem 8.3.6, the algorithm to construct the solution of the dynamic optimization problem starting at _x ∈ S_ is the following. 

(i) Find (by a suitable guess) or show theoretically the existence of a solution _v_ 0 to (8.3.12). 

- (ii) Verify that (8.3.14) holds for such a _v_ 0. 

(iii) Construct a map _γ_<sup>_∗_</sup> : _S → C_ such that 



(assuming that this is possible, i.e. all the static optimization problems above, for _x ∈ S_ , have solution). Note that, if successful, this part is basically already contained in the solution of the previous item when computing 



_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

156 



(v) Consider the Markovian control process _c_<sup>_∗_</sup> = _{c_<sup>_∗_</sup> _n_<sup>_}n∈_N,definedby</sup> 



If these steps are performed, then, by construction, _c_<sup>_∗_</sup> _∈A_ 0( _x_ ) and verifies (8.3.15). So, it is optimal for the problem starting at _x_ . The corresponding optimal state trajectory is _X_<sup>0</sup><sup>_,x,c∗_</sup> = _X_<sup>_∗_</sup> _._ 

### **8.4 Solution of selected problems** 

To illustrate the dynamic programming method we apply it to the examples described in Section 8.2. 

#### **8.4.1 Optimal stochastic growth** 

Consider the problem of Subsection 8.2.1 replacing _K_ with _Q_ and with the following specifications: 



where _A_ : _Z →_ [0 _, A_<sup>¯</sup> ], _A_<sup>¯</sup> _>_ 0, and _µ_ is a given probability law on a discrete set _E ⊂_ [0 _, A_<sup>¯</sup> ]. The Bellman equation is written on _S_ = [0 _, ∞_ ) _× Z_ as 



where 



and 



We guess a solution to the Bellman equation (8.4.1) in the form 



for some function _α_ : _Z →_ [0 _, ∞_ ). Letting _v_ 0 in the form above, we have 



where 



We need to maximize the expression above over _γ ∈_ Γ( _x_ ). With _v_ 0 given as in (8.4.2) we have 



_8.4. SOLUTION OF SELECTED PROBLEMS_ 

157 

The expression above vanishes if and only if 



Moreover 



Hence, _γ_<sup>_∗_</sup> ( _x_ ) is the unique maximum point of _g_ ( _x, γ_ ) + _βLγv_ 0( _x_ ) over Γ0( _x_ ) and it is interior. The corresponding maximum value is 



Hence (8.4.1) becomes 



Recalling the definition of _LZ_ , we get a functional equation and the problem becomes solving the fixed point problem of finding _α_ : _Z →_ R such that 



Then, Theorem 8.3.6 can be applied. 

**Exercise 8.4.1.** _Solve_ (8.4.3) _under the following further specifications._ 



#### **8.4.2 Optimal portfolio** 

We consider the optimal portfolio problem described in Subsection 8.2.2 with some further specifications (cf. the binomial model of Section 6.2.5). First of all, we take 



where the process _{ξn}n∈N\{_ 0 _}_ is an i.i.d. sequence valued in _{u, d} ⊂_ R such that 



We assume that _−_ 1 _< d < r < u._ This condition expresses the absence of arbitrage in the market (cf. again Section 6.2.5). From the point of view of portfolio optimization this condition assures that the solution is not trivial: if this condition does not hold, clearly the investor invests everything in one of the asset. Precisely, she/he invests 

- (i) the whole portfolio in the risky asset if _r < d_ ; 

- (ii) the whole portfolio in the riskless asset if _u < d_ . 

_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

158 

and convenient way: The portfolio dynamics is 



Note that we have the implications 

and 

if and only if 



i.e. if and only if 



Notice that _D ⊇_ [0 _,_ 1]. So, by induction over _n ∈N_ , starting from _W_ 0 = _x ≥_ 0, we have P _{Wn ≥_ 0 _}_ = 1 for each _n ∈N_ if and only if 



We consider the problem of maximizing 



with the convention log 0 = _−∞_ , over the _{Fn_<sup>_ξ}_</sup> _n∈N_<sup>-adapted control processes</sup><sup>_π_=</sup><sup>_{π_</sup> _n_<sup>_}_</sup> _n∈N_<sup>such</sup> that the corresponding portfolio process is positive with probability 1 at the terminal date _N_ . For what we said, it follows that this is the set 



The Bellman equation reads as 



with terminal condition 



One easily sees (e.g. by induction) that 



for a suitable real sequence _{an}n∈N⊂_ R. Plugging this structure into the right hand side of (8.4.6), we get 



_8.4. SOLUTION OF SELECTED PROBLEMS_ 

159 

where 



We have 



The above expression vanishes if and only if 



Moreover 



so we deduce that _γ_<sup>_∗_</sup> is the unique maximum point of _f_ over _D_ and is interior. The corresponding maximum value is 



Coming back to (8.4.7), we have 



So, we find the the relation 



It follows, by the arguments of Section 8.3.4, that the optimal strategy is given by the constant _γ_<sup>_∗_</sup> and 



**Exercise 8.4.2.** _Solve the same problem when the optimization problem is maximizing, over the same set of admissible control processes_ (8.4.5) _, the functional_ 



_Notice that in this case the feedback map γ_<sup>_∗_</sup> _depends on the state x._ 

#### **8.4.3 Optimal inventory** 

Consider the optimal inventory problem described in Subsection 8.2.3 with the following specification: 



for some i.i.d. sequence of discrete random variables random variables _{ξn_ +1 : Ω _→ E ⊂_ R<sup>+</sup> _}n∈N ,_ which we take as the random sequence generating randomness in the system. The agent aims at minimizing 



where _q ≥_ 0 and _f_ 0 : R _→_ R<sup>+</sup> convex and such that 



_CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

160 

As we have seen, this problem can be rigorously formulated within the general setting provided by Subsection 8.1. In this case the process _D_ is a very special Markov process. Indeed, it is a Markov process just constructed as an independent sequence. This allows to simplify the formulation by considering just a one-dimensional process as state process. Set 



Then the controlled dynamics of _X_ is 



The functional (8.4.8) above is rewritten as 



Setting the problem for generic initial data ( _j, x_ ) _∈N ×_ R and noting that in the expression above the term _f_ 0( _x_ 0 + _ξ_ 0) does not depend on _u_ , we can set the optimization problems<sup>7</sup> 



where 



and 

_A_ ˆ( _j_ ) := _{u_ = _{un_ : Ω _→_ R<sup>+</sup> _}n∈N j_ : _u {Fn_<sup>_j,ξ}_</sup> _n∈N_<sup>_j−_adapted</sup><sup>_}._</sup> 

**Proposition 8.4.3.** _For each j ∈N the function V_ ( _j, ·_ ) _is nonnegative and convex._ 

_Proof._ The fact that _V_ is nonnegative is clear. Let us show convexity. Let _ε >_ 0 and _x, y ∈_ R and _λ ∈_ [0 _,_ 1]. Take _u_<sup>_x_</sup> _, u_<sup>_y_</sup> _∈ A_<sup>ˆ</sup> ( _j_ ) such that 

_J_ ( _j, x_ ; _u_<sup>_x_</sup> ) _≤ V_ ( _j, x_ ) + _ε, J_ ( _j, x_ ; _u_<sup>_y_</sup> ) _≤ V_ ( _j, y_ ) + _ε._ Set _u_<sup>_λ_</sup> := _λu_<sup>_x_</sup> + (1 _− λ_ ) _u_<sup>_y_</sup> . We have _u_<sup>_λ_</sup> _∈ A_<sup>ˆ</sup> ( _j_ ) and 



So 



By arbitrariness of _ε_ we get the claim. 

> 7Note that there are no constraints, so _A_ ( _j, x_ ) = _A_ ˆ( _j_ ) for each ( _j, x_ ) _∈N ×_ R. 

_8.4. SOLUTION OF SELECTED PROBLEMS_ 

161 

The value function _V_ satisfies the Bellman equation, i.e. 



with 



Consider now the set of functions 



and the operators 



The operators _Tn_ are convex preserving, meaning that they map convex functions into convex ones. Hence, defining 



we have _Tn_ : _Sc → Sc_ . Hence, by Proposition 8.4.3 and by (8.4.9) the function 



admits a minimizer _Cn_<sup>_∗_(</sup><sup>_x′_)</sup><sup>_∈_R+</sup><sup>_._ByTheorem8.3.6theproblemhasasolution.Itcanbesolved</sup> numerically by computing recursively backward _V_ — passing through the computation of _Tn_ — and the optimizers _Cn_<sup>_∗_(</sup><sup>_x′_).</sup> 

162 _CHAPTER 8. DISCRETE TIME STOCHASTIC OPTIMAL CONTROL_ 

## **Appendix A** 

# **Liminf and limsup of real sequences** 

Let _{xn}n∈_ N be a sequence of real numbers. The sequence of the definitive infimum 



is an increasing sequence. Therefore there exists (finite or not) 



This value is denoted by lim inf _n→∞ xn_ . Similarly, we denote 



Notice that the above objects always exist (finite or infinite). Moreover, we have 



and 



if and only if lim _n→∞ xn_ exists, in which case 



**Exercise A.0.1.** _Determine_ lim inf _n→∞ and_ lim sup _n→∞ of the following sequences:_ 

_1. xn_ = ( _−_ 1)<sup>_n_</sup> _;_ 

_2. xn_ = ( _−_ 1)<sup>_n_</sup> (1 + 1 _/n_ ) _;_ 

_3. xn_ = ( _−_ 1)<sup>_n_</sup> _n._ 

163 

164 _APPENDIX A. LIMINF AND LIMSUP OF REAL SEQUENCES_ 

## **Appendix B** 

# **Series** 

### **B.1 Series with nonnegative terms** 

Let _I_ be a set of indices having the cardinality of N and let _f_ : _I →_ [0 _,_ + _∞_ ]. Given a bijection 



define 



Then, by monotonicity, there exists (finite or infinite) the limit 



This limit is denoted by the symbol 



It is possible to show that limit above does not depend on the choice of the bijection, i.e., if 



is another bijection, then 



It follows that we can denote without ambiguity the above numbers (finite or infinite) by the general symbol 



Let now _I_ = _I_<sup>_′_</sup> _× I_<sup>_′′_</sup> . We can consider, other than a bijection of _I_ with N, which defines 



also a bijection of _I_<sup>_′_</sup> _× I_<sup>_′′_</sup> with N<sup>2</sup> : 



It turns out that 



165 

_APPENDIX B. SERIES_ 

166 

The common value above is also denoted by 



Also in this case the numbers (finite or infinite) in the equality above do not depend on the bijection chosen and are denoted without ambiguity, respectively, by 



### **B.2 Absolutely convergent series** 

Let _I_ be a set of indices have the cardinality of N and let _f_ : _I →_ R. Given a bjiection 



define 



Assume that<sup>�</sup> _x∈I_<sup>_|f_(</sup><sup>_x_)</sup><sup>_| < ∞_.Then,itispossibletoprovethatthereexistsfinitethelimit</sup> 



This limit is denoted by the symbol 



It is possible to show that limit above does not depend on the choice of the bijection, i.e., if 



is another bijection, then 



It follows that we can denote without ambiguity the above (finite) numbers finite by the general symbol 



Finally, if _I_ = _I_<sup>_′_</sup> _× I_<sup>_′′_</sup> the same results described in the case of nonnegative terms apply. 

# **Bibliography** 

- [1] D. Acemoglu, _Introduction to Modern Economic Growth_ , Princeton University Press, 2009. 

- [2] Q. Berger, F. Caravenna, and P. Dai Pra, _Probabilit`a_ , Springer, 2021. 

- [3] D. Bertsekas, _Dynamic Programming and Optimal Control, Volume I_ , Third Edition, Athena Scientifica, 2005. 

- [4] D. Bertsekas, _Dynamic Programming and Optimal Control, Volume II_ , Athena Scientifica, 1995. 

- [5] P. Billingsley, _Probability and Measure_ , Third Edition, Wiley, 1995. 

- [6] T. Bjork, _Arbitrage theory in continuous time_ (Third edition), Oxford University Press, 2009. 

- [7] P. Br´emaud, _Markov Chains. Gibbs fields, Monte Carlo simulation, and Queues_ , Springer, 1999. 

- [8] K.L. Chung and F. Ait-Sahlia, _Elementary probability theory: with stochastic processes and an introduction to mathematical finance_ . Springer, 2006. 

- [9] G. Dall’Aglio, _Calcolo delle probabilit`a_ , Zanichelli, Bologna, 2003. 

- [10] G. Letta, _Probabilit`a elementare_ . Zanichelli, 1993. 

- [11] J. Jacod and P. Protter, _Probability Essentials_ . Springer, 2004. 

- [12] J.G. Kemeny and J.L. Snell, _Finite Markov Chains_ , University Series in Undergraduate Mathematics, 1960. 

- [13] A. Pascucci and W. Runggaldier, _Finanza Matematica: Teoria e Problemi per Modelli Multi-periodali_ , Springer, 2009. 

- [14] W. Woess, _Catene di Markov e teoria del potenziale nel discreto_ . Quaderni UMI (n. 41), Editrice Pitagora Bologna, 1996. 

- [15] J. Zabczyk, _Chance and Decision: Stochastic Control in Discrete Time_ , Quaderni della Scuola Normale Superiore, 1996. 

167 

