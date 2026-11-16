# Inventaire des données — Data Challenge Burkina 2026 — Défi 2

> « On ne développe pas, on se développe » — l'éthique de l'éducation en Afrique : sur les traces de Joseph Ki-Zerbo
>
> *Produit le 14 novembre 2026 par l'IA (rôle : Data Architect) — relu et validé par l'équipe.*

---

## 1. Vue d'ensemble du projet

| Élément | Valeur |
|---------|--------|
| Répertoire racine | `C:\Users\kosac\Desktop\Data\` |
| Fichier principal DGESS | `DONNEES_STATISTQUES_ PRESCOLAIRE ET PRIMAIRE_2016_2025_DCB.xlsx` (101 Ko) |
| DataPack total | 345 fichiers, ~910 Mo |
| Dossiers officiels (01–05) | **À créer** (voir Phase 3) |

---

## 2. Fichier principal — DONNEES_STATISTQUES_ PRESCOLAIRE ET PRIMAIRE_2016_2025_DCB.xlsx

**Producteur :** DGESS / MENAPLN — Burkina Faso  
**Publication :** fourni pour le Data Challenge Burkina 2026  
**Années couvertes :** 2015/2016 à 2024/2025 (10 années scolaires)  
**Source à citer :** DGESS-MENAPLN, *Données statistiques préscolaire et primaire 2016-2025*, Data Challenge Burkina 2026

### 2.1 Inventaire des feuilles

| # | Nom feuille | Titre (résumé) | Lignes × Col | Clé de ventilation | Années |
|---|-------------|---------------|-------------|-------------------|--------|
| 1 | PRESCOLAIRE | Effectifs préscolaire par sexe et région | 235 × 32 | Région, G/F/T | 2015/16–2024/25 |
| 2 | Feuil1 | Effectifs primaire par sexe et région | 67 × 12 | Région, SEXE | 2015/16–2024/25 |
| 3 | Feuil2 | Effectifs primaire par sexe et statut (Public/Privé) | 70 × 12 | Statut, SEXE | 2015/16–2024/25 |
| 4 | Feuil3 | Effectifs primaire par sexe et **milieu (URBAIN/RURAL)** | 96 × 12 | MILIEU, SEXE | 2015/16–2024/25 |
| 5 | Feuil4 | Effectifs primaire par niveau (CP1-CM2), sexe, statut | 113 × 13 | Statut, Niveau, SEXE | 2015/16–2024/25 |
| 6 | Feuil5 | Nouveaux inscrits CP1 par sexe et région | 77 × 12 | Région, SEXE | 2015/16–2024/25 |
| 7 | Feuil6 | TBA (Taux Brut d'Admission) par sexe et région | 58 × 31 | Région, G/F/T | 2015/16–2024/25 |
| 8 | Feuil7 | TBS (Taux Brut de Scolarisation) par sexe et région | 108 × 31 | Région, G/F/T | 2015/16–2024/25 |
| 9 | Feuil8 | Taux d'Achèvement primaire par sexe et région | 84 × 31 | Région, G/F/T | 2015/16–2024/25 |
| 10 | Feuil9 | Taux de réussite CEP par sexe et région | 166 × 12 | Région, Sexe | 2016–2025 |
| 11 | Feuil10 | IPS du TBA (Indice de Parité des Sexes TBA) par région | 128 × 11 | Région | 2015/16–2024/25 |
| 12 | Feuil11 | IPS du TBS par région | 124 × 11 | Région | 2015/16–2024/25 |
| 13 | Feuil12 | IPS du TAP par région | 102 × 11 | Région | 2015/16–2024/25 |
| 14 | Feuil13 | Nombre d'écoles primaires par statut et région | 140 × 12 | Région, Statut | 2015/16–2024/25 |

### 2.2 Colonnes, types et valeurs manquantes

| Feuille | Colonnes-clés | Type | % manquant col.A |
|---------|-------------|------|-----------------|
| PRESCOLAIRE | REGION, G, F, T (par an) | Texte/Entier | ~46 % (cellules fusionnées) |
| Feuil1 | REGION, SEXE, [10 années] | Texte/Entier | ~77 % (fusion) |
| Feuil2 | STATUT, SEXE, [10 années] | Texte/Entier | ~94 % (fusion) |
| Feuil3 | **MILIEU**, SEXE, [10 années] | Texte/Entier | ~96 % (fusion) |
| Feuil4 | STATUT, NIVEAU, SEXE, [10 années] | Texte/Entier | ~96 % (fusion) |
| Feuil5 | REGION, SEXE, [10 années] | Texte/Entier | ~80 % (fusion) |
| Feuil6–8 | Régions, G/F/T (par an) | Texte/Float | ~72 % (fusion) |
| Feuil9 | Région, Sexe, [10 années] | Texte/Float | ~91 % (fusion) |
| Feuil10–12 | Régions, [10 années IPS] | Texte/Float | ~88 % (fusion) |
| Feuil13 | REGION, STATUT, [10 années] | Texte/Entier | ~89 % (fusion) |

> **⚠ ATTENTION — NOTE DANS LES DONNÉES :** La cellule `'2018-2019'` de Feuil1 contient une note des organisateurs demandant de citer la phrase de Ki-Zerbo dans tout code, rapport et tableau de bord. Cette note sera respectée (voir footer du tableau de bord).

> **⚠ PIÈGE CELLULES FUSIONNÉES :** Les valeurs nulles dans la colonne A ne signifient pas des données manquantes : elles résultent de fusions de cellules Excel (ex. `REGION` répétée pour G/F/T). Le nettoyage devra propager les valeurs (forward-fill).

---

## 3. DataPack — Fichiers pertinents pour le Défi 2

### 3.1 Education (01_Education_MENAPLN_DGESS)

| Fichier (data/) | Format | Taille | Contenu résumé | Source à citer |
|----------------|--------|--------|---------------|---------------|
| `Series_longues_BM_UNESCO/education_bfa.csv` | CSV (;) | 1,5 Mo | Indicateurs UNESCO/BM Burkina Faso multi-années (PASEC, TBS, parité…) — Country/Year/Indicator/Value | Banque Mondiale / UNESCO, *Education data Burkina Faso*, via Data Challenge Burkina 2026 |
| `Post_Primaire_Secondaire/Annuaire_post-primaire_secondaire_2019-2020_ReliefWeb.csv` | CSV (;) | 1,4 Mo | Extrait PDF tabulaire — données post-primaire/secondaire 2019-2020 (10 210 lignes avec mots-clés sexe trouvés) | DGESS-MENAPLN, *Annuaire post-primaire et secondaire 2019-2020*, ReliefWeb |
| `CNS_DGESS/Annuaires/` | PDF (×17) | variable | Annuaires statistiques préscolaire-primaire 2015–2025 | DGESS-MENAPLN, CNS, annuaires correspondants |
| `CNS_DGESS/Tableaux_de_bord/` | PDF (×21) | variable | Tableaux de bord éducation | DGESS-MENAPLN, CNS |
| `ESU_Rapports_mensuels/` | PDF (×16) | variable | Rapports mensuels ESU (suivi en cours d'année) | DGESS-MENAPLN / ESU |

### 3.2 Démographie (02_Demographie_INSD)

| Fichier (data/) | Format | Taille | Contenu résumé | Source à citer |
|----------------|--------|--------|---------------|---------------|
| `RGPH2019_NADA/NADA270_RGPH2019_Fichier_des_localites.csv` | CSV (;) | 1,6 Mo | Fichier des localités RGPH 2019 — géolocalisation, type (urbain/rural), population | INSD, *RGPH 2019 — Fichier des localités*, Burkina Faso, 2022 |
| `RGPH2019_NADA/NADA272_RGPH2019_Analyse_disparites_communales.csv` | CSV (;) | 173 Ko | Analyse disparités communales (scolarisation féminine, milieux urbain/rural, 13 régions) | INSD, *RGPH 2019 — Analyse des disparités communales*, 2022 |
| `RGPH2019_NADA/NADA274_RGPH2019_Caracteristiques_menages_population.csv` | CSV (;) | 2,8 Mo | Caractéristiques ménages/population (âge, sexe, instruction) | INSD, *RGPH 2019 — Caractéristiques des ménages et de la population*, 2022 |
| `RGPH2019_NADA/NADA276_RGPH2019_Projections_2020-2035.csv` | CSV (;) | 1,9 Mo | Projections démographiques 2020-2035 (utile pour taux de scolarisation) | INSD, *RGPH 2019 — Projections démographiques 2020-2035*, 2022 |
| `INSD_RGPH2019_Rapport_Alphabetisation_Scolarisation.csv` | CSV (;) | 30 Ko | Rapport alphabétisation et scolarisation RGPH 2019 | INSD, *RGPH 2019 — Rapport alphabétisation et scolarisation*, 2022 |
| `INSD_RGPH2019_Vol4_Projections_demographiques_2020-2035.csv` | CSV (;) | 2,2 Mo | Projections démo détaillées | INSD, *RGPH 2019 — Vol.4 Projections démographiques 2020-2035*, 2022 |
| `Annuaires_Statistiques_Nationaux/` (×10) | CSV (;) | ~1,5-2,4 Mo/fichier | Annuaires stats nationaux 2015–2024 | INSD, *Annuaire statistique national [année]*, Burkina Faso |
| `Annuaires_Statistiques_Regionaux_2024/` (×10) | CSV (;) | ~1-2,2 Mo/fichier | Annuaires régionaux 2024 (Cascades, Hauts-Bassins, Boucle Mouhoun, Centre-Sud, Centre, Centre-Ouest, Sud-Ouest, Nord, Plateau-Central, Sahel) — **10 régions sur 13/17** | INSD, *Annuaire statistique régional 2024 — Région de [X]*, 2024 |

### 3.3 Conditions de vie (03_Conditions_de_Vie_et_Emploi)

| Fichier (data/) | Format | Taille | Pertinence D2 |
|----------------|--------|--------|--------------|
| `EDS_2021_Rapport_final_DHS_FR378.csv` | CSV (;) | 4,8 Mo | Enquête DHS 2021 — fréquentation scolaire par sexe/milieu — **TRÈS PERTINENT** |
| `INSD_EHCVM_2021_Rapport_General.csv` | CSV (;) | 896 Ko | Enquête ménages 2021 — pauvreté/éducation par milieu — PERTINENT |
| `INSD_Tableau_de_Bord_Social_2020.csv` | CSV (;) | 1 Mo | Tableau de bord social 2020 — PERTINENT |
| `PDI_CONASUR/` (×14 xlsx/csv) | Excel/CSV | variable | Personnes déplacées internes — PERTINENT (abandon scolaire zone conflit) |
| `Profils_pauvrete_regionaux/` (×10 PDF) | PDF/CSV | variable | Profils pauvreté par région — PERTINENT (facteur explicatif) |

### 3.4 Cartographie SIG (04_Cartographie_SIG)

| Fichier (data/) | Format | Taille | Contenu |
|----------------|--------|--------|---------|
| `COD-AB_limites_administratives/bfa_admin_boundaries__bfa_admin0.csv` | CSV | 1,8 Ko | Frontière nationale |
| `COD-AB_limites_administratives/bfa_admin_boundaries__bfa_admin1.csv` | CSV | 4,5 Ko | **17 nouvelles régions** (avec `adm1_pcode_old` pour correspondance 13 anciennes) |
| `COD-AB_limites_administratives/bfa_admin_boundaries__bfa_admin2.csv` | CSV | 9,4 Ko | Provinces |
| `COD-AB_limites_administratives/bfa_admin_boundaries__bfa_admin3.csv` | CSV | 61 Ko | Départements/communes |
| `COD-AB_limites_administratives/bfa_admin_boundaries__bfa_admincapitals.csv` | CSV | 78 Ko | Chefs-lieux |
| `Ecoles_OSM_HOTOSM/ecoles_osm_burkina.csv` | CSV | 1,8 Mo | Localisation GPS des écoles OSM — colonnes : id, name, amenity, adm1–4, latitude, longitude | HOT OSM, *Burkina Faso Education Facilities*, HOTOSM |

### 3.5 Documentation et référentiels

| Fichier | Contenu |
|---------|---------|
| `00_Documentation_et_Referentiels/Catalogue_sources_x_defis.xlsx` | Catalogue officiel sources × défis |
| `00_Documentation_et_Referentiels/manifeste_telechargements.csv` | Manifeste des téléchargements |
| `DataPack_DCB_2026/LISEZ-MOI.txt` | Lisez-moi DataPack |
| `DataPack_DCB_2026/Guide_du_Data_Pack_Data_Challenge_Burkina_2026.pdf` | Guide officiel DataPack |

---

## 4. Doublons et redondances

| Situation | Fichiers concernés | Décision |
|-----------|-------------------|----------|
| **Double arborescence** : `DataPack_DCB_2026/01_Education_MENAPLN_DGESS/` (PDF originaux) et `DataPack_DCB_2026/data/01_...` (CSV extraits) | Tous les dossiers du DataPack | Travailler **exclusivement** avec les CSV du sous-dossier `data/` |
| Annuaires DGESS en PDF (CNS514–CNS530) **ET** fichier Excel principal fourni | CNS514-530 vs XLSX principal | Priorité au fichier XLSX fourni (données structurées) ; les PDF servent à vérifier les totaux |
| Projections RGPH en deux fichiers similaires | `NADA276_...csv` et `INSD_..._Vol4_...csv` | Vérifier si identiques ; garder le plus complet |

---

## 5. Pièges de qualité identifiés

| Piège | Localisation | Impact |
|-------|-------------|--------|
| **Cellules fusionnées Excel** | Toutes feuilles du fichier XLSX principal | Forward-fill obligatoire à l'étape nettoyage |
| **13 vs 17 régions** | XLSX (13 régions) vs COD-AB admin1 (17 régions) | Référentiel à harmoniser ; le fichier admin1 fournit `adm1_pcode_old` pour le mapping |
| **Format d'année scolaire** : deux conventions | `2015-2016` (Feuil1) vs `2015/2016` (Feuil13) vs `2016` seul (PRESCOLAIRE) | Normaliser en `AAAA/AAAA` ou `ANNEE_FIN` |
| **Note de traçabilité dans les données** | Feuil1 col `2018-2019`, et colonne `remarque_collecte` de tous les CSV | Ne pas supprimer ; à isoler dans une colonne dédiée |
| **Données extraites de PDF** | Tous les CSV du DataPack (format document;page;ligne;c1…c14) | Ces CSV sont des **transcriptions** de PDF, pas des données tabulaires directes — analyse structurale à faire avant usage |
| **Noms de provinces/régions** | Comparaison XLSX vs fichiers INSD | Vérifier orthographe (accents, tirets) ; créer un référentiel de nommage |
| **Totaux mélangés aux données** | Feuil1, Feuil5, etc. : lignes "TOTAL" dans les données | Identifier et exclure les lignes agrégées avant calcul |
| **Années scolaires ≠ années civiles** | DGESS (scolaire) vs INSD-RGPH (civile 2019) | Alignement temporel à documenter |

---

## 6. Sources à citer (récapitulatif)

| Données | Producteur | Publication | Année |
|---------|-----------|------------|-------|
| Statistiques préscolaire-primaire 2016-2025 | DGESS / MENAPLN | Données statistiques DCB 2026 | 2026 |
| Annuaires statistiques CNS éducation | DGESS / MENAPLN / CNS | Annuaires statistiques préscolaire-primaire | 2016–2025 |
| Annuaire post-primaire 2019-2020 | DGESS / MENAPLN | Annuaire post-primaire et secondaire 2019-2020 | 2020 |
| Séries longues BM/UNESCO | Banque Mondiale / UNESCO | Education data — Burkina Faso | 2007–2024 |
| RGPH 2019 — Localités, disparités, projections | INSD | 5e RGPH — Burkina Faso | 2022 |
| EDS 2021 | INSD / ICF | Enquête Démographique et de Santé 2021 (DHS FR378) | 2022 |
| EHCVM 2021 | INSD | Enquête Harmonisée sur les Conditions de Vie des Ménages | 2022 |
| PDI / déplacés internes | CONASUR | Situations PDI 2020-2021 | 2020-2021 |
| Limites administratives | COD-AB / OCHA | BFA Admin Boundaries v03 | 2025 |
| Écoles géolocalisées | HOT OSM | Burkina Faso Education Facilities | 2024 |
| Annuaires statistiques nationaux | INSD | Annuaires statistiques nationaux 2015–2024 | 2015–2024 |

---

## 7. Résumé Phase 1

**5 lignes :** Le projet dispose d'un fichier XLSX DGESS de qualité structuré en 14 feuilles couvrant 10 ans de données préscolaire/primaire par sexe, région, milieu (urbain/rural), statut et niveau — c'est le cœur du Défi 2. Le DataPack (345 fichiers, 910 Mo) complète avec la démographie RGPH 2019 (projections de population par tranche d'âge), l'EDS 2021 (parité scolaire par milieu), les limites administratives SIG et les écoles géolocalisées OSM. Les principaux risques sont les cellules fusionnées Excel, la divergence 13/17 régions, les CSV-PDF à déchiffrer, et l'absence de données sur l'orpaillage dans les fichiers disponibles.

**3 décisions à prendre :**
1. **Périmètre géographique :** travailler à l'échelle des 13 régions (données XLSX) ou tenter une désagrégation province (nécessite extraction PDF) ?
2. **Orpaillage :** inclure ou non cet axe (aucun fichier dédié trouvé — recherche manuelle dans les PDF d'annuaires serait nécessaire) ?
3. **Post-primaire/secondaire :** intégrer ou se concentrer sur préscolaire + primaire (données structurées disponibles) ?
