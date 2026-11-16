# DOCUMENTATION OFFICIELLE — DATA CHALLENGE BURKINA 2026
## ÉDITION ÉDUCATION | DÉFI 2 : DISPARITÉS D'ACCÈS À L'ÉDUCATION

> **Épigraphe :**  
> *« On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo*

---

**Code et Nom de l'Équipe :** TEAMDATALYS  
**Composition de l'Équipe (2 personnes) :**
- **Membre 1 :** Data Engineer & Data Analyst
- **Membre 2 :** Data Architect & Data Scientist  
**Défi Choisi :** DÉFI 2 — Analyse des disparités d'accès à l'école (parité fille-garçon, écart urbain-rural)  
**Date de finalisation :** 15 novembre 2026 (Dépôt officiel avant la clôture du 18 novembre 2026)  
**Volume de documentation :** 14 pages équivalentes (Strictement conforme au plafond de 15 pages)

---

# TABLE DES MATIÈRES

1. **SECTION 1 : LE DÉFI (1 page)** ........................................................................ Page 2
   - 1.1 Contexte et question officielle
   - 1.2 Notre angle différenciant : la parité dans les deux sens
   - 1.3 Objectifs opérationnels et impact attendu

2. **SECTION 2 : LES DONNÉES (2 pages)** ................................................................... Page 3
   - 2.1 Description du corpus statistique DGESS (2015-2025)
   - 2.2 Référentiels géographiques et données d'appui
   - 2.3 Tri raisonné du DataPack et tableau des sources

3. **SECTION 3 : LA PRÉPARATION DES DONNÉES (2-3 pages)** ................................................ Page 5
   - 3.1 Détection et traitement des pièges de qualité
   - 3.2 Résorption des cellules fusionnées et détection des sous-totaux
   - 3.3 Normalisation des 13 régions et des années scolaires
   - 3.4 Contrôles arithmétiques et journal d'audit

4. **SECTION 4 : LA MÉTHODE ANALYTIQUE ET ARCHITECTURE (3 pages)** ...................................... Page 7
   - 4.1 Architecture du parcours de données et schéma relationnel
   - 4.2 Distinguo méthodologique : Ratio d'inscrits vs IPS officiel
   - 4.3 Cadre normatif UNESCO de parité bidirectionnelle
   - 4.4 Modélisation des pentes temporelles et test de $\sigma$-convergence

5. **SECTION 5 : LES RÉSULTATS EMPIRIQUES (3 pages)** ..................................................... Page 10
   - 5.1 Cartographie des disparités régionales et double lecture du genre
   - 5.2 Rattrapage historique du milieu rural national
   - 5.3 Démonstration de la $\sigma$-convergence interrégionale
   - 5.4 Analyse exploratoire des facteurs associés et hypothèse orpaillage

6. **SECTION 6 : LA RÉPONSE AU DÉFI ET RECOMMANDATIONS (1-2 pages)** .................................... Page 12
   - 6.1 Synthèse de la réponse au Défi 2
   - 6.2 Recommandations d'action publique ciblées par profil de région
   - 6.3 Outil d'aide à la décision : Fiche régionale opérationnelle

7. **SECTION 7 : LA REPRODUCTION ET ENCADREMENT ÉTHIQUE (1 page)** ...................................... Page 14
   - 7.1 Guide de réexécution de la solution interactive locale
   - 7.2 Synthèse des limites scientifiques formelles
   - 7.3 Encart de traçabilité : Usage raisonné et critique de l'IA

---

\newpage

# SECTION 1 : LE DÉFI (1 page)

### 1.1 Contexte national et question officielle
L'éducation constitue le socle du développement humain et de la souveraineté économique du Burkina Faso. Comme le rappelait l'illustre historien et pédagogue burkinabè Joseph Ki-Zerbo dans son plaidoyer fondateur : *« On ne développe pas, on se développe »*. L'accès universel et équitable à l'école demeure toutefois confronté à de profondes asymétries territoriales et de genre, exacerbées au cours de la dernière décennie par des chocs sécuritaires majeurs, des déplacements internes de populations et des dynamiques économiques locales contrastées.

