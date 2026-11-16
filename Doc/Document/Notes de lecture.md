# Notes de lecture (version 2)

**Littérature sur les MNBC, les dépôts bancaires et le crédit : ce que les textes disent réellement, et ce que cela change pour notre travail**

> **Statut** : notes de travail, préalables à la section « Revue de littérature » de l'article. Elles ne remplacent pas une lecture personnelle des textes.
> **Mise à jour** : 10 novembre 2026 (v2). Remplace la version précédente.
> **Cadre du travail** : resserrement du crédit bancaire dans l'espace BCEAO (UEMOA) à la suite d'une sortie de dépôts vers une MNBC **hypothétique**. Les résultats sont des scénarios conditionnels, pas des prévisions. Les données d'adoption (Ree), d'enquête (Bidder et al.) et de calibration (Whited et al.) servent d'**ancrages de paramètres** et d'analogues, jamais de preuves directes pour l'UEMOA.
> **Règle** : chaque fait chiffré vient du texte indiqué. Les paraphrases sont de moi ; aucune citation longue. Quand une phrase est une **inférence de ma part**, elle est signalée comme telle.

## Ce que la v2 change (à lire en premier)

1. **Whited, Wu & Xiao** et **Ree** passent de [R]/[P] à **[L]**. Whited et al. corrige notre calibration de φ (§1.7, §4.1).
2. **Bidder, Jackson & Rottner** passe de [R] à **[L] partiel**. Leur résultat négatif dépend du non-recyclage par la banque centrale : c'est notre λ (§1.9, §4.4).
3. **Deux textes UEMOA sur le sujet** ajoutés (Tadenyo 2021 ; Sissoko & Dembélé 2025). La phrase « aucune étude » du §4.6 est reformulée.
4. **Statut de la MNBC à la BCEAO** documenté (presse, juillet 2026) : toujours pas de décision de déploiement (§1.12).
5. **Dates et chiffres corrigés** : les chiffres d'adoption de l'eNaira datent de fin novembre 2022, pas 2021 (§1.8).
6. Plusieurs références **recoupées via les bibliographies** des textes lus (§5). Recoupé ne veut pas dire vérifié à la source.

---

## 0. Profondeur de lecture (à respecter dans l'article)

| Code | Signification |
|---|---|
| **[L]** | Texte lu en grande partie ou en totalité (sections indiquées) |
| **[P]** | Lu partiellement (extraction tronquée, résumé officiel ou extraits) |
| **[R]** | Résumé ou description par d'autres textes seulement : on ne cite que ce que le résumé permet d'affirmer |

