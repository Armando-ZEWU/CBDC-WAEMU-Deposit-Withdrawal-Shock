# Simulation de choc de retrait

**Migration de dépôts vers une MNBC hypothétique : à quelles conditions le crédit bancaire en souffre-t-il ? (cadre UEMOA, huit pays comme groupes, zoom sur la Côte d'Ivoire)**

> **Statut du document** : bloc théorique (question, notations, hypothèses, équations) avec les choix de calibration validés. **Version 3** : cadre UEMOA (8 pays comme groupes de banques, Côte d'Ivoire en zoom) ; refinancement BCEAO porté par λ (hors de B) ; D = « dépôts et emprunts » (définition de la Commission Bancaire) ; b stricte en base et b large en borne haute ; calibration sur une fourchette 2021-2025. Les données et leurs justifications sont dans « Données.md » et « Données Extrait.xlsx ». Le code reste à écrire.
> **Nature du travail** : exercice **conditionnel et contrefactuel**. La BCEAO n'a pas de MNBC en circulation (hors projet e-CFA). Ce travail n'estime donc pas l'effet d'une monnaie existante : il identifie les paramètres dont dépend l'existence d'un effet.

---

## 0. L'idée en 30 secondes

Une MNBC (Monnaie Numérique de Banque Centrale) est de la monnaie de banque centrale sous forme numérique, détenue directement par le public. Si des ménages y transfèrent une partie de leurs dépôts, **les banques perdent une ressource** avec laquelle elles financent leurs prêts.

La question n'est pas « les dépôts baissent-ils ? » (c'est évident), mais : **les banques peuvent-elles absorber cette perte sans réduire le crédit ?** Elles ont deux types d'amortisseurs : leur propre matelas de liquidité (réserves, titres facilement vendables) et le retour d'une partie des fonds, appelé ici recyclage (la banque centrale peut leur prêter en retour, ou les utilisateurs peuvent redéposer). Tant que ces amortisseurs suffisent, le crédit ne bouge pas. Au-delà d'un **seuil critique**, les banques doivent prêter moins.

Comme la MNBC serait émise par la BCEAO pour **toute l'union**, le travail se place au niveau de l'UEMOA. Les huit pays jouent le rôle de groupes de banques aux matelas différents : un pays peut franchir son seuil bien avant les autres.

Le travail cherche ce seuil, et ce dont il dépend.

**Exemple chiffré (purement illustratif, non calibré).** Pour 100 FCFA de dépôts, une banque prête 80 FCFA. Si 10 % des dépôts partent vers la MNBC et que rien ne revient, elle perd 10 FCFA de ressources. Elle dispose d'un matelas de liquidité de 6 FCFA : elle l'utilise, puis doit réduire ses prêts de 4 FCFA, soit de 80 à 76, une baisse de **5 %**. Avec un matelas de 10 FCFA ou plus, **aucune baisse**.

---

## 1. Question de recherche

> **Sous quelles conditions une migration de dépôts vers une MNBC hypothétique se transforme-t-elle en contraction du crédit bancaire dans l'UEMOA ?**

**Questions dérivées**

- **Q1 (existence).** Le seuil critique ζ\* est-il atteignable dans la plage de conversion plausible, ou les banques absorbent-elles le choc sans toucher au crédit ?
- **Q2 (leviers).** De quoi ζ\* dépend-il le plus : des tampons de liquidité des banques (b) ou du recyclage des fonds vers le système bancaire (λ), c'est-à-dire du design de la MNBC ?
- **Q3 (hétérogénéité).** Le seuil de l'union dans son ensemble masque-t-il des pays dont les banques franchissent leur seuil beaucoup plus tôt ?

**Zoom Côte d'Ivoire** : cas d'étude au sein de l'union (41 % des dépôts de l'UEMOA en 2025), avec un bilan détaillé et l'analyse de la composition des dépôts.

**Ce que ce travail ne prétend pas faire** : prédire l'adoption d'une MNBC, ni estimer l'impact d'une MNBC existante, ni modéliser une panique bancaire (ruée), qui est un phénomène de coordination distinct, traité en extension.

---

## 2. Notations

