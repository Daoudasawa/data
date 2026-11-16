# Journal des interactions IA — Data Challenge Burkina 2026 — Défi 2

> « On ne développe pas, on se développe » — l'éthique de l'éducation en Afrique : sur les traces de Joseph Ki-Zerbo

**Équipe :** TEAMDATALYS  
**Défi :** Défi 2 — Disparités d'accès à l'éducation  
**Outil IA utilisé :** Antigravity (Google DeepMind) — Modèle d'assistance technique  
**Règle :** Données sensibles non envoyées à l'IA — inspection de structure uniquement.

---

## Entrée 1 — 14 novembre 2026, 21h48

### Ce que nous avons demandé à l'IA
- Rôle : Data Architect et chef de projet.
- Lire le document officiel du challenge (PDF).
- Phase 1 : inventaire complet de tous les fichiers (structure, noms de colonnes, dimensions, années, sources) — mode lecture seule.
- Phase 2 : test de faisabilité du Défi 2 (parité fille-garçon, urbain/rural).
- Phase 3 : contrôle de conformité.
- Phase 4 : plan de travail jour par jour du 14 au 18/11.

### Ce que l'IA a fait (résumé technique)
- Exploré la structure du projet avec PowerShell (`Get-ChildItem -Recurse`).
- Inspecté le fichier XLSX principal avec `openpyxl` (lecture structure uniquement : noms de feuilles, dimensions, 5 premières lignes, noms de colonnes).
- Inspecté les CSV du DataPack (premières lignes uniquement) pour identifier le format et le contenu.
- Vérifié l'existence des dossiers 01–05 (tous manquants → créés).
- Produit 4 fichiers Markdown dans `docs/`.

### Ce que l'IA a produit
- `docs/00_inventaire.md`
- `docs/01_faisabilite_D2.md`
- `docs/02_conformite.md`
- `docs/03_plan-travail.md`

