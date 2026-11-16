# Plan de travail opérationnel — Data Challenge Burkina 2026 — Défi 2
## Du 14 au 18 novembre 2026 (Équipe de 2 personnes)

> *Document de référence mis à jour au 15 novembre 2026 — Validé avec les contraintes figées du Défi 2.*
>
> « On ne développe pas, on se développe » — l'éthique de l'éducation en Afrique : sur les traces de Joseph Ki-Zerbo

---

## 1. Rappel des contraintes et objectifs méthodologiques

- **Périmètre temporel :** 10 années scolaires (2015/2016 à 2024/2025).
- **Périmètre éducatif :** Préscolaire et Primaire.
- **Maille géographique pivot :** **13 régions historiques** (Boucle du Mouhoun, Cascades, Centre, Centre-Est, Centre-Nord, Centre-Ouest, Centre-Sud, Est, Hauts-Bassins, Nord, Plateau-Central, Sahel, Sud-Ouest).
- **Axe Urbain / Rural :** Échelle nationale (série primaire issue de `Feuil3`).
- **Indicateurs clés retenus :** Données officielles DGESS validées (TBA, TBS, TAP, Réussite CEP, et Indices de Parité des Sexes associés).
- **Orpaillage & Contexte :** Traitement analytique qualitatif documenté (revue des facteurs de vulnérabilité, corrélation documentaire).
- **Jalons critiques non négociables :**
  - **Gel des fonctionnalités et des calculs :** Lundi 16 novembre à 23h59.
  - **Marge de sécurité finale :** Clôture de tous les dépôts au moins 2 heures avant l'heure officielle le 18 novembre.
  - **Documentation :** Rédigée au fil de l'eau (1 à 2 sections par jour, ≤ 15 pages).

---

## 2. Répartition des rôles

| Membre | Rôles officiels portés | Périmètre de responsabilité principale |
|--------|-------------------------|------------------------------------------|
| **Personne A** | **Data Engineer** & **Data Analyst** | Ingestion, scripts de nettoyage, forward-fill, tables régionales/milieu, calculs d'écarts et graphiques comparatifs. |
| **Personne B** | **Data Architect** & **Data Scientist** | Modélisation panel, contrôle d'intégrité/totaux, tableau de bord interactif, cartographie, interprétation & synthèse stratégique. |

---

## 3. Plan d'action détaillé jour par jour

```
                CALENDRIER DE L'ÉQUIPE (14 - 18 NOVEMBRE 2026)
  14 Nov (J1)          15 Nov (J2)          16 Nov (J3)          17 Nov (J4)          18 Nov (J5)
 [Collecte/Audit]    [Nettoyage/Transfo]   [Analyse/App]      [Doc/Validation]     [Dépôt final]
  Audit structure     Forward-fill & panel  Cartes & Graphiques  Doc finale (15 p.)   Dépôt (H - 2h)
  Fichiers bruts v1   Totaux vérifiés       Streamlit/App        Test à blanc         Marge sécurité
  LISEZ-MOI 01        LISEZ-MOI 02 & 03     GEL LUNDI 23h59      LISEZ-MOI 04 & 05    Pitch prêt
```

---

### Jour 1 — Samedi 14 novembre : Cadrage, Collecte et Audit initial
**Objectif de la journée :** Environnement initialisé, sources brutes inventoriées et sécurisées dans `01_collecte/`.

| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Récupération du code équipe (`EXX`) sur la plateforme | Personne A | 15 min | Identifiant équipe figé |
| Copie des jeux bruts vers `01_collecte/` avec nommage strict | Personne A (Engineer) | 30 min | `EXX_01-collecte_D2_engineer_dgess-prescolaire-primaire-brut_v1.xlsx`<br>`EXX_01-collecte_D2_engineer_datapack-education-bfa-brut_v1.csv` |
| Rédaction du guide de collecte | Personne A (Engineer) | 30 min | `01_collecte/LISEZ-MOI.txt` ou `.md` |
| Inventaire technique et test de faisabilité | Personne B (Architect) | 1h00 | `docs/00_inventaire.md`<br>`docs/01_faisabilite_D2.md` |
| Rapprochement initial d'un total national avec l'annuaire PDF | Personne B (Architect) | 45 min | Première trace de vérification des totaux |
| Rédaction de la **Section 1 de la doc** (*Le défi*, 1 page) | Personne B (Architect) | 45 min | `docs/sections/section_1_defi.md` |