Le **DÉFI 2** du Data Challenge Burkina 2026 pose une interrogation centrale et concrète aux analystes de données :
> *« Où les écarts d'accès à l'école sont-ils les plus grands (filles-garçons, ville-campagne) et comment évoluent-ils ? »*

### 1.2 Notre angle différenciant : La parité dans les deux sens
La plupart des travaux d'évaluation réduisent la question du genre à la dénonciation du déficit d'accès des filles. Or, l'analyse minutieuse des données statistiques du primaire burkinabè révèle une réalité plus complexe et nuancée que **Team Datalys** a choisi de placer au cœur de son analyse : **l'inégalité dans les deux sens**.
- Dans certaines régions du Burkina Faso, ce sont effectivement les **filles qui sont sévèrement défavorisées** ($IPS < 0{,}97$).
- Dans d'autres régions, à l'inverse, ce sont les **garçons qui sont défavorisés** ($IPS > 1{,}03$), subissant un décrochage scolaire précoce au profit d'activités rémunératrices informelles, notamment l'orpaillage artisanal.

Cet angle est systématiquement croisé avec l'évolution de la fracture entre le **milieu urbain** et le **milieu rural** sur dix cohortes scolaires complètes (2015/2016 à 2024/2025).

### 1.3 Objectifs opérationnels et impact attendu
Notre travail ne vise pas une simple description statistique rétrospective, mais la livraison d'un **outil d'aide à la décision publique territoriale**. Nos objectifs opérationnels sont triples :
1. **Mesurer et cartographier** sans ambiguïté les poches régionales d'inégalité selon les normes internationales de l'UNESCO.
2. **Fournir un outil de pilotage interactif réexécutable** permettant à un directeur régional ou à un planificateur ministériel de visualiser immédiatement les déficits de sa circonscription.
3. **Formuler des recommandations différenciées par profil de territoire** pour éviter l'inefficacité des politiques nationales uniformes.

---

\newpage

# SECTION 2 : LES DONNÉES (2 pages)

### 2.1 Description du corpus statistique principal (DGESS / MENAPLN)
L'analyse empirique repose au premier chef sur le fichier statistique officiel mis à disposition par la Direction Générale des Études et des Statistiques Sectorielles (DGESS) du Ministère de l'Éducation Nationale, de l'Alphabétisation et de la Promotion des Langues Nationales (MENAPLN) : `DONNEES_STATISTQUES_ PRESCOLAIRE ET PRIMAIRE_2016_2025_DCB.xlsx`.

Ce classeur de 100 968 octets structure en 14 feuilles de calcul une série administrative continue couvrant dix années scolaires (2015/2016 à 2024/2025) :
- `PRESCOLAIRE` : Évolution des effectifs préscolaires par sexe, statut, milieu et région (235 lignes $\times$ 32 colonnes).
- `Feuil1` : Effectifs du primaire ventilés par région et sexe sur 10 ans (67 lignes $\times$ 12 colonnes).
- `Feuil2` : Effectifs du primaire ventilés par statut (Public, Privé) et sexe (70 lignes $\times$ 12 colonnes).
- `Feuil3` : Effectifs du primaire ventilés par milieu (**URBAIN, RURAL, NATIONAL**) et sexe (96 lignes $\times$ 12 colonnes).
- `Feuil4` : Effectifs du primaire ventilés par niveau (CP1 à CM2), statut et sexe (113 lignes $\times$ 13 colonnes).
- `Feuil6`, `Feuil7`, `Feuil8` : Taux Bruts officiels (Taux Brut d'Admission TBA, Taux Brut de Scolarisation TBS, Taux d'Achèvement du Primaire TAP) ventilés par sexe (Garçons, Filles, Total) et région.
- `Feuil10`, `Feuil11`, `Feuil12` : Indices de Parité des Sexes (IPS) officiels calculés par la DGESS pour le TBA, le TBS et le TAP.
- `Feuil9` : Taux de réussite à l'examen du Certificat d'Études Primaires (CEP) par région et sexe (2016 à 2025).
- `Feuil13` : Nombre d'écoles primaires réparties par région et statut (Public, Privé, Total).

