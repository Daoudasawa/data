# Plan du Parcours des Données — Data Challenge Burkina 2026 — Défi 2

> « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
>
> **Équipe :** TEAMDATALYS | **Rôle responsable :** Data Architect & Data Engineer

---

## 1. Vue d'ensemble de l'architecture du pipeline

Le traitement des données du Défi 2 est structuré selon un flux strictement unidirectionnel et étanche en 5 étapes. Aucune étape aval ne modifie les sorties de l'étape amont.

```
+----------------------------------------------------------------------------------------------------+
| 01_COLLECTE (Sources brutes non modifiées)                                                         |
| - Classeur DGESS 2016-2025 (14 feuilles, 100 Ko) | Limites SIG OCHA admin1 (4,5 Ko)                |
| - Séries longues BM/UNESCO (1,5 Mo)              | Annuaire Post-Primaire 2019-2020 (1,4 Mo)       |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 02_NETTOYAGE (Standardisation, audit et séparation)                                                |
| - utils-nettoyage_v1.py (dictionnaire 13 régions canoniques, convertisseur multi-formats d'années) |
| - Forward-fill vertical des cellules fusionnées pour combler les faux NaN                          |
| - Isolation des sous-totaux et de la ligne "NATIONAL" dans totaux-officiels-controle_v1.csv        |
| - Sorties propres unitaire (Primaire Région, Milieu, Préscolaire, Indicateurs DGESS, Écoles)       |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 03_TRANSFORMATION (Modélisation, enrichissement et schématisation relationnelle)                   |
| - Référentiel des 13 régions historiques & correspondance vers les 17 nouvelles régions SIG        |
| - Table panel maître : region × annee_scolaire (130 lignes) avec profil de parité (UNESCO)        |
| - Table panel milieu national : comparaison urbain vs rural et part du rural sur 10 ans            |
| - Schéma relationnel PostgreSQL (schema-donnees_v2.sql) et Dictionnaire des variables (CSV)        |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 04_ANALYSE (Exploration empirique, régressions et cartographie)                                    |
| - Cartographie choroplèthe SIG sur les 13 régions (via mapping R17)                               |
| - Analyse de la dynamique temporelle (pente de régression, convergence / divergence spatiale)       |
| - Solution interactive locale réexécutable en une commande (Streamlit / Plotly)                    |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 05_INTERPRÉTATION & RECOMMANDATIONS (Aide à la décision et restitution)                           |
| - Réponses officielles au défi (zones d'écarts majeurs, temporalité, facteurs associés)          |
| - Fiche opérationnelle d'une page pour un directeur régional de l'éducation                        |
| - Rapport final d'évaluation (15 pages maximum, sections 1 à 7)                                    |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Définitions méthodologiques et règles de calcul

### 2.1 Ratios d'effectifs bruts vs Indice de Parité des Sexes (IPS) officiel
Une rigueur particulière a été apportée pour distinguer deux métriques souvent confondues :
1. **Ratio d'effectifs inscrits ($Ratio_{F/G}$)** :
   $$\text{Ratio}_{F/G} = \frac{\text{Effectif Filles inscrites}}{\text{Effectif Garçons inscrits}}$$
   Il mesure le rapport brut des élèves présents dans les classes.
2. **Indice de Parité des Sexes officiel du TBS ($IPS_{TBS}$)** :
   $$\text{IPS}_{TBS} = \frac{\text{TBS Filles}}{\text{TBS Garçons}} = \frac{\text{Effectif Filles} / \text{Population scolarisable Filles}}{\text{Effectif Garçons} / \text{Population scolarisable Garçons}}$$
   *Enseignement méthodologique majeur :* Dans des régions comme la Boucle du Mouhoun, les filles sont moins nombreuses en valeur absolue dans les écoles ($Ratio_{F/G} = 0{,}94$), mais leur TBS est supérieur à celui des garçons ($IPS_{TBS} = 1{,}04$). Cela s'explique par la structure démographique (garçons plus nombreux dans la population d'âge scolaire). Notre analyse présente systématiquement les deux indicateurs pour éviter tout biais d'interprétation.

### 2.2 Seuils de parité (Norme UNESCO / ISU)
Pour caractériser la parité fille-garçon dans les deux sens, nous adoptons la norme internationale de l'Institut de Statistique de l'UNESCO :
- **$IPS < 0{,}97$ : Filles défavorisées** (déficit d'accès féminin).
- **$0{,}97 \le IPS \le 1{,}03$ : Zone de parité atteinte** (équilibre relatif entre les sexes).
- **$IPS > 1{,}03$ : Garçons défavorisés** (déficit d'accès ou décrochage masculin précoce).

---

## 3. Contrôle des totaux et réconciliation de données

| Étape de contrôle | Résultat constaté | Statut d'intégrité |
|---|---|:---:|
| Somme des 13 régions vs Total National (Primaire) | 2015-2016 : $\sum 13 \text{ régions} = 2\,873\,049 = \text{Total National}$ | ✅ Écart = 0 |
| Somme Urbain + Rural vs Total National (Milieu) | 2015-2016 : $782\,683 + 2\,090\,366 = 2\,873\,049 = \text{Total National}$ | ✅ Écart = 0 |
| Cohérence arithmétique $T = F + G$ (Primaire) | 130 lignes régionales vérifiées | ✅ 100% exact |
| Cohérence arithmétique $T = F + G$ (Préscolaire) | 130 lignes régionales vérifiées | ✅ 100% exact |
| Cohérence $Total = Public + Privé$ (Écoles) | 130 lignes régionales vérifiées | ✅ 100% exact |
