# -*- coding: utf-8 -*-
"""
==============================================================================
SIMULATION DE CHOC DE RETRAIT
Migration de dépôts vers une MNBC hypothétique : à quelles conditions le
crédit bancaire de l'UEMOA en souffre-t-il ?
(8 pays comme groupes de banques, zoom sur la Côte d'Ivoire)
==============================================================================

POUR QUI EST CE FICHIER ?
-------------------------
Pour toi, et pour n'importe qui, même sans formation en économie. Chaque étape,
chaque résultat, chaque scénario, chaque graphique et chaque test de sécurité
est expliqué en commentaires, avec des images. Lis les blocs "EXPLICATION
ÉCONOMIQUE" : ils racontent ce que le code fait, sans formule.

L'HISTOIRE EN UN PARAGRAPHE (L'IMAGE DU RÉSERVOIR)
--------------------------------------------------
Une banque est comme un château d'eau. Les dépôts des clients, c'est l'eau qui
entre. Les prêts, c'est l'eau qu'elle distribue à l'économie. Au fond du
château, elle garde un RÉSERVOIR DE SECOURS : son "matelas" de liquidité
(billets en caisse et argent déposé à la banque centrale).

Imagine maintenant une monnaie numérique de banque centrale (MNBC). Si des
clients y transfèrent une partie de leurs dépôts, l'eau sort du château :
c'est la FUITE (notée zêta, ζ, en % des dépôts).

 - Tant que le réservoir de secours n'est pas vide, la banque s'en sert et ne
   change rien : le crédit est intact.
 - Quand il est à sec, la banque doit fermer le robinet des prêts : le crédit
   BAISSE. Le moment précis où le réservoir se vide s'appelle le SEUIL CRITIQUE.
 - Un ROBINET DE RETOUR (lambda, λ) peut remettre de l'eau : la banque centrale
   re-prête aux banques, ou les clients redéposent. λ = 0 : aucun retour.
   λ = 1 : tout revient, le crédit ne bouge jamais.

L'union compte 8 pays, donc 8 châteaux d'eau de tailles et de réservoirs
différents. L'eau ne passe pas par magie d'un château à l'autre : un pays peut
être à sec pendant qu'un autre déborde. C'est l'HÉTÉROGÉNÉITÉ, et plusieurs
graphiques la montrent pays par pays.

COMMENT LE LANCER (SPYDER)
--------------------------
1. Place ce fichier dans le dossier principal "Simulation de Choc de Retrait/".
2. Le classeur doit être dans le sous-dossier Data/ :
      Simulation de Choc de Retrait/Data/Données Extrait.xlsx
3. Ouvre ce fichier dans Spyder, puis appuie sur F5 (tout lancer), ou exécute
   cellule par cellule (Ctrl+Entrée) : chaque "# %%" ci-dessous est une cellule.
4. Les résultats sont écrits dans le dossier "Resultats/" (créé
   automatiquement) : un classeur Excel et les graphiques PNG.
Bibliothèques utilisées (toutes incluses dans Anaconda) : pandas, numpy,
matplotlib, openpyxl.

LES ÉTAPES
----------
 Étape 0 : Outils et réglages
 Étape 1 : Charger les données
 Étape 2 : Calibrer (mesurer le "réservoir" de chaque pays)
 Étape 3 : Le cœur du modèle (la formule) + test de sécurité G1
 Étape 4 : Lancer les scénarios
 Étape 5 : Tests de sécurité n°2 (sur les résultats)
 Étape 6 : Produire les sorties S0 à S10 (tableaux et graphiques)
 Étape 7 : Dernier test de sécurité (tous les graphiques existent) et bilan

LES SORTIES ATTENDUES (CHAQUE SORTIE A SON OU SES GRAPHIQUES)
-------------------------------------------------------------
 S0  : Calibration : le réservoir de chaque pays       -> graphique S0
 S1  : Seuils critiques                                 -> graphique S1
 S2  : Courbes de contraction du crédit                 -> S2, S2b, S2c
 S3  : Sensibilité du seuil (réservoir et robinet)      -> S3, S3b
 S4  : Part de l'union touchée, qui porte la baisse     -> S4, S4b, S4c
 S5  : Règle du plafond de détention                    -> S5, S5b
 S6  : Robustesse sur phi                               -> S6
 S7  : Zoom Côte d'Ivoire                               -> S7
 S8  : Fourchette 2021-2025                             -> S8
 S9  : Chiffres-clés                                    -> S9 (+ phrases)
 S10 : Robustesse à l'erreur de mesure du réservoir     -> S10a, S10b, S10c

GRAPHIQUES DE L'HÉTÉROGÉNÉITÉ (PAYS PAR PAYS)
---------------------------------------------
 S0 (carte des réservoirs), S1 (seuil de chaque pays), S2b (courbe de chaque
 pays), S4 (escalier des pays touchés), S4b (qui porte la baisse), S4c (carte de
 chaleur pays x fuite).

LES SCÉNARIOS TESTÉS (CHAQUE SCÉNARIO A SON GRAPHIQUE)
------------------------------------------------------
 - la fuite ζ : de 0 % à 30 % des dépôts                      -> S2, S2b
 - le robinet de retour λ : 0, 0,5, 1 (et 5 valeurs dans S3b)   -> S2, S3, S3b
 - la réaction du crédit phi : 0,25 ; 0,5 ; 1                   -> S6
 - le réservoir : "stricte" (base) ou "large" (borne haute)     -> S2c
 - le plafond de détention : 2, 5, 10, 20 % des dépôts          -> S5, S5b
 - l'année : 2021 à 2025                                        -> S4, S8
 - l'erreur de mesure du réservoir : x0,5 ; x0,75 ; x1 ; x1,25  -> S10a-c

CE QUE LE CODE NE FAIT PAS
--------------------------
 - Il ne PRÉDIT PAS combien de gens adopteront une MNBC : la fuite ζ est un
   scénario testé, pas une prévision.
 - Il ne modélise PAS une panique bancaire (ruée) : c'est un autre phénomène
   (coordination des déposants), pas traité ici.
 - Il ne regarde PAS le temps : chaque année est une photo avant/après, sans
   film ni délais de réaction.
 - Il ne distingue PAS les banques d'un même pays (aucune donnée par banque).
 - Il ne mesure PAS le retour du crédit sur les dépôts (effet de second tour) :
   la baisse réelle pourrait être plus forte.
 - Il ne fait PAS d'estimation économétrique (pas de régression) : c'est une
   calibration suivie d'une simulation.
 - Ses seuils ne sont PAS des résultats empiriques : ce sont les conséquences
   d'une formule appliquée à des données observées en 2021-2025.
==============================================================================
"""

# %% ==========================================================================
# ÉTAPE 0 : OUTILS ET RÉGLAGES
# =============================================================================
# EXPLICATION ÉCONOMIQUE
#   Avant de commencer, on ouvre la boîte à outils et on fixe les réglages
#   du scénario. Tous les chiffres qu'on peut vouloir changer sont ici, au même
#   endroit, comme le tableau de bord d'une voiture.
# =============================================================================
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# --- Où sont les fichiers ? ---------------------------------------------------
# Le code cherche tout par rapport à l'emplacement de CE fichier, pour marcher
# sur n'importe quel ordinateur sans changer de chemin.
try:
    DOSSIER = Path(__file__).resolve().parent.parent
except NameError:                      # cas : cellule lancée seule dans Spyder
    DOSSIER = Path.cwd().parent
FICHIER_DONNEES = DOSSIER / "Data" / "Données Extrait.xlsx"
DOSSIER_SORTIES = DOSSIER / "Resultats"
DOSSIER_GRAPHS = DOSSIER_SORTIES / "Graphiques"
DOSSIER_SORTIES.mkdir(exist_ok=True)
DOSSIER_GRAPHS.mkdir(exist_ok=True)

# --- Réglages économiques -----------------------------------------------------
# Réserves obligatoires : la part des dépôts que la banque DOIT garder en
# réserve à la banque centrale (3 %). Cet argent est déjà "pris" : ce n'est pas
# un vrai matelas. On le soustrait donc du réservoir.
# (Chiffre issu de la presse financière : à vérifier dans le texte BCEAO.)
RESERVES_OBLIGATOIRES = 0.03

# La fuite ζ : de 0 % à 30 % des dépôts, par pas de 0,1 %.
ZETAS = np.round(np.arange(0.0, 0.3000001, 0.001), 4)
ZETAS_LARGE = np.round(np.arange(0.0, 0.6000001, 0.002), 4)   # pour le graphique S2c
ZETAS_CLES = [0.01, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30]

# Le robinet de retour λ : trois lectures simples.
#   0   = la MNBC est lancée sans aucune aide de la BCEAO
#   0,5 = la BCEAO re-prête la moitié de ce qui sort
#   1   = la BCEAO re-prête tout (le crédit ne bouge jamais)
LAMBDAS = [0.0, 0.5, 1.0]
LAMBDAS_FINS = [0.0, 0.25, 0.5, 0.75, 1.0]      # pour le graphique S3b

# phi : quelle part du manque d'argent est comblée en prêtant moins.
# Cas de base = 1 (borne haute). On teste aussi 0,25 et 0,5.
PHIS = [0.25, 0.5, 1.0]
PHI_BASE = 1.0

# Deux façons de mesurer le réservoir (voir étape 2).
VARIANTE_BASE = "b_stricte"       # monnaie de banque centrale uniquement
VARIANTE_HAUTE = "b_large"        # + titres d'État : borne haute
VARIANTES = [VARIANTE_BASE, VARIANTE_HAUTE]

# Plafonds de détention testés : la part maximale des dépôts qui PEUT partir.
PLAFONDS = [0.02, 0.05, 0.10, 0.20]

# Erreur de mesure du réservoir (sortie S10). Le vrai réservoir = kappa x notre
# mesure. kappa = 0,5 : notre mesure est TROP HAUTE de moitié (cas probable, car
# nos comptes incluent des avoirs étrangers et interbancaires). kappa = 1,25 :
# notre mesure est trop basse (cas des titres achetés par des non-banques).
KAPPAS = [0.50, 0.75, 1.00, 1.25]

# Années.
ANNEES = [2021, 2022, 2023, 2024, 2025]
ANNEES_CLES = [2023, 2024, 2025]      # 2023 = cas bas, 2024 = centre, 2025 = cas haut
PAYS_ZOOM = "Côte d'Ivoire"