### 2.2 Données auxiliaires et référentiels géographiques
Pour géoréférencer et contextualiser les statistiques scolaires, Team Datalys a mobilisé deux sources d'appui issues du DataPack officiel :
1. **Limites administratives COD-AB / OCHA** (`bfa_admin1.csv`) : Référentiel des limites régionales du Burkina Faso, fournissant la table de correspondance essentielle entre les 13 anciennes régions statistiques et les 17 nouvelles entités administratives issues du découpage de 2024/2025.
2. **Séries longues Banque Mondiale / UNESCO** (`education_bfa.csv`) : Base de données internationale permettant d'adosser l'analyse à l'historique macroéconomique de la scolarisation au Burkina Faso depuis 2007.

### 2.3 Tri raisonné du DataPack et tableau des sources
Conformément aux instructions des organisateurs exigeant de concentrer les dépôts sur les données utiles au défi choisi, Team Datalys a audité les 345 fichiers du DataPack et formalisé leur statut dans la table de référence `TEAMDATALYS_01-collecte_D2_architect_ref-sources_v1.csv` :

| ID Source | Producteur | Publication & Millésime | Fichier brut déposé | Rôle / Statut Défi 2 |
|---|---|---|---|:---:|
| **SRC-01** | DGESS / MENAPLN | Statistiques préscolaire & primaire 2016-2025 (2026) | `..._dgess-prescolaire-primaire-brut_v1.xlsx` | **RETENU** (Cœur empirique) |
| **SRC-02** | COD-AB / OCHA | Burkina Faso Administrative Boundaries v03 (2025) | `..._sig-admin1-limites-brut_v1.csv` | **RETENU** (Pivot spatial SIG) |
| **SRC-03** | BM / UNESCO UIS | World Development Indicators - Education BFA (2024) | `..._unesco-bm-education-long-terme-brut_v1.csv` | **RETENU** (Cadrage macro) |
| **SRC-04** | DGESS / MENAPLN | Annuaire post-primaire et secondaire 2019-2020 (2020) | `..._post-primaire-2019-2020-brut_v1.csv` | **RETENU** (Mention contextuelle) |
| **SRC-05** | INSD (RGPH 2019) | Projections démographiques 2020-2035 (2022) | N/A (DataPack) | **ÉCARTÉ** (Format PDF non tabulaire) |
| **SRC-06** | INSD / ICF | Enquête Démographique et de Santé EDS 2021 (2022) | N/A (DataPack) | **ÉCARTÉ** (Données transversales) |
| **SRC-07** | CONASUR | Rapports PDI 2020-2021 (2021) | N/A (DataPack) | **ÉCARTÉ** (Couverture 2 ans incomplète) |
| **SRC-08** | Secteur Minier | Registre géolocalisé d'orpaillage artisanal | *NON TROUVÉ DANS LE DATAPACK* | **ÉCARTÉ** (Traitement qualitatif) |

---

\newpage

# SECTION 3 : LA PRÉPARATION DES DONNÉES (2-3 pages)

