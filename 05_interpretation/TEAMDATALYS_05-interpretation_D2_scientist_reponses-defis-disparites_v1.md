# Réponses Officielles au Défi 2 — Disparités d'Accès à l'Éducation
## Data Challenge Burkina 2026 (Édition Éducation)

> « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
>
> **Équipe :** TEAMDATALYS | **Rôle responsable :** Data Scientist & Data Analyst

---

## Question centrale du Défi 2 :
*« Où les écarts d'accès à l'école sont-ils les plus grands (filles-garçons, ville-campagne) et comment évoluent-ils ? »*

---

### 1. OÙ les écarts sont-ils les plus grands ?

L'analyse de la cohorte récente (2024-2025) et de l'ensemble de la série 10 ans révèle deux réalités géographiques contrastées :

#### A. Disparités Filles-Garçons : Une dualité spatiale marquée
1. **La zone critique du déficit féminin : Le SAHEL**
   - Le Sahel enregistre le plus fort éloignement absolu à la parité de tout le Burkina Faso : **IPS du TBS = 0,9087** en 2024-2025 (contre 0,9804 en moyenne nationale).
   - Les filles y subissent un sous-accès structurel massif : le TBS des filles n'est que de **16,9 %** contre **18,6 %** pour les garçons.
   - Les Cascades (IPS = 0,9443) et le Plateau-Central (IPS = 0,9619) se situent également sous le seuil d'équité UNESCO (0,97).
2. **La zone d'inversion masculine : SUD-OUEST et CENTRE-OUEST**
   - À l'opposé, les régions du Sud-Ouest et du Centre-Ouest ont connu une prédominance des filles inscrites. En 2015-2016, le Sud-Ouest affichait un IPS record de **1,0636** (Garçons défavorisés) et le Centre-Ouest **1,0446**.
   - En 2024-2025, sur les effectifs inscrits, le Centre-Ouest compte encore **142 458 filles** pour **135 631 garçons** ($Ratio_{F/G} = 1{,}0503$), confirmant la persistance de poches où les garçons décrochent plus tôt.

#### B. Disparités Ville-Campagne (Niveau National)
- En 2015-2016, le milieu rural constituait la véritable fracture de genre du pays : **IPS Rural = 0,9202** (Filles sévèrement défavorisées) alors que le milieu urbain était déjà à la parité (**IPS Urbain = 1,0112**), soit un gouffre de **0,091 point**.
- En 2024-2025, le milieu rural national s'est hissé à **0,9716**, franchissant le seuil de parité UNESCO. L'écart ville-campagne s'est réduit à **0,0405 point**.

---

### 2. COMMENT ces écarts évoluent-ils ? (Dynamique temporelle 2015-2025)

Notre modélisation économétrique longitudinale met en évidence trois dynamiques historiques :

1. **Une $\sigma$-convergence territoriale avérée** :
   - L'écart-type interrégional annuel de l'IPS du TBS a régressé de **0,0381** en 2015-2016 à **0,0303** en 2024-2025 (contraction de plus de 20 %).
   - Les disparités entre régions se sont donc globalement resserrées au cours de la décennie.
2. **Le rattrapage des régions de l'Est et du Centre-Nord** :
   - Le Centre-Nord présente la plus forte pente de féminisation ($+0{,}0072$/an, $R^2 = 0{,}78$), passant de 0,9483 ("Filles défavorisées") à 0,9846 ("Parité atteinte").
   - Le Centre-Est progresse également de $+0{,}0065$/an, passant de 0,9621 à 0,9772.
3. **Deux trajectoires de décrochage préoccupantes** :
   - **Le Sahel** : Seule région du pays s'enfonçant dans une pente négative continue ($-0{,}0027$/an), son IPS reculant de 0,9471 à 0,9087.
   - **Le Sud-Ouest** : La région connaît une masculinisation relative rapide ($-0{,}0103$/an), son IPS passant de 1,0636 à 0,9691.

---

### 3. QUELS SONT les facteurs associés (et limites) ?

1. **Infrastructures et encadrement** :
   - La corrélation entre la taille moyenne des écoles (élèves par école) et l'IPS est quasi-nulle ($r = +0{,}20$). L'accès paritaire ne dépend pas de la taille physique des complexes scolaires mais de leur proximité géographique.
2. **Chocs sécuritaires et fermetures de classes** :
   - Les régions sahéliennes et septentrionales sous forte contrainte sécuritaire (Sahel, Est) concentrent les plus faibles taux de scolarisation globale (TBS < 25 %), avec un impact asymétrique d'éviction sur les filles.
3. **Orpaillage artisanal (Hypothèse qualitative documentée)** :
   - Dans les bassins aurifères du Sud-Ouest et des Cascades, l'attraction précoce des jeunes garçons vers les travaux de lavage et d'extraction explique qualitativement le déficit relatif masculin observé lors des premières cohortes.

---

### 4. CE QUI RESTE INCONNU (Limites de l'exercice)

1. **Croisement intra-régional Urbain × Rural** : Non documenté par la DGESS ; nous ne pouvons mesurer si le rural sahélien est plus inégalitaire que le rural des Hauts-Bassins.
2. **Recensement des enfants orpailleurs** : Aucun registre géolocalisé ne permet d'isoler la part exacte d'abandon liée à l'orpaillage par rapport à la pauvreté agricole.
3. **Parcours post-primaire et secondaire** : L'absence de séries temporelles administratives sur le secondaire empêche de mesurer si la parité atteinte au CM2 se brise à l'entrée au collège.
