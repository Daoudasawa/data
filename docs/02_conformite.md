# Contrôle de conformité — Data Challenge Burkina 2026 — Défi 2

> *Statut au 15 novembre 2026 — Rôle : Data Architect & Chef de projet — Équipe de 2 personnes.*
>
> « On ne développe pas, on se développe » — l'éthique de l'éducation en Afrique : sur les traces de Joseph Ki-Zerbo

---

## 1. Cadrage et contraintes figées du Défi 2

| Paramètre | Choix acté | Justification & Règle |
|-----------|------------|-----------------------|
| **Verdict de faisabilité** | **FAISABLE AVEC LIMITES** | Faisabilité démontrée sur DGESS 2015/16–2024/25 avec limites documentées. |
| **Pivot géographique** | **13 régions historiques** | Cohérence avec la série temporelle DGESS 10 ans ; table de passage vers les 17 nouvelles régions si cartographie SIG. |
| **Périmètre scolaire** | **Préscolaire + Primaire** | Données complètes et structurées 2015/2016 à 2024/2025 (10 cohortes). |
| **Axe Urbain / Rural** | **Échelle nationale (Feuil3)** | Ventilation urbain/rural disponible au niveau national sur le primaire ; pas de croisement direct région × milieu dans le tableau tabulaire. |
| **Indicateurs d'accès** | **Indicateurs DGESS validés** | Utilisation directe des indicateurs officiels calculés : TBA, TBS, TAP, CEP et IPS associés. |
| **Facteur orpaillage** | **Analyse qualitative documentée** | Absence de registre quantitatif géolocalisé d'orpaillage dans le DataPack : intégration sous forme de cadrage contextuel et d'hypothèse explicative documentée. |

---

## 2. Checklist des exigences organisateurs (01 à 05)

| Exigence organisateur | Statut | Détail / Action requise |
|-----------------------|:------:|-------------------------|
| **Dossier 01_collecte** | ✅ Fait | Répertoire créé. Copie des fichiers bruts non modifiés avec convention de nommage. |
| **Dossier 02_nettoyage** | ✅ Fait | Répertoire créé. Prêt à recevoir les scripts et sorties nettoyées (forward-fill, normalisation). |
| **Dossier 03_transformation** | ✅ Fait | Répertoire créé. Prêt pour les tables panels (13 régions, milieu, temps). |
| **Dossier 04_analyse** | ✅ Fait | Répertoire créé. Prêt pour graphiques, cartes et livrable interactif. |
| **Dossier 05_interpretation** | ✅ Fait | Répertoire créé. Prêt pour notes de synthèse, fiches recommandations et pitch. |
| **Intégrité des fichiers bruts** | ✅ Fait | Règle absolue : aucun fichier source de `01_collecte/` n'est édité directement. |

---

## 3. Convention de nommage et traçabilité

Format strict obligatoire : `EQUIPE_ETAPE_DEFI_ROLE_description_vN` (sans espace, sans accent, versionné).

| Composante | Règle appliquée | Valeur pour le projet |
|------------|-----------------|------------------------|
| `EQUIPE` | Code officiel d'équipe | `EXX` (à remplacer dès consultation de l'espace candidat) |
| `ETAPE` | Étape du parcours (01 à 05) | `01-collecte`, `02-nettoyage`, `03-transformation`, `04-analyse`, `05-interpretation` |
| `DEFI` | Code défi retenu | `D2` |
| `ROLE` | Rôle exécutant | `engineer`, `architect`, `analyst`, `scientist` |
| `description` | Noms explicites en minuscules avec tirets | ex. `effectifs-primaire-region-propre` |
| `vN` | Versionnement incrémental | `v1`, `v2`, etc. |
| **Un fichier = une étape** | Pas de fichiers fourre-tout | Respecté par script et jeu de données unitaire. |

---

## 4. Checklist des dépôts et documentation

| Livrable requis | Statut | Description & Action |
|-----------------|:------:|----------------------|
| **LISEZ-MOI (01_collecte)** | ⚠️ À faire | Description des sources brutes, producteur, année, méthode d'acquisition. |
| **LISEZ-MOI (02_nettoyage)** | ⚠️ À faire | Journal des règles de nettoyage, gestion des fusions et typages. |
| **LISEZ-MOI (03_transformation)** | ⚠️ À faire | Dictionnaire des variables du panel, jointures et métriques. |
| **LISEZ-MOI (04_analyse)** | ⚠️ À faire | Guide des scripts d'analyse, restitution visuelle et tableau de bord. |
| **LISEZ-MOI (05_interpretation)** | ⚠️ À faire | Synthèse des enseignements, limites et recommandations opérationnelles. |
| **Journal de nettoyage** | ⚠️ À faire | Documenter précisément chaque transformation de colonne et suppression de ligne total. |
| **Vérification des totaux** | ⚠️ À faire | Rapprochement des sommes calculées avec les publications officielles (annuaires CNS). |
| **Journal IA (`ia_log.md`)** | ✅ Fait | Présent dans `docs/ia_log.md`, mis à jour à chaque étape. |

---

## 5. Structuration de la documentation finale (15 pages max)

| Section du rapport | Plafond pages | Contenu prévu |
|--------------------|:-------------:|---------------|
| **1. Le défi** | 1 p. | Problématique du Défi 2, contexte burkinabè, parité dans les deux sens (F défavorisées vs G défavorisés). |
| **2. Les données** | 2 p. | Présentation de la série DGESS 2016-2025, indicateurs officiels, données auxiliaires (EDS, SIG). |
| **3. La préparation** | 2–3 p. | Pipeline de nettoyage (cellules fusionnées, filtres de sous-totaux, harmonisation 13 régions). |
| **4. La méthode** | 3 p. | Métriques retenues (IPS TBS, TBA, TAP, ratio F/G), segmentation géographique et temporelle. |
| **5. Les résultats** | 3 p. | Cartographie des 13 régions, dynamique urbain/rural national, identification des zones de rupture. |
| **6. La réponse au défi** | 1–2 p. | Diagnostic précis : où les écarts sont-ils maximaux ? Comment évoluent-ils ? Impact contextuel (conflit, PDI, orpaillage). |
| **7. La reproduction** | 1 p. | Procédure pas-à-pas pour relancer la chaîne de traitement et le tableau de bord localement. |
| **TOTAL** | **13–15 p.** | **Strictement inférieur ou égal à 15 pages (critère éliminatoire).** |

---

## 6. Alignement avec les critères du jury

| Critère d'évaluation | Implémentation dans notre projet |
|----------------------|-----------------------------------|
| **Caractère innovant** | Double lecture de la parité (garçons défavorisés dans certaines régions vs filles dans d'autres) croisée avec le milieu urbain/rural. |
| **Pertinence & Rigueur** | Utilisation exclusive des indicateurs officiels audités, chaîne de calcul reproductible, totaux vérifiés. |
| **Visualisation & UX** | Solution interactive locale se relançant en 1 commande (`streamlit run` ou script graphique autonome). |
| **Impact opérationnel** | Recommandations ciblées selon la typologie régionale d'inégalité (inversion de parité, décrochage rural). |
| **Faisabilité technique** | Code propre, modulaire, dépendant uniquement de bibliothèques standards ou légères sans dépendances instables. |
| **Reproductibilité** | Fichiers d'étapes versionnés, journal de bord IA, documentation technique section 7 testée à blanc. |