### 3.1 Détection et typologie des pièges de qualité
L'audit approfondi du classeur source brut a mis en lumière cinq anomalies structurelles majeures qui auraient irrémédiablement faussé les calculs statistiques si un nettoyage rigoureux n'avait pas été opéré :
1. **Les fusions de cellules verticales (faux NaN)** : Dans les feuilles `Feuil1`, `Feuil3`, `Feuil9`, `Feuil13`, le nom de l'entité géographique ou du milieu n'est renseigné que sur la première ligne d'un bloc de trois (Garçons), laissant les lignes suivantes (Filles, Total) sous forme de cellules vides (`None` sous Python).
2. **Le mélange de sous-totaux et de totaux nationaux** : La ligne `NATIONAL` ou `Total général` est imbriquée au sein des mêmes colonnes que les 13 régions. Une agrégation brute sans filtrage aurait doublé la population scolaire nationale.
3. **L'hétérogénéité des formats temporels** : Trois conventions coexistent dans le même classeur : `2015-2016` (Feuil1), `2015/16` ou `2015-16` (Feuil6 à 12), `2016` (PRESCOLAIRE et Feuil9), et `2015/2016` (Feuil13).
4. **Variations orthographiques régionales** : Présence de tirets ou d'espaces (`PLATEAU CENTRAL` vs `PLATEAU-CENTRAL`).
5. **Notes textuelles de traçabilité dans les cellules de données** : La cellule d'en-tête `2018-2019` de `Feuil1` et la colonne `2017` de `Feuil6` contenaient une note de consigne institutionnelle de plusieurs paragraphes incrustée directement dans le libellé de colonne.

### 3.2 Pipeline de nettoyage et algorithmes mis en œuvre
Pour garantir une traçabilité totale et le respect de la règle « aucune correction silencieuse », Team Datalys a conçu le script modulaire `TEAMDATALYS_02-nettoyage_D2_engineer_utils-nettoyage_v1.py` et le programme de nettoyage `scripts/etape2_nettoyage.py` :

```python
# Extrait du traitement de forward-fill contrôlé (Feuil1)
current_region = None
for r in range(3, 45):
    c1 = ws1.cell(r, 1).value
    if c1 is not None and str(c1).strip() != "":
        current_region = normaliser_region(c1) # Standardisation canonique
    # Le libellé canonique est propagé de manière déterministe sur les lignes Filles et Total
```

- **Propagation déterministe (*Forward-fill*)** : Application d'un algorithme propageant le nom de la région uniquement sur les deux cellules sous-jacentes strictement associées (Garçons $\rightarrow$ Filles $\rightarrow$ Total).
- **Isolation des lignes de contrôle** : Extraction des lignes `NATIONAL`, `Burkina Faso` et `Total général` dans un fichier dédié `TEAMDATALYS_02-nettoyage_D2_engineer_totaux-officiels-controle_v1.csv` pour servir de référence de vérification documentaire.
- **Normalisation temporelle unifiée** : Conversion systématique de toutes les expressions d'années scolaires vers le standard `AAAA-AAAA` (début et fin d'année scolaire).
- **Standardisation des 13 régions canoniques** : Mapping exhaustif des variantes typographiques vers un référentiel à 13 régions en majuscules avec tirets normalisés.

### 3.3 Contrôles automatiques d'intégrité et journal d'audit
Chaque table produite dans `02_nettoyage/` a été soumise à une série de tests d'assertions arithmétiques bloquantes :
- **Règle 1 :** $\text{Effectif Total} = \text{Effectif Garçons} + \text{Effectif Filles}$ (130 lignes régionales et 20 lignes milieu contrôlées, 0 écart).
- **Règle 2 :** $\text{Écoles Total} = \text{Écoles Public} + \text{Écoles Privé}$ (130 lignes contrôlées, 0 écart).
- **Règle 3 :** $\sum_{i=1}^{13} \text{Effectif Région}_i = \text{Total National Officiel}$ (Vérifié sur les 10 années scolaires, divergence nulle).
- **Règle 4 :** $\text{Effectif Urbain} + \text{Effectif Rural} = \text{Total National Officiel}$ (Vérifié sur les 10 années, exactitude parfaite).

Toutes ces opérations sont consignées ligne par ligne dans le livrable d'ingénierie `TEAMDATALYS_02-nettoyage_D2_engineer_journal-nettoyage_v1.md`.

---

\newpage

# SECTION 4 : LA MÉTHODE ANALYTIQUE ET ARCHITECTURE (3 pages)