# Look des graphiques : style "ggplot" (le même habillage que le package R).
plt.style.use("ggplot")
COULEURS = {"agg": "#1F77B4", "part": "#D62728", "ci": "#2CA02C", "gris": "#7F7F7F"}
COULEURS_ANNEES = {2021: "#9ECAE1", 2022: "#6BAED6", 2023: "#D62728", 2024: "#FF7F0E", 2025: "#2CA02C"}
GRAPHIQUES_PRODUITS = {}     # nom du fichier -> ce qu'il montre (pour l'index final)


def sauver_graphique(fig, nom, description):
    """Enregistre le graphique en PNG dans Resultats/Graphiques et l'affiche."""
    chemin = DOSSIER_GRAPHS / f"{nom}.png"
    fig.savefig(chemin, dpi=150, bbox_inches="tight")
    GRAPHIQUES_PRODUITS[nom] = description
    plt.show()
    print(f"   -> graphique enregistré : {chemin.name}")


# %% ==========================================================================
# ÉTAPE 1 : CHARGER LES DONNÉES
# =============================================================================
# EXPLICATION ÉCONOMIQUE
#   On ouvre le "carnet de comptes" des banques : pour chaque pays (8) et chaque
#   année (2021 à 2025), les chiffres publiés par la Commission Bancaire :
#     D  = tout l'argent que les clients ont déposé (l'eau qui entre)
#     L  = les prêts accordés à l'économie (l'eau distribuée)
#     Caisse + comptes à la banque centrale/correspondants = le réservoir de secours
#     Titres = obligations d'État que les banques détiennent
#   Tous ces montants sont en millions de FCFA.
#
# CE QUE FAIT LE CODE
#   Lit l'onglet "Données_pays" du classeur "Données Extrait.xlsx". Chaque ligne
#   = un pays pour une année (8 pays x 5 années = 40 lignes).
# =============================================================================
print("=" * 78)
print("ÉTAPE 1 : chargement des données")
print("=" * 78)

if not FICHIER_DONNEES.exists():
    raise FileNotFoundError(
        "Fichier introuvable : " + str(FICHIER_DONNEES) + "\n"
        "Vérifie que ce script est dans 'Simulation de Choc de Retrait/' et que "
        "le classeur 'Données Extrait.xlsx' est dans le sous-dossier 'Data/'."
    )

NOMS_COLONNES = [
    "annee", "pays", "rapport", "statut", "D", "L", "a_vue", "a_terme", "caisse",
    "co_deb", "t_trans", "t_plac", "t_inv", "actif", "emprunts_clientele",
    "garanties", "fonds_propres", "emprunts_interbancaires",
]
donnees = pd.read_excel(FICHIER_DONNEES, sheet_name="Données_pays", header=4)
donnees.columns = NOMS_COLONNES
donnees = donnees.dropna(subset=["annee"]).copy()
donnees["annee"] = donnees["annee"].astype(int)
PAYS = list(donnees["pays"].unique())
print(f"   {len(donnees)} lignes chargées : {donnees['pays'].nunique()} pays, "
      f"années {donnees['annee'].min()} à {donnees['annee'].max()}.")

# %% ==========================================================================
# ÉTAPE 2 : CALIBRER (MESURER LE RÉSERVOIR DE CHAQUE PAYS)
# =============================================================================
# EXPLICATION ÉCONOMIQUE
#   On mesure, pays par pays, trois choses :
#
#   (a) rho = L / D : "à quel point la banque est prêtée". Si rho = 0,75, sur
#       100 FCFA déposés, 75 sont déjà sortis en prêts.
#
#   (b) b = le RÉSERVOIR de secours, en % des dépôts. C'est l'argent liquide que
#       la banque peut utiliser pour encaisser une fuite SANS toucher aux prêts.
#       Deux versions :
#         - b STRICTE (cas de base) = (caisse + comptes ordinaires débiteurs
#           de trésorerie) / D - réserves obligatoires. Seule la monnaie de
#           banque centrale compte, car si une banque vend un titre à une autre
#           banque, l'argent change de poche sans que le système en gagne.
#         - b LARGE (borne haute) = b stricte + titres de transaction et de
#           placement. Elle SURESTIME le vrai matelas : on la garde pour
#           montrer la marge d'erreur.
#
#   (c) w = le POIDS du pays : sa part dans tous les dépôts de l'union. La Côte
#       d'Ivoire pèse ~41 % en 2025 : son réservoir compte plus que celui de la
#       Guinée-Bissau (0,5 %).
#
# CE QUE FAIT LE CODE
#   Ajoute ces colonnes au tableau, puis produit la SORTIE S0 (tableau et carte
#   de chaleur du réservoir de chaque pays et de chaque année).
# =============================================================================
print("\n" + "=" * 78)
print("ÉTAPE 2 : calibration")
print("=" * 78)

calib = donnees.copy()
calib["rho"] = calib["L"] / calib["D"]
calib["b_stricte_brute"] = (calib["caisse"] + calib["co_deb"]) / calib["D"]
calib["b_large_brute"] = (calib["caisse"] + calib["co_deb"]
                          + calib["t_trans"] + calib["t_plac"]) / calib["D"]
calib["b_stricte_avant_plancher"] = calib["b_stricte_brute"] - RESERVES_OBLIGATOIRES
calib["b_large_avant_plancher"] = calib["b_large_brute"] - RESERVES_OBLIGATOIRES

# PLANCHER À ZÉRO : un réservoir ne peut pas être négatif dans le modèle.
# (Dans les données 2021-2025, ce plancher n'est jamais activé.)
nb_planchers = int((calib["b_stricte_avant_plancher"] < 0).sum()
                   + (calib["b_large_avant_plancher"] < 0).sum())
calib["b_stricte"] = calib["b_stricte_avant_plancher"].clip(lower=0.0)
calib["b_large"] = calib["b_large_avant_plancher"].clip(lower=0.0)

calib["poids"] = calib["D"] / calib.groupby("annee")["D"].transform("sum")
calib["part_a_vue"] = calib["a_vue"] / calib["D"]

# Agrégat UEMOA par année : l'union vue comme UN SEUL grand bilan "moyen".
lignes_agregat = []
for annee, g in calib.groupby("annee"):
    lignes_agregat.append({
        "annee": annee,
        "D_md": g["D"].sum() / 1000, "L_md": g["L"].sum() / 1000,
        "rho": g["L"].sum() / g["D"].sum(),
        "b_stricte": float((g["poids"] * g["b_stricte"]).sum()),
        "b_large": float((g["poids"] * g["b_large"]).sum()),
    })
agregat = pd.DataFrame(lignes_agregat).set_index("annee")

# --- SORTIE S0 : tableau de calibration --------------------------------------
# LECTURE : chaque case = la taille du réservoir de secours, en % des dépôts.
# Plus c'est grand, plus le pays peut encaisser de fuite avant de réduire le
# crédit. Un pays avec 4 % peut encaisser une fuite de 4 % ; un pays avec 15 %,
# une fuite de 15 %.
S0 = (calib.pivot(index="pays", columns="annee", values="b_stricte") * 100).round(1)
S0.loc["UEMOA (agrégé)"] = (agregat["b_stricte"] * 100).round(1)
print("\nSORTIE S0 : réservoir b stricte, en % des dépôts")
print(S0.to_string())
print(f"\n   Planchers à zéro activés : {nb_planchers} (0 = jamais nécessaire)")

# --- GRAPHIQUE S0 : carte de chaleur des réservoirs --------------------------
# EXPLICATION ÉCONOMIQUE
#   Une case = le réservoir d'un pays une année donnée. Plus la case est foncée,
#   plus le pays est protégé. On voit d'un coup d'oeil : (1) les lignes pâles =
#   pays fragiles (Bénin, Togo), (2) les colonnes pâles = années de liquidité
#   rare (2023), (3) que la dernière ligne (l'union) est une MOYENNE qui cache
#   ces écarts. C'est le portrait de l'hétérogénéité en une image.
fig, ax = plt.subplots(figsize=(8.5, 5.5))
ordre = list(S0.sort_values(2025).index)
mat = S0.loc[ordre].values.astype(float)
im = ax.imshow(mat, cmap="YlGnBu", aspect="auto")
ax.set_xticks(range(len(S0.columns)))
ax.set_xticklabels([str(c) for c in S0.columns])
ax.set_yticks(range(len(ordre)))
ax.set_yticklabels(ordre)
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        ax.text(j, i, f"{mat[i, j]:.1f}", ha="center", va="center",
                color="white" if mat[i, j] > np.nanmax(mat) * 0.6 else "black", fontsize=9)
ax.grid(False)
fig.colorbar(im, label="Réservoir b stricte (% des dépôts)")
ax.set_title("S0 : le réservoir de chaque pays, année par année")
fig.tight_layout()
sauver_graphique(fig, "S0_carte_reservoirs", "Réservoir b de chaque pays et année (carte de chaleur)")

# %% ==========================================================================
# ÉTAPE 3 : LE CŒUR DU MODÈLE
# =============================================================================
# EXPLICATION ÉCONOMIQUE
#   La formule tient en trois gestes, comme remplir un seau :
#
#   1. PERTE NETTE      = (1 - λ) x ζ
#      De la fuite ζ, une partie λ revient par le robinet de retour. Ce qui
#      manque vraiment, c'est (1 - λ) fois ce qui est parti.
#
#   2. MANQUE            = max( 0 ; perte nette - b )
#      La banque utilise d'abord son réservoir. S'il suffit, le manque est
#      zéro (le crédit ne bouge pas). Sinon, le manque est ce que le réservoir
#      n'a pas couvert.
#
#   3. BAISSE DU CRÉDIT = phi x manque / rho
#      Pour combler le manque, la banque prête moins. On divise par rho pour
#      exprimer la baisse en % du crédit existant. (La baisse ne peut jamais
#      dépasser 100 %.)
#
#   SEUIL CRITIQUE : la fuite à partir de laquelle le manque devient positif :
#                          zêta* = b / (1 - λ)
#   Avec λ = 0 : le seuil est égal au réservoir. Avec λ = 0,5 : il double.
#   Avec λ = 1 : il n'existe pas (le robinet de retour compense tout).
#
#   EXEMPLE CONCRET (le même que dans le document) :
#   100 FCFA de dépôts, 80 de prêts (rho = 0,8). Fuite de 10 % (10 FCFA), aucun
#   retour. Réservoir : 6 FCFA. Manque = 10 - 6 = 4 FCFA. La banque réduit ses
#   prêts de 4 sur 80 = 5 %. Si le réservoir faisait 10 FCFA ou plus : 0 %.
#
# CE QUE FAIT LE CODE
#   Définit les fonctions ci-dessous, puis exécute le TEST DE SÉCURITÉ G1.
# =============================================================================
print("\n" + "=" * 78)
print("ÉTAPE 3 : cœur du modèle et test de sécurité G1")
print("=" * 78)