### Ce que nous avons vérifié / corrigé / rejeté
- [Vérifié par l'équipe : Confirmation de la structure des feuilles XLSX et du verdict FAISABLE AVEC LIMITES]

---

## Entrée 2 — 15 novembre 2026, 04h30

### Ce que nous avons demandé à l'IA
- Valider le verdict FAISABLE AVEC LIMITES pour le Défi 2.
- Figer les contraintes techniques et méthodologiques :
  - Pivot = 13 régions historiques.
  - Périmètre = Préscolaire + Primaire (2015/16–2024/25).
  - Milieu urbain/rural = Échelle nationale (Feuil3).
  - Indicateurs DGESS calculés privilégiés (TBA, TBS, TAP, IPS, CEP).
  - Orpaillage = Traitement qualitatif documenté.
- Actualiser et aligner `docs/02_conformite.md` et `docs/03_plan-travail.md` pour 2 personnes du 14 au 18 novembre avec gel le 16 au soir et 2h de marge avant clôture le 18.

### Ce que l'IA a fait (résumé technique)
- Mis à jour `docs/02_conformite.md` intégrant le tableau des contraintes actées, la checklist des étapes 01 à 05, le gabarit de la documentation (15 p. max) et l'alignement sur les critères du jury.
- Restructuré `docs/03_plan-travail.md` avec ventilation par personne (Membre 1: Engineer/Analyst, Membre 2: Architect/Scientist), livrables versionnés conformes à la nomenclature officielle, jalon de gel strict le 16 novembre à 23h59, et clôture ciblée à 18h00 le 18 novembre.

### Ce que l'IA a produit
- `docs/02_conformite.md` (v2)
- `docs/03_plan-travail.md` (v2)

### Ce que nous avons vérifié / corrigé / rejeté
- [Vérifié par l'équipe : Validation de l'heure limite 20h00, cible de dépôt 18h00, et attribution des rôles nominatifs]

---

## Entrée 3 — 15 novembre 2026, 05h00 (Étape 1 : Collecte)

### Ce que nous avons demandé à l'IA
- Déployer l'Étape 1 (`01_collecte`) avec le code d'équipe `TEAMDATALYS`.
- Copier les fichiers sources sans altération avec nommage officiel `TEAMDATALYS_01-collecte_D2_..._v1.*`.
- Établir la table de référence des sources `ref_sources_v1.csv` identifiant les données retenues et écartées.
- Rédiger le fichier `01_collecte/LISEZ-MOI.txt`.

### Ce que l'IA a fait (résumé technique)
- Écrit et exécuté `scripts/etape1_collecte.py` : copie de 4 fichiers bruts vers `01_collecte/` avec contrôle d'intégrité par hachage SHA256 (correspondance stricte source/destination).
- Généré `TEAMDATALYS_01-collecte_D2_architect_ref-sources_v1.csv` recensant 8 sources potentielles (4 retenues pour l'analyse, 4 écartées avec motifs explicités).
- Rédigé `01_collecte/LISEZ-MOI.txt` décrivant chaque fichier déposé, la citation officielle et les justifications d'éviction.

### Ce que l'IA a produit
- `scripts/etape1_collecte.py`
- `01_collecte/TEAMDATALYS_01-collecte_D2_engineer_dgess-prescolaire-primaire-brut_v1.xlsx`
- `01_collecte/TEAMDATALYS_01-collecte_D2_engineer_sig-admin1-limites-brut_v1.csv`
- `01_collecte/TEAMDATALYS_01-collecte_D2_engineer_unesco-bm-education-long-terme-brut_v1.csv`
- `01_collecte/TEAMDATALYS_01-collecte_D2_engineer_post-primaire-2019-2020-brut_v1.csv`
- `01_collecte/TEAMDATALYS_01-collecte_D2_architect_ref-sources_v1.csv`
- `01_collecte/LISEZ-MOI.txt`

### Ce que nous avons vérifié / corrigé / rejeté
- [Vérifié par l'équipe : Conformité du nommage et présence des 4 fichiers bruts]

---

## Entrée 4 — 15 novembre 2026, 05h12 (Étape 2 : Nettoyage)

### Ce que nous avons demandé à l'IA
- Nettoyer feuille par feuille le classeur brut DGESS (primaire région, milieu urbain/rural, préscolaire région, indicateurs d'accès/parité, écoles).
- Traiter les pièges : forward-fill des cellules fusionnées, isolation des lignes de totaux, normalisation des 13 régions et des années scolaires `AAAA-AAAA`.
- Produire les scripts utilitaires, les tables propres individuelles, la table des totaux officiels de contrôle, le journal de nettoyage exhaustif et le `LISEZ-MOI.txt`.

### Ce que l'IA a fait (résumé technique)
- Conçu `scripts/utils_nettoyage.py` et déposé `TEAMDATALYS_02-nettoyage_D2_engineer_utils-nettoyage_v1.py` contenant le mapping canonique des 13 régions, le convertisseur d'années multi-formats et la vérification arithmétique `T = F + G`.
- Conçu et exécuté `scripts/etape2_nettoyage.py` qui traite `Feuil1`, `Feuil3`, `PRESCOLAIRE` (Tableau 1), `Feuil6` à `Feuil12` et `Feuil13`.
- Validé que 100% des lignes d'effectifs respectent `effectif_total == effectif_garcons + effectif_filles` et que chaque table régionale propre compte exactement 130 lignes (13 régions × 10 années).
- Généré le journal de nettoyage `journal-nettoyage_v1.md` et `02_nettoyage/LISEZ-MOI.txt`.

### Ce que l'IA a produit
- `scripts/utils_nettoyage.py`
- `scripts/etape2_nettoyage.py`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_utils-nettoyage_v1.py`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_effectifs-primaire-region-propre_v1.csv`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_effectifs-primaire-milieu-propre_v1.csv`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_effectifs-prescolaire-region-propre_v1.csv`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_architect_indicateurs-dgess-region-propre_v1.csv`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_ecoles-primaire-region-propre_v1.csv`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_totaux-officiels-controle_v1.csv`
- `02_nettoyage/TEAMDATALYS_02-nettoyage_D2_engineer_journal-nettoyage_v1.md`
- `02_nettoyage/LISEZ-MOI.txt`

### Ce que nous avons vérifié / corrigé / rejeté
- [Vérifié par l'équipe : Contrôle arithmétique des 130 lignes et vérification manuelle de 3 cellules sur l'étape 02]

---

## Entrée 5 — 15 novembre 2026, 05h40 (Étape 3 : Transformation)

### Ce que nous avons demandé à l'IA
- Exécuter l'Étape 3 (`03_transformation`) :
  - Référentiel des 13 régions avec table de correspondance vers les 17 nouvelles régions SIG.
  - Table panel maître unifiée (13 régions × 10 ans) intégrant effectifs, écoles, préscolaire, indicateurs officiels et classification de parité UNESCO dans les deux sens (<0.97 Filles défavorisées, >1.03 Garçons défavorisés).
  - Table panel national milieu (Urbain vs Rural) sur 10 ans.
  - Schéma relationnel DDL PostgreSQL (`schema-donnees_v2.sql`) réexécutable à blanc.
  - Dictionnaire des variables (CSV) et plan du parcours des données (.md).
  - Rédaction du `LISEZ-MOI.txt`.

### Ce que l'IA a fait (résumé technique)
- Écrit et exécuté `scripts/etape3_transformation.py` générant le référentiel des 13 régions (`pcode_13`, chef-lieu, correspondance R17), le panel régional maître (130 lignes × 27 colonnes) et le panel milieu (10 années).
- Implémenté la classification de parité selon la norme standard UNESCO / ISU pour les deux sens de l'inégalité.
- Rédigé le schéma relationnel DDL PostgreSQL (`schema-donnees_v2.sql`) avec clés étrangères, contraintes `CHECK` et vues analytiques.
- Produit le dictionnaire technique `dictionnaire-variables_v1.csv`, le plan de parcours `parcours-donnees_v1.md` et `03_transformation/LISEZ-MOI.txt`.

### Ce que l'IA a produit
- `scripts/etape3_transformation.py`
- `03_transformation/TEAMDATALYS_03-transformation_D2_architect_referentiel-13-regions_v1.csv`
- `03_transformation/TEAMDATALYS_03-transformation_D2_architect_panel-regional-education-10ans_v1.csv`
- `03_transformation/TEAMDATALYS_03-transformation_D2_engineer_panel-national-milieu-10ans_v1.csv`
- `03_transformation/TEAMDATALYS_03-transformation_D2_architect_schema-donnees_v2.sql`
- `03_transformation/TEAMDATALYS_03-transformation_D2_architect_dictionnaire-variables_v1.csv`
- `03_transformation/TEAMDATALYS_03-transformation_D2_architect_parcours-donnees_v1.md`
- `03_transformation/LISEZ-MOI.txt`

### Ce que nous avons vérifié / corrigé / rejeté
- [Vérifié par l'équipe : Validation des 130 lignes du panel maître et confirmation de la cohérence arithmétique]

---

## Entrée 6 — 15 novembre 2026, 06h05 (Étape 4 : Analyse et Solution locale)

### Ce que nous avons demandé à l'IA
- Exécuter l'Étape 4 (`04_analyse`) :
  - Matrice régionale IPS et classement des disparités dans les deux sens (Filles vs Garçons défavorisés).
  - Modélisation des pentes temporelles (régression OLS) et test formel de sigma-convergence spatiale (Data Scientist).
  - Analyse comparative dynamique urbain/rural national.
  - Corrélations exploratoires avec facteurs associés (taille d'école, scolarisation globale).
  - Cadrage contextuel qualitatif sur l'orpaillage artisanal documenté.
  - Développement de la solution interactive réexécutable en local (Streamlit `app.py`, `requirements.txt`, `lancer_dashboard.bat`).
  - Rédaction du `LISEZ-MOI.txt`.

### Ce que l'IA a fait (résumé technique)
- Écrit et exécuté `scripts/etape4_analyse.py` produisant les 5 jeux tabulaires d'analyse et la note qualitative sur l'orpaillage.
- Démontré la sigma-convergence spatiale (baisse de l'écart-type interrégional de 0,0381 à 0,0303) et identifié les zones critiques (Sahel avec IPS de 0,9087) et d'inversion masculine.
- Conçu l'application Streamlit `04_analyse/dashboard_app/app.py` organisée en 5 onglets avec graphiques Altair interactifs, filtres temporels/spatiaux et footer obligatoire Joseph Ki-Zerbo.
- Rédigé `04_analyse/LISEZ-MOI.txt`.

### Ce que l'IA a produit
- `scripts/etape4_analyse.py`
- `04_analyse/TEAMDATALYS_04-analyse_D2_analyst_matrice-parite-regionale_v1.csv`
- `04_analyse/TEAMDATALYS_04-analyse_D2_analyst_classement-regions-parite_v1.csv`
- `04_analyse/TEAMDATALYS_04-analyse_D2_scientist_pentes-evolution-convergence_v1.csv`
- `04_analyse/TEAMDATALYS_04-analyse_D2_analyst_analyse-urbain-rural_v1.csv`
- `04_analyse/TEAMDATALYS_04-analyse_D2_scientist_correlations-facteurs-associes_v1.csv`
- `04_analyse/TEAMDATALYS_04-analyse_D2_analyst_contexte-orpaillage-qualitatif_v1.md`
- `04_analyse/dashboard_app/app.py`
- `04_analyse/dashboard_app/requirements.txt`
- `04_analyse/dashboard_app/lancer_dashboard.bat`
- `04_analyse/LISEZ-MOI.txt`

### Ce que nous avons vérifié / corrigé / rejeté
- [À remplir par l'équipe : ...]

---

## Entrée 7 — 15 novembre 2026, 06h20 (Étape 5 : Interprétation, Documentation finale & Audit de conformité)

### Ce que nous avons demandé à l'IA
- Exécuter l'Étape 5 (`05_interpretation`) :
  - Rédiger les réponses explicites et exhaustives aux questions du Défi 2 (`reponses-defis-disparites_v1.md`).
  - Établir les recommandations de politiques éducatives territorialisées et chiffrées (`recommandations-politiques-educatives_v1.md`).
  - Concevoir une fiche opérationnelle de synthèse d'une page pour un décideur local : le Directeur Régional du Sahel (`fiche-directeur-regional-sahel_v1.md`).
  - Rédiger `05_interpretation/LISEZ-MOI.txt`.
- Rédiger la grande documentation finale du projet de 14 pages (`docs/TEAMDATALYS_documentation_D2_v1.md`) selon les 7 sections du plan officiel du jury.
- Créer un script d'audit automatisé du nommage de tous les fichiers du projet (`scripts/check_noms.py`).
- Produire le document d'audit de conformité finale et la grille d'évaluation du jury (`docs/conformite_finale.md`).

### Ce que l'IA a fait (résumé technique)
- Rédigé les 3 livrables d'interprétation pour le Data Analyst et le Data Scientist dans `05_interpretation/` avec diagnostic bi-directionnel chiffré et recommandations articulées selon les 4 profils territoriaux.
- Rédigé `05_interpretation/LISEZ-MOI.txt` résumant les fichiers et leurs correspondances avec les rôles.
- Rédigé le rapport complet de documentation de 14 pages [docs/TEAMDATALYS_documentation_D2_v1.md](file:///c:/Users/kosac/Desktop/Data/docs/TEAMDATALYS_documentation_D2_v1.md) respectant à la lettre les 7 parties officielles (Défi, Données, Préparation, Méthode, Résultats, Réponse au Défi, Reproduction), enrichi de visualisations textuelles, de formules mathématiques KaTeX et de l'épigraphe de Joseph Ki-Zerbo.
- Écrit et exécuté `scripts/check_noms.py` : contrôle de 36 fichiers sur les 5 dossiers ; résultat 100% conforme (0 erreur, 0 caractère accentué, 0 espace, 0 placeholder EXX résiduel).
- Rédigé le rapport de conformité finale `docs/conformite_finale.md` évaluant le projet face aux 13 règles non négociables et aux 6 critères d'évaluation du jury.

### Ce que l'IA a produit
- `05_interpretation/TEAMDATALYS_05-interpretation_D2_scientist_reponses-defis-disparites_v1.md`
- `05_interpretation/TEAMDATALYS_05-interpretation_D2_scientist_recommandations-politiques-educatives_v1.md`
- `05_interpretation/TEAMDATALYS_05-interpretation_D2_analyst_fiche-directeur-regional-sahel_v1.md`
- `05_interpretation/LISEZ-MOI.txt`
- `docs/TEAMDATALYS_documentation_D2_v1.md`
- `scripts/check_noms.py`
- `docs/conformite_finale.md`

### Ce que nous avons vérifié / corrigé / rejeté
- [À remplir par l'équipe : ...]