### 4.1 Architecture du parcours de données et schéma relationnel
L'architecture technique repose sur un modèle de données en étoile déployable sur PostgreSQL (`TEAMDATALYS_03-transformation_D2_architect_schema-donnees_v2.sql`). Le schéma sépare rigoureusement les dimensions géographiques et temporelles des tables de faits analytiques :

```sql
-- Extrait du schéma relationnel PostgreSQL (03_transformation)
CREATE TABLE fait_education_regionale (
    id_fait                 SERIAL PRIMARY KEY,
    code_region_13          VARCHAR(10) REFERENCES ref_region(code_region_13),
    annee_scolaire          VARCHAR(9) REFERENCES ref_annee_scolaire(annee_scolaire),
    primaire_garcons        INTEGER NOT NULL CHECK (primaire_garcons >= 0),
    primaire_filles         INTEGER NOT NULL CHECK (primaire_filles >= 0),
    primaire_total          INTEGER NOT NULL CHECK (primaire_total = primaire_garcons + primaire_filles),
    primaire_ratio_f_g      NUMERIC(6,4),
    profil_parite_effectifs VARCHAR(30) NOT NULL,
    ips_tbs                 NUMERIC(6,4),
    profil_parite_tbs       VARCHAR(30) NOT NULL,
    eleves_par_ecole        NUMERIC(6,1),
    CONSTRAINT uq_region_annee UNIQUE (code_region_13, annee_scolaire)
);
```

### 4.2 Distinguo méthodologique fondamental : Ratio d'inscrits vs IPS officiel du TBS
Une contribution analytique essentielle de Team Datalys consiste à dissiper une confusion fréquente dans le débat public entre :
1. **Le ratio des effectifs scolarisés ($Ratio_{F/G}$)** :
   $$Ratio_{F/G} = \frac{\text{Effectif Filles présentes à l'école}}{\text{Effectif Garçons présents à l'école}}$$
2. **L'Indice de Parité des Sexes officiel du TBS ($IPS_{TBS}$)** :
   $$IPS_{TBS} = \frac{TBS_{Filles}}{TBS_{Garçons}} = \frac{\text{Effectif Filles} / \text{Population Filles (6-11 ans)}}{\text{Effectif Garçons} / \text{Population Garçons (6-11 ans)}}$$

*Démonstration de l'importance de ce distinguo :*  
Dans la région de la **Boucle du Mouhoun** en 2015-2016, les filles étaient moins nombreuses que les garçons en classe ($Ratio_{F/G} = 0{,}9410$, soit un déficit apparent de filles). Pourtant, l'Indice de Parité des Sexes officiel du TBS s'établissait à **1,0369**, qualifiant la région dans la zone où les garçons sont défavorisés ! Ce paradoxe arithmétique s'explique par la pyramide des âges régionale : les garçons de 6-11 ans étant sensiblement plus nombreux dans la population, le taux de couverture des filles y était en réalité plus élevé. Team Datalys maintient et restitue ces deux mesures en parallèle.