**Critère de sortie J1 :** Dossier `01_collecte/` complet, non modifiable, journal IA initialisé.

---

### Jour 2 — Dimanche 15 novembre : Nettoyage et Transformation (Panel 13 régions)
**Objectif de la journée :** Extraction propre des 14 feuilles Excel, résorption des cellules fusionnées, constitution du panel 10 ans sur les 13 régions et de la série milieu.

#### Matin : Nettoyage (`02_nettoyage/`)
| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Script de nettoyage `Feuil1` (Primaire effectifs par région/sexe) : forward-fill, filtre des totaux | Personne A (Engineer) | 1h30 | `EXX_02-nettoyage_D2_engineer_effectifs-primaire-region-propre_v1.csv` |
| Script de nettoyage `Feuil3` (Primaire par milieu urbain/rural national) | Personne A (Engineer) | 45 min | `EXX_02-nettoyage_D2_engineer_effectifs-primaire-milieu-propre_v1.csv` |
| Script de nettoyage `PRESCOLAIRE` (Effectifs préscolaires par région/sexe) | Personne A (Engineer) | 45 min | `EXX_02-nettoyage_D2_engineer_effectifs-prescolaire-region-propre_v1.csv` |
| Script de nettoyage des indicateurs officiels (`Feuil6` TBA, `Feuil7` TBS, `Feuil8` TAP, `Feuil10-12` IPS, `Feuil9` CEP) | Personne B (Architect) | 1h30 | `EXX_02-nettoyage_D2_architect_indicateurs-ips-tbs-tba-region-propre_v1.csv` |
| Rédaction du journal de nettoyage et du guide | Personne A (Engineer) | 30 min | `EXX_02-nettoyage_D2_engineer_journal-nettoyage_v1.md`<br>`02_nettoyage/LISEZ-MOI.txt` |

#### Après-midi : Transformation & Rapprochement (`03_transformation/`)
| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Harmonisation des libellés des 13 régions (casse, accents, codes) | Personne B (Architect) | 45 min | `EXX_03-transformation_D2_architect_referentiel-13-regions_v1.csv` |
| Fusion en table panel unifiée : `region × annee × sexe × effectifs × tbs × tba × tap × ips` | Personne B (Architect) | 1h30 | `EXX_03-transformation_D2_architect_panel-regional-education-10ans_v1.csv` |
| Table unifiée série milieu national : `milieu × annee × sexe × effectifs` | Personne A (Engineer) | 45 min | `EXX_03-transformation_D2_engineer_panel-national-milieu-10ans_v1.csv` |
| Contrôle de cohérence : somme des 13 régions vs total national officiel | Personne A & B | 45 min | Note de validation des totaux annexée au journal |
| Rédaction de la **Section 2** (*Les données*, 2 p.) et **Section 3** (*La préparation*, 2-3 p.) | Personne B & A | 1h30 | `docs/sections/section_2_donnees.md`<br>`docs/sections/section_3_preparation.md` |
| Rédaction du guide de transformation | Personne B (Architect) | 20 min | `03_transformation/LISEZ-MOI.txt` |

**Critère de sortie J2 :** Données propres et tabulaires prêtes pour analyse ; tables panels consolidées et totaux vérifiés.

---

### Jour 3 — Lundi 16 novembre : Analyse, Tableau de bord & GEL DES FONCTIONNALITÉS
**Objectif de la journée :** Production de toutes les métriques de disparités, visualisations, application interactive fonctionnelle et gel à 23h59.