def manque_relatif(zeta, lam, b):
    """Manque d'argent après usage du réservoir, en % des dépôts."""
    return np.maximum(0.0, (1.0 - lam) * np.asarray(zeta) - b)


def baisse_credit_pct(zeta, lam, phi, b, rho):
    """Baisse du crédit, en fraction du crédit existant (0,05 = 5 %)."""
    return np.minimum(1.0, phi * manque_relatif(zeta, lam, b) / rho)


def seuil_critique(b, lam):
    """Fuite à partir de laquelle le crédit commence à baisser.
    Avec lam = 1, il n'existe pas : on renvoie l'infini."""
    b = np.asarray(b, dtype=float)
    if lam >= 1.0:
        return np.full_like(b, np.inf)
    return b / (1.0 - lam)


def calculer_union(sous, zetas, lam, phi, variante):
    """
    Fait tourner le modèle pour les 8 pays d'UNE année et renvoie :
      - la baisse du crédit pays par pays,
      - la somme des 8 pays (= la liquidité NE circule PAS entre pays),
      - l'agrégat UEMOA (= l'union comme UN SEUL bilan : la liquidité circule
        parfaitement entre pays).
    La réalité se situe entre les deux : c'est pourquoi on montre les deux.
    """
    zetas = np.asarray(zetas)
    D = sous["D"].to_numpy()[:, None]            # millions de FCFA
    L = sous["L"].to_numpy()[:, None]
    b = sous[variante].to_numpy()[:, None]
    manque = np.maximum(0.0, (1.0 - lam) * zetas[None, :] - b)   # en % des dépôts
    baisse_md_k = np.minimum(L, phi * manque * D)                 # ne dépasse pas L
    pays_pct = baisse_md_k / L
    part_md = baisse_md_k.sum(axis=0) / 1000.0                    # milliards FCFA
    part_pct = baisse_md_k.sum(axis=0) / L.sum()
    # agrégat : un seul bilan moyen
    w = (D / D.sum()).ravel()
    b_agg = float((w * b.ravel()).sum())
    rho_agg = float(L.sum() / D.sum())
    agg_pct = baisse_credit_pct(zetas, lam, phi, b_agg, rho_agg)
    agg_md = agg_pct * L.sum() / 1000.0
    return {"pays_pct": pays_pct, "pays_md": baisse_md_k / 1000.0,
            "part_pct": part_pct, "part_md": part_md,
            "agg_pct": agg_pct, "agg_md": agg_md, "b_agg": b_agg, "rho_agg": rho_agg}


# --- GARDE-FOUS : compteur de tests ------------------------------------------
# EXPLICATION ÉCONOMIQUE
#   Un garde-fou, c'est le contrôle technique de la voiture avant le départ :
#   le code se vérifie lui-même. Si un test échoue, le programme S'ARRÊTE avec
#   un message clair, au lieu de produire des résultats faux qui auraient l'air
#   crédibles. Chaque test est expliqué par une image.
journal_garde_fous = []


def garde_fou(code, nom, condition, explication):
    """Enregistre le test, l'affiche, et arrête le programme s'il échoue."""
    statut = "OK" if bool(condition) else "ÉCHEC"
    journal_garde_fous.append({"Test": code, "Ce qu'il vérifie": nom,
                               "Statut": statut, "Image": explication})
    print(f"   [{statut}] {code} : {nom}")
    if statut == "ÉCHEC":
        raise AssertionError(f"Garde-fou {code} échoué : {nom}. {explication}")


# GARDE-FOU G1 : l'exemple du document
# IMAGE : si on branche la formule sur l'exemple de la page 1 du document
# (100 de dépôts, 80 de prêts, fuite 10, réservoir 6), elle doit donner
# exactement 5 %. Sinon, elle est mal câblée, comme une calculatrice qui
# répond 3 à 1+1.
garde_fou("G1", "l'exemple du document donne exactement 5 %",
          abs(float(baisse_credit_pct(0.10, 0.0, 1.0, 0.06, 0.80)) - 0.05) < 1e-12,
          "100 de dépôts, 80 de prêts, fuite 10 %, réservoir 6 % -> baisse de 5 %.")

# %% ==========================================================================
# ÉTAPE 4 : LANCER LES SCÉNARIOS
# =============================================================================
# EXPLICATION ÉCONOMIQUE
#   Un scénario, c'est un "et si ?". On pose la question pour toutes les
#   combinaisons possibles, comme un météorologue qui teste plusieurs
#   conditions :
#       - Pour chaque ANNÉE (2021 à 2025) : l'état du réservoir de l'époque.
#       - Pour chaque FUITE ζ (0 à 30 %) : combien de dépôts quittent.
#       - Pour chaque ROBINET λ (0 ; 0,5 ; 1) : l'aide de la BCEAO.
#       - Pour chaque RÉACTION phi (0,25 ; 0,5 ; 1) : si la banque coupe tout
#         ou seulement en partie.
#       - Pour chaque RÉSERVOIR : stricte (base) ou large (borne haute).
#   Cela donne environ 270 000 résultats, rangés dans un seul grand tableau et
#   dans un classeur de courbes que les graphiques viennent consulter.
#
# CE QUE FAIT LE CODE
#   Boucle sur toutes les combinaisons et stocke, pour chaque ligne, la baisse
#   du crédit en % et en milliards de FCFA, pour : l'union comme un seul bilan,
#   la somme des 8 pays, et chacun des 8 pays.
# =============================================================================
print("\n" + "=" * 78)
print("ÉTAPE 4 : scénarios")
print("=" * 78)

COURBES = {}          # (annee, variante, lam, phi, entite) -> (pct, milliards)
morceaux = []
for annee in ANNEES:
    sous = calib[calib["annee"] == annee].reset_index(drop=True)
    for variante in VARIANTES:
        for lam in LAMBDAS:
            for phi in PHIS:
                r = calculer_union(sous, ZETAS, lam, phi, variante)
                base = {"annee": annee, "variante": variante, "lam": lam, "phi": phi}
                entites = {"UEMOA agrégé": (r["agg_pct"], r["agg_md"]),
                           "UEMOA pays par pays": (r["part_pct"], r["part_md"])}
                for i, pays in enumerate(sous["pays"]):
                    entites[pays] = (r["pays_pct"][i], r["pays_md"][i])
                for nom, (pct_, md_) in entites.items():
                    COURBES[(annee, variante, lam, phi, nom)] = (pct_, md_)
                    morceaux.append(pd.DataFrame({**base, "zeta": ZETAS,
                                                  "entite": nom,
                                                  "baisse_pct": pct_, "baisse_md": md_}))
resultats = pd.concat(morceaux, ignore_index=True)
print(f"   {len(resultats):,} résultats calculés.".replace(",", " "))


def courbe(annee, entite, lam=0.0, phi=PHI_BASE, variante=VARIANTE_BASE, md=False):
    """Récupère une courbe déjà calculée (en % du crédit, ou en milliards si md)."""
    pct_, md_ = COURBES[(annee, variante, lam, phi, entite)]
    return md_ if md else pct_


def idx_zeta(z):
    """Position de la fuite z dans la grille ZETAS."""
    return int(np.argmin(np.abs(ZETAS - z)))


# %% ==========================================================================
# ÉTAPE 5 : TESTS DE SÉCURITÉ N°2 (SUR LES RÉSULTATS)
# =============================================================================
# EXPLICATION ÉCONOMIQUE
#   Maintenant que le code a calculé, on vérifie que les résultats respectent
#   les lois du bon sens économique.
# =============================================================================
print("\n" + "=" * 78)
print("ÉTAPE 5 : tests de sécurité")
print("=" * 78)

# GARDE-FOU G2 : si tout revient (λ = 1), le crédit ne bouge jamais
# IMAGE : si le robinet de retour remet toute l'eau qui sort, le réservoir ne
# se vide jamais. Le crédit doit donc rester à zéro de baisse, partout.
garde_fou("G2", "λ = 1 : aucune baisse du crédit nulle part",
          resultats.loc[resultats["lam"] == 1.0, "baisse_pct"].abs().max() < 1e-12,
          "Tout l'argent revient : pas de manque, pas de baisse.")

# GARDE-FOU G3 : plus la fuite est grande, plus la baisse est grande
# IMAGE : si on verse plus d'eau hors du château, le niveau ne peut pas
# remonter. La courbe de baisse ne doit jamais descendre quand ζ augmente.
tri = resultats.sort_values(["annee", "variante", "lam", "phi", "entite", "zeta"])
diff = tri.groupby(["annee", "variante", "lam", "phi", "entite"])["baisse_pct"].diff()
garde_fou("G3", "la baisse ne diminue jamais quand la fuite augmente",
          diff.dropna().min() >= -1e-12,
          "Plus d'eau qui sort ne peut pas faire baisser la baisse.")

# GARDE-FOU G4 : en dessous du seuil, aucune baisse
# IMAGE : tant que le réservoir n'est pas vide, personne ne ferme le robinet
# des prêts. Pour chaque pays, la baisse doit être nulle jusqu'à son seuil.
ok_seuil = True
for annee in ANNEES:
    sous = calib[calib["annee"] == annee]
    for _, ligne in sous.iterrows():
        for variante in VARIANTES:
            for lam in [0.0, 0.5]:
                s = float(seuil_critique(ligne[variante], lam))
                c = courbe(annee, ligne["pays"], lam, PHI_BASE, variante)
                if np.abs(c[ZETAS <= s - 1e-9]).max(initial=0.0) > 1e-12:
                    ok_seuil = False
garde_fou("G4", "sous le seuil critique, la baisse est nulle (tous pays, toutes années)",
          ok_seuil, "Réservoir non vide : le crédit est intact.")

# GARDE-FOU G5 : la moyenne ne dépasse jamais la somme des pays
# IMAGE : si on regarde l'union comme UN SEUL grand château, on voit un réservoir
# moyen et on conclut "tout va bien". Mais si un pays est à sec pendant qu'un
# autre déborde, l'eau ne passe pas par magie de l'un à l'autre. La baisse
# réelle, pays par pays, est donc toujours au moins aussi grande que celle de
# la moyenne (c'est l'inégalité de Jensen).
ecart_jensen = max(
    float(np.max(courbe(a, "UEMOA agrégé", l, p, v, md=True) - courbe(a, "UEMOA pays par pays", l, p, v, md=True)))
    for a in ANNEES for v in VARIANTES for l in LAMBDAS for p in PHIS)
