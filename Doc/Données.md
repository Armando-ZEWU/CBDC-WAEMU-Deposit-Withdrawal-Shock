# Données

**Calibration du modèle « Simulation de choc de retrait » : données extraites, calculs, décisions et lacunes**

> **Statut** : version de travail 3 (choix de modélisation validés, voir §7 ; résultats de l'extraction des 8 pays, voir §9 et le classeur « Données Extrait.xlsx »). Tous les chiffres viennent des rapports annuels de la Commission Bancaire de l'UMOA (2021, 2023, 2024, 2025), sauf mention contraire. Le rapport 2022 est un scan sans couche de texte : il n'a pas été exploité ; les chiffres 2022 proviennent des rapports 2023 et 2024.
> **Unités** : milliards de FCFA, sauf mention. Les rapports publient en millions ; les montants ont été divisés par 1 000.
> **Convention** : [R] = repris d'un rapport ; [C] = calculé ici ; [H] = hypothèse ou décision de modélisation.

---

## 1. Sources et traçabilité

| Élément | Rapport | Localisation (page PDF) |
|---|---|---|
| D et L, UEMOA 2023-2025 | Rapport 2025 | « Chiffres clés », p. 29 |
| D et L, UEMOA 2021-2022 | Rapport 2023 | Agrégats UEMOA, p. 102 |
| Bilan Côte d'Ivoire 2023-2025 (actif, passif, emplois-ressources) | Rapport 2025 | Annexe II.2.3.b, p. 192-194 |
| Crédits et dépôts Côte d'Ivoire 2021-2022 | Rapports 2023 et 2024 | Annexe II.2.3, Emplois-ressources (pages 2023 : 194-196 ; 2024 : à relever) |
| Coefficient de liquidité par pays | Rapports 2021, 2023, 2024, 2025 | Rapport 2025 : tableau n° 19, p. 105 ; conformité : tableau n° 20, p. 106 |
| Monnaie électronique (EME) | Rapport 2025 | C.2, p. 32 |

**Règle de millésime** : pour chaque année, on retient la valeur du rapport **le plus récent** qui la publie. Les données sont révisées : par exemple, les dépôts de l'UEMOA en 2023 sont de 45 054,1 dans le rapport 2023 (provisoire) et de 44 986,3 dans le rapport 2025. Les données de **2025 sont provisoires**.

---

## 2. UEMOA : dépôts, crédits, ratio crédit/dépôts [R, C]

| Année | D : dépôts et emprunts | L : crédits | ρ = L/D [C] |
|---|---|---|---|
| 2021 | 38 906,2 | 27 454,0 | 0,706 |
| 2022 | 43 754,3 | 32 715,3 | 0,748 |
| 2023 | 44 986,3 | 34 929,7 | 0,777 |
| 2024 | 48 429,5 | 36 699,9 | 0,758 |
| 2025 (prov.) | 56 200,2 | 38 731,6 | 0,689 |

*Lecture : en 2025, les dépôts progressent de 16,0 % et les crédits de 5,5 %. Le ratio crédit/dépôts recule donc nettement : les banques ont gagné des ressources plus vite qu'elles n'ont prêté.*

---

## 3. Côte d'Ivoire [R, C]

| Année | D : dépôts et emprunts | L : crédits | ρ [C] | Part de la Côte d'Ivoire dans D UEMOA [C] | Part dans L UEMOA [C] |
|---|---|---|---|---|---|
| 2021 | 14 003,8 | 9 689,1 | 0,692 | 36,0 % | 35,3 % |
| 2022 | 15 582,0 | 11 034,0 | 0,708 | 35,6 % | 33,7 % |
| 2023 | 16 112,0 | 12 026,2 | 0,746 | 35,8 % | 34,4 % |
| 2024 | 18 573,4 | 13 315,0 | 0,717 | 38,4 % | 36,3 % |
| 2025 (prov.) | 23 048,8 | 14 904,6 | 0,647 | 41,0 % | 38,5 % |

**Constat** : la valeur de 0,85 de la première version n'est compatible ni avec l'UEMOA (0,69 à 0,78 selon l'année) ni avec la Côte d'Ivoire (0,65 à 0,75). Le ρ de la Côte d'Ivoire est **plus bas** que celui de l'UEMOA chaque année.

### 3.1 Composition de D, Côte d'Ivoire 2025 [R, C]

| Poste | Montant | Part de D [C] |
|---|---|---|
| Dépôts à vue | 14 912,3 | 64,7 % |
| Dépôts à terme et bons de caisse | 3 744,6 | 16,2 % |
| Comptes d'épargne à régime spécial | 3 209,4 | 13,9 % |
| Autres | 1 182,5 | 5,1 % |
| **Total D** | **23 048,8** | 100 % |
| *dont dépôts de garantie reçus* | *991,4* | *4,3 %* |
| *dont emprunts à la clientèle* | *0,6* | *≈ 0,002 %* |

**Conclusion sur « dépôts et emprunts »** : l'agrégat de la Commission Bancaire correspond, pour la Côte d'Ivoire, aux **dettes envers la clientèle**. Les emprunts de la clientèle sont négligeables, et les emprunts interbancaires (2 545,5 en 2025) sont classés à part. La réserve de l'hypothèse HI6 du document principal (« D contient des emprunts non convertibles ») est donc **beaucoup plus faible que prévu**. Le vrai point d'attention est autre : D contient des dépôts de garantie, des dépôts à terme et de l'épargne, moins facilement convertibles que les dépôts à vue.

**Non extrait** : la ventilation de D entre ménages, entreprises et État, utile pour le plafond de détention (ζ_cap). À chercher dans les rapports.

---

## 4. Liquidité réglementaire [R]

### 4.1 La norme applicable

Le coefficient de liquidité exige que les **disponibilités et les emplois à durée résiduelle ≤ 3 mois couvrent au moins 75 % des exigibilités de même maturité**. Le dispositif prudentiel de 2018 prévoit aussi un RLCT (court terme) et un RLLT (long terme), que **les rapports 2023, 2024 et 2025 disent « pas encore applicables »**. Il n'y a donc **pas de LCR au sens de Bâle** dans l'UEMOA à ce jour.

**Seuil** : le rapport 2021 affiche « ≥ 50 % », les rapports 2023-2025 « ≥ 75 % ». La date du changement n'est pas établie (le rapport 2022 est un scan non lu).

### 4.2 Valeurs observées

| Année | UEMOA | Côte d'Ivoire |
|---|---|---|
| 2021 | 109,1 % | 104,7 % |
| 2022 | 107,3 % | 105,1 % |
| 2023 | 104,2 % | 102,8 % |
| 2024 | 106,8 % | 103,3 % |
| 2025 (prov.) | 128,6 % | 127,1 % |

**Autres pays, 2025** : Bénin 123,0 % ; Burkina Faso 79,5 % ; Guinée-Bissau 105,4 % ; Mali 128,4 % ; Niger 84,7 % ; Sénégal 241,3 % ; Togo 118,8 %.

**Conformité, Côte d'Ivoire 2025** : 27 banques sur 28 respectent le coefficient (tableau n° 20).

### 4.3 Pourquoi ce coefficient n'est pas une mesure de B [H]

Le numérateur du coefficient compte aussi les **crédits qui arrivent à échéance dans moins de trois mois**. Or ne pas renouveler ces crédits, c'est précisément la contraction du crédit que le modèle cherche à mesurer. Utiliser ce coefficient pour estimer B reviendrait à supposer ce qu'on veut démontrer. Il sert en revanche d'**indicateur de dispersion** entre pays (Burkina Faso et Niger sont proches du seuil de 75 %), utile pour le scénario σ\_b.

---

## 5. Calibration de b : deux approximations [C, H]

Aucun rapport ne publie directement B. On reconstruit deux approximations à partir du bilan agrégé des banques ivoiriennes (actif).

### 5.1 Composantes du bilan, Côte d'Ivoire [R]

| Poste (actif) | 2023 | 2024 | 2025 (prov.) |
|---|---|---|---|
| Caisse | 370,3 | 528,1 | 632,2 |
| Comptes ordinaires débiteurs (trésorerie et interbancaire) | 1 325,6 | 2 397,4 | 3 622,5 |
| Titres de transaction | 192,9 | 232,3 | 351,6 |
| Titres de placement | 4 251,5 | 5 154,7 | 5 084,8 |
| Titres d'investissement (exclus de B) | 2 130,3 | 2 068,3 | 3 293,5 |
| D (pour mémoire) | 16 112,0 | 18 573,4 | 23 048,8 |

### 5.2 Approximations de b [C]

| Approximation | Définition | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| **b stricte, brute** | (caisse + comptes ordinaires débiteurs) / D | 10,5 % | 15,7 % | 18,5 % |
| **b stricte, nette** (retenue en base) | brute − 3 % (réserves obligatoires approximées par 3 % de D) | **7,5 %** | **12,8 %** | **15,5 %** |
| b large, nette | stricte nette + titres de transaction et de placement | 35,1 % | 41,8 % | 39,1 % |

### 5.3 Décision de modélisation retenue [H] : la b stricte pour le système (voir §7)

Deux raisons.

1. **Argument d'agrégation.** Quand une banque vend un titre d'État à une autre banque de la zone, la liquidité passe d'une banque à l'autre : le système n'en gagne pas. Pour le **système bancaire pris dans son ensemble**, seule la monnaie de banque centrale (caisse et avoirs à la BCEAO) constitue un tampon net. Les titres ne créent de liquidité nette que s'ils sont achetés par des non-banques ou mis en pension auprès de la BCEAO, ce dernier cas relevant de **λ**, par la décision déjà prise (refinancement dans λ). La b large est donc à garder comme **borne supérieure de sensibilité**, pas comme valeur de base.
2. **Profondeur de marché.** Une vente simultanée de titres par plusieurs banques ferait baisser les prix. Une décote unique est insuffisante pour modéliser cet effet.

### 5.4 Limites de la b stricte [H]

- Les **comptes ordinaires débiteurs** regroupent les avoirs à la BCEAO, chez d'autres banques (intra-système, qui s'annulent pour le système) et auprès de correspondants à l'étranger. Ils ne se séparent pas dans ces rapports : la b stricte est donc une **borne supérieure** de la liquidité en monnaie centrale.
- Les **3 % de réserves obligatoires** sont appliqués à D comme approximation ; l'assiette réelle n'est pas dans ces rapports.
- Le chiffre varie beaucoup avec l'année : 7,5 % en 2023, 15,5 % en 2025. Les comptes ordinaires débiteurs ont été multipliés par 2,7 en deux ans. **Il ne faut pas calibrer b sur une seule année.**

### 5.5 Recoupement avec la BCEAO (source secondaire) [R]

Un article de presse financière cite, pour l'UEMOA en mars 2026, 4 734 milliards de réserves constituées pour 1 094 requis, soit un excédent de ≈ **3 640** [C]. Rapporté à D UEMOA 2025 (56 200), cela donne ≈ **6,5 %** [C]. Les dates diffèrent (mars 2026 contre fin 2025). Ce chiffre n'inclut que les réserves à la BCEAO : il est cohérent avec une b stricte qui serait une borne supérieure. **À vérifier dans le rapport BCEAO source**, pas dans la presse.

### 5.6 Lecture provisoire (non un résultat)

Avec ζ\* = b / (1 − λ), et λ = 0 en cas de base, un b compris entre **6,5 % et 15,5 %** signifie qu'il faudrait convertir **de l'ordre de 6 à 15 % des dépôts** avant que le crédit ne commence à baisser. Pour la Côte d'Ivoire en 2025, ça représente environ 1 500 à 3 600 milliards de FCFA, soit un ordre de grandeur à comparer à l'ampleur plausible de la conversion. Cette comparaison reste à faire (Q1) et dépend de la plage retenue pour ζ.

---

## 6. Ancrage pour ζ : monnaie électronique (EME) [R, C]

| UEMOA | 2023 | 2024 | 2025 (prov.) |
|---|---|---|---|
| Encours de monnaie électronique | 1 124 | 1 422 | 1 923 |
| Rapporté à D UEMOA [C] | 2,5 % | 2,9 % | 3,4 % |

**Lecture** : l'encours de monnaie électronique a augmenté de plus de moitié en deux ans et représente aujourd'hui un peu plus de 3 % des dépôts. C'est l'analogue régional le plus proche d'une substitution numérique, mais il comporte deux réserves :

- l'encours des EME est adossé à des fonds placés dans le système bancaire (la « trésorerie nette » des EME est de 2 110 en 2025), donc ce n'est pas nécessairement une fuite nette de dépôts ;
- le chiffre 2023 des « Chiffres clés » BCEAO (≈ 959) diffère de celui du rapport 2025 (1 124) : périmètre ou millésime différent, à éclaircir.

---

## 7. Choix de modélisation et justifications

Chaque choix est présenté avec ce qui a été **écarté** et **pourquoi**, parce qu'un rapporteur demandera pourquoi pas l'alternative.

### 7.1 Tableau récapitulatif

| # | Sujet | Retenu | Écarté | Pourquoi |
|---|---|---|---|---|
| C1 | Cadre | **UEMOA** principal, 8 pays comme groupes, **Côte d'Ivoire** en zoom | Côte d'Ivoire seule ; UEMOA agrégée sans pays | Une MNBC serait émise par la BCEAO pour l'union entière ; λ, réserves obligatoires et norme de liquidité se décident à ce niveau. Les pays fournissent une hétérogénéité observée |
| C2 | Refinancement BCEAO | Dans **λ** | Dans B | Mobilisation en cas de choc = choix de politique, pas stock observable. Évite le double comptage |
| C3 | Définition de D | « Dépôts et emprunts » (Commission Bancaire) | Dettes envers la clientèle ; dépôts à vue seuls | Définition publiée dans les rapports pour tous les pays, donc extraction homogène. En pratique quasi identique à la clientèle (Côte d'Ivoire) |
| C4 | Définition de B | **b stricte nette** en base ; **b large** en borne haute | b large en base ; coefficient de liquidité ; réserves BCEAO seules | Voir §7.3 |
| C5 | Année de calibration | **Fourchette 2021-2025** | Une seule année (2025 ou 2023) | b a doublé en deux ans ; une année unique cache un choix arbitraire |
| C6 | Hypothèse HI6 | Réécrite : le risque est la composition de D | Maintenue (« D contient des emprunts non convertibles ») | Emprunts de la clientèle négligeables (0,6 sur 23 049 en Côte d'Ivoire 2025) |
| C7 | Hétérogénéité | **Entre pays** (observée) ; σ_b en complément | σ_b seul, inventé ; banque par banque | Aucune donnée par banque trouvée ; l'écart entre pays est mesurable |
| C8 | Millésime | Rapport **le plus récent** publiant l'année | Première publication | Les données sont révisées (ex. D UEMOA 2023 : 45 054,1 puis 44 986,3) |
| C9 | Réserves obligatoires | **3 % de D** (approximation) | Les ignorer ; assiette réelle | Assiette absente des rapports ; les ignorer surestimerait b |
| C10 | Norme de liquidité | **Coefficient de liquidité à 75 %**, pas de LCR | Parler de LCR | RLCT et RLLT « pas encore applicables » selon les rapports 2023-2025 |

### 7.2 Détail des choix principaux

**C1. Pourquoi l'UEMOA et non la Côte d'Ivoire seule.**
- *Cohérence institutionnelle* : la BCEAO émettrait la MNBC (projet e-CFA) et fixe refinancement, réserves et norme prudentielle pour l'union. Une MNBC « ivoirienne » n'existe pas comme objet de politique.
- *Hétérogénéité observée* : le coefficient de liquidité 2025 va de 79,5 % (Burkina Faso) à 241,3 % (Sénégal). Chaque pays devient un groupe k avec son bₖ et son poids wₖ = Dₖ / D.
- *Équations* : celles du document principal, avec l'indice de banque i remplacé par l'indice de pays k :

$$\frac{\Delta L}{L} = \frac{\varphi}{\rho}\sum_{k=1}^{8} w_k\,\max\{0,\ (1-\lambda)\zeta - b_k\},\qquad \zeta^*_k=\frac{b_k}{1-\lambda},\qquad \zeta^*_{\min}=\min_k \zeta^*_k$$

- *Zoom Côte d'Ivoire* : 41 % des dépôts UEMOA en 2025 ; bilan détaillé disponible (§3 et §5.1) ; sert de cas d'étude de la composition de D.
- **Limites assumées** : (i) la dispersion entre pays **sous-estime** la dispersion entre banques ; (ii) les groupes bancaires panafricains et le marché interbancaire régional peuvent faire circuler la liquidité entre pays, donc la partition par pays surestime la fragilité si la circulation est parfaite ; (iii) un même ζ pour les 8 pays est une simplification (bancarisation et mobile money diffèrent). **Lecture** : l'agrégat UEMOA donne le cas où la liquidité circule parfaitement (contraction minimale, d'après l'inégalité de Jensen), la partition par pays le cas où elle ne circule pas du tout. La réalité se situe entre les deux.

**C2. Refinancement dans λ.** Le refinancement déjà accordé est une dette existante, pas une capacité. Ce que la BCEAO accepterait de prêter après un choc dépend d'une décision de politique et du design de la MNBC, pas d'un stock observable : c'est exactement ce que λ représente. L'inclure aussi dans B compterait deux fois la même ressource et surestimerait ζ\*.

**C3. D = « dépôts et emprunts ».** Choix de commodité contrôlée : c'est l'agrégat que la Commission Bancaire publie pour chaque pays et chaque année, donc l'extraction est homogène. Contrôle effectué pour la Côte d'Ivoire : l'agrégat coïncide avec les dettes envers la clientèle (§3.1). **Reste à faire** : le même contrôle pour les sept autres pays.

**C5. Pourquoi une fourchette.** b stricte nette : 7,5 % (2023), 12,8 % (2024), 15,5 % (2025). Calibrer sur 2025 revient à prendre un pic de liquidité (coefficient de liquidité de 103 % à 127 % en un an, chiffres provisoires). Calibrer sur 2023 prend un creux. Une MNBC arriverait à une date et dans un état de liquidité inconnus. Les années 2021 et 2022 s'ajoutent pour savoir si 7,5 % est un niveau habituel.

**C6. HI6 réécrite.** L'hypothèse initiale était réfutée par les données (§3.1). Le point réel : D contient des dépôts à terme (16,2 %), de l'épargne (13,9 %) et des garanties (4,3 %), moins convertibles que les dépôts à vue (64,7 %). Cela éclaire la plage de ζ sans changer les équations.

**C9. 3 % de D.** Le coefficient de réserves obligatoires est de 3 % (source secondaire, à vérifier dans le texte BCEAO). Appliqué à D plutôt qu'à l'assiette réelle, que les rapports ne publient pas. Erreur probable : faible, car l'assiette et D sont de même ordre.

### 7.3 Pourquoi la b stricte comme base (C4)

| Option | Raison de l'écarter ou de la retenir |
|---|---|
| **b stricte nette** (caisse + comptes ordinaires débiteurs − 3 % de D) | **Retenue.** Seule la monnaie de banque centrale est un tampon net pour le système |
| b large (ajoute titres de transaction et de placement) | **Borne haute.** Une vente de titres à une autre banque ne crée pas de liquidité pour le système ; une vente simultanée ferait baisser les prix ; la mise en pension BCEAO relève de λ |
| Coefficient de liquidité | **Écarté.** Son numérateur compte les crédits arrivant à échéance sous trois mois : ne pas les renouveler *est* la contraction mesurée |
| Excédent de réserves BCEAO seul (≈ 6,5 %) | **Recoupement seulement.** Source secondaire, UEMOA seulement, date différente |

**Pourquoi ce n'est pas un choix de commodité.** La b stricte donne un résultat plus « intéressant » que la b large (ζ\* de 7 à 15 % contre 35 à 42 %), mais ce n'est pas la raison du choix. La raison est l'argument d'agrégation. Les deux versions sont publiées pour que le lecteur voie l'effet du choix.

**Erreurs en sens inverse, assumées.** La b stricte est une borne **haute** de la monnaie centrale (les comptes ordinaires débiteurs incluent des avoirs interbancaires et à l'étranger). Elle **ignore** les titres achetés par des non-banques, dont les détentions ne sont pas disponibles.

---

## 8. Corrections à reporter dans « Simulation de choc de retrait »

| Point | Correction |
|---|---|
| ρ | Remplacer « UMOA 2023 ≈ 0,78 » par la série du §2 et §3 ; indiquer que ρ varie de 0,65 à 0,78 |
| HI6 | Réécrire : D = dettes envers la clientèle (emprunts négligeables). Le risque est la composition de D (garanties, terme, épargne), pas les emprunts |
| B | Ajouter l'argument d'agrégation : B de base = monnaie centrale ; titres en sensibilité haute |
| LCR | Préciser : RLCT et RLLT non applicables ; norme actuelle = coefficient de liquidité à 75 % |
| b | Ne plus présenter b comme un nombre : b ∈ [6,5 % ; 15,5 %] selon l'année et la définition |
| Cadre | Titre et périmètre : UEMOA comme cas principal, Côte d'Ivoire en zoom ; indice i des banques remplacé par k des 8 pays (voir §7.2) |
| HM2 | Remplacer l'hétérogénéité « inventée » (σ_b) par l'hétérogénéité observée entre pays ; σ_b reste en sensibilité complémentaire |
| HM6 | Remplacer « UEMOA puis Côte d'Ivoire » par « UEMOA principal, Côte d'Ivoire en zoom » |

---

## 9. Résultats de l'extraction (8 pays, 2021-2025)

**Fichier** : « Données Extrait.xlsx » (onglets Données_pays, Calculs, Synthèse_UEMOA, Coef_liquidité, Contrôles, Brut_millésimes). **Contrôle** : la somme des 8 pays reproduit D, L et le total du bilan publiés pour l'UEMOA, avec des écarts de 0,05 milliard au plus (arrondis). Paramètres utilisés : réserves obligatoires approximées à 3 % de D, λ = 0.

### 9.1 UEMOA, agrégat [C]

| Année | D (Md) | L (Md) | ρ | b stricte nette | ζ\*min (pays le plus fragile) | Pays |
|---|---|---|---|---|---|---|
| 2021 | 38 906 | 27 454 | 0,706 | 13,2 % | 8,8 % | Togo |
| 2022 | 43 754 | 32 715 | 0,748 | 11,1 % | 4,3 % | Bénin |
| 2023 | 44 986 | 34 930 | 0,777 | 7,7 % | 3,9 % | Bénin |
| 2024 | 48 429 | 36 700 | 0,758 | 10,1 % | 4,5 % | Bénin |
| 2025 (prov.) | 56 200 | 38 732 | 0,689 | 13,3 % | 7,1 % | Bénin (Togo à égalité) |

### 9.2 b stricte nette par pays [C]

| Pays | 2021 | 2022 | 2023 | 2024 | 2025 (prov.) | Poids dans D 2025 |
|---|---|---|---|---|---|---|
| Bénin | 10,1 % | 4,3 % | 3,9 % | 4,5 % | 7,1 % | 8,3 % |
| Burkina Faso | 11,3 % | 7,7 % | 7,3 % | 9,3 % | 10,5 % | 11,8 % |
| Côte d'Ivoire | 15,4 % | 13,8 % | 7,5 % | 12,8 % | 15,5 % | 41,0 % |
| Guinée-Bissau | 26,8 % | 16,6 % | 13,5 % | 18,7 % | 20,6 % | 0,5 % |
| Mali | 12,4 % | 11,2 % | 7,0 % | 8,6 % | 16,1 % | 10,2 % |
| Niger | 12,2 % | 13,1 % | 8,3 % | 8,6 % | 10,6 % | 2,6 % |
| Sénégal | 13,6 % | 12,5 % | 10,4 % | 10,0 % | 13,7 % | 19,0 % |
| Togo | 8,8 % | 7,0 % | 7,2 % | 6,8 % | 7,1 % | 6,5 % |

### 9.3 Lectures

1. **Fourchette UEMOA.** Avec λ = 0, le seuil agrégé ζ\*agg = b va de **7,7 % (2023) à 13,3 % (2025)**, en passant par 11 % à 13 % en 2021-2022. L'année 2023 est le creux, 2025 (provisoire) le haut.
2. **L'hétérogénéité entre pays pèse.** Le pays le plus fragile a un seuil de 3,9 % à 8,8 %, soit 40 % à 70 % du seuil agrégé selon l'année. Illustration (non un résultat du modèle) : en 2023, à ζ = 8 %, le modèle agrégé prédit une contraction presque nulle, alors que 76 % des dépôts sont dans des pays qui ont franchi leur seuil, et la contraction cumulée par pays est environ 2,7 fois plus forte.
3. **Une conjecture est réfutée.** Je pensais que le Burkina Faso et le Niger, proches du seuil de 75 % du coefficient de liquidité en 2025, seraient les plus fragiles. Selon la b stricte, ce n'est pas le cas (10,5 % et 10,6 %, dans la moyenne). Les plus bas sont le **Bénin et le Togo** (≈ 7 % en 2025). Les deux mesures ne disent pas la même chose : le coefficient de liquidité inclut les crédits à échéance courte (§4.3), pas la b.
4. **HI6 vérifiée pour les 8 pays.** Emprunts à la clientèle : au plus 0,9 % de D (Sénégal, 2024). Dépôts à vue : 40 % à 66 % de D. Dépôts de garantie : 1,4 % à 8,6 %. La réécriture de HI6 (§7, C6) tient pour toute l'union.
5. **ρ par pays** : de 0,58 à 0,88 selon le pays et l'année, contre 0,69 à 0,78 pour l'UEMOA.
6. **Aucun b négatif** : le plancher à zéro n'est jamais activé.

### 9.4 Précautions

- Une première extraction avait mélangé deux tableaux côte à côte sur une page du rapport 2025 (Niger) et donnait une b du Niger de 48 % : détecté, corrigé, tous les postes ré-extraits.
- Les valeurs révisées entre rapports sont conservées (onglet Brut_millésimes). Exemple : titres de placement de la Côte d'Ivoire en 2023, 4 776,6 Md (rapport 2023) contre 4 251,5 Md (rapport 2025). La règle retenue est celle du rapport le plus récent.
- Le chiffre de 2025 est provisoire pour tous les pays.
- Les comptes ordinaires débiteurs mélangent avoirs à la BCEAO, interbancaires et étrangers (§5.4) : b stricte = borne haute.

---

## 10. Lacunes et prochaines étapes

**Non trouvé ou non extrait**

- Ratios de liquidité **par banque** (σ\_b reste un scénario).
- Séparation des comptes ordinaires débiteurs entre BCEAO, banques et étranger.
- Assiette et réserves obligatoires effectives de la Côte d'Ivoire.
- Ventilation de D par type de déposant.
- Rapport 2022 (scan) : à OCRiser seulement si les chiffres 2022 de 2023 et 2024 s'avèrent insuffisants.

**Décisions validées** (détail et justifications au §7) : b stricte en base et b large en borne haute ; fourchette 2021-2025 ; HI6 réécrite ; UEMOA comme cas principal avec les 8 pays comme groupes et la Côte d'Ivoire en zoom.

**Étape suivante** : (1) mettre à jour « Simulation de choc de retrait » (cadre UEMOA, HM2, HM6, HI6, ρ et b, §8) ; (2) construire la grille de scénarios (ζ, λ, φ) et écrire le code ; (3) vérifier le coefficient de réserves obligatoires et le recoupement BCEAO à la source.
