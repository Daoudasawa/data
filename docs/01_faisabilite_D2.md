# Faisabilité — Défi 2 : Disparités d'accès à l'éducation

> *Produit le 14 novembre 2026 — IA (Data Architect) — à relire et valider par l'équipe.*

---

## 1. Les effectifs sont-ils ventilés par SEXE ?

**OUI — preuve directe.**

| Niveau | Fichier | Colonnes |
|--------|---------|---------|
| Préscolaire | XLSX, feuille `PRESCOLAIRE` | `G` (garçons), `F` (filles), `T` (total) — par région, 10 années |
| Primaire par région | XLSX, feuille `Feuil1` | `SEXE` = GARCONS / FILLES / TOTAL — par région |
| Primaire par statut | XLSX, feuille `Feuil2` | `SEXE` = GARCONS / FILLES / TOTAL — par statut (Public/Privé) |
| Primaire par milieu | XLSX, feuille `Feuil3` | `SEXE` = GARCONS / FILLES / TOTAL — **par MILIEU (URBAIN/RURAL)** |
| Primaire par niveau | XLSX, feuille `Feuil4` | `SEXE` = GARCONS / FILLES / TOTAL — par niveau (CP1 à CM2) |
| Nouveaux inscrits CP1 | XLSX, feuille `Feuil5` | `SEXE` = GARCONS / FILLES — par région |
| TBA, TBS, TAP | XLSX, feuilles `Feuil6–8` | `G` / `F` / `T` par région |
| Réussite CEP | XLSX, feuille `Feuil9` | `Sexe` = Garçons / Filles — par région |
| IPS (TBA/TBS/TAP) | XLSX, feuilles `Feuil10–12` | Ratio F/G calculé — par région |
| Post-primaire | `data/.../Annuaire_post-primaire_2019-2020.csv` | 10 210 lignes avec mots-clés sexe (PDF extrait — structuration à faire) |

**Conclusion :** ventilation par sexe disponible pour le préscolaire et le primaire sur 10 ans, avec indicateurs de parité (IPS) déjà calculés.

---

## 2. Y a-t-il une distinction URBAIN / RURAL ?

**OUI pour le primaire — DIRECTEMENT dans le fichier XLSX.**

| Fichier | Feuille | Colonne | Valeurs |
|---------|---------|---------|--------|
| XLSX principal | `Feuil3` | `MILIEU` | `URBAIN` / `RURAL` |

- Données disponibles par sexe (GARCONS / FILLES / TOTAL) et par milieu, sur 10 années (2015/16–2024/25).
- **Pour le préscolaire :** aucune distinction urbain/rural dans le fichier XLSX principal — NON TROUVÉ directement. À chercher dans les annuaires CNS PDF ou les données INSD.
- **Pour le post-primaire/secondaire :** NON TROUVÉ dans les données tabulaires disponibles (PDF uniquement, 2019-2020).
- **Complément possible :** EDS 2021 (`data/03_Conditions_de_Vie_et_Emploi/EDS_2021_Rapport_final_DHS_FR378.csv`) contient des données de fréquentation scolaire par sexe et milieu (urbain/rural) — mais au format extraction PDF, structuration nécessaire.

---

## 3. Niveau géographique et référentiel régional

### Niveau disponible
- **XLSX principal :** niveau **RÉGION** (variable `REGION`).
- **13 régions** identifiées dans les données (Boucle du Mouhoun, Cascades, Centre, Centre-Est, Centre-Nord, Centre-Ouest, Centre-Sud, Est, Hauts-Bassins, Nord, Plateau-Central, Sahel, Sud-Ouest).

### Référentiel 13 vs 17 régions
- Le fichier `bfa_admin_boundaries__bfa_admin1.csv` (COD-AB 2025) utilise les **17 nouvelles régions** (découpage 2024-2025).
- Ce fichier contient une colonne `adm1_pcode_old` qui pointe vers les 13 anciennes régions — **la clé de correspondance existe**.
- **Risque :** les données DGESS 2015-2025 sont sur 13 régions ; les cartes SIG sont sur 17. Il faudra soit agréger les nouvelles régions, soit travailler avec le référentiel à 13 régions.