garde_fou("G5", "l'agrégat UEMOA ne dépasse jamais la somme des pays (Jensen)",
          ecart_jensen < 1e-9, "La moyenne cache les pays à sec : elle sous-estime la baisse.")

# GARDE-FOU G6 : les poids des pays totalisent 100 %
# IMAGE : si on découpe un gâteau en huit parts, les parts doivent refaire un
# gâteau entier. Les poids (part de chaque pays dans les dépôts) valent 1.
garde_fou("G6", "les poids des 8 pays totalisent 100 % chaque année",
          np.allclose(calib.groupby("annee")["poids"].sum(), 1.0),
          "Huit parts d'un même gâteau = un gâteau.")

# GARDE-FOU G7 : toute baisse est comprise entre 0 % et 100 %
# IMAGE : on ne peut pas perdre moins que rien, ni plus que tout. Pas de
# baisse négative ni supérieure à 100 %, et aucun chiffre manquant.
garde_fou("G7", "toutes les baisses sont entre 0 % et 100 %, sans valeur manquante",
          resultats["baisse_pct"].between(0, 1).all() and not resultats["baisse_pct"].isna().any(),
          "Entre rien et tout, et pas de case vide.")

# GARDE-FOU G8 : on retrouve les chiffres déjà publiés dans le classeur
# IMAGE : c'est la contre-épreuve de la pesée. Le réservoir de l'union calculé
# ici doit être le même que celui déjà calculé dans le classeur Excel
# (onglet Synthèse_UEMOA). Si les deux balances donnent le même poids, c'est
# que l'extraction et la calibration sont fiables.
try:
    synthese = pd.read_excel(FICHIER_DONNEES, sheet_name="Synthèse_UEMOA", header=2).iloc[:5]
    attendu = synthese.set_index("Année")["b stricte nette"].astype(float)
    ecart = float((attendu.sort_index() - agregat["b_stricte"].sort_index()).abs().max())
    garde_fou("G8", "le réservoir UEMOA égale celui du classeur Excel (écart < 0,001 point)",
              ecart < 1e-5, "Deux calculs indépendants donnent le même résultat.")
except (ValueError, KeyError) as e:
    print(f"   [IGNORÉ] G8 : onglet Synthèse_UEMOA illisible ({e})")

print(f"\n   Tous les garde-fous de cette étape sont passés "
      f"({sum(j['Statut'] == 'OK' for j in journal_garde_fous)}/{len(journal_garde_fous)}).")

# %% ==========================================================================
# ÉTAPE 6 : PRODUIRE LES SORTIES (TABLEAUX ET GRAPHIQUES)
# =============================================================================
print("\n" + "=" * 78)
print("ÉTAPE 6 : sorties")
print("=" * 78)


def milliards(x):
    """Montant en milliards de FCFA avec espace comme séparateur de milliers."""
    return f"{x:,.0f}".replace(",", " ")


def pct(x, n=1):
    """Fraction -> texte en pourcentage avec virgule décimale."""
    return f"{x * 100:.{n}f} %".replace(".", ",")


def seuils_annee(annee, lam, variante=VARIANTE_BASE, kappa=1.0):
    """Seuils de l'année : par pays, le plus fragile, et agrégé."""
    sous = calib[calib["annee"] == annee]
    b = sous[variante].to_numpy() * kappa
    sk = seuil_critique(b, lam)
    sagg = float(seuil_critique(float((sous["poids"].to_numpy() * b).sum()), lam))
    return sk, float(np.min(sk)), sagg


# ----------------------------------------------------------------------------
# SORTIE S1 : TABLEAU ET GRAPHIQUE DES SEUILS CRITIQUES
# EXPLICATION ÉCONOMIQUE
#   Pour chaque pays et année : à partir de quelle fuite ζ le crédit commence à
#   baisser ? C'est la réponse à la question Q1 du mémoire : "le seuil est-il
#   atteignable ?". Un seuil de 7 % veut dire : tant que moins de 7 % des
#   dépôts s'en vont, les banques de ce pays n'ont rien à changer.
#   Trois lignes spéciales :
#     - "Pays le plus fragile" : le premier pays à craquer.
#     - "UEMOA agrégé" : le seuil si l'union était un seul bilan.
#     - λ = 1 : "illimité" (le robinet de retour compense tout).
#
#   GRAPHIQUE S1 : un point par pays et par année, sur une règle graduée en %
#   de fuite. Plus le point est à GAUCHE, plus le pays craque tôt. La taille du
#   point = le poids du pays (la Côte d'Ivoire est un gros point, la Guinée-
#   Bissau un petit). Les deux traits verticaux sont le seuil de l'union vue
#   comme un seul bilan en 2023 (le plus bas) et 2025 (le plus haut). Tous les
#   points à gauche du trait sont des pays que la moyenne protège à tort.
# ----------------------------------------------------------------------------
lignes_s1 = []
for annee in ANNEES:
    sous = calib[calib["annee"] == annee]
    for variante in VARIANTES:
        for lam in LAMBDAS:
            sk, smin, sagg = seuils_annee(annee, lam, variante)
            for pays, s in zip(sous["pays"], sk):
                lignes_s1.append([annee, variante, lam, pays, s])
            lignes_s1.append([annee, variante, lam, "UEMOA agrégé", sagg])
            lignes_s1.append([annee, variante, lam, "Pays le plus fragile (minimum)", smin])
S1 = pd.DataFrame(lignes_s1, columns=["annee", "reservoir", "lambda", "entite", "seuil"])
S1_affiche = S1.copy()
S1_affiche["seuil"] = S1_affiche["seuil"].apply(lambda x: "illimité" if np.isinf(x) else round(x * 100, 2))
print("\nSORTIE S1 : seuils critiques (cas de base : réservoir stricte, λ = 0), en % des dépôts")
vue = S1[(S1["reservoir"] == VARIANTE_BASE) & (S1["lambda"] == 0.0)].pivot(index="entite", columns="annee", values="seuil")
print((vue * 100).round(1).to_string())

fig, ax = plt.subplots(figsize=(10, 5.5))
ordre_pays = list(calib[calib["annee"] == 2025].sort_values("b_stricte")["pays"])
for annee in ANNEES:
    sous = calib[calib["annee"] == annee].set_index("pays")
    ax.scatter([sous.loc[p, "b_stricte"] * 100 for p in ordre_pays], range(len(ordre_pays)),
               s=[sous.loc[p, "poids"] * 1500 + 25 for p in ordre_pays], alpha=0.75,
               color=COULEURS_ANNEES[annee], label=str(annee), edgecolor="white")
for annee, ls_ in [(2023, "--"), (2025, ":")]:
    ax.axvline(seuils_annee(annee, 0.0)[2] * 100, color=COULEURS_ANNEES[annee], ls=ls_, lw=1.4,
               label=f"seuil union (un seul bilan) {annee}")
ax.set_yticks(range(len(ordre_pays)))
ax.set_yticklabels(ordre_pays)
ax.set_xlabel("Seuil critique ζ* (% des dépôts), λ = 0, réservoir stricte")
ax.set_title("S1 : à partir de quelle fuite chaque pays craque (taille du point = poids du pays)")
ax.legend(fontsize=8, ncol=2, loc="lower right")
fig.tight_layout()
sauver_graphique(fig, "S1_seuils_par_pays", "Seuil critique de chaque pays et année, taille = poids")

# ----------------------------------------------------------------------------
# SORTIE S2 : COURBES DE CONTRACTION DU CRÉDIT
# EXPLICATION ÉCONOMIQUE
#   La courbe montre, pour chaque niveau de fuite ζ (axe horizontal), de combien
#   le crédit baisse (axe vertical). Elle a la forme d'un COUDE :
#       - à plat à zéro tant que le réservoir tient (rien ne se passe),
#       - puis une pente qui monte dès que le réservoir est vide.
#   Deux courbes à comparer :
#       BLEUE  = l'union comme un seul bilan (la liquidité circule parfaitement)
#       ROUGE  = les 8 pays pris séparément (la liquidité ne circule pas)
#   L'ÉCART entre bleu et rouge est le COÛT D'IGNORER LES DIFFÉRENCES entre
#   pays : la moyenne cache les pays déjà à sec. La courbe verte est la Côte
#   d'Ivoire. Le trait gris pointillé est l'agrégat avec le réservoir "large"
#   (borne haute). Une colonne par λ : à λ = 1, tout est plat (neutralité).
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(len(ANNEES_CLES), len(LAMBDAS), figsize=(13, 10), sharex=True, sharey=True)
for i, annee in enumerate(ANNEES_CLES):
    for j, lam in enumerate(LAMBDAS):
        ax = axes[i, j]
        ax.plot(ZETAS * 100, courbe(annee, "UEMOA agrégé", lam) * 100, color=COULEURS["agg"], lw=2, label="UEMOA : un seul bilan")
        ax.plot(ZETAS * 100, courbe(annee, "UEMOA pays par pays", lam) * 100, color=COULEURS["part"], lw=2, label="UEMOA : 8 pays séparés")
        ax.plot(ZETAS * 100, courbe(annee, PAYS_ZOOM, lam) * 100, color=COULEURS["ci"], lw=1.3, label="Côte d'Ivoire")
        ax.plot(ZETAS * 100, courbe(annee, "UEMOA agrégé", lam, variante=VARIANTE_HAUTE) * 100, color=COULEURS["gris"],
                lw=1.2, ls="--", label="UEMOA, réservoir large (borne haute)")
        ax.set_title(f"{annee} | λ = {lam:g}", fontsize=10)
        if i == len(ANNEES_CLES) - 1:
            ax.set_xlabel("Fuite ζ (% des dépôts)")
        if j == 0:
            ax.set_ylabel("Baisse du crédit (%)")
axes[0, 0].legend(fontsize=8, loc="upper left")
fig.suptitle("S2 : baisse du crédit selon la fuite des dépôts (φ = 1)", fontsize=13)
fig.tight_layout()
sauver_graphique(fig, "S2_courbes_contraction", "Courbes de contraction : un seul bilan, 8 pays, Côte d'Ivoire")