| Texte | Profondeur |
|---|---|
| Meller & Soons (2023) | **[L]** (texte quasi intégral) |
| Adalid et al. (2022) | **[L]** (§1 à 4 ; conclusion coupée) |
| Fritz, Krüger & Wong (2024) | **[L]** (intégral) |
| Kumhof & Noone (2018) | **[L]** (§1 à 7.2 ; fin du §7 et conclusion non lues) |
| Bouis et al. (2024) | **[L]** (résumé, §1 à 4 jusqu'à la Box 4 ; §5 sur les politiques non lu) |
| Trinnou (2023, COFEB) | **[L]** (intégral) |
| **Whited, Wu & Xiao (2023)** | **[L]** (texte intégral, 55 pages, version IHS WP 47) |
| **Ree (2023)** | **[L]** (PDF du FMI intégral) |
| **Bidder, Jackson & Rottner (2025)** | **[L] partiel** (texte principal et annexes A-B de BIS WP 1280 ; annexes C à H non lues) |
| **Tadenyo (2021, COFEB)** | **[P]** (extraction tronquée ; résultats et tableaux principaux lus) |
| **Sissoko & Dembélé (2025)** | **[P]** (extraction tronquée ; Table 6 et références lues) |
| BCEAO, Rapport annuel 2025 | **[R]** (via Financial Afrik, 23 juillet 2026 ; PDF source non lu) |
| BCEAO, DEAE n° 21/01 | **[R]** (extrait de recherche seulement) |
| Brunnermeier & Niepelt, Andolfatto, Keister & Sanches, Chiu et al., Schilling et al., Ahnert et al., Burlon et al., Diamond & Dybvig, Di Maggio et al., Saxegaard, Khwaja & Mian | **[R]** (résumés ; description par Adalid et al., Bouis et al., Whited et al. et Bidder et al.) |

---

## 1. Les textes lus

### 1.1 Meller & Soons (2023) : le plus proche de notre exercice **[L]**

**Référence** : Barbara Meller, Oscar Soons, « Know your (holding) limits: CBDC, financial stability and central bank reliance », ECB Occasional Paper No 326 (août 2023) ; version DNB Working Paper 771.

**Question.** Comment une MNBC affecterait-elle les bilans des banques et de la banque centrale ?

**Méthode et données.** Modèle d'optimisation sous contraintes où chaque banque choisit comment répondre à une sortie de dépôts, en fonction des coûts, des réserves, du collatéral et d'une tolérance au risque de liquidité. Données de 2 319 banques de la zone euro (≈ 95 % des actifs bancaires), 3e trimestre 2021. Trois scénarios de tolérance : A (les banques utilisent tout le tampon volontaire), B (elles en gardent la moitié, cas de base), C (elles n'y touchent pas).

**Résultats chiffrés.**
- Plafond de 3 000 € par personne × 340 millions d'habitants ≈ 1 000 milliards, soit **15 % des dépôts de détail** : sortie considérée comme « la plus extrême ».
- Cas de base B : le système absorbe **20 %** de sortie des dépôts de détail avec les seules réserves excédentaires existantes (40 % en scénario A). Avec les données 2019, où les réserves étaient plus faibles (≈ 6 % des actifs contre ≈ 14 % en 2021), ces seuils tombent à **12 %** (B) et **20 %** (A).
- Pour la sortie extrême de 15 % : 82 % sont remplacés par des réserves propres, 14 % par du financement interbancaire non garanti à moyen terme, 2 % et 1 % par d'autres sources.
- Part de la sortie qu'une banque absorbe seule : α\_i = min(100 %, R\_i / D\_i). Plus de 90 % des grandes banques et 40 % des plus petites y parviennent pour 20 % de sortie.
- **Hétérogénéité entre pays** (tableau B.1) : la capacité d'absorber sans réserves supplémentaires va de 24 % (Slovaquie, scénario A) et 14 % (scénario B) à 100 % et 64 % (Belgique) ; zone euro : 40 % et 20 %.
- Un marché interbancaire cloisonné par pays ne change presque rien aux conclusions.
- Scénario de ruée : des seuils de liquidité sont franchis pour une part significative du système à partir de 16 % de sortie. Les sorties observées en Grèce (2015) et à Chypre (2013) étaient d'environ 20 %.

**Hypothèses et limites (à reprendre telles quelles).**
- **Le crédit est supposé constant** : l'étude porte sur l'effet à court terme sur la liquidité, pas sur le crédit.
- Marché interbancaire parfait dans le cas de base ; même pourcentage de sortie dans toutes les banques.
- La banque centrale fournit la liquidité demandée via ses opérations normales (note 9).
- Les auteurs précisent que ces résultats ne sont pas des prévisions.

**Pour nous.**
- Leur α\_i est l'analogue direct de notre b : ce que la banque peut absorber avec ses réserves sans rien emprunter.
- Leur scénario B (garder la moitié du tampon) correspond à notre **κ = 0,5** de la sortie S10. On peut donc réinterpréter κ : erreur de mesure **ou** préférence de liquidité.
- Notre ajout : passer de la liquidité au **crédit**, ce qu'ils n'étudient pas.
- Attention aux définitions : leur dénominateur est les dépôts de détail à vue, leur numérateur inclut les billets et la liquidité nette de leurs contraintes réglementaires. Les ordres de grandeur ne se comparent donc que prudemment.

### 1.2 Adalid et al. (2022) : les quatre canaux d'ajustement **[L]**

**Référence** : Ramón Adalid, Álvaro Álvarez-Blázquez, Katrin Assenmacher, Lorenzo Burlon, Maria Dimou, Carolina López-Quiles, Natalia Martín Fuentes, Barbara Meller, Manuel A. Muñoz, Petya Radulova, Costanza Rodriguez d'Acri, Tamarah Shakir, Gabriela Šílová, Oscar Soons, Alexia Ventula Veghazy (2022), « Central bank digital currency and bank intermediation: Exploring different approaches for assessing the effects of a digital euro on euro area banks », ECB Occasional Paper No 293, mai 2022.

**Apport central.** Quatre canaux par lesquels les banques s'ajustent : (I) restituer des billets ; (II) réduire leurs **réserves excédentaires** ; (III) emprunter à la banque centrale ; (IV) vendre des actifs à la banque centrale.
- Dans une économie sans friction, une MNBC est neutre pour l'intermédiation, parce que le bilan de la banque centrale s'ajuste.
- Les frictions (collatéral, réglementation de liquidité, stigmate de l'emprunt à la banque centrale) modifient ce résultat.
- Limite naturelle du canal II : les réserves excédentaires du système (≈ 4,3 billions d'euros en septembre 2021).

**Chiffres utiles.**
- Trois scénarios d'adoption : modérée (488 milliards), forte (7,49 billions), plafonnée à 3 000 € (1 148 milliards). La substitution de dépôts va de 0,5 % à 18 % des passifs bancaires.
- Avec un plafond de 3 000 € et 50 % de substitution des billets, il reste ≈ 12,5 % des dépôts à vue des ménages. Chaque tranche de 1 000 € de plafond ≈ 2 % des dépôts de la clientèle (≈ 340 milliards).
- Scénarios cités dans la littérature : sortie de 5 à 10 % des actifs bancaires (García et al., 2020) ; 20 % des dépôts des ménages et des entreprises non financières (Banque d'Angleterre, 2021).
- Simulation bancaire : pour des sorties de 4 % ou 8 %, presque toutes les banques utilisent leurs propres réserves. Le financement de la banque centrale n'intervient qu'à partir de ≈ 18 % (si les banques gardent la moitié de leurs tampons) ou 30 % (si elles utilisent tout).
- **Concentration des réserves** : 4 % des banques (60 % des actifs) détiennent plus de 74 % des réserves excédentaires.
- Cours de bourse : les banques les plus dépendantes des dépôts réagissent davantage aux annonces ; une réallocation de parts de marché du crédit d'environ 1,5 % est observée, temporaire.
- Ruées : un modèle calibré sur la Grèce et Chypre montre qu'une MNBC sans plafond accroît l'ampleur et la vitesse d'une ruée ; un plafond dur de 3 000 € compense cet effet.

**Pour nous.** Notre **B** est leur canal II ; notre **λ** est leur canal III (refinancement) ou IV (achats). Notre plage de ζ (0 à 30 %) couvre les scénarios de la littérature.

### 1.3 Fritz, Krüger & Wong (2024) **[L]**

**Référence** : Benedikt Fritz, Ulrich Krüger, Lui Hsian Wong (2024), « Digital euro: short-term effects on the liquidity of German banks considering holding limits », Deutsche Bundesbank Technical Paper 05/2024.

**Méthode.** Excédent de liquidité fondé sur le LCR ; déficit de liquidité = max(0 ; sorties nettes attendues − actifs liquides de haute qualité). Quatre scénarios : tous les clients utilisent leur plafond ; seuls les clients en ligne ; distribution réelle des soldes ; redistribution de liquidité au sein des réseaux de banques.

**Résultats.**
- Certaines caisses d'épargne et banques coopératives sont vulnérables.
- Avec un plafond de 3 000 €, le déficit agrégé reste d'environ 2 % des actifs liquides du système.
- Environ la moitié des ménages ne pourraient pas utiliser un plafond de 3 000 € en entier.
- Si la liquidité est redistribuée efficacement au sein des réseaux, la part de banques en déficit diminue des deux tiers.

**Pour nous.** La redistribution au sein d'un réseau est l'analogue de la **circulation de la liquidité entre pays** : l'agrégat UEMOA suppose qu'elle est parfaite, la partition par pays qu'elle est nulle.

### 1.4 Kumhof & Noone (2018) **[L]**

**Référence** : Michael Kumhof, Clare Noone (2018), « Central bank digital currencies — design principles and balance sheet implications », Bank of England Staff Working Paper No 725 ; version publiée : *Economic Analysis and Policy* 71 (2021), 553-572.

**Apport.** Quatre principes de conception : taux ajustable ; MNBC et réserves distinctes ; pas de convertibilité garantie des dépôts en MNBC ; émission contre titres éligibles. Si ces principes sont respectés, le financement des banques n'est pas nécessairement réduit et le crédit n'a pas à se contracter.
- Le crédit total n'est **jamais directement affecté** au premier tour. Des effets de second tour existent via les taux de prêt et la réglementation (NSFR, LCR).
- Si les titres vendus à la banque centrale viennent de non-banques, les dépôts ne quittent pas le système bancaire dans son ensemble.
- Sur les plafonds : les auteurs craignent qu'ils compromettent la parité et l'usage de la MNBC ; ils renvoient à l'argument selon lequel un plafond assez haut pour servir est trop haut pour contenir une ruée.

**Pour nous.** Ils soutiennent notre choix de partition B / λ et notre définition de B comme monnaie de banque centrale. Ils sont aussi la voix **sceptique sur les plafonds**, à opposer à Bindseil, Meller & Soons.

### 1.5 Bouis et al. (2024) : cadre du FMI **[L, sauf §5]**

**Référence** : Romain Bouis, Gaston Gelos, Paavo Miettinen, Fumitaka Nakamura, Erlend Nier, Gabriel Soderberg (2024), « Central Bank Digital Currencies and Financial Stability: Balance Sheet Analysis and Policy Choices », IMF Working Paper WP/24/226.

**Apport.** Scénarios de bilan numérotés de 0 à 4-B.
- **Scénario 0** : la MNBC remplace des **billets** ; effet limité sur les banques. Les auteurs notent qu'il concerne les économies où l'usage des espèces domine, comme certains pays africains et caribéens.
- **Scénario 1** : les banques ont des réserves excédentaires et les utilisent ; effets limités.
- **Scénarios 2 et 3** : la banque centrale accroît son bilan (prêts aux banques ou achats de titres) ; les ratios de liquidité se dégradent mais **les prêts ne changent pas** au premier tour.
- **Scénario 4** : second tour (coûts de financement répercutés sur les taux de prêt) : le crédit baisse de 4 % (4-A) et 8 % (4-B) dans l'exemple stylisé, en unités arbitraires.

**Autres points utiles.**
- Encadré 1 : le total des réserves bancaires ne change que par des opérations de la banque centrale. Les transactions entre banques déplacent les réserves sans les créer.
- Les preuves empiriques sur le lien entre monnaie de banque centrale et crédit sont rares ; une corrélation négative entre part des billets dans les dépôts et crédit/PIB (131 pays, R² ≈ 0,24) n'est pas causale.
- Les effets sont plus préoccupants dans les économies où les entreprises dépendent du crédit bancaire.
- La conception (plafonds, rémunération nulle, interopérabilité) est le levier principal pour limiter les risques.

**Pour nous.** Le cadre de référence de notre partition **B (scénario 1) / λ (scénarios 2-3) / second tour (scénario 4)**. Il nous oblige à reconnaître que notre contraction de crédit **par le rationnement des quantités** est plus brutale que ce que la littérature suppose.

### 1.6 Trinnou (2023, COFEB) : mobile money et politique monétaire en UEMOA **[L]**

**Référence** : Gbêmèho Mathieu Trinnou (2023), « Impact du mobile money sur l'efficacité de la politique monétaire : cas de l'UEMOA », Documents d'Études et de Recherche, COFEB/BCEAO, N° DER/2023/03, décembre 2023.

**Méthode et données.** Modèle SVAR par pays, 8 pays ; données mensuelles, janvier 2018 à décembre 2022 (53 observations utilisées) ; PIB mensualisé par spline cubique ; restrictions récursives qui rendent le mobile money exogène.

**Résultats.**
- Sauf au Niger et au Togo, un choc positif sur les services financiers mobiles accroît la masse monétaire, les dépôts bancaires et les créances sur l'économie.
- Exemples (en points de PIB pour un choc d'un écart-type) : Burkina Faso, masse monétaire + 0,55, dépôts + 0,42, créances + 0,23 ; Côte d'Ivoire, + 0,45, + 0,20, + 0,17 ; Mali, dépôts + 0,21, créances + 0,21 ; Bénin, dépôts + 0,18, créances + 0,30.
- Seule la Côte d'Ivoire montre un effet sur l'inflation (+ 0,18 point), via la circulation fiduciaire.
- Contexte : de 18,2 millions de comptes en 2014 à 131 millions en 2021 ; 63 895 milliards de FCFA d'opérations en 2021 ; 60 % des comptes chez les établissements de monnaie électronique, 40 % chez les banques. Le taux d'activité des points de service est de 6 % au Niger contre plus de 40 % ailleurs.

**Limites (à signaler).** Échantillon court ; spline pour le PIB ; identification récursive imposée ; mesure du choc en écart-type, pas en part des dépôts converties ; le texte ne distingue pas les comptes de cantonnement de la monnaie électronique, déjà placés en banque.

**⚠ À revérifier dans le texte.** La page COFEB de l'étude dit, dans son résumé, que les effets sur la croissance et l'inflation ne sont pas significatifs dans l'Union. Notre ligne « Côte d'Ivoire + 0,18 sur l'inflation » doit être confrontée à la formulation exacte du corps du texte (significativité, seuil, horizon) avant citation.

**Pour nous.** Le meilleur analogue régional d'une substitution numérique : il suggère une **complémentarité** avec les dépôts et non une fuite. Une MNBC différerait du mobile money par l'absence d'intermédiaire bancaire, ce que l'étude ne teste pas.

### 1.7 Whited, Wu & Xiao (2023) : calibration américaine du lien dépôts-crédit **[L]**

**Référence** : Toni Whited, Yufeng Wu, Kairong Xiao, « Will Central Bank Digital Currency Disintermediate Banks? », IHS Working Paper 47 (2023) ; circule depuis 2022. **Working paper** : le dépôt de l'IHS le classe « non évalué par les pairs » (SSOAR indique l'inverse) ; Bidder et al. le citent comme « unpublished ». Publication en revue non trouvée.

**Méthode.** Modèle structurel de demande de monnaie (dépôts, cash, MNBC) estimé sur les **banques américaines, 1994-2019** (Call Reports), avec un marché de gros de financement profond. **La MNBC est synthétique** : aucune donnée n'existe, ses attributs sont ceux du cash, d'un dépôt transactionnel et d'une prime « digitale » de 20 % empruntée à une étude externe.

**Résultats chiffrés.**
- 1 $ de MNBC retire **81,5 cents de dépôts** et **18,9 cents de crédit** (passage dépôts vers crédit ≈ **23 %** si la MNBC n'est pas rémunérée, ≈ **29 %** si elle l'est). C'est le « un quart » de nos notes.
- La MNBC prend peu au cash (≈ 11 cents), parce que le cash pèse ≈ 7 % de leur marché des dépôts.
- Trois canaux, par ordre d'importance : quantité des dépôts (≈ 15,8 cents), profits (≈ 11,4), coût du financement de gros et risque de taux (≈ 8,4).
- MNBC rémunérée au taux directeur : elle capte ≈ 31 % du marché. MNBC intermédiée avec commodité et commissions à 100 % : environ −34 cents de crédit par dollar.
- **Hétérogénéité de taille** : le passage vers le crédit est nettement plus fort pour les petites banques que pour les grandes.
- **Benchmark pour les marchés émergents** : ils citent Khwaja & Mian (2008, *AER* 98(4), 1413-42) : ≈ 60 cents de crédit perdus par dollar de dépôt perdu (Pakistan). Vu seulement via cette citation, à lire à la source.

**⚠ Incohérence du paper.** Les effets par taille de banque diffèrent entre le texte (§6.3), le Tableau 7 et le §7.3 (par exemple 40,7 contre 38,9 cents pour le crédit des petites banques). Ne retenir que le sens qualitatif, ou citer le tableau explicitement.

**Pour nous.**
- Le ≈ 0,25 vaut pour un marché de gros profond. **Ce n'est pas la borne basse pour l'UEMOA** : un marché de gros mince ressemble à leurs petites banques ou au cas pakistanais (§4.1).
- Cash dominant : le cas du scénario 0 de Bouis et al. et notre paramètre π sont renforcés (§4.2).
- Les 80 cents sont conditionnels à la qualité supposée de la MNBC.

### 1.8 Ree (2023) : l'eNaira un an après **[L]**

**Référence** : Jookyung Ree (2023), « Nigeria's eNaira, One Year After », IMF Working Paper WP/23/104, 16 mai 2023. DOI 10.5089/9798400241642.001. Working paper du FMI, avertissement « recherche en cours ».

**Chiffres vérifiés dans le PDF.**
- ≈ 860 000 portefeuilles de détail, soit 0,8 % des comptes bancaires actifs.
- ≈ 14 000 transactions par semaine, soit 1,5 % du nombre de portefeuilles (d'où « 98,5 % non utilisés dans une semaine donnée »).
- Valeur hebdomadaire moyenne : 923 millions de nairas, soit 0,0018 % de M3.
- ≈ 802 000 transactions depuis le lancement, **moins que de portefeuilles** : la plupart n'ont servi qu'une fois au plus.
- ≈ 100 000 portefeuilles marchands, environ un onzième des marchands équipés d'un terminal de paiement.

**⚠ Date.** Le texte écrit « fin novembre 2021 ». Impossible : l'eNaira est lancé le 25 octobre 2021, et le paper donne 500 000 portefeuilles en 25 jours, puis +63 jours pour 600 000 et +143 jours pour 700 000, soit 231 jours, donc vers juin 2022 pour 700 000. Les graphiques courent jusqu'à fin novembre 2022. **Inférence de ma part** : les 860 000 datent de **fin novembre 2022**, et le « 2021 » est une coquille du paper, reprise par la presse. À écrire ainsi : « fin novembre 2022 (le texte indique 2021, incompatible avec sa propre chronologie) ».

**Pièges d'interprétation.**
1. **0,0018 % de M3 est un flux hebdomadaire rapporté à un stock.** Ce n'est pas la part des dépôts passée en eNaira. Ne jamais l'utiliser comme estimation de ζ.
2. **98,5 % est un ratio transactions/portefeuilles** calculé par l'auteur, pas une mesure de portefeuilles distincts actifs. À écrire « ordre de grandeur ».
3. **Ree n'estime aucune substitution dépôts vers eNaira.** Bilan descriptif d'un pays sur un an, avec un écart de change parallèle de 60 % qui brouille tout. Il montre ζ ≈ 0 pendant la première année d'une MNBC africaine, pas plus.

**Ce qui sert au modèle.**
- **Plafonds réels** : paliers de solde de 120 000 à 5 000 000 de nairas selon la vérification d'identité ; marchands sans plafond mais avec un balayage quotidien vers leur compte bancaire ; eNaira non rémunéré. Analogue concret de ζ\_cap, et l'auteur juge que cela limite la désintermédiation.
- **Complément ou substitut du mobile money** : l'auteur défend la complémentarité (plafonds, pas de services annexes). Argument conceptuel, pas résultat empirique ; recoupe Trinnou.
- **Équilibres multiples (Annexe II)** : modèle stylisé de l'auteur, sans estimation. Adoption basse tant qu'un seuil n'est pas franchi, puis emballement. Conséquence à écrire en limite : la distribution de ζ est plutôt **bimodale** qu'uniforme sur [0 ; 30 %].
- **Référence à ajouter** : BIS (2021), *Central Bank Digital Currencies: financial stability implications*, citée par Ree pour le scénario où les banques rétablissent leur LCR par du financement de gros. Non vérifiée par moi.

### 1.9 Bidder, Jackson & Rottner (2025) : désintermédiation lente et rapide **[L partiel]**

**Référence** : Rhys Bidder, Timothy Jackson, Matthias Rottner (2025), « CBDC and banks: disintermediating fast and slow », BIS Working Paper No 1280, juillet 2025 ; versions antérieures : Deutsche Bundesbank Discussion Paper 15/2024 ; Liverpool WP. **Working paper** : pas de version publiée trouvée. Lu : texte principal et annexes A-B ; annexes C à H non lues.

**Enquête** (Bundesbank, Survey on Consumer Expectations, avril 2023, ≈ 5 700 répondants, **hypothétique**).
- Temps normal : 43,2 % détiendraient un euro numérique non rémunéré ; 54,3 % s'il l'était au taux du compte courant. Part moyenne ≈ 9 % du portefeuille ; ≈ 21 % chez les « keen ».
- Stress : 58 % (avec information sur la sécurité de la monnaie centrale) contre 49 % retireraient vers l'euro numérique. Entre 25 et 35 % de ceux qui n'en détiendraient pas en temps normal le feraient quand même en stress. La part restée sur compte baisse d'environ 23 % : l'euro numérique **augmente** les retraits, il ne fait pas que remplacer le cash. Le cash reste l'actif refuge dominant.
- Confiance dans la BCE : confiance forte = +10 points sur la probabilité d'adoption ; confiance faible = −22 points ; avoir été adulte en Allemagne de l'Est avant 1989 = −6 points.

**Modèle.** DSGE à ruées endogènes (équilibres multiples, sunspot), calibré sur la zone euro 2000-2023 ; la demande de MNBC est calibrée sur l'enquête (ratio MNBC/cash de 0,66 en base).
- Probabilité annuelle de ruée : **2,46 %** avec MNBC, **1,34 %** sans (une ruée tous les ~40 ans contre ~75 ans) ; **1,16 %** avec un plafond ; **0,92 %** avec une MNBC rémunérée indexée sur le taux directeur.
- Plafond optimal ≈ **1 750 €** en base, ≈ 2 750 € en scénario « keen » (note 17). Les auteurs le disent « en ligne » avec les 3 000 € discutés dans le débat européen. Ils jugent les plafonds plus simples et plus robustes que la rémunération, qui exigerait un taux négatif en pleine ruée.

**Pourquoi leur résultat négatif est conditionnel.** La banque centrale investit les fonds de MNBC en titres. Ils notent eux-mêmes que si elle les replaçait **instantanément en dépôts bancaires** (Brunnermeier-Niepelt), les ruées d'équilibre disparaîtraient. **C'est notre λ.**

**Réserves.**
- L'enquête donne des allocations hypothétiques de 1 000 € par mois et de 5 000 € de stock, chez des Allemands réputés attachés au cash : pas une part du stock de dépôts, et pas transposable à l'UEMOA.
- Dans le modèle, la désintermédiation lente est minuscule (dépôts 3,51 contre 3,53, soit −0,6 % ; spread ≈ 7 points de base). La MNBC prend surtout au cash, parce que le ratio MNBC/cash est la cible. L'enquête montre la baisse proportionnelle la plus forte sur les dépôts. Les auteurs admettent ne pas reproduire cash et MNBC à la fois en normal et en stress. **Inférence de ma part** : le modèle sous-estime probablement la désintermédiation lente.
- La fréquence de ruée (une tous les 75 ans) est une cible calibrée : ne retenir que les écarts relatifs.
- Pas de banques hétérogènes, pas d'assurance-dépôts, ruées systémiques seulement.
- Incohérence mineure : l'introduction annonce un optimum entre 1 500 et 2 500 €, la note 17 donne 2 750 € pour le scénario « keen ».

### 1.10 Tadenyo (2021, COFEB) : liquidité bancaire et crédit en UEMOA **[P]**

**Référence** : Tadenyo (2021), « Liquidité bancaire et financement de l'économie dans l'UEMOA », COFEB/BCEAO, Document d'Étude et de Recherche n° 04/2021 (intitulé et prénom de l'auteur à reconfirmer sur le PDF).

**Méthode.** Panel de 94 banques, 2010-2019, trimestriel ; régressions de la croissance du crédit sur des ratios de liquidité et de refinancement (GMM) ; modèle à seuil sur le refinancement BCEAO.

**Résultats et contexte utiles.**
- La liquidité propre et le refinancement BCEAO sont associés positivement à la croissance du crédit.
- **Seuil estimé** : ≈ 2 510 milliards de FCFA de refinancement BCEAO (intervalle 1 669 à 3 435). **Ce n'est pas notre seuil** : c'est le niveau au-delà duquel un effet sur la croissance du crédit apparaît. À distinguer explicitement d'un seuil d'absorption de retrait.
- **Marché interbancaire mince** : emprunt interbancaire quotidien moyen de 1,5 à 3,6 milliards, contre des avances BCEAO de plusieurs milliers de milliards. Cela soutient un φ élevé.
- **Régime de refinancement** : la BCEAO a volontairement tenu son offre sous la demande après 2016 (guichet marginal plafonné à 2 fois les fonds propres), puis l'a gonflée en 2020 avec les mesures de crise. Du texte de Tadenyo, pas des décisions BCEAO elles-mêmes.
- **Concentration** (relevé à reconfirmer) : les grandes banques détiendraient l'essentiel de la liquidité (≈ 79 %) et des avances BCEAO (≈ 86 %) à fin 2020.
- Ratio créances/dépôts moyen légèrement supérieur à 100 % sur 2007-2020 : D ≈ L, cohérent avec la règle empirique de Whited et al.

**Réserves.**
1. **Ce n'est pas un passage dépôts vers crédit** : le papier régresse la croissance du crédit sur un ratio de liquidité. **Ne pas calibrer φ dessus.**
2. Le test de Hansen donne p = 1,000 partout et le Sargan atteint 2 815 : signe probable de prolifération d'instruments (retards jusqu'à 13 pour 94 banques), donc test peu informatif. **Inférence de ma part** : je n'ai pas vu le nombre d'instruments.
3. Texte et tableaux divergent (liquidité fin 2020 : 2 809 milliards dans le texte, 1 600 dans le Tableau 1b). Reprendre les chiffres dans les statistiques BCEAO.

### 1.11 Sissoko & Dembélé (2025) : seul texte UEMOA sur MNBC et banques **[P]**

**Référence** : Sissoko & Dembélé (2025), *Revue Internationale de la Recherche Scientifique* (Revue-IRS), ISSN 2958-8413 ; PDF : revue-irs.com, téléchargement 1093/723. **Titre, prénoms et numéro à compléter depuis le PDF.** Revue que je ne connais pas : rigueur de l'évaluation à vérifier.

**Nature.** Discussion qualitative, institutionnaliste. Leur tableau de désintermédiation (−5 % à −50 % des dépôts selon l'adoption) est signé « Source : Auteurs », **sans modèle décrit**, et les auteurs reconnaissent le caractère prospectif de ces chiffres.

**À ne pas reprendre :**
- l'attribution à Bindseil (2020) d'une réallocation de 30 à 50 % des dépôts en cinq ans, que je n'ai pas retrouvée (Bidder et al. associent Bindseil 2020 au repère de 3 000 €) ;
- une « note technique BCEAO 2025 sur le projet pilote eCFA », introuvable sur les sites que j'ai vus, et qui contredit la ligne BCEAO de juillet 2026 (§1.12) ;
- un « IMF (2023) » dont le lien est une page générique.

**Usage** : discussion anticipative de l'UEMOA, **jamais pour ses chiffres**.

### 1.12 Statut de la MNBC à la BCEAO **[R]**

- **Financial Afrik (23 juillet 2026)**, sur le Rapport annuel 2025 de la BCEAO (présenté le 22 juillet 2026) : aucune décision de déploiement n'est prise ; une phase d'études est en cours. **Presse, pas le rapport lui-même** : à confirmer dans le PDF.
- D'autres sites annoncent une « expérimentation lancée » ou un lancement « imminent ». Ils contredisent cette ligne et sont de fiabilité faible. Pour l'un d'eux, j'ai vu le titre d'une mise en demeure publiée par Financial Afrik, sans l'avoir lue. À écarter.
- **Conséquence** : le cadrage « MNBC hypothétique et conditionnelle » reste correct au 10 novembre 2026.

### 1.13 Textes cités dans les textes lus (non lus)

Brunnermeier & Niepelt (2019) ; Andolfatto (2021) ; Keister & Sanches (2022-2023) ; Chiu et al. (2022-2023) ; Burlon et al. (2024) ; Diamond & Dybvig (1983) ; Muñoz & Soons (2023, ECB WP 2801) ; Ahnert et al. (2023) ; Khwaja & Mian (2008) ; Bindseil (2020, ECB WP 2351). Adalid et al., Bouis et al., Whited et al. et Bidder et al. les décrivent comme suit : neutralité sous refinancement (B&N, Kumhof & Noone) ; absence d'effet sur le crédit mais baisse du profit sous pouvoir de marché (Andolfatto) ; éviction du crédit sous concurrence parfaite sans financement de gros (Keister & Sanches) ; une ruée par panique, dont l'ampleur est indépendante de la disponibilité de MNBC (Muñoz & Soons dans Adalid et al.).

**Piste ouverte [R]** : BCEAO, DEAE n° 21/01 sur les mécanismes de transmission de la politique monétaire en UEMOA. Un extrait de recherche attribue à une hausse du taux du marché monétaire un effet sur le ratio de prêts bancaires beaucoup plus fort pour les petites banques que pour les grandes (≈ 0,090 contre ≈ 0,011 point). Cohérent avec Whited et al., mais **vu seulement en extrait** : ouvrir le PDF avant citation.

---

## 2. Ce que la littérature dit : sept messages

1. **L'effet dépend de qui finance la MNBC.** Elle puise dans des billets (aucun effet bancaire), dans des réserves excédentaires (effet faible) ou dans des dépôts compensés par la banque centrale (effet sur le coût du financement). Bouis et al., Adalid et al.
2. **La neutralité est le cas de référence, les frictions la modifient.** Brunnermeier-Niepelt, Kumhof-Noone, Adalid et al.
3. **Au premier tour, le crédit ne baisse pas.** Il baisse au second tour, via le prix du financement. Kumhof-Noone, Bouis et al. L'ordre de grandeur dépend de la profondeur du marché de gros : un quart de la baisse des dépôts aux États-Unis (Whited et al.), plus de la moitié pour les petites banques ou le Pakistan (Whited et al. citant Khwaja & Mian) ; −4 à −8 % dans un exemple stylisé (Bouis et al., unités arbitraires).
4. **Les plafonds de détention sont la mesure la plus citée.** Un plafond de 3 000 € contiendrait l'impact en zone euro (Meller & Soons, Fritz et al., Adalid et al.). Bidder et al. trouvent un optimum plus bas (≈ 1 750 €) et le jugent « en ligne » avec 3 000 €, ce qui n'est pas une preuve de suffisance. Kumhof & Noone doutent qu'un plafond utile soit assez bas.
5. **L'hétérogénéité est systématique.** Entre banques (Adalid, Fritz, Whited), entre pays (Meller & Soons, confiance chez Bidder) ; la redistribution de liquidité y répond (Fritz).
6. **Les ruées sont un problème distinct.** Elles dépendent de la conception, et la littérature n'est pas d'accord sur leur probabilité (Bidder : la MNBC l'augmente sans plafond ; Muñoz & Soons : ampleur indépendante).
7. **Le recyclage décide du signe du résultat.** Si la banque centrale replace les fonds dans les banques, les effets négatifs disparaissent (Brunnermeier-Niepelt ; reconnu par Bidder et al.). Sinon, la MNBC peut déstabiliser. C'est le levier que λ représente dans notre modèle.

---

## 3. Correspondances avec notre modèle

| Notre élément | Équivalent dans la littérature | Lien |
|---|---|---|
| B (monnaie centrale excédentaire) | Canal II (Adalid) ; scénario 1 (Bouis) ; α\_i (Meller & Soons) | Fort |
| λ (recyclage) | Canal III (refinancement) ; scénarios 2-3 ; équivalence B&N ; hypothèse de non-recyclage chez Bidder et al. | Fort ; **λ dépend du régime BCEAO** (Tadenyo) |
| Seuil ζ\* | Sortie à partir de laquelle la banque centrale doit fournir de la liquidité (≈ 18-20 % en zone euro) | Notre seuil est **plus bas** (7-13 %) : définitions et contexte différents. À ne pas confondre avec le seuil de refinancement de Tadenyo |
| Plafond ζ\_cap | Plafond de 3 000 € ≈ 15 % des dépôts de détail ; paliers de l'eNaira (Ree) | Nos plafonds de 2 à 20 % couvrent cette plage |
| Partition par pays / agrégat | Tableau B.1 (Meller & Soons) ; marché interbancaire cloisonné ; redistribution intra-réseau (Fritz) ; confiance (Bidder) | Fort |
| κ (erreur de mesure) | Scénarios de tolérance A/B/C de Meller & Soons | Réinterprétation possible |
| φ (répercussion sur le crédit) | 0,25 (Whited et al., marché de gros profond) ; ≈ 0,5-0,6 (petites banques ; Khwaja & Mian via Whited) ; second tour (Bouis, scénario 4) | **À recalibrer vers le haut** pour l'UEMOA, à confirmer |
| π (part de la MNBC financée par des dépôts) | Scénario 0 (Bouis) ; cash ≈ 7 % chez Whited ; adoption faible (Ree) | Nouveau paramètre |

---

## 4. Conséquences pour notre travail : ce que la lecture force à corriger

1. **Notre contraction du crédit est une borne haute par construction, et φ est un paramètre central.** Elle suppose que le déficit résiduel est comblé en rationnant les quantités (HI1). La littérature fait baisser le crédit par le **prix** (second tour). **Correction par rapport à la v1** : le ≈ 0,25 de Whited et al. vaut pour un marché de gros profond, **pas pour l'UEMOA**. Pour une zone où le marché interbancaire est mince (Tadenyo), le repère pertinent commence plus haut (≈ 0,5-0,6 selon leurs petites banques et le cas pakistanais, à confirmer à la source). Présenter φ comme une fourchette, borne haute φ = 1.
2. **ζ n'est pas forcément une fuite de dépôts.** Dans une économie où les espèces dominent, la MNBC peut d'abord puiser dans les billets (scénario 0 de Bouis et al.), et le mobile money montre une complémentarité avec les dépôts (Trinnou). **Ajouter un paramètre π : la part de la MNBC financée par des dépôts**, avec π < 1 comme cas réaliste. Le seuil exprimé en MNBC totale serait ζ\*/π. Ne pas déduire ζ d'une adoption observée : Ree donne un flux, pas un stock, et sa première année est un cas de ζ ≈ 0.
3. **Notre b est brut des préférences de liquidité des banques.** Meller & Soons montrent que les banques ne veulent pas tout utiliser (scénario B : la moitié du tampon volontaire). Notre b correspond à leur scénario A. **κ = 0,5 est donc un cas de base plausible**, pas un cas pessimiste. À remonter dans le texte.
4. **λ est conditionnel au régime, pas un cas extrême.** En zone euro, les travaux supposent que la banque centrale fournit la liquidité demandée (Meller & Soons, note 9 ; Adalid et al.). Bidder et al. montrent que le signe du résultat dépend du recyclage. Pour l'UEMOA, la BCEAO a rationné le refinancement en régime normal après 2016 et l'a gonflé en 2020 (Tadenyo). **Présenter λ comme une fonction du contexte (normal ou crise)**, pas comme 0 ou 1.
5. **Nos seuils sont plus bas que ceux de la zone euro** (7-13 % contre 12-20 % de sortie absorbable), mais les définitions diffèrent (leur dénominateur est les dépôts de détail ; ils incluent les billets ; ils appliquent des contraintes de LCR). **Ne pas conclure que l'UEMOA est plus fragile** sans harmoniser.
6. **Reformulation de la phrase sur la lacune.** Ancienne version : « aucune étude lue n'applique la logique de seuil à l'UEMOA ». **Nouvelle version proposée** : « À notre connaissance, et dans la littérature examinée jusqu'au 10 novembre 2026, aucune étude ne quantifie, pour l'UEMOA, le resserrement du crédit qu'entraînerait une sortie de dépôts vers une MNBC hypothétique, à partir des bilans bancaires. Les travaux les plus proches sont qualitatifs et scénarisés (Sissoko & Dembélé, 2025) ou portent sur le lien entre liquidité et crédit sans MNBC (Tadenyo, 2021). » **À reconfirmer** après lecture complète de Sissoko & Dembélé (extraction tronquée) : vérifier s'ils chiffrent aussi un effet sur le crédit.
7. **Notre modèle est un choc exogène, pas un modèle de ruée.** Bidder et al. expliquent pourquoi la sortie peut être bien plus grande en stress, ce que nous n'endogénéisons pas. À écrire en limite. Ne pas déduire ζ en stress de l'adoption en temps normal (25 à 35 % de ceux qui n'adopteraient pas retireraient quand même).
8. **Justifier ζ par pays, ou discuter l'hétérogénéité.** La confiance explique une part importante de l'adoption chez Bidder et al. ; Tadenyo et Meller & Soons montrent des profils de liquidité inégaux entre banques et entre pays. Un ζ unique pour les huit pays est une hypothèse à défendre.
9. **Cadrage institutionnel.** La BCEAO indique en juillet 2026 qu'aucune décision de déploiement n'est prise (presse, à confirmer dans le rapport). Écrire la MNBC comme **scénario conditionnel**, pas comme projet imminent.

---

## 5. Références

**Recoupées via les bibliographies des textes lus (non vérifiées à la source)** : Andolfatto, *Economic Journal* 131(634), 525-540 (Bidder et al. écrivent 2020, le volume date de 2021) ; Fernández-Villaverde, Sanches, Schilling & Uhlig, *Review of Economic Dynamics* 41, 225-242 ; Khwaja & Mian (2008), *AER* 98(4), 1413-42 ; Keister & Monnet (2022), *JEDC* 142, 104501 ; Muñoz & Soons (2023), ECB WP 2801 ; Williamson (2022), « CBDC and flight to safety », *JEDC* 142, 104146 ; Keister & Sanches, *Review of Economic Studies*, en ligne mars 2022 (rdac017) ; Chiu et al., *JPE* (2022 chez Bidder et al., à confirmer sur le volume imprimé) ; Burlon, Muñoz & Smets (2024), *AEJ: Macroeconomics* ; Kim & Kwon (2022), *JMCB* ; Bindseil (2020), « Tiered CBDC and the financial system », ECB WP 2351 ; Meller & Soons (2023), ECB OP 326, août 2023.
**Remarque** : la date d'un article (en ligne ou volume imprimé) varie d'une source à l'autre. Choisir la date du volume imprimé une fois vérifiée.

**Toujours non vérifiés** : Williamson (2022), *J. Political Economy* 130(11), 2829-2861 (**article différent** de celui du *JEDC* ci-dessus) ; Gross & Letizia (2023), IMF WP 2023/009 ; Assenmacher et al. (2021), ECB WP 2578 (Bidder et al. citent un autre papier : WP 2811, 2023) ; Castrén, Kavonius & Rancan (2022), *J. Financial Stability* 60 ; Gorelova et al. (2022), Banque du Canada ; Merrouche & Nier (2012) ; Grodecka-Messi & Zhang (2023) ; Agur, Ari & Dell'Ariccia (2022) ; Mawejje & Lakuma (2019), *Financial Innovation* 5(1) ; Kipkemboi & Bahia (2019), GSMA ; BIS (2021), *Central Bank Digital Currencies: financial stability implications* (cité par Ree).

**À compléter** : titre complet et prénoms de Sissoko & Dembélé ; titre et prénom exacts de Tadenyo ; confirmation du numéro de la revue Revue-IRS.

**À lire en priorité** (accès gratuit, apportent des chiffres) :
1. BCEAO, Rapport annuel 2025 (PDF source) : vérifier la ligne sur la MNBC.
2. BCEAO, DEAE n° 21/01 : hétérogénéité par taille de banque dans l'UEMOA.
3. Khwaja & Mian (2008) : à lire pour trancher la borne basse de φ.
4. Fin de Kumhof & Noone ; §5 de Bouis et al. ; annexes C à H de Bidder et al.
5. BIS (2021), *Financial stability implications* ; Krüger & Wong (2026).

**À chercher** : autres publications COFEB et FMI sur l'UEMOA, littérature francophone, textes sur le cantonnement des fonds de monnaie électronique, éventuel article publié de Whited et al.

---

## 6. Plan proposé pour la section « Revue de littérature »

1. **Ce que fait une MNBC aux bilans bancaires** : canaux d'ajustement et neutralité (Adalid, Kumhof & Noone, Bouis, Brunnermeier & Niepelt).
2. **Les frictions et le crédit** : second tour, pouvoir de marché, éviction, profondeur du marché de gros (Keister & Sanches, Andolfatto, Chiu et al., Whited et al., Khwaja & Mian).
3. **Les simulations de liquidité bancaire et les plafonds** : Meller & Soons, Fritz et al., Bindseil, Bidder et al.
4. **Ruées, recyclage et conception** : désintermédiation lente et rapide ; le rôle du recyclage (Bidder et al., Brunnermeier & Niepelt).
5. **Hétérogénéité et circulation de la liquidité** : entre banques et entre pays.
6. **L'Afrique et l'UEMOA** : adoption (Ree, Sun & Rizaldy), mobile money (Trinnou), liquidité et crédit (Tadenyo), discussion anticipative (Sissoko & Dembélé), contexte institutionnel BCEAO.
7. **La lacune et notre contribution** : passer de la liquidité (Meller & Soons) au **resserrement du crédit** dans une union monétaire à 8 pays aux matelas inégaux, sous une MNBC hypothétique, avec test de robustesse sur la mesure de b, φ recalibré et λ conditionnel au régime.

**Tensions à écrire** : neutralité contre éviction ; plafond efficace contre plafond inutile (Kumhof & Noone) ; migration progressive contre ruée ; recyclage qui neutralise le risque contre recyclage rationné (Tadenyo).