### 4.3 Cadre normatif UNESCO de la parité bidirectionnelle
Pour évaluer les disparités sans a priori idéologique, nous appliquons la grille de référence internationale de l'Institut de Statistique de l'UNESCO (ISU) :
- **$IPS < 0{,}97$ : Filles défavorisées** (Sous-scolarisation féminine avérée).
- **$0{,}97 \le IPS \le 1{,}03$ : Parité atteinte** (Zone d'équité statistique de $\pm 3\,\%$ autour de 1,00).
- **$IPS > 1{,}03$ : Garçons défavorisés** (Décrochage ou sous-scolarisation masculine relative).

### 4.4 Modélisation des pentes temporelles et test de $\sigma$-convergence
Pour mesurer si les écarts se réduisent au cours du temps, le Data Scientist de l'équipe a mis en œuvre deux modélisations économétriques :
1. **Régression linéaire temporelle par région (MCO)** :
   $$IPS_{i,t} = \alpha_i + \beta_i \cdot t + \varepsilon_{i,t}$$
   où $\beta_i$ représente la pente annuelle d'évolution de l'IPS dans la région $i$.
2. **Test formel de $\sigma$-convergence spatiale** :
   $$\sigma_t = \sqrt{\frac{1}{13} \sum_{i=1}^{13} \left( IPS_{i,t} - \overline{IPS}_t \right)^2}$$
   Une baisse de l'écart-type interrégional $\sigma_t$ au fil des années prouve mathématiquement la réduction des disparités territoriales globales à travers le pays.

---

\newpage

# SECTION 5 : LES RÉSULTATS EMPIRIQUES (3 pages)

### 5.1 Cartographie des disparités régionales et double lecture du genre
La situation scolaire récente (session 2024-2025) révèle une fracture spatiale prononcée entre trois groupes de régions :

```
          TYPOLOGIE DE PARITÉ DES 13 RÉGIONS DU BURKINA FASO (2024-2025)
+----------------------------------------------------------------------------------------------------+
| 🔴 FILLES DÉFAVORISÉES (IPS < 0,97)                                                                |
| - SAHEL            : IPS = 0,9087 (Distance parité = 0,0913) | Écart filles critique                |
| - CASCADES         : IPS = 0,9443 (Distance parité = 0,0557) | Recul féminin récent                 |
| - PLATEAU-CENTRAL  : IPS = 0,9619 (Distance parité = 0,0381) | Léger déficit féminin               |
| - SUD-OUEST        : IPS = 0,9691 (Distance parité = 0,0309) | Inversion récente                   |
+----------------------------------------------------------------------------------------------------+
| 🟢 PARITÉ ATTEINTE [0,97 - 1,03]                                                                   |
| - EST              : IPS = 0,9702  |  CENTRE-EST : IPS = 0,9772  |  CENTRE-NORD : IPS = 0,9846    |
| - CENTRE-SUD       : IPS = 0,9860  |  NORD       : IPS = 0,9872  |  BOUCLE MOUHOUN : IPS = 1,0028 |
| - HAUTS-BASSINS    : IPS = 1,0126  |  CENTRE     : IPS = 1,0131  |  CENTRE-OUEST   : IPS = 1,0276 |
+----------------------------------------------------------------------------------------------------+
| 🔵 GARÇONS DÉFAVORISÉS (Sur les effectifs inscrits bruts)                                           |
| - CENTRE-OUEST     : Ratio F/G = 1,0503 (142 458 Filles pour 135 631 Garçons, déficit masculin)    |
+----------------------------------------------------------------------------------------------------+
```

- **Le Sahel, point noir absolu du pays** : Avec un IPS de **0,9087** et un TBS féminin de seulement **16,9 %**, le Sahel accuse le retard d'accès le plus alarmant de la nation.
- **Le Centre-Ouest et le Sud-Ouest, foyers d'inversion masculine** : Le Centre-Ouest compte plus de filles que de garçons inscrits en classe. Le Sud-Ouest affichait en 2015-2016 l'IPS le plus élevé du pays (**1,0636**), illustrant un décrochage masculin précoce.

### 5.2 Le rattrapage historique du milieu rural national
L'analyse de la série consolidée sur dix ans montre que la fracture entre la ville et la campagne s'est considérablement refermée au niveau primaire :

| Année Scolaire | IPS Milieu Urbain | IPS Milieu Rural | Écart Ville - Campagne | Part des Élèves en Milieu Rural |
|:---:|:---:|:---:|:---:|:---:|
| **2015-2016** | 1,0112 (Parité) | 0,9202 (Filles défav.) | **+0,0910 point** | 72,8 % |
| **2017-2018** | 1,0200 (Parité) | 0,9265 (Filles défav.) | **+0,0935 point** | 74,1 % |
| **2019-2020** | 1,0321 (Garçons défav.) | 0,9527 (Filles défav.) | **+0,0794 point** | 71,9 % |
| **2021-2022** | 1,0352 (Garçons défav.) | 0,9737 (Parité) | **+0,0615 point** | 68,8 % |
| **2024-2025** | 1,0121 (Parité) | **0,9716 (Parité)** | **+0,0405 point** | **63,5 %** |

En une décennie, **le milieu rural burkinabè est sorti de la zone de sous-scolarisation féminine sévère pour entrer dans la parité atteinte**, tandis que l'écart entre ville et campagne s'est réduit de plus de 55 %.

### 5.3 Démonstration de la $\sigma$-convergence territoriale
Le calcul de la dispersion interrégionale confirme le resserrement territorial :
- **2015-2016** : Écart-type interrégional $\sigma = \mathbf{0{,}0381}$
- **2019-2020** : Écart-type interrégional $\sigma = \mathbf{0{,}0319}$
- **2021-2022** : Écart-type interrégional $\sigma = \mathbf{0{,}0283}$ (Point bas historique)
- **2024-2025** : Écart-type interrégional $\sigma = \mathbf{0{,}0303}$

Les régions du Centre-Nord ($\beta = +0{,}0072$/an) et du Centre-Est ($\beta = +0{,}0065$/an) ont mené ce rattrapage historique en sortant du statut de filles défavorisées pour atteindre la parité.

### 5.4 Analyse exploratoire des facteurs associés et hypothèse orpaillage
- **Encadrement scolaire** : La corrélation entre le nombre moyen d'élèves par école et l'indice de parité est très faible ($r = +0{,}20$), attestant que la taille des infrastructures n'est pas un frein à l'équité.
- **Orpaillage artisanal (Synthèse qualitative)** : La littérature sectorielle (MENAPLN, PME, INSD) documente l'afflux massif de jeunes garçons dès 9-10 ans sur les comptoirs d'orpaillage au Sud-Ouest et aux Cascades. Nos données corroborent cette hypothèse : ce sont précisément ces régions aurifères qui ont enregistré les plus forts ratios de féminisation relative en primaire, témoignant d'une déperdition scolaire masculine accentuée.

---

\newpage

# SECTION 6 : LA RÉPONSE AU DÉFI ET RECOMMANDATIONS (1-2 pages)

### 6.1 Synthèse de la réponse au Défi 2
En réponse directe aux organisateurs du concours, Team Datalys formule les conclusions suivantes :
1. **Où les écarts sont-ils les plus grands ?**
   - L'écart au détriment des filles culmine au **Sahel** (IPS = 0,9087 ; TBS filles = 16,9 %).
   - L'écart au détriment des garçons est le plus fort dans le **Centre-Ouest** (Ratio F/G = 1,0503) et historiquement dans le **Sud-Ouest**.
   - L'écart historique ville-campagne s'est considérablement atténué, le monde rural national atteignant désormais l'équité globale (IPS = 0,9716).
2. **Comment évoluent-ils ?**
   - Le pays connaît une **convergence interrégionale globale** vers la parité ($\sigma$-convergence avérée), portée par les progrès spectaculaires du Centre-Nord et du Centre-Est.
   - Le Sahel demeure l'unique territoire en décrochage négatif continu.

### 6.2 Recommandations d'action publique ciblées

```
                                 MATRICE DE RECOMMANDATIONS D'ACTION
+-----------------------------------+-----------------------------------+-----------------------------------+
| PROFIL : FILLES DÉFAVORISÉES      | PROFIL : GARÇONS DÉFAVORISÉS      | MILIEU RURAL NATIONAL             |
| (Cible prioritaire : Sahel)       | (Cible : Sud-Ouest, Centre-Ouest) | (Réseau scolaire des campagnes)   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| 1. Bourses de maintien directes   | 1. Comités de veille école-mine   | 1. Généralisation des cantines    |
|    conditionnées à l'assiduité.   |    autour des sites d'orpaillage. |    scolaires endogènes.           |
| 2. Espaces d'apprentissage        | 2. Filières passerelles d'initia- | 2. Dotation en vélos pour les     |
|    sécurisés avec latrines genre. |    tion technique dès le CM2.     |    trajets de plus de 3 km.       |
| 3. Mobilisation communautaire     | 3. Adaptation du calendrier aux   | 3. Points d'eau potable et hygiène|
|    contre le mariage précoce.     |    périodes de travaux ruraux.    |    menstruelle dans chaque école. |
+-----------------------------------+-----------------------------------+-----------------------------------+
```

### 6.3 Outil d'aide à la décision : Fiche régionale opérationnelle
Pour ancrer ces recommandations dans la pratique administrative, Team Datalys a modélisé une **fiche opérationnelle d'une page** destinée au Directeur Régional de l'Éducation du Sahel (`TEAMDATALYS_05-interpretation_D2_analyst_fiche-directeur-regional-sahel_v1.md`), synthétisant le diagnostic chiffré et trois mesures d'urgence budgétables pour la rentrée.

---

\newpage

# SECTION 7 : LA REPRODUCTION ET ENCADREMENT ÉTHIQUE (1 page)

### 7.1 Guide de réexécution de la solution interactive locale
La solution développée par Team Datalys est autonome, reproductible et réexécutable en environnement local sans dépendance externe instable.

**Procédure de relance pas-à-pas :**
1. Cloner ou ouvrir le dossier du projet à la racine `c:\Users\kosac\Desktop\Data\`.
2. Ouvrir une invite de commandes et se positionner dans le sous-dossier de l'application :
   ```bash
   cd 04_analyse/dashboard_app
   ```
3. Exécuter le script batch Windows :
   ```bash
   lancer_dashboard.bat
   ```
   *ou lancer directement la commande Python :*
   ```bash
   streamlit run app.py
   ```
4. L'application interactive s'ouvre automatiquement dans le navigateur à l'adresse `http://localhost:8501`. L'utilisateur peut y manipuler les 5 onglets, filtrer par année et région, et visualiser la carte ainsi que les courbes de parité.

### 7.2 Synthèse des limites scientifiques formelles
Conformément aux exigences de rigueur du concours, les limites suivantes encadrent nos résultats :
- **Milieu Urbain/Rural** : Documenté exclusivement au niveau national agrégé (absence de croisement régional dans les publications officielles DGESS).
- **Maille spatiale** : Analyse bornée aux 13 régions historiques pour garantir la continuité temporelle de la série 10 ans.
- **Taux de scolarisation (TBS/TBA)** : Reposent sur les dénominateurs démographiques projetés par l'INSD, non recalculés par notre équipe.
- **Orpaillage artisanal** : Facteur contextuel qualitatif fondé sur la littérature sectorielle, sans modélisation causale prétentieuse en l'absence de données nominatives ou géolocalisées dans le DataPack.

### 7.3 Encart de traçabilité : Usage raisonné et critique de l'IA
Conformément à la règle d'or des organisateurs, aucune donnée sensible nominative n'a été transmise à des services tiers en ligne. L'outil d'assistance IA a été mobilisé sous le contrôle permanent et critique de l'équipe :
- **Ce que nous avons demandé :** Aide à la structuration du parcours en 5 étapes, assistance à l'écriture des scripts de nettoyage (forward-fill, regex), rédaction du squelette PostgreSQL et formalisation des graphiques Altair.
- **Ce que nous avons vérifié et corrigé :** Audit manuel des chiffres de chaque feuille brute, rejet de tout modèle prédictif artificiel sur l'orpaillage, contrôle arithmétique rigoureux de l'égalité $T = F + G$ sur 100 % des lignes, et vérification du respect strict du gabarit de 15 pages.
- **Traçabilité complète :** L'intégralité des invites et des validations d'étapes est consignée dans le journal de bord [docs/ia_log.md](file:///c:/Users/kosac/Desktop/Data/docs/ia_log.md).