# --- GRAPHIQUE S2b : UNE COURBE PAR PAYS (HÉTÉROGÉNÉITÉ) ----------------------
# EXPLICATION ÉCONOMIQUE
#   Huit petits graphiques, un par pays, avec une courbe par année. Chaque pays
#   a son propre "coude" : le Bénin et le Togo décollent très tôt, la Guinée-
#   Bissau très tard. Les courbes d'un même pays se superposent mal d'une année
#   à l'autre : le réservoir change avec la conjoncture (2023 = courbe rouge,
#   la plus à gauche). C'est la preuve visuelle que "l'UEMOA" n'est pas un
#   bloc : la même fuite de 10 % est indolore pour l'un et coûteuse pour l'autre.
fig, axes = plt.subplots(2, 4, figsize=(15, 7.5), sharex=True, sharey=True)
for ax, pays in zip(axes.ravel(), PAYS):
    for annee in ANNEES:
        ax.plot(ZETAS * 100, courbe(annee, pays) * 100, color=COULEURS_ANNEES[annee],
                lw=2.2 if annee in ANNEES_CLES else 1.2, label=str(annee))
    poids25 = float(calib[(calib["annee"] == 2025) & (calib["pays"] == pays)]["poids"].iloc[0])
    ax.set_title(f"{pays} (poids 2025 : {poids25 * 100:.0f} %)", fontsize=10)
axes[0, 0].legend(fontsize=8, title="Année", loc="upper left")
for ax in axes[1]:
    ax.set_xlabel("Fuite ζ (% des dépôts)")
for ax in axes[:, 0]:
    ax.set_ylabel("Baisse du crédit (%)")
fig.suptitle("S2b : la courbe de chaque pays (λ = 0, φ = 1, réservoir stricte)", fontsize=13)
fig.tight_layout()
sauver_graphique(fig, "S2b_courbes_par_pays", "Une courbe de contraction par pays et par année")

# --- GRAPHIQUE S2c : RÉSERVOIR STRICTE CONTRE LARGE (SCÉNARIO "RÉSERVOIR") ----
# EXPLICATION ÉCONOMIQUE
#   Ce scénario compare nos deux façons de mesurer le réservoir. En trait plein :
#   la b stricte (seulement la monnaie de banque centrale). En pointillé : la b
#   large (on y ajoute les titres d'État). Le réservoir large est BEAUCOUP plus
#   gros (≈ 40 % des dépôts), donc le crédit ne commence à baisser qu'après une
#   fuite de 40 % : irréaliste. C'est une BORNE HAUTE : même en comptant tout ce
#   qui pourrait, en théorie, être vendu, le seuil reste très loin. On étend
#   l'axe à 60 % pour voir le coude du réservoir large.
fig, ax = plt.subplots(figsize=(10, 5.5))
for annee in ANNEES:
    sous = calib[calib["annee"] == annee].reset_index(drop=True)
    for variante, ls_ in [(VARIANTE_BASE, "-"), (VARIANTE_HAUTE, "--")]:
        r = calculer_union(sous, ZETAS_LARGE, 0.0, PHI_BASE, variante)
        ax.plot(ZETAS_LARGE * 100, r["agg_pct"] * 100, ls=ls_, color=COULEURS_ANNEES[annee],
                lw=2 if annee in ANNEES_CLES else 1,
                label=f"{annee} {'stricte' if variante == VARIANTE_BASE else 'large'}")
ax.set_xlabel("Fuite ζ (% des dépôts)")
ax.set_ylabel("Baisse du crédit (%), UEMOA un seul bilan")
ax.set_title("S2c : réservoir stricte (plein) contre large (pointillé), λ = 0")
ax.legend(fontsize=8, ncol=2)
fig.tight_layout()
sauver_graphique(fig, "S2c_reservoir_stricte_large", "Scénario réservoir : stricte contre large, jusqu'à 60 % de fuite")

# ----------------------------------------------------------------------------
# SORTIE S3 : CARTE DE SENSIBILITÉ DU SEUIL
# EXPLICATION ÉCONOMIQUE
#   Question Q2 du mémoire : qu'est-ce qui protège le plus, un GROS RÉSERVOIR
#   (b, axe horizontal) ou un ROBINET DE RETOUR puissant (λ, axe vertical) ?
#   La couleur donne le seuil : plus c'est jaune, plus la fuite tolérable
#   est grande. Lecture : en se déplaçant vers le HAUT (plus de retour), le seuil
#   monte très vite (il double à λ = 0,5, triple à λ = 0,67...). En se déplaçant
#   vers la DROITE (plus de réservoir), il monte proportionnellement. La bande
#   verticale grisée = la zone des réservoirs observés pour l'UEMOA en 2021-2025.
#   Conclusion visuelle : le design de la MNBC (λ) pèse au moins autant que le
#   réservoir des banques.
# ----------------------------------------------------------------------------
bs = np.arange(0.0, 0.3001, 0.005)
ls = np.arange(0.0, 0.9001, 0.01)
BB, LL = np.meshgrid(bs, ls)
SS = BB / (1.0 - LL)
fig, ax = plt.subplots(figsize=(9, 6.5))
im = ax.imshow(np.minimum(SS, 0.6) * 100, origin="lower", aspect="auto",
               extent=[0, 30, 0, 0.9], cmap="viridis")
cs = ax.contour(bs * 100, ls, np.minimum(SS, 0.6) * 100, levels=[5, 10, 15, 20, 30], colors="white", linewidths=0.8)
ax.clabel(cs, fmt="%d %%", fontsize=8)
bmin, bmax = agregat["b_stricte"].min() * 100, agregat["b_stricte"].max() * 100
ax.axvspan(bmin, bmax, color="white", alpha=0.25)
ax.text((bmin + bmax) / 2, 0.84, "UEMOA\n2021-2025", ha="center", color="white", fontsize=9)
ax.grid(False)
ax.set_xlabel("Réservoir b (% des dépôts)")
ax.set_ylabel("Robinet de retour λ")
ax.set_title("S3 : seuil critique ζ* = b / (1 − λ)")
fig.colorbar(im, label="Seuil ζ* (% des dépôts, plafonné à 60 %)")
fig.tight_layout()
sauver_graphique(fig, "S3_carte_sensibilite", "Seuil selon le réservoir b et le robinet de retour λ")

# --- GRAPHIQUE S3b : EFFET DU ROBINET λ (SCÉNARIO "λ") ------------------------
# EXPLICATION ÉCONOMIQUE
#   On tourne le robinet de retour : λ = 0 (aucune aide) jusqu'à λ = 1 (la BCEAO
#   re-prête tout). Chaque valeur de λ DÉCALE le coude vers la droite : plus le
#   robinet est ouvert, plus la fuite tolérable est grande, et la pente
#   s'aplatit. À λ = 1, la courbe est collée à zéro. Lecture économique : la
#   politique de la banque centrale agit AUTANT que les caractéristiques des
#   banques.
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=True)
for ax, annee in zip(axes, [2023, 2025]):
    sous = calib[calib["annee"] == annee].reset_index(drop=True)
    for lam, couleur in zip(LAMBDAS_FINS, plt.cm.Blues(np.linspace(0.35, 0.95, len(LAMBDAS_FINS)))):
        r = calculer_union(sous, ZETAS, lam, PHI_BASE, VARIANTE_BASE)
        ax.plot(ZETAS * 100, r["agg_pct"] * 100, color=couleur, lw=2, label=f"λ = {lam:g}")
    ax.set_title(f"UEMOA un seul bilan, {annee}")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].set_ylabel("Baisse du crédit (%)")
axes[0].legend()
fig.suptitle("S3b : plus le robinet de retour est ouvert, plus le coude recule", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S3b_effet_lambda", "Scénario λ : courbes pour λ de 0 à 1")

# ----------------------------------------------------------------------------
# SORTIE S4 : PART DE L'UNION TOUCHÉE, QUI PORTE LA BAISSE
# EXPLICATION ÉCONOMIQUE
#   (S4) Pour chaque niveau de fuite, quelle part des dépôts de l'union se trouve
#   dans des pays DÉJÀ À SEC ? Courbe en escalier : chaque marche = un pays qui
#   franchit son seuil. Une marche haute = un gros pays qui craque (la Côte
#   d'Ivoire pèse ~41 % en 2025). C'est la réponse à Q3 : la moyenne dit
#   "tout va bien", l'escalier dit "attention, tel pays est déjà touché".
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5))
for annee in ANNEES:
    sous = calib[calib["annee"] == annee]
    seuils_k = seuil_critique(sous[VARIANTE_BASE].to_numpy(), 0.0)
    couverture = [(sous["poids"].to_numpy() * (z > seuils_k)).sum() for z in ZETAS]
    ax.step(ZETAS * 100, np.array(couverture) * 100, where="post",
            color=COULEURS_ANNEES[annee], lw=2 if annee in ANNEES_CLES else 1, label=str(annee))
ax.set_xlabel("Fuite ζ (% des dépôts)")
ax.set_ylabel("Part des dépôts de l'union dans des pays touchés (%)")
ax.set_title("S4 : part de l'union touchée (λ = 0, réservoir stricte)")
ax.legend(title="Année")
fig.tight_layout()
sauver_graphique(fig, "S4_part_union_touchee", "Escalier : part des dépôts de l'union dans des pays au-delà de leur seuil")

# --- GRAPHIQUE S4b : QUI PORTE LA BAISSE ? (HÉTÉROGÉNÉITÉ) -------------------
# EXPLICATION ÉCONOMIQUE
#   Pour une fuite donnée, chaque colonne empile ce que PERD CHAQUE PAYS, en
#   milliards de FCFA. On voit à la fois combien l'union perd au total (la
#   hauteur) ET qui paie la facture (les couleurs). En 2025, à 10 % de fuite,
#   seuls le Bénin et le Togo paient ; en 2023, six pays paient, la Côte d'Ivoire
#   en tête. Ça répond à "la moyenne cache-t-elle des pays ?" en montrant les
#   pays eux-mêmes.
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
coul_pays = dict(zip(PAYS, plt.cm.tab10(np.linspace(0, 1, 10))[:len(PAYS)]))
zs = [0.05, 0.08, 0.10, 0.15, 0.20]
for ax, annee in zip(axes, ANNEES_CLES):
    bas = np.zeros(len(zs))
    for pays in PAYS:
        vals = np.array([courbe(annee, pays, md=True)[idx_zeta(z)] for z in zs])
        ax.bar([f"{int(z * 100)} %" for z in zs], vals, bottom=bas, color=coul_pays[pays], label=pays)
        bas += vals
    ax.set_title(f"{annee} (λ = 0)")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].set_ylabel("Baisse du crédit (milliards de FCFA)")
