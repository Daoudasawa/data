# Journal de Nettoyage des Données — Défi 2

> « On ne développe pas, on se développe » — l'éthique de l'éducation en Afrique : sur les traces de Joseph Ki-Zerbo

**Équipe :** TEAMDATALYS  
**Rôle responsable :** Data Engineer  
**Fichier source brut :** `TEAMDATALYS_01-collecte_D2_engineer_dgess-prescolaire-primaire-brut_v1.xlsx` (14 feuilles)  

---

## 1. Principes de nettoyage appliqués

1. **Aucune correction silencieuse** : Chaque règle de transformation est explicitée ci-dessous avec son motif et le nombre de lignes impactées.
2. **Préservation absolue des données brutes** : Aucune donnée de `01_collecte/` n'a été modifiée.
3. **Normalisation canonique** :
   - **13 régions** : Harmonisation orthographique et suppression des variantes typographiques (ex: `PLATEAU CENTRAL` standardisé en `PLATEAU-CENTRAL`).
   - **Années scolaires** : Alignement strict sur la norme `AAAA-AAAA` (début et fin d'année scolaire).
   - **Sexe** : Standardisation en colonnes dédiées `effectif_garcons`, `effectif_filles`, `effectif_total`.
4. **Contrôles d'intégrité arithmétique** : Vérification systématique que `effectif_total == effectif_garcons + effectif_filles` sur 100% des lignes.

---

## 2. Table récapitulative des opérations de nettoyage

| Opération / Action | Feuille(s) source | Problème détecté (Pourquoi) | Traitement appliqué (Comment) | Lignes impactées |
|---|---|---|---|:---:|
| Forward-fill et normalisation des régions | `Feuil1` | Cellules fusionnées verticales pour la colonne REGION générant des faux NaN pour FILLES et TOTAL | Propagation vers le bas du nom de région et standardisation canonique | 28 |
| Séparation des totaux nationaux | `Feuil1` | Ligne 'NATIONAL' mélangée aux 13 régions statistiques | Extraction des lignes NATIONAL vers table d'audit et conservation exclusive des 13 régions | 10 |
| Nettoyage et structuration milieu urbain/rural | `Feuil3` | Cellules fusionnées pour MILIEU et présence de sous-totaux | Forward-fill du milieu, isolation de la ligne NATIONAL et calcul des écarts F-G | 9 |
| Extraction Tableau 1 préscolaire et normalisation des colonnes multiples | `PRESCOLAIRE` | Structure avec plusieurs tableaux verticaux dans la même feuille et colonnes G/F/T triplées par an | Extraction ciblée du Tableau 1 (lignes 2 à 17), normalisation des 10 années et contrôle arithmétique T = F + G | 14 |
| Consolidation des indicateurs officiels (TBA, TBS, TAP, IPS, CEP) | `Feuil6, Feuil7, Feuil8, Feuil9, Feuil10, Feuil11, Feuil12` | Indicateurs dispersés sur 7 feuilles séparées avec formats d'en-tête hétérogènes | Alignement sur la grille normalisée des 13 régions x 10 années scolaires et fusion en schéma analytique unique | 130 |
| Nettoyage et contrôle des écoles primaires | `Feuil13` | Cellules fusionnées pour REGION et présence de la ligne NATIONAL | Forward-fill, contrôle arithmétique Total = Public + Privé et export des 13 régions | 130 |

---

## 3. Résultats des contrôles automatiques d'intégrité

| Contrôle automatique | Règle attendue | Statut constaté | Commentaire |
|---|---|:---:|---|
| Complétude spatiale | 13 régions historiques | ✅ Conforme | Les 13 régions sont présentes sans omission ni doublon |
| Complétude temporelle | 10 années scolaires (2015-2016 à 2024-2025) | ✅ Conforme | Chaque région possède exactement 10 points annuels continus |
| Dimension des tables régionales | 13 régions × 10 ans = 130 lignes | ✅ Conforme | Exactement 130 lignes dans chaque table régionale propre |
| Cohérence arithmétique Primaire | Total = Garçons + Filles | ✅ Conforme | 130/130 lignes vérifiées sans aucun écart |
| Cohérence arithmétique Milieu | Total = Garçons + Filles | ✅ Conforme | 20/20 lignes vérifiées sans aucun écart |
| Cohérence arithmétique Préscolaire | Total = Garçons + Filles | ✅ Conforme | 130/130 lignes vérifiées sans aucun écart |
| Cohérence arithmétique Écoles | Total = Public + Privé | ✅ Conforme | 130/130 lignes vérifiées sans aucun écart |
| Cohérence nationale | Somme Urbain + Rural = Total National | ✅ Conforme | Vérifié sur les 10 années (écart = 0) |
| Absence de valeurs négatives | Toutes valeurs ≥ 0 | ✅ Conforme | Zéro anomalie détectée |
| Isolation des totaux | Aucune ligne 'TOTAL' ou 'NATIONAL' résiduelle | ✅ Conforme | Exportées dans un fichier de contrôle dédié |