### Niveau province ou commune
- NON TROUVÉ directement dans les données tabulaires structurées du XLSX.
- Possible via extraction des PDF annuaires (long, hors scope pour 5 jours).
- Le fichier `NADA270_RGPH2019_Fichier_des_localites.csv` (RGPH 2019) contient des localités avec milieu urbain/rural et population, mais c'est une transcription PDF à structurer.

---

## 4. Années disponibles et format

| Source | Années | Format |
|--------|--------|--------|
| XLSX PRESCOLAIRE | 2015/2016 à 2024/2025 | Année seule (2016, 2017…) |
| XLSX Feuil1–5 (primaire) | 2015/2016 à 2024/2025 | `2015-2016`, `2016-2017`… |
| XLSX Feuil6–8 (taux) | 2015/2016 à 2024/2025 | `2015/16`, `2016/17`… |
| XLSX Feuil9 (CEP) | 2016 à 2025 | Années civiles (fin d'année scolaire) |
| XLSX Feuil10–12 (IPS) | 2015-16 à 2024-25 | `2015-16`, `2016-17`… |
| BM/UNESCO CSV | 2007–2024 | Années civiles |
| RGPH 2019 | 2019 | Ponctuel |
| EDS 2021 | 2021 | Ponctuel |

**Piège confirmé :** trois formats de notation des années scolaires coexistent dans le même fichier → normalisation obligatoire.

---

## 5. Lignes « Total » mélangées aux provinces/régions

**OUI — confirmé.**

Dans les feuilles `Feuil1`, `Feuil5`, `Feuil9`, des lignes avec un libellé de région vide suivi d'une ligne `TOTAL` ou équivalente sont présentes. Les feuilles `Feuil2`, `Feuil3` ont des sous-totaux par statut/milieu.

**Action requise :** identifier les lignes agrégées (Total national, Total par région) et les exclure avant tout calcul, ou les conserver dans une table séparée pour vérification.

---

## 6. Population par tranche d'âge (pour calculer des taux)

**PARTIELLEMENT DISPONIBLE.**

| Source | Contenu | Limite |
|--------|---------|--------|
| `NADA276_RGPH2019_Projections_2020-2035.csv` | Projections pop. 2020-2035 — probablement par tranche d'âge, région | Format extraction PDF à structurer |
| `INSD_RGPH2019_Vol4_Projections_demographiques_2020-2035.csv` | Idem (doublon probable) | Format extraction PDF |
| `NADA274_RGPH2019_Caracteristiques_menages_population.csv` | Pop. par âge/sexe/région (RGPH 2019) | Format extraction PDF |

**Verdict :** les données de population existent (RGPH 2019 + projections) mais sont au format extraction PDF (document;page;ligne;c1…cn), ce qui nécessite un travail de structuration non négligeable.

**Alternative pragmatique :** utiliser les **IPS (Indices de Parité des Sexes) déjà calculés** dans Feuil10–12 pour l'analyse de parité, et les **ratios d'effectifs F/G** comme proxy de l'accès relatif. Signaler explicitement dans la documentation que les **taux bruts de scolarisation** (Feuil6–8) sont préférables aux effectifs bruts car ils tiennent compte de la population.

---

## 7. Données sur enseignants, salles, abandons, orpaillage

| Thème | Disponibilité | Source |
|-------|-------------|--------|
| **Nombre d'écoles** | ✅ Feuil13 du XLSX : écoles primaires par statut et région, 10 ans | DGESS/XLSX |
| **Localisation GPS écoles** | ✅ `Ecoles_OSM_HOTOSM/ecoles_osm_burkina.csv` | HOT OSM |
| **Enseignants** | ⚠ NON TROUVÉ dans les données tabulaires disponibles. Probablement dans les PDF annuaires (CNS514-530). | À vérifier manuellement dans 1-2 PDF |
| **Salles de classe** | ⚠ NON TROUVÉ dans les données tabulaires disponibles | À vérifier dans PDF |
| **Abandons scolaires par cause** | ❌ NON TROUVÉ — aucun fichier dédié avec cause d'abandon | - |
| **Orpaillage** | ❌ NON TROUVÉ — aucun fichier de localisation de sites d'orpaillage dans le DataPack | Chercher sur BRGM, MinMines BF ou ITIE |
| **Personnes Déplacées Internes (PDI)** | ✅ 14 fichiers CONASUR (xlsx/csv) 2020-2021 — pertinent comme facteur de déscolarisation | CONASUR |

---

## 8. Pièges de qualité

| Piège | Gravité | Mitigation |
|-------|---------|-----------|
| Cellules fusionnées Excel → faux NaN | 🔴 Élevée | Forward-fill à l'étape nettoyage |
| 13 anciennes régions (données) vs 17 nouvelles (SIG) | 🔴 Élevée | Utiliser `adm1_pcode_old` du fichier admin1 ; travailler en 13 régions |
| Trois formats d'année scolaire dans le même fichier | 🟠 Moyenne | Normalisation en colonne `annee_scolaire` standard |
| CSV = extractions PDF (non tabulaires) | 🔴 Élevée pour les CSV hors XLSX principal | Préférer le XLSX pour l'analyse principale ; extraction PDF en appoint |
| Noms de régions : casse et accents variables | 🟠 Moyenne | Table de correspondance canonique (majuscules normalisées) |
| Note de traçabilité dans cellule de données | 🟡 Faible | Isoler dans une colonne `remarque` ; ne pas supprimer |
| Totaux agrégés mélangés aux données | 🟠 Moyenne | Détecter par présence de libellés "TOTAL" ou valeur nulle en clé |
| Année scolaire ≠ année civile | 🟡 Faible | Documenter la convention choisie (ex. : 2016 = fin de l'année scolaire 2015/2016) |
| Données RGPH 2019 : point unique en 2019 | 🟡 Faible | Population de référence figée — signaler que les taux 2016-2025 reposent sur des projections |

---

## 9. Verdict de faisabilité

### ✅ FAISABLE AVEC LIMITES

**Ce qui est robustement faisable :**
- Analyse de la **parité fille-garçon** (IPS, ratios F/G, TBS/TBA/TAP) au niveau **régional**, sur **10 ans** (2015/16–2024/25) — données structurées et directement exploitables.
- Analyse de l'**écart urbain-rural** au niveau national, sur 10 ans — données structurées (Feuil3).
- **Cartographie** des disparités par région — SIG disponible, 13 régions mappables.
- **Évolution temporelle** (tendances, convergence ou divergence des IPS) — 10 points de données.
- **Visualisation interactive** (tableau de bord) : données suffisantes.

**Limites à documenter obligatoirement :**
1. **Pas de croisement région × milieu** (urbain/rural par région) dans les données tabulaires disponibles — les données DGESS donnent soit par région, soit par milieu national, pas les deux croisés.
2. **Pas de données sur l'orpaillage** dans le DataPack — facteur explicatif non quantifiable directement ; possible mention qualitative avec sources externes à citer.
3. **Post-primaire/secondaire** : uniquement l'année 2019-2020 en format PDF extrait non structuré — analyse longitudinale impossible pour ce niveau.
4. **Taux de scolarisation** (numérateur/dénominateur) : les TBS sont disponibles dans Feuil6–8 (déjà calculés par DGESS) ; les effectifs bruts seuls ne permettent pas de calculer des taux sans population par tranche d'âge, et cette population est dans des PDF à structurer.
5. **Niveau province/commune** : non disponible dans les données tabulaires — analyse limitée au niveau régional (13 régions).