axes[0].legend(fontsize=8, loc="upper left")
fig.suptitle("S4b : qui porte la baisse du crédit ? (réservoir stricte, φ = 1)", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S4b_qui_porte_la_baisse", "Barres empilées : contribution de chaque pays à la baisse (milliards FCFA)")

# --- GRAPHIQUE S4c : CARTE DE CHALEUR PAYS x FUITE (HÉTÉROGÉNÉITÉ) ------------
# EXPLICATION ÉCONOMIQUE
#   Chaque case = la baisse du crédit d'UN pays (en % de SON crédit) pour une
#   fuite donnée. Lecture en ligne : combien un pays résiste ; lecture en
#   colonne : qui souffre le plus pour une fuite donnée. Deux panneaux : 2023
#   (année de liquidité rare) et 2025 (année confortable). La moitié gauche
#   reste blanche : c'est la zone où personne ne bouge.
zs_c = [0.05, 0.08, 0.10, 0.12, 0.15, 0.20]
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), sharey=True)
for ax, annee in zip(axes, [2023, 2025]):
    mat = np.array([[courbe(annee, p)[idx_zeta(z)] * 100 for z in zs_c] for p in PAYS])
    im = ax.imshow(mat, cmap="Reds", aspect="auto", vmin=0, vmax=18)
    ax.set_xticks(range(len(zs_c)))
    ax.set_xticklabels([f"{int(z * 100)} %" for z in zs_c])
    ax.set_yticks(range(len(PAYS)))
    ax.set_yticklabels(PAYS)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, f"{mat[i, j]:.1f}", ha="center", va="center",
                    color="white" if mat[i, j] > 10 else "black", fontsize=9)
    ax.grid(False)
    ax.set_title(f"{annee} (λ = 0)")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
fig.colorbar(im, ax=axes, label="Baisse du crédit du pays (% de son crédit)", shrink=0.9)
fig.suptitle("S4c : pays par pays, qui souffre quand ? (réservoir stricte, φ = 1)", fontsize=12)
sauver_graphique(fig, "S4c_carte_pays_fuite", "Carte de chaleur : baisse du crédit de chaque pays selon la fuite")

# ----------------------------------------------------------------------------
# SORTIE S5 : RÈGLE DU PLAFOND DE DÉTENTION
# EXPLICATION ÉCONOMIQUE
#   La banque centrale peut limiter ce que chacun peut détenir en MNBC. Ça fixe
#   un PLAFOND : même si tout le monde voulait convertir, au maximum telle part
#   des dépôts peut partir. On compare ce plafond au seuil critique :
#       VERT  : plafond <= seuil du pays le plus fragile -> aucun pays touché,
#               le design suffit à protéger (même si les ménages se ruent).
#       ORANGE: plafond entre le seuil du pays le plus fragile et celui de la
#               moyenne -> certains pays sont touchés alors que la moyenne
#               paraît saine : la zone que la moyenne cache.
#       ROUGE : plafond au-dessus du seuil agrégé -> l'union est touchée.
#   On n'a pas de donnée fiable sur le nombre d'utilisateurs ni le plafond
#   individuel : on teste donc directement des plafonds de 2 à 20 % des dépôts.
# ----------------------------------------------------------------------------
lignes_s5 = []
for annee in ANNEES:
    for lam in LAMBDAS:
        _, smin, sagg = seuils_annee(annee, lam)
        for cap in PLAFONDS:
            code = 0 if cap <= smin else (1 if cap <= sagg else 2)
            lignes_s5.append([annee, lam, cap, smin, sagg, code,
                              ["Aucun pays touché", "Certains pays touchés", "Union touchée"][code]])
S5 = pd.DataFrame(lignes_s5, columns=["annee", "lambda", "plafond", "seuil_pays_fragile", "seuil_agrege", "code", "diagnostic"])
cmap = ListedColormap(["#2CA02C", "#FF7F0E", "#D62728"])
fig, axes = plt.subplots(1, len(LAMBDAS), figsize=(13, 4.2), sharey=True)
for j, lam in enumerate(LAMBDAS):
    mat = (S5[S5["lambda"] == lam].pivot(index="plafond", columns="annee", values="code")
           .sort_index(ascending=False))
    axes[j].imshow(mat.values, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    axes[j].set_xticks(range(len(mat.columns)))
    axes[j].set_xticklabels([str(c) for c in mat.columns])
    axes[j].set_yticks(range(len(mat.index)))
    axes[j].set_yticklabels([f"{int(c * 100)} %" for c in mat.index])
    axes[j].set_title(f"λ = {lam:g}")
    axes[j].grid(False)
    axes[j].set_xlabel("Année")
axes[0].set_ylabel("Plafond de détention (% des dépôts)")
fig.suptitle("S5 : vert = aucun pays touché | orange = certains pays | rouge = l'union", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S5_regle_plafond", "Diagnostic du plafond de détention : vert, orange, rouge")

# --- GRAPHIQUE S5b : LE PLAFOND SUR LA COURBE (SCÉNARIO "PLAFOND") -------------
# EXPLICATION ÉCONOMIQUE
#   On repose les plafonds (traits verticaux) sur les courbes de baisse du
#   crédit. Un plafond agit comme un MUR : la fuite ne peut pas aller au-delà.
#   On lit directement la perte maximale que ce mur laisse passer : le point où
#   le trait vertical coupe la courbe. Un mur à 2 % est loin à gauche du coude :
#   aucune perte. Un mur à 20 % laisse passer la partie la plus pentue.
fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
for ax, annee in zip(axes, [2023, 2025]):
    ax.plot(ZETAS * 100, courbe(annee, "UEMOA agrégé") * 100, color=COULEURS["agg"], lw=2, label="UEMOA un seul bilan")
    ax.plot(ZETAS * 100, courbe(annee, "UEMOA pays par pays") * 100, color=COULEURS["part"], lw=2, label="UEMOA 8 pays séparés")
    for cap in PLAFONDS:
        perte = courbe(annee, "UEMOA pays par pays")[idx_zeta(cap)] * 100
        ax.axvline(cap * 100, color="black", ls=":", lw=1)
        ax.text(cap * 100 + 0.3, 27, f"plafond {int(cap * 100)} %\nperte max {perte:.1f} %", fontsize=8, va="top")
    ax.set_title(f"{annee} (λ = 0)")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].set_ylabel("Baisse du crédit (%)")
axes[0].legend(loc="center left")
fig.suptitle("S5b : le plafond de détention agit comme un mur sur la fuite possible", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S5b_plafond_sur_courbe", "Scénario plafond : traits verticaux sur les courbes de baisse")

# ----------------------------------------------------------------------------
# SORTIE S6 : TEST DE ROBUSTESSE SUR PHI
# EXPLICATION ÉCONOMIQUE
#   phi est notre hypothèse la plus discutable : on a supposé que la banque
#   comble le manque ENTIÈREMENT en prêtant moins (phi = 1). En réalité elle
#   peut aussi relever ses taux de dépôt ou emprunter. Ce test montre que phi
#   change la PENTE (la gravité) mais PAS LE SEUIL : les trois courbes
#   décollent au même endroit. Le message du mémoire (à partir de quelle fuite
#   ça se passe) ne dépend donc pas de cette hypothèse fragile.
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=True)
for ax, annee in zip(axes, [2023, 2025]):
    for phi, style in zip(PHIS, [":", "--", "-"]):
        ax.plot(ZETAS * 100, courbe(annee, "UEMOA agrégé", phi=phi) * 100, ls=style,
                color=COULEURS["agg"], lw=2, label=f"φ = {phi:g}")
    s = float(seuil_critique(agregat.loc[annee, "b_stricte"], 0.0))
    ax.axvline(s * 100, color="black", lw=0.8)
    ax.text(s * 100 + 0.3, 1, f"seuil {pct(s)}", fontsize=9)
    ax.set_title(f"UEMOA agrégé, {annee}, λ = 0")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].set_ylabel("Baisse du crédit (%)")
axes[0].legend()
fig.suptitle("S6 : φ change la pente, pas le seuil", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S6_robustesse_phi", "Scénario φ : trois pentes, un seul seuil")

# ----------------------------------------------------------------------------
# SORTIE S7 : ZOOM CÔTE D'IVOIRE
# EXPLICATION ÉCONOMIQUE
#   La Côte d'Ivoire pèse ~41 % des dépôts de l'union (2025) : c'est le cas
#   d'étude. Le tableau donne, pour quelques fuites, la baisse du crédit en %
#   et en MILLIARDS de FCFA (un pourcentage seul ne dit pas l'enjeu). Il donne
#   aussi la fuite en % des DÉPÔTS À VUE : si seuls les dépôts à vue migrent
#   (les plus faciles à convertir), une fuite de 10 % de l'ensemble des dépôts
#   représente une part bien plus grande des dépôts à vue (environ 15 %).
#   Les deux graphiques : à gauche la baisse en % du crédit ivoirien, à droite
#   la même baisse en milliards de FCFA (l'enjeu réel).
# ----------------------------------------------------------------------------
lignes_s7 = []
for annee in ANNEES:
    ligne = calib[(calib["annee"] == annee) & (calib["pays"] == PAYS_ZOOM)].iloc[0]
    for lam in [0.0, 0.5]:
        for z in ZETAS_CLES:
            b = float(ligne[VARIANTE_BASE])
            p = float(baisse_credit_pct(z, lam, PHI_BASE, b, ligne["rho"]))
            lignes_s7.append([annee, lam, z, z / ligne["part_a_vue"], p, p * ligne["L"] / 1000.0])
S7 = pd.DataFrame(lignes_s7, columns=["annee", "lambda", "zeta", "zeta_en_part_depots_a_vue",
                                      "baisse_credit_pct", "baisse_credit_milliards_FCFA"])
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for annee in ANNEES:
    axes[0].plot(ZETAS * 100, courbe(annee, PAYS_ZOOM) * 100, color=COULEURS_ANNEES[annee],
                 lw=2 if annee in ANNEES_CLES else 1, label=str(annee))
    axes[1].plot(ZETAS * 100, courbe(annee, PAYS_ZOOM, md=True), color=COULEURS_ANNEES[annee],
                 lw=2 if annee in ANNEES_CLES else 1, label=str(annee))
axes[0].set_ylabel("Baisse du crédit ivoirien (%)")
axes[1].set_ylabel("Baisse du crédit ivoirien (milliards de FCFA)")
for ax in axes:
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].legend(title="Année")
fig.suptitle(f"S7 : {PAYS_ZOOM}, λ = 0, réservoir stricte", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S7_zoom_cote_ivoire", "Côte d'Ivoire : baisse du crédit en % et en milliards de FCFA")

# ----------------------------------------------------------------------------
# SORTIE S8 : FOURCHETTE 2021-2025
# EXPLICATION ÉCONOMIQUE
#   Le réservoir des banques change d'une année à l'autre (de 7,7 % en 2023 à
#   13,3 % en 2025 pour l'union) : il dépend du cycle de liquidité. Une MNBC
#   arriverait à une date inconnue. On ne donne donc pas UN chiffre mais une
#   BANDE : la baisse la plus faible et la plus forte observées sur 2021-2025.
#   C'est le résultat honnête : "entre x et y".
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=True)
lignes_s8 = []
for ax, lam in zip(axes, [0.0, 0.5]):
    for entite, couleur, nom in [("UEMOA agrégé", COULEURS["agg"], "UEMOA un seul bilan"),
                                 ("UEMOA pays par pays", COULEURS["part"], "UEMOA 8 pays séparés")]:
        pile = np.vstack([courbe(a, entite, lam) for a in ANNEES])
        bmin_, bmax_ = pile.min(axis=0), pile.max(axis=0)
        ax.fill_between(ZETAS * 100, bmin_ * 100, bmax_ * 100, color=couleur, alpha=0.3, label=nom)
        ax.plot(ZETAS * 100, bmax_ * 100, color=couleur, lw=1)
        ax.plot(ZETAS * 100, bmin_ * 100, color=couleur, lw=1)
        for z in ZETAS_CLES:
            lignes_s8.append([entite, lam, z, bmin_[idx_zeta(z)], bmax_[idx_zeta(z)]])
    ax.set_title(f"λ = {lam:g}")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].set_ylabel("Baisse du crédit (%)")