Légende des statuts : **Donnée** (mesurable sur des statistiques réelles), **Scénario** (valeur choisie car non observable), **Design** (dépend de la conception de la MNBC), **Robustesse** (paramètre testé en fin d'analyse), **Dérivé** (calculé à partir des autres).

| Symbole | Définition | En clair (lecture économique) | Source / statut |
|---|---|---|---|
| **k** | Indice d'un pays de l'UEMOA (8 groupes : Bénin, Burkina Faso, Côte d'Ivoire, Guinée-Bissau, Mali, Niger, Sénégal, Togo) | Chaque pays regroupe ses banques, avec son propre matelas de liquidité et sa propre taille. | Notation |
| **D** (Dₖ pour un pays) | Dépôts et emprunts (en FCFA), au sens des statistiques de la Commission Bancaire | L'argent que les clients confient aux banques : c'est la ressource principale avec laquelle elles financent leurs prêts. En pratique, cet agrégat coïncide avec les dettes envers la clientèle (voir HI6). | Commission Bancaire de l'UMOA, rapports annuels (UEMOA 2025 : 56 200 milliards, provisoire). **Donnée** |
| **L** (Lₖ) | Crédit à l'économie (en FCFA) | Les prêts accordés aux ménages et aux entreprises. C'est la variable dont on étudie la baisse. | Commission Bancaire (UEMOA 2025 : 38 732 milliards, provisoire). **Donnée** |
| **ρ = L/D** (ρₖ) | Ratio crédit / dépôts | La part des dépôts transformée en prêts. Plus il est élevé, plus la banque est « prêtée ». | UEMOA : 0,69 à 0,78 (2021-2025) ; par pays : 0,58 à 0,88 ; Côte d'Ivoire : 0,65 à 0,75. La valeur de 0,85 de la première version n'était pas sourcée. **Donnée** |
| **ζ** (zêta) ∈ [0, 1] | Part des dépôts convertie en MNBC | Sur 100 FCFA de dépôts, combien partent vers la monnaie numérique de banque centrale. C'est le **choc**. Attention : c'est une part de **valeur** déplacée, pas un taux d'adoption (nombre d'utilisateurs). | Non observable. **Scénario** (balayé sur une grille) |
| **λ** ∈ [0, 1] | Taux de recyclage : part des fonds convertis qui revient vers le système bancaire | Quand un dépôt part vers la MNBC, la banque n'est pas forcément perdante. Trois canaux : le **refinancement par la BCEAO** (elle prête en retour aux banques), le redépôt par les utilisateurs, le financement de gros. λ = 0 : rien ne revient, y compris aucune aide de la BCEAO. λ = 1 : tout revient. | Dépend de la conception de la MNBC et de la politique de la BCEAO. **Design** (scénarios) |
| **B** (Bₖ) | Tampon de liquidité mobilisable (en FCFA) | Le « matelas » que les banques détiennent déjà et peuvent utiliser **sans réduire leurs prêts et sans l'aide de la banque centrale**. Pour le système, seule la **monnaie de banque centrale** compte : caisse et avoirs à la BCEAO, au-delà des réserves obligatoires. Mesuré par approximation : caisse + comptes ordinaires débiteurs de trésorerie (borne haute) − réserves obligatoires (3 % de D). Le **refinancement BCEAO n'en fait pas partie** : il est porté par λ. | Commission Bancaire, bilans par pays (voir §6). **Donnée** (approximée) |
| **b = B/D** (bₖ) | Tampon relatif | Le matelas rapporté aux dépôts : sur 100 FCFA de dépôts, combien de FCFA sont disponibles pour absorber un choc. | UEMOA (agrégé) : **7,7 % à 13,3 %** selon l'année 2021-2025 (b stricte nette). **Donnée** (dérivé) |
| **b large** | Variante de b qui ajoute les titres de transaction et de placement | Borne haute de sensibilité : une vente de titres à une autre banque ne crée pas de liquidité pour le système, donc cette version surestime le matelas réel. | UEMOA : 41 % à 47 %. **Donnée** (dérivé) |
| **wₖ = Dₖ / D** | Poids du pays k | Part du pays k dans l'ensemble des dépôts de l'union (Côte d'Ivoire : 41 % en 2025). | **Donnée** |
| **b̄ = Σ wₖ bₖ** | Tampon moyen pondéré | Le matelas « moyen » de l'union, pondéré par la taille des pays. | **Dérivé** |
| **σ_b** | Dispersion des tampons entre banques d'un même pays | Mesure l'inégalité **à l'intérieur** de chaque pays, que les données par pays ne montrent pas. Aucune donnée par banque disponible. | **Scénario** (sensibilité complémentaire) |
| **N, c** | Nombre d'utilisateurs éligibles ; plafond individuel de détention (FCFA) | Une MNBC peut limiter le montant détenu par personne. N × c est le maximum théorique qui peut quitter les banques. | Choix de design. **Design / Scénario** |
| **ζ_cap = min{1, N·c / D}** | Plafond de la conversion | Borne supérieure de ζ imposée par le design : même si tout le monde voulait convertir, le plafond limite ce qui peut partir. | **Dérivé** |
| **φ** ∈ [0, 1] | Taux de répercussion sur le crédit (pass-through) | Parmi le manque de ressources qui reste après usage du matelas, quelle part est comblée en prêtant moins (le reste pouvant l'être par d'autres moyens : hausse des taux de dépôt, émission de dette...). Cas de base : φ = 1. | **Robustesse** ({0,25 ; 0,5 ; 1}) |
| **ΔL / L** | Contraction du crédit (en %) | Ce que l'on cherche à mesurer : de combien le crédit baisse. | **Dérivé** (résultat) |
| **ζ\*ₖ** | Seuil critique du pays k | La conversion à partir de laquelle les banques du pays k doivent commencer à réduire leurs prêts. | **Dérivé** |
| **ζ\*_min** | Seuil du pays le plus fragile | Premier point où **un** pays est touché. | **Dérivé** |
| **ζ\*_agg** | Seuil agrégé | Le seuil si l'union était un seul grand bilan : cas où la liquidité circulerait parfaitement entre pays. | **Dérivé** |
| **S(ζ)** | Part du système touchée | La proportion des dépôts de l'union située dans des pays qui ont franchi leur seuil. | **Dérivé** |

---

## 3. Hypothèses

Les hypothèses sont classées par nature. Pour chacune : ce qu'elle dit, comment la comprendre sans formalisme, et ce qui se passe si elle est fausse.

### 3.1 Hypothèses théoriques

| ID | Énoncé | En clair | Si elle est fausse |
|---|---|---|---|
| **HT1** | Ordre d'ajustement : les banques utilisent d'abord leur tampon, et ne réduisent le crédit qu'en dernier recours. | Face à une perte de dépôts, une banque préfère puiser dans ses réserves plutôt que refuser des prêts à ses clients. | Si les banques coupent le crédit avant d'avoir épuisé leur matelas, la contraction commence plus tôt : ζ\* est **surestimé**. |
| **HT2** | La contrainte déterminante est la **liquidité**, pas le capital. | Le problème d'une banque qui perd des dépôts est de trouver de l'argent liquide, pas d'avoir assez de fonds propres. | Si les contraintes de capital pèsent aussi, la contraction peut être plus forte que celle calculée. |
| **HT3** | Le taux de recyclage λ est **identique pour tous les pays** (et toutes les banques). | Toutes les banques de l'union ont le même accès au refinancement de la banque centrale et reçoivent la même part des fonds recyclés. | En réalité, les petites banques accèdent moins facilement au refinancement. Dans ce cas λ devient λₖ et les seuils diffèrent davantage. *(Simplification ajoutée pour garder le modèle lisible.)* |

### 3.2 Hypothèses empiriques

| ID | Énoncé | En clair | Si elle est fausse |
|---|---|---|---|
| **HE1** | ζ est inconnu et sera **balayé par scénarios**, ancrés sur l'expérience des MNBC existantes et du mobile money dans la région. | Comme aucune MNBC n'existe dans l'UEMOA, on ne devine pas une valeur : on teste une plage de valeurs et on regarde à partir de quand le crédit réagit. Repère régional : l'encours de monnaie électronique représente 2,5 % à 3,4 % de D (2023-2025). | Si la plage choisie est trop étroite ou mal ancrée, la conclusion « seuil atteignable ou non » est biaisée. |
| **HE2** | b est **mesurable par pays** sur les bilans publiés par la Commission Bancaire ; λ est fixé par scénario de design. | Le matelas des banques est une réalité observable. Le recyclage, lui, dépend de choix de conception qui n'ont pas encore été faits. | Si b est mal mesuré (par exemple en comptant des liquidités déjà exigées par la réglementation), le seuil est **surestimé**. |

### 3.3 Hypothèses méthodologiques

| ID | Énoncé | En clair | Si elle est fausse |
|---|---|---|---|
| **HM1** | Modèle **statique** à une période. | Une photo avant/après, pas un film : on ignore le temps de réaction, la progressivité de l'adoption et les ajustements successifs. | Les effets dynamiques (adoption lente, boucles de rétroaction) ne sont pas capturés. |
| **HM2** | Hétérogénéité **observée entre pays** : chaque pays est un groupe k avec son tampon bₖ et son poids wₖ. La dispersion entre banques d'un même pays (σ_b) est ajoutée en sensibilité complémentaire. | On ne dispose pas de données par banque, mais on mesure le matelas de chaque pays : on s'en sert pour voir si la moyenne de l'union cache des pays fragiles. | La dispersion entre pays **sous-estime** la dispersion entre banques : le seuil réel des banques les plus fragiles est plus bas. |
| **HM3** | Le plafond ζ_cap borne la **grille de ζ**, il n'est pas un mécanisme de comportement. | On compare simplement le seuil ζ\* au maximum que le design autorise : si le plafond empêche d'atteindre le seuil, le problème ne peut pas survenir. | Aucun comportement d'évitement du plafond n'est modélisé. |
| **HM4** | La robustesse à φ est testée séparément. | Le seuil ne dépend pas de φ ; on vérifie seulement que la **pente** au-dessus du seuil change, pas la conclusion. | Si φ interagissait avec le seuil, il faudrait le modéliser de façon structurelle. |
| **HM5** | Partition B / λ : le refinancement BCEAO est porté par λ, pas par B. | Le « matelas » est ce que la banque détient déjà ; l'aide de la banque centrale est un choix de politique et de design. On évite ainsi de compter deux fois la même ressource. | Si le refinancement était aussi dans B, ζ\* serait **surestimé**. Si un scénario de λ suppose un refinancement contre collatéral, ce collatéral ne doit pas aussi être vendu dans B. |
| **HM6** | Cadre : **UEMOA comme cas principal**, huit pays comme groupes, Côte d'Ivoire en zoom. | La MNBC serait émise pour toute l'union ; liquidité, réserves et norme prudentielle se décident au niveau de la BCEAO. La Côte d'Ivoire est un cas d'étude, pas le cadre. | Si la liquidité circule parfaitement entre pays, l'agrégat UEMOA est plus pertinent que la partition par pays. S'il n'y a aucune circulation, la partition l'est. La réalité se situe entre les deux : on présente les deux. |
| **HM7** | **Calibration en fourchette** sur 2021-2025, pas sur une seule année. | b varie beaucoup avec le cycle de liquidité (agrégat UEMOA : 7,7 % en 2023, 13,3 % en 2025). Une MNBC arriverait à une date et dans un état de liquidité inconnus. | Calibrer sur une seule année fixerait un résultat arbitraire, à un facteur proche de deux près. |
| **HM8** | **b stricte** (monnaie de banque centrale) en base ; **b large** (avec titres) en borne haute. | Pour l'ensemble du système bancaire, vendre un titre d'État à une autre banque déplace la liquidité sans en créer. Seule la monnaie centrale est un tampon net. | Si des non-banques (assurances, caisses de retraite, investisseurs étrangers) achètent beaucoup de titres, la b stricte **sous-estime** le matelas réel. Je n'ai pas de données sur leurs détentions. |

### 3.4 Hypothèses implicites (assumées ouvertement)

| ID | Énoncé | En clair | Si elle est fausse |
|---|---|---|---|
| **HI1** | Dans le cas de base (φ = 1), l'ajustement se fait **entièrement par la quantité** : le manque de ressources est comblé en prêtant moins. | La banque ne relève pas les taux sur les dépôts, n'émet pas d'obligations, n'absorbe pas la perte sur ses profits. C'est une **borne haute** de l'effet. | Si d'autres canaux existent, la contraction réelle est plus faible. |
| **HI2** | Aucune réponse de politique monétaire au-delà de celle portée par λ (refinancement et recyclage). | La BCEAO ne change ni ses taux, ni ses règles de réserves en réaction au choc. | Une réponse active relèverait λ ou b, donc le seuil. |
| **HI3** | ζ mesure une **valeur** de dépôts déplacée, pas un taux d'adoption. | Ce qui compte pour la banque est le montant qui part, pas le nombre de personnes qui s'inscrivent. | Confondre les deux, comme dans la première version, fausse l'ampleur du choc. |
| **HI4** | Le plafond N·c / D suppose que **tous** les utilisateurs atteignent leur plafond, et ne couvre que les détenteurs éligibles. | C'est un maximum théorique, pas une prévision. Les dépôts des entreprises ne sont pas couverts par un plafond individuel. | Si les entreprises pèsent lourd dans les dépôts, ζ_cap sous-estime l'exposition. |
| **HI5** | Pas de **rétroaction** de la baisse du crédit sur les dépôts. | Un prêt non accordé crée en retour moins de dépôts dans l'économie. On ignore cet effet de second tour. | La contraction réelle serait **plus forte** que celle calculée. |
| **HI6** | D, mesuré en « dépôts et emprunts », coïncide avec les **dettes envers la clientèle** ; ζ est une part de D. Le vrai enjeu est la **composition** de D. | Les emprunts de la clientèle sont négligeables (au plus 0,9 % de D dans les huit pays). En revanche, les dépôts à vue ne représentent que 40 % à 66 % de D, le reste étant du terme, de l'épargne et des dépôts de garantie, moins facilement convertibles. | Si seuls les dépôts à vue migrent, une valeur de ζ = 10 % de D correspond à 15 % à 25 % des dépôts à vue : le choc serait plus concentré que ne le suggère ζ. |
| **HI7** | **ζ et λ sont communs aux huit pays.** | La conversion et le recyclage sont les mêmes partout, alors que bancarisation et usage du mobile money diffèrent d'un pays à l'autre. | Si ζ diffère selon les pays, les pays les plus numérisés franchissent leur seuil plus tôt. |

---

## 4. Équations

### 4.1 Perte nette de financement

Quand la part ζ des dépôts du pays k est convertie, une fraction λ revient (refinancement BCEAO, redépôt des utilisateurs ou financement de gros). La perte nette de ressources est :

$$\Delta F_k = (1-\lambda)\,\zeta\, D_k$$

*Lecture : de chaque FCFA qui part, λ revient ; ce qui manque réellement est (1 − λ) fois ce qui est parti.*

### 4.2 Déficit résiduel après usage du tampon

Les banques du pays absorbent d'abord la perte avec leur matelas B_k. Ce qui reste est le **déficit résiduel** :

$$G_k = \max\{0,\ (1-\lambda)\,\zeta\, D_k - B_k\} = D_k\,\max\{0,\ (1-\lambda)\zeta - b_k\}$$

*Lecture : si le matelas couvre la perte, il n'y a pas de déficit (G = 0). Sinon, le déficit est la partie de la perte que le matelas ne couvre pas.*

### 4.3 Contraction du crédit : un pays

Par HI1, le déficit résiduel est comblé en réduisant le crédit, avec un taux de répercussion φ :

$$\boxed{\ \frac{\Delta L_k}{L_k} = \min\left\{1,\ \frac{\varphi\,\max\{0,\ (1-\lambda)\zeta - b_k\}}{\rho_k}\right\}\ }$$

*Lecture : la baisse du crédit est le déficit rapporté au crédit initial du pays. Elle ne peut pas dépasser 100 %.*

### 4.4 Contraction du crédit : UEMOA

$$\boxed{\ \frac{\Delta L}{L} = \frac{\varphi}{\rho}\ \sum_{k=1}^{8} w_k\,\max\{0,\ (1-\lambda)\zeta - b_k\}\ }$$

où ρ = L/D est le ratio crédit/dépôts agrégé de l'union (formule valable tant qu'aucun pays n'épuise la totalité de son crédit).

*Lecture : la baisse du crédit de l'union est la moyenne pondérée des déficits de chaque pays. Le zoom Côte d'Ivoire utilise les mêmes équations avec k = Côte d'Ivoire.*

### 4.5 Seuils critiques

Seuil du pays k : ζ\*ₖ = bₖ / (1 − λ), car c'est la valeur de ζ pour laquelle (1 − λ)ζ = bₖ.

$$\boxed{\ \zeta^*_k = \frac{b_k}{1-\lambda}\ }\qquad
\boxed{\ \zeta^*_{\min} = \min_k \frac{b_k}{1-\lambda}\ }\qquad
\boxed{\ \zeta^*_{agg} = \frac{\bar b}{1-\lambda}\ }$$

*Lecture : plus le matelas b est grand et plus le recyclage λ est élevé, plus le seuil est haut. Quand λ se rapproche de 1, le seuil devient très grand : le recyclage neutralise le choc.*

**Part du système touchée à un niveau de conversion ζ :**

$$S(\zeta) = \sum_k w_k\,\mathbf{1}\{\zeta > \zeta^*_k\}$$

*Lecture : la proportion des dépôts de l'union située dans des pays dont le seuil est dépassé.*

### 4.6 Pourquoi l'hétérogénéité compte (inégalité de Jensen)

Comme la fonction max{0, ·} est convexe, et que Σ wₖ [(1−λ)ζ − bₖ] = (1−λ)ζ − b̄ :

$$\sum_k w_k\,\max\{0,\ x_k\}\ \ge\ \max\Big\{0,\ \sum_k w_k x_k\Big\}\qquad\text{avec}\quad x_k=(1-\lambda)\zeta-b_k$$

*Lecture : le modèle agrégé (l'UEMOA comme un seul bilan) **sous-estime** la contraction du crédit dès que les matelas sont inégaux. L'agrégat correspond au cas où la liquidité circule parfaitement entre les pays (contraction minimale), la partition par pays au cas où elle ne circule pas du tout. On a toujours ζ\*_min ≤ ζ\*_agg.*

### 4.7 Règle de décision avec le plafond de détention

La conversion possible est bornée : ζ ∈ [0, ζ_cap], avec

$$\zeta_{cap} = \min\left\{1,\ \frac{N\,c}{D}\right\}$$

| Situation | Interprétation |
|---|---|
| ζ_cap ≤ ζ\*_min | Aucun pays n'est touché : le canal bancaire est **non binding par le design**, quel que soit le comportement des ménages. |
| ζ\*_min < ζ_cap ≤ ζ\*_agg | Certains pays sont touchés alors que l'union moyenne paraît protégée : **la zone que l'agrégé cache**. |
| ζ_cap > ζ\*_agg | L'union est touchée en moyenne : le design laisse la porte ouverte, il faut agir sur λ ou sur b. |

### 4.8 Robustesse au taux de répercussion φ

Le seuil ζ\* ne dépend pas de φ : φ ne change que la **pente** de la contraction au-dessus du seuil. On vérifie la robustesse sur φ ∈ {0,25 ; 0,5 ; 1}.

### 4.9 Conventions et cas limites

- **λ = 1** : tout revient aux banques, le déficit est nul (G = 0) quel que soit ζ. C'est la **neutralité** (Brunnermeier & Niepelt, à vérifier et citer correctement lors de la revue de littérature).
- **λ = 0 et b = 0** : ζ\* = 0, toute conversion réduit le crédit.
- **b net négatif** : plancher à zéro dans le calcul de ζ\*. Ne s'est produit dans aucun pays ni aucune année de l'extraction.
- **Dimensions** : ζ, λ, b, φ, ρ sont des nombres purs (sans unité) ; D, L, B sont en FCFA.

---

## 5. Ce que ce bloc apporte, et ce qu'il n'apporte pas

**Ce qui est mécanique.** Les signes : ζ\* augmente avec b et avec λ. Ce n'est pas un résultat, c'est une conséquence des équations.

**Où se trouve le contenu scientifique :**

1. **L'ordre de grandeur de b**, mesuré sur les bilans de l'UEMOA : 7,7 % à 13,3 % pour l'union (b stricte nette), selon l'année. La conclusion en dépend entièrement.
2. **La comparaison ζ\* contre ζ_cap** (et contre la plage plausible de ζ) : elle répond à Q1.
3. **La dispersion entre pays** : le seuil du pays le plus fragile vaut 40 % à 70 % du seuil agrégé selon l'année (3,9 % à 8,8 %). Elle répond à Q3 et peut renverser une conclusion de type « non binding ».
4. **La sensibilité à λ** : elle dit quel levier de design compte le plus (Q2).

**Résultat possible à accepter d'avance.** Si b s'avère élevé, la conclusion sera que le canal bancaire n'est pas binding à adoption modérée. C'est un résultat valide, même s'il contredit l'intuition de départ. À ce stade, les données indiquent un b modéré, pas négligeable : la question reste ouverte.

**Limites assumées** : modèle statique, pas de panique (ruée), pas de rétroaction du crédit sur les dépôts, ajustement par la quantité seulement, λ et ζ communs à tous les pays, dispersion intra-pays non observée, comptes ordinaires débiteurs incluant des avoirs étrangers et interbancaires (b stricte = borne haute), données 2025 provisoires.

---

## 6. Calibration : décisions et plan

### 6.1 Décisions prises

1. **Refinancement BCEAO dans λ**, pas dans B (HM5).
2. **UEMOA cas principal**, 8 pays comme groupes, Côte d'Ivoire en zoom (HM6).
3. **D = « dépôts et emprunts »**, coïncidant avec les dettes envers la clientèle (HI6).
4. **b stricte en base, b large en borne haute** (HM8).
5. **Fourchette 2021-2025** plutôt qu'une année (HM7).

### 6.2 Composition de B

| Composante | Dans B ? | Remarque |
|---|---|---|
| Caisse | Oui | |
| Comptes ordinaires débiteurs de trésorerie | Oui, **borne haute** | Mélangent avoirs à la BCEAO, interbancaires et étrangers : non séparables dans les rapports |
| Réserves obligatoires | Non | Approximées par 3 % de D (assiette non publiée ; coefficient à vérifier à la source) |
| Titres de transaction et de placement | **Seulement dans b large** | Vendre un titre à une autre banque ne crée pas de liquidité pour le système |
| Titres d'investissement | Non | Détenus jusqu'à l'échéance |
| Refinancement BCEAO | **Non (dans λ)** | Les refinancements déjà consentis sont une dette existante, pas une capacité |
| Coefficient de liquidité de l'UMOA | **Non utilisé comme mesure de B** | Son numérateur compte des crédits à échéance courte : ne pas les renouveler est la contraction mesurée |
| Fonds propres | Non | Hypothèse HT2 |

### 6.3 Valeurs de calibration (extrait ; détail dans « Données.md » §9)

b stricte nette de l'UEMOA, avec λ = 0 et réserves obligatoires à 3 % de D :

| Année | 2021 | 2022 | 2023 | 2024 | 2025 (prov.) |
|---|---|---|---|---|---|
| b agrégée (donc ζ\*_agg à λ = 0) | 13,2 % | 11,1 % | 7,7 % | 10,1 % | 13,3 % |
| ζ\*_min (pays le plus fragile) | 8,8 % (Togo) | 4,3 % (Bénin) | 3,9 % (Bénin) | 4,5 % (Bénin) | 7,1 % (Bénin) |
| ρ de l'union | 0,706 | 0,748 | 0,777 | 0,758 | 0,689 |

Les pays aux tampons les plus bas sont le **Bénin et le Togo**. La Côte d'Ivoire se situe entre 7,5 % (2023) et 15,5 % (2025).

### 6.4 Sources et mode d'accès

| Donnée | Source | Accès |
|---|---|---|
| D, L, caisse, titres, comptes ordinaires débiteurs (par pays, annuel) | Commission Bancaire de l'UMOA, rapports annuels 2021, 2023, 2024, 2025 (annexes II.2.x.b) | Manuel (PDF), extrait dans « Données Extrait.xlsx » |
| Coefficient de liquidité par pays | Mêmes rapports | Manuel (PDF) |
| Réserves constituées et requises | BCEAO, rapports sur la politique monétaire et données mensuelles | Manuel |
| Séries monétaires et financières | Base des Données Économiques et Financières de la BCEAO | Interface web + export Excel (pas d'API documentée trouvée) |
| Ratios de comparaison | FMI / Banque mondiale | API ou téléchargement (comparaison seulement, pas pour B) |

### 6.5 Points ouverts

- **Coefficient de réserves obligatoires** (3 % utilisé) : source secondaire, à vérifier dans le texte BCEAO.
- **Norme de liquidité de l'UMOA** : le coefficient de liquidité (seuil de 75 % dans les rapports 2023-2025, 50 % dans le rapport 2021) est en vigueur ; le RLCT et le RLLT sont indiqués « pas encore applicables ». Il n'y a donc pas de LCR de Bâle dans l'union à ce jour. La date du passage de 50 % à 75 % reste à établir (rapport 2022 en scan, non lu).
- **Dispersion intra-pays (σ_b)** : aucun ratio de liquidité par banque trouvé ; reste un scénario (HM2).
- **Circulation de la liquidité entre pays** : non mesurée ; l'agrégat et la partition par pays encadrent la réalité (HM6).
- **Détention de titres par les non-banques** : non disponible ; elle conditionne le choix entre b stricte et b large (HM8).
- **Chiffres 2025** : provisoires, à actualiser à la sortie du rapport suivant.