#### Matin : Analyse et Visualisations clés (`04_analyse/`)
| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Analyse des disparités régionales et identification des 2 sens de parité (filles défavorisées vs garçons défavorisés) | Personne A (Analyst) | 1h15 | `EXX_04-analyse_D2_analyst_matrice-parite-regionale_v1.csv` |
| Graphiques d'évolution temporelle (2015-2025) : convergence / divergence par région | Personne A (Analyst) | 1h00 | `EXX_04-analyse_D2_analyst_courbes-evolution-ips-10ans_v1.png` |
| Analyse de la dynamique Urbain vs Rural national (taux de féminisation, écarts de croissance) | Personne A (Analyst) | 45 min | `EXX_04-analyse_D2_analyst_comparaison-dynamique-urbain-rural_v1.png` |
| Cartographie régionale des IPS (carte choroplèthe sur les 13 régions avec GeoJSON adapté) | Personne B (Scientist) | 1h30 | `EXX_04-analyse_D2_scientist_carte-disparites-13-regions-2025_v1.png` |

#### Après-midi : Solution réexécutable & Gel
| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Développement de la solution interactive locale (Streamlit ou script Plotly autonome) avec footer Ki-Zerbo | Personne B (Scientist) | 2h30 | `EXX_04-analyse_D2_scientist_dashboard-disparites/app.py`<br>`requirements.txt` |
| Test de réexécution complète en environnement isolé (lancement sans erreur) | Personne A (Analyst) | 30 min | Script de lancement validé (`run.bat` ou équivalent) |
| Rédaction de la **Section 4** (*La méthode*, 3 p.) | Personne B (Scientist) | 1h00 | `docs/sections/section_4_methode.md` |
| Rédaction du guide d'analyse | Personne A (Analyst) | 20 min | `04_analyse/LISEZ-MOI.txt` |
| **GEL OFFICIEL DES FONCTIONNALITÉS (23h59)** : arrêt de tout ajout d'indicateur ou feature | Personne A & B | 15 min | `docs/gel_fonctionnalites.md` |

**Critère de sortie J3 :** Tous les chiffres, graphiques et le tableau de bord sont stabilisés et gelés.

---

### Jour 4 — Mardi 17 novembre : Interprétation, Recommandations & Rédaction complète
**Objectif de la journée :** Rédiger le rapport officiel (≤ 15 pages), formaliser les recommandations d'impact et tester la reproductibilité totale.

#### Matin : Interprétation et Recommandations (`05_interpretation/`)
| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Formulation des réponses au Défi : où les écarts sont-ils les plus grands ? Comment évoluent-ils ? | Personne B (Scientist) | 1h30 | `EXX_05-interpretation_D2_scientist_reponses-defis-disparites_v1.md` |
| Analyse qualitative du contexte (vulnérabilités sécuritaires, orpaillage artisanal, zones d'accueil PDI) | Personne A (Analyst) | 1h00 | Inclus dans la note d'interprétation |
| Élaboration de 4 à 5 recommandations opérationnelles d'action publique ciblées | Personne B & A | 1h00 | `EXX_05-interpretation_D2_scientist_recommandations-politiques-educatives_v1.md` |
| Rédaction de la **Section 5** (*Les résultats*, 3 p.) et **Section 6** (*La réponse au défi*, 1-2 p.) | Personne B (Scientist) | 1h30 | `docs/sections/section_5_resultats.md`<br>`docs/sections/section_6_reponse.md` |
| Rédaction du guide d'interprétation | Personne A (Analyst) | 20 min | `05_interpretation/LISEZ-MOI.txt` |

#### Après-midi : Consolidation de la documentation et audit
| Tâche | Rôle / Porteur | Durée | Livrable attendu |
|-------|----------------|:-----:|-------------------|
| Rédaction de la **Section 7** (*La reproduction*, 1 p.) | Personne A (Engineer) | 45 min | `docs/sections/section_7_reproduction.md` |
| Assemblage du rapport final complet (Sections 1 à 7) | Personne B & A | 1h30 | `docs/EXX_documentation_D2_v1.pdf` (strictement ≤ 15 pages) |
| Contrôle strict du gabarit (compteur de pages, qualité des figures, citations des sources) | Personne A | 30 min | Rapport certifié conforme ≤ 15 pages |
| Audit de conformité exhaustif des 5 dossiers (`01` à `05`) et des noms de fichiers | Personne B | 45 min | Checklist de conformité émargée |

**Critère de sortie J4 :** Rapport PDF de 15 pages finalisé, tous les fichiers de toutes les étapes vérifiés.

---

### Jour 5 — Mercredi 18 novembre : Répétition, Contrôle et Dépôt final (H - 2h)
**Objectif de la journée :** Dépôt sécurisé avec 2 heures d'avance minimum, sauvegarde locale des accusés de réception.

| Heure indicative | Action | Responsable | Critère de validation |
|------------------|--------|:-----------:|-----------------------|
| 08h30 - 09h30 | Test ultime de reproduction "from scratch" sur une machine propre | Personne A | Exécution sans accroc de la chaîne |
| 09h30 - 10h30 | Relecture éditoriale finale de la documentation (orthographe, légendes) | Personne B | Document verrouillé |
| 10h30 - 11h30 | Vérification du manifeste de dépôt (taille, cohérence des versions `v1`, présence des LISEZ-MOI) | Personne A & B | Zéro anomalie de nommage |
| **Clôture - 2h** | **Téléversement des livrables sur la plateforme du challenge** | **Personne A & B** | **Dépôt validé et horodaté** |
| Post-dépôt | Capture d'écran de l'accusé de réception et archivage local | Personne B | Preuve de soumission conservée |
| Après-midi | Préparation du support de présentation orale (5-7 slides) pour la phase finale | Personne A & B | Support de pitch prêt |

---

## 4. Plan "Minimum Viable" (Plan B en cas d'imprévu)

Si un goulot d'étranglement survient avant le gel du lundi 16 :
1. **Périmètre réduit garanti :** Se limiter au Primaire (Feuil1 effectifs, Feuil3 milieu, Feuil11 IPS du TBS).
2. **Visualisation simplifiée :** Si l'application Streamlit rencontre un blocage technique d'exécution, fournir un script Python générant un rapport HTML interactif ou 3 figures PNG haute résolution autonomes.
3. **Documentation prioritaire :** Garantir en priorité la Section 1 (Défi), Section 3 (Préparation), Section 5 (Résultats), Section 6 (Réponse) et Section 7 (Reproduction) dans la limite des 15 pages.

---

## 5. Synthèse des livrables finaux par étape

```
01_collecte/
  ├── EXX_01-collecte_D2_engineer_dgess-prescolaire-primaire-brut_v1.xlsx
  ├── EXX_01-collecte_D2_engineer_datapack-education-bfa-brut_v1.csv
  └── LISEZ-MOI.txt

02_nettoyage/
  ├── EXX_02-nettoyage_D2_engineer_effectifs-primaire-region-propre_v1.csv
  ├── EXX_02-nettoyage_D2_engineer_effectifs-primaire-milieu-propre_v1.csv
  ├── EXX_02-nettoyage_D2_engineer_effectifs-prescolaire-region-propre_v1.csv
  ├── EXX_02-nettoyage_D2_architect_indicateurs-ips-tbs-tba-region-propre_v1.csv
  ├── EXX_02-nettoyage_D2_engineer_journal-nettoyage_v1.md
  └── LISEZ-MOI.txt

03_transformation/
  ├── EXX_03-transformation_D2_architect_referentiel-13-regions_v1.csv
  ├── EXX_03-transformation_D2_architect_panel-regional-education-10ans_v1.csv
  ├── EXX_03-transformation_D2_engineer_panel-national-milieu-10ans_v1.csv
  └── LISEZ-MOI.txt

04_analyse/
  ├── EXX_04-analyse_D2_analyst_matrice-parite-regionale_v1.csv
  ├── EXX_04-analyse_D2_analyst_courbes-evolution-ips-10ans_v1.png
  ├── EXX_04-analyse_D2_analyst_comparaison-dynamique-urbain-rural_v1.png
  ├── EXX_04-analyse_D2_scientist_carte-disparites-13-regions-2025_v1.png
  ├── EXX_04-analyse_D2_scientist_dashboard-disparites/ (app.py, requirements.txt, run.bat)
  └── LISEZ-MOI.txt

05_interpretation/
  ├── EXX_05-interpretation_D2_scientist_reponses-defis-disparites_v1.md
  ├── EXX_05-interpretation_D2_scientist_recommandations-politiques-educatives_v1.md
  └── LISEZ-MOI.txt

docs/
  └── EXX_documentation_D2_v1.pdf (≤ 15 pages, 7 sections)
```