axes[0].legend()
fig.suptitle("S8 : bande des résultats sur 2021-2025 (φ = 1, réservoir stricte)", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S8_fourchette", "Bande min-max des courbes sur 2021-2025")
S8 = pd.DataFrame(lignes_s8, columns=["entite", "lambda", "zeta", "baisse_min", "baisse_max"])

# ----------------------------------------------------------------------------
# SORTIE S9 : CHIFFRES-CLÉS (PHRASES ET GRAPHIQUE)
# EXPLICATION ÉCONOMIQUE
#   Les résultats traduits en langage courant, prêts à être recopiés dans le
#   mémoire. Les montants sont en milliards de FCFA, et chaque chiffre donne sa
#   fourchette sur 2021-2025. Le graphique résume les phrases : pour quatre
#   niveaux de fuite, la perte de crédit de l'union (en milliards de FCFA,
#   pays par pays), avec le trait vertical = la fourchette sur 2021-2025.
#   Barres bleues : aucune aide de la BCEAO (λ = 0). Barres orange : la BCEAO
#   re-prête la moitié (λ = 0,5). La différence entre les deux couleurs est
#   la valeur de l'aide de la banque centrale.
# ----------------------------------------------------------------------------
phrases = []
seuil_agg = {a: seuils_annee(a, 0.0)[2] for a in ANNEES}
seuil_min = {a: seuils_annee(a, 0.0)[1] for a in ANNEES}
a_bas, a_haut = min(seuil_agg, key=seuil_agg.get), max(seuil_agg, key=seuil_agg.get)
phrases.append(f"Sans aide de la BCEAO (λ = 0), le seuil critique de l'UEMOA va de {pct(seuil_agg[a_bas])} "
               f"({a_bas}) à {pct(seuil_agg[a_haut])} ({a_haut}) des dépôts, en le voyant comme un seul bilan.")
pf_bas = min(seuil_min, key=seuil_min.get)
pf_haut = max(seuil_min, key=seuil_min.get)
phrases.append(f"Le pays le plus fragile craque bien plus tôt : de {pct(seuil_min[pf_bas])} ({pf_bas}) "
               f"à {pct(seuil_min[pf_haut])} ({pf_haut}) des dépôts.")
zs9 = [0.05, 0.10, 0.15, 0.20]
donnees_s9 = {}
for lam in [0.0, 0.5]:
    for z in zs9:
        i = idx_zeta(z)
        agg_ = [courbe(a, "UEMOA agrégé", lam)[i] for a in ANNEES]
        part_ = [courbe(a, "UEMOA pays par pays", lam)[i] for a in ANNEES]
        md_ = [courbe(a, "UEMOA pays par pays", lam, md=True)[i] for a in ANNEES]
        nb = [int((z > seuils_annee(a, lam)[0]).sum()) for a in ANNEES]
        donnees_s9[(lam, z)] = (min(md_), float(np.mean(md_)), max(md_))
        phrases.append(
            f"Si {pct(z, 0)} des dépôts partent et que {pct(lam, 0)} reviennent (λ = {f'{lam:g}'.replace('.', ',')}) : "
            f"en un seul bilan le crédit baisse de {pct(min(agg_))} à {pct(max(agg_))} ; "
            f"pays par pays, de {pct(min(part_))} à {pct(max(part_))}, "
            f"soit {milliards(min(md_))} à {milliards(max(md_))} milliards de FCFA ; "
            f"{min(nb)} à {max(nb)} pays sur 8 sont au-delà de leur seuil.")
phrases.append("Si λ = 1 (la BCEAO re-prête tout ce qui sort), le crédit ne baisse jamais : c'est la neutralité.")
S9 = pd.DataFrame({"Phrase": phrases})
print("\nSORTIE S9 : chiffres-clés")
for ph in phrases:
    print("  -", ph)

fig, ax = plt.subplots(figsize=(10, 5.5))
largeur = 0.38
x = np.arange(len(zs9))
for k, (lam, couleur, nom) in enumerate([(0.0, COULEURS["agg"], "λ = 0 (aucune aide)"),
                                         (0.5, "#FF7F0E", "λ = 0,5 (la BCEAO re-prête la moitié)")]):
    moy = np.array([donnees_s9[(lam, z)][1] for z in zs9])
    mn = np.array([donnees_s9[(lam, z)][0] for z in zs9])
    mx = np.array([donnees_s9[(lam, z)][2] for z in zs9])
    ax.bar(x + (k - 0.5) * largeur, moy, largeur, color=couleur, label=nom,
           yerr=[moy - mn, mx - moy], capsize=4, ecolor="black")
ax.set_xticks(x)
ax.set_xticklabels([f"{int(z * 100)} %" for z in zs9])
ax.set_xlabel("Fuite ζ (% des dépôts)")
ax.set_ylabel("Baisse du crédit de l'union (milliards de FCFA)")
ax.set_title("S9 : chiffres-clés (barre = moyenne 2021-2025, trait = min-max selon l'année)")
ax.legend()
fig.tight_layout()
sauver_graphique(fig, "S9_chiffres_cles", "Perte de crédit de l'union selon la fuite, avec et sans aide de la BCEAO")

# ----------------------------------------------------------------------------
# SORTIE S10 : ROBUSTESSE À L'ERREUR DE MESURE DU RÉSERVOIR
# EXPLICATION ÉCONOMIQUE
#   La faiblesse la plus probable de ce travail : on ne sait pas mesurer PARFAITEMENT
#   le réservoir. Nos "comptes ordinaires débiteurs" incluent des avoirs
#   étrangers et interbancaires qui ne sont pas de la vraie monnaie de banque
#   centrale. Notre mesure est donc probablement TROP HAUTE. Pour voir si les
#   conclusions tiennent, on rejoue tout avec un vrai réservoir égal à notre
#   mesure multipliée par un coefficient kappa :
#       kappa = 0,5  : notre mesure est trop haute de moitié (cas pessimiste)
#       kappa = 0,75 : trop haute d'un quart
#       kappa = 1    : notre mesure est juste (cas de base)
#       kappa = 1,25 : trop basse d'un quart (titres achetés par des non-banques)
#   Comme le seuil vaut κ x b / (1 - λ), il bouge EXACTEMENT proportionnellement
#   à kappa : un réservoir surestimé de moitié divise tous les seuils par 2.
#
#   Trois graphiques :
#     S10a : comment les seuils se déplacent quand kappa change.
#     S10b : comment les courbes de baisse du crédit se déplacent.
#     S10c : si le plafond de détention de 5 % ou 10 % résiste à cette erreur.
#   Et un tableau : la MARGE DE SÉCURITÉ de chaque plafond = de combien on peut
#   s'être trompé sur le réservoir avant que le plafond cesse de protéger.
# ----------------------------------------------------------------------------
# --- S10a : seuils selon kappa ----------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5))
lignes_s10 = []
for annee in ANNEES:
    agg_k, min_k = [], []
    for kappa in KAPPAS:
        _, smin, sagg = seuils_annee(annee, 0.0, VARIANTE_BASE, kappa)
        agg_k.append(sagg)
        min_k.append(smin)
        lignes_s10.append([annee, kappa, sagg, smin])
    ax.plot(KAPPAS, np.array(agg_k) * 100, color=COULEURS_ANNEES[annee], lw=2 if annee in ANNEES_CLES else 1,
            marker="o", label=f"{annee} union (un seul bilan)")
    ax.plot(KAPPAS, np.array(min_k) * 100, color=COULEURS_ANNEES[annee], lw=2 if annee in ANNEES_CLES else 1,
            marker="s", ls="--", label=f"{annee} pays le plus fragile")
for cap in [0.05, 0.10]:
    ax.axhline(cap * 100, color="black", ls=":", lw=1)
    ax.text(1.255, cap * 100, f"plafond {int(cap * 100)} %", fontsize=8, va="center")
ax.axvline(1.0, color="grey", lw=0.8)
ax.set_xticks(KAPPAS)
ax.set_xlabel("κ : vrai réservoir / réservoir mesuré (0,5 = notre mesure est trop haute de moitié)")
ax.set_ylabel("Seuil critique ζ* (% des dépôts), λ = 0")
ax.set_title("S10a : les seuils bougent proportionnellement à l'erreur de mesure")
ax.legend(fontsize=7, ncol=2)
fig.tight_layout()
sauver_graphique(fig, "S10a_seuils_selon_kappa", "Seuils selon l'erreur de mesure du réservoir")
S10 = pd.DataFrame(lignes_s10, columns=["annee", "kappa", "seuil_agrege", "seuil_pays_fragile"])

# --- S10b : courbes selon kappa ---------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
couleurs_k = dict(zip(KAPPAS, ["#D62728", "#FF7F0E", "#1F77B4", "#2CA02C"]))
for ax, annee in zip(axes, [2023, 2025]):
    sous = calib[calib["annee"] == annee].reset_index(drop=True)
    for kappa in KAPPAS:
        sk = sous.copy()
        sk[VARIANTE_BASE] = sk[VARIANTE_BASE] * kappa
        r = calculer_union(sk, ZETAS, 0.0, PHI_BASE, VARIANTE_BASE)
        ax.plot(ZETAS * 100, r["agg_pct"] * 100, color=couleurs_k[kappa], lw=2, label=f"κ = {kappa:g} : un seul bilan")
        ax.plot(ZETAS * 100, r["part_pct"] * 100, color=couleurs_k[kappa], lw=1.3, ls="--", label=f"κ = {kappa:g} : 8 pays")
    ax.set_title(f"{annee} (λ = 0)")
    ax.set_xlabel("Fuite ζ (% des dépôts)")
axes[0].set_ylabel("Baisse du crédit (%)")
axes[0].legend(fontsize=7, ncol=2, loc="upper left")
fig.suptitle("S10b : si le réservoir est surestimé (κ < 1), le coude recule vers la gauche", fontsize=12)
fig.tight_layout()
sauver_graphique(fig, "S10b_courbes_selon_kappa", "Courbes de baisse du crédit selon l'erreur de mesure")

# --- S10c : le plafond résiste-t-il à l'erreur ? -----------------------------
lignes_s10c = []
for annee in ANNEES:
    for kappa in KAPPAS:
        _, smin, sagg = seuils_annee(annee, 0.0, VARIANTE_BASE, kappa)
        for cap in PLAFONDS:
            code = 0 if cap <= smin else (1 if cap <= sagg else 2)
            lignes_s10c.append([annee, kappa, cap, code])
S10c = pd.DataFrame(lignes_s10c, columns=["annee", "kappa", "plafond", "code"])
fig, axes = plt.subplots(1, 2, figsize=(12, 4.2), sharey=True)
for ax, cap in zip(axes, [0.05, 0.10]):
    mat = (S10c[S10c["plafond"] == cap].pivot(index="kappa", columns="annee", values="code")
           .sort_index(ascending=False))
    ax.imshow(mat.values, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(range(len(mat.columns)))
    ax.set_xticklabels([str(c) for c in mat.columns])
    ax.set_yticks(range(len(mat.index)))
    ax.set_yticklabels([f"κ = {k:g}" for k in mat.index])
    ax.grid(False)
    ax.set_title(f"Plafond de {int(cap * 100)} % (λ = 0)")
    ax.set_xlabel("Année")
fig.suptitle("S10c : le plafond protège-t-il si le réservoir est mal mesuré ? "
             "(vert = aucun pays touché | orange = certains | rouge = l'union)", fontsize=10)
fig.tight_layout()
sauver_graphique(fig, "S10c_plafond_selon_kappa", "Le plafond de 5 % et 10 % résiste-t-il à l'erreur de mesure ?")

# --- S10 : table de la marge de sécurité --------------------------------------
# MARGE DE SÉCURITÉ d'un plafond = de combien on peut avoir SURESTIMÉ le
# réservoir du pays le plus fragile avant que le plafond cesse de protéger.
# Exemple : seuil du pays fragile = 4 %, plafond = 2 % -> on peut s'être trompé
# de 50 % (le vrai réservoir peut être la moitié de notre mesure) et le plafond
# protège encore. Marge négative : le plafond ne protège déjà plus.
lignes_marge = []
for annee in ANNEES:
    _, smin, _ = seuils_annee(annee, 0.0)
    for cap in PLAFONDS:
        lignes_marge.append([annee, cap, smin, 1.0 - cap / smin])
S10_marges = pd.DataFrame(lignes_marge, columns=["annee", "plafond", "seuil_pays_fragile",
                                                 "surestimation_tolerable_du_reservoir"])
print("\nSORTIE S10 : marge de sécurité (surestimation tolérable du réservoir, en %, négatif = ne protège déjà plus)")
print((S10_marges.pivot(index="plafond", columns="annee", values="surestimation_tolerable_du_reservoir") * 100).round(0).to_string())

# ----------------------------------------------------------------------------
# GARDE-FOUS SUPPLÉMENTAIRES (SORTIE S10)
# ----------------------------------------------------------------------------
# GARDE-FOU G9 : kappa = 1 redonne exactement le cas de base
# IMAGE : si on dit "notre mesure est exacte", on doit retomber sur les
# résultats déjà calculés. Si le test de robustesse change le cas de base alors
# qu'on n'a rien changé, il est mal branché.
ok9 = True
for annee in ANNEES:
    sous = calib[calib["annee"] == annee].reset_index(drop=True)
    sk = sous.copy()
    sk[VARIANTE_BASE] = sk[VARIANTE_BASE] * 1.0
    r = calculer_union(sk, ZETAS, 0.0, PHI_BASE, VARIANTE_BASE)
    ok9 &= bool(np.allclose(r["agg_pct"], courbe(annee, "UEMOA agrégé")))
    ok9 &= bool(np.allclose(r["part_pct"], courbe(annee, "UEMOA pays par pays")))
garde_fou("G9", "κ = 1 redonne exactement le cas de base", ok9,
          "Sans erreur de mesure, le test de robustesse ne change rien.")

# GARDE-FOU G10 : le seuil est proportionnel à kappa
# IMAGE : si le réservoir réel est la moitié de ce qu'on croyait, le seuil
# est la moitié aussi (ni plus, ni moins). C'est une règle de trois : si la
# courbe ne la respecte pas, la formule est faussée.
ok10 = True
for annee in ANNEES:
    for kappa in KAPPAS:
        _, smin1, sagg1 = seuils_annee(annee, 0.0, VARIANTE_BASE, 1.0)
        _, smink, saggk = seuils_annee(annee, 0.0, VARIANTE_BASE, kappa)
        ok10 &= abs(smink - kappa * smin1) < 1e-12 and abs(saggk - kappa * sagg1) < 1e-12
garde_fou("G10", "le seuil est proportionnel à κ (règle de trois)", ok10,
          "Réservoir réel = moitié de la mesure -> seuil = moitié du seuil.")

# %% ==========================================================================
# ÉCRITURE DU CLASSEUR DE RÉSULTATS ET DERNIER TEST
# =============================================================================
fichier_sortie = DOSSIER_SORTIES / "Resultats_simulation.xlsx"

# GARDE-FOU G11 : tous les graphiques promis existent bien
# IMAGE : un restaurant qui annonce 25 plats doit les avoir tous en cuisine.
# Le code vérifie que chaque graphique annoncé en tête de fichier a bien été
# enregistré sur le disque.
ATTENDUS = ["S0_carte_reservoirs", "S1_seuils_par_pays", "S2_courbes_contraction", "S2b_courbes_par_pays",
            "S2c_reservoir_stricte_large", "S3_carte_sensibilite", "S3b_effet_lambda", "S4_part_union_touchee",
            "S4b_qui_porte_la_baisse", "S4c_carte_pays_fuite", "S5_regle_plafond", "S5b_plafond_sur_courbe",
            "S6_robustesse_phi", "S7_zoom_cote_ivoire", "S8_fourchette", "S9_chiffres_cles",
            "S10a_seuils_selon_kappa", "S10b_courbes_selon_kappa", "S10c_plafond_selon_kappa"]
garde_fou("G11", f"les {len(ATTENDUS)} graphiques annoncés existent tous",
          all((DOSSIER_GRAPHS / f"{n}.png").exists() for n in ATTENDUS),
          "Chaque sortie promise a bien son image.")

with pd.ExcelWriter(fichier_sortie, engine="openpyxl") as w:
    pd.DataFrame({"Contenu": [
        "S0_Calibration : réservoir b stricte (% des dépôts) par pays et année",
        "S1_Seuils : seuil critique par pays, année, λ et réservoir ('illimité' si λ = 1)",
        "S5_Plafond : diagnostic du plafond de détention",
        "S7_Zoom_CI : Côte d'Ivoire, baisse en % et en milliards de FCFA",
        "S8_Fourchette : bande min-max sur 2021-2025",
        "S9_Chiffres_cles : phrases prêtes à l'emploi",
        "S10_Seuils_kappa, S10_Marges, S10_Plafond_kappa : robustesse à l'erreur de mesure",
        "Garde_fous : résultat des tests de sécurité",
        "Index_graphiques : la liste des graphiques et ce qu'ils montrent",
        "Les images sont dans le dossier Graphiques/"]}).to_excel(w, sheet_name="Lisez-moi", index=False)
    S0.to_excel(w, sheet_name="S0_Calibration")
    S1_affiche.to_excel(w, sheet_name="S1_Seuils", index=False)
    S5.to_excel(w, sheet_name="S5_Plafond", index=False)
    S7.to_excel(w, sheet_name="S7_Zoom_CI", index=False)
    S8.to_excel(w, sheet_name="S8_Fourchette", index=False)
    S9.to_excel(w, sheet_name="S9_Chiffres_cles", index=False)
    S10.to_excel(w, sheet_name="S10_Seuils_kappa", index=False)
    S10_marges.to_excel(w, sheet_name="S10_Marges", index=False)
    S10c.to_excel(w, sheet_name="S10_Plafond_kappa", index=False)
    pd.DataFrame(journal_garde_fous).to_excel(w, sheet_name="Garde_fous", index=False)
    pd.DataFrame({"Fichier": [f"{k}.png" for k in GRAPHIQUES_PRODUITS],
                  "Ce qu'il montre": list(GRAPHIQUES_PRODUITS.values())}).to_excel(
        w, sheet_name="Index_graphiques", index=False)
    for feuille in w.sheets.values():
        for col in feuille.columns:
            feuille.column_dimensions[col[0].column_letter].width = 28

print(f"\n   Garde-fous passés : {sum(j['Statut'] == 'OK' for j in journal_garde_fous)}/{len(journal_garde_fous)}")
print(f"   {len(GRAPHIQUES_PRODUITS)} graphiques produits.")
print(f"   -> classeur enregistré : {fichier_sortie.name}")
print("\nTERMINÉ. Résultats dans :", DOSSIER_SORTIES)