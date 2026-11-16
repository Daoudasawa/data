# « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
"""
Script d'exécution Étape 1 : Collecte et référencement des données brutes.
1. Copie les fichiers sources sans aucune modification vers 01_collecte/ avec nommage officiel.
2. Génère la table structurée des sources (ref_sources) recensant données retenues et écartées.
3. Vérifie par empreinte SHA256 que les données brutes copiées sont strictement identiques aux originaux.
"""

import os
import shutil
import hashlib
import csv

BASE_DIR = r"c:\Users\kosac\Desktop\Data"
COLLECTE_DIR = os.path.join(BASE_DIR, "01_collecte")
EQUIPE = "TEAMDATALYS"
DEFI = "D2"

os.makedirs(COLLECTE_DIR, exist_ok=True)

# 1. Cartographie des fichiers bruts à copier
FICHIERS_A_COPIER = [
    {
        "source": os.path.join(BASE_DIR, "DONNEES_STATISTQUES_ PRESCOLAIRE ET PRIMAIRE_2016_2025_DCB.xlsx"),
        "destination": os.path.join(COLLECTE_DIR, f"{EQUIPE}_01-collecte_{DEFI}_engineer_dgess-prescolaire-primaire-brut_v1.xlsx"),
        "role": "engineer",
        "description": "Données scolaires statistiques officielles DGESS (14 feuilles, 2015-2025)"
    },
    {
        "source": os.path.join(BASE_DIR, "DataPack_DCB_2026", "data", "04_Cartographie_SIG", "COD-AB_limites_administratives", "bfa_admin_boundaries__bfa_admin1.csv"),
        "destination": os.path.join(COLLECTE_DIR, f"{EQUIPE}_01-collecte_{DEFI}_engineer_sig-admin1-limites-brut_v1.csv"),
        "role": "engineer",
        "description": "Référentiel des limites administratives régionales (17 régions et mapping 13 anciennes)"
    },
    {
        "source": os.path.join(BASE_DIR, "DataPack_DCB_2026", "data", "01_Education_MENAPLN_DGESS", "Series_longues_BM_UNESCO", "education_bfa.csv"),
        "destination": os.path.join(COLLECTE_DIR, f"{EQUIPE}_01-collecte_{DEFI}_engineer_unesco-bm-education-long-terme-brut_v1.csv"),
        "role": "engineer",
        "description": "Séries temporelles longues éducation Banque Mondiale / UNESCO (comparaison macro)"
    },
    {
        "source": os.path.join(BASE_DIR, "DataPack_DCB_2026", "data", "01_Education_MENAPLN_DGESS", "Post_Primaire_Secondaire", "Annuaire_post-primaire_secondaire_2019-2020_ReliefWeb.csv"),
        "destination": os.path.join(COLLECTE_DIR, f"{EQUIPE}_01-collecte_{DEFI}_engineer_post-primaire-2019-2020-brut_v1.csv"),
        "role": "engineer",
        "description": "Annuaire statistique post-primaire et secondaire 2019-2020 (mention contextuelle)"
    }
]

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

print("=== 1. COPIE ET VÉRIFICATION D'INTÉGRITÉ SHA256 ===")
for item in FICHIERS_A_COPIER:
    src = item["source"]
    dst = item["destination"]
    shutil.copy2(src, dst)
    hash_src = sha256_file(src)
    hash_dst = sha256_file(dst)
    assert hash_src == hash_dst, f"Erreur d'intégrité sur {dst}"
    size = os.path.getsize(dst)
    print(f"OK: {os.path.basename(dst)} ({size:,} octets) | SHA256={hash_dst[:12]}...")

# 2. Production de la table ref_sources
REF_SOURCES_PATH = os.path.join(COLLECTE_DIR, f"{EQUIPE}_01-collecte_{DEFI}_architect_ref-sources_v1.csv")

SOURCES = [
    {
        "id_source": "SRC-01",
        "producteur": "DGESS / MENAPLN",
        "publication": "Données statistiques préscolaire et primaire 2016-2025",
        "annee_publication": "2026",
        "fichier_brut_local": f"{EQUIPE}_01-collecte_{DEFI}_engineer_dgess-prescolaire-primaire-brut_v1.xlsx",
        "feuilles_utilisees": "PRESCOLAIRE, Feuil1 (primaire région), Feuil2 (statut), Feuil3 (milieu), Feuil4 (niveau), Feuil5 (CP1), Feuil6 (TBA), Feuil7 (TBS), Feuil8 (TAP), Feuil9 (CEP), Feuil10 (IPS TBA), Feuil11 (IPS TBS), Feuil12 (IPS TAP), Feuil13 (écoles)",
        "portee_geographique": "National et 13 régions",
        "periode_couverte": "2015/2016 à 2024/2025",
        "usage_defi2": "Source centrale d'analyse (effectifs, milieu national, parité F/G, indicateurs officiels)",
        "statut_retenu": "RETENU",
        "motif_si_ecarte": "N/A",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-02",
        "producteur": "COD-AB / OCHA Burkina Faso",
        "publication": "Burkina Faso - Administrative Boundaries (bfa_admin1)",
        "annee_publication": "2025",
        "fichier_brut_local": f"{EQUIPE}_01-collecte_{DEFI}_engineer_sig-admin1-limites-brut_v1.csv",
        "feuilles_utilisees": "Table unique (admin1_pcode, adm1_pcode_old)",
        "portee_geographique": "17 nouvelles régions et 13 anciennes régions",
        "periode_couverte": "2025",
        "usage_defi2": "Table de correspondance pour relier les 13 régions historiques aux géométries SIG",
        "statut_retenu": "RETENU",
        "motif_si_ecarte": "N/A",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-03",
        "producteur": "Banque Mondiale / UNESCO UIS",
        "publication": "World Development Indicators / Education Statistics Burkina Faso",
        "annee_publication": "2024",
        "fichier_brut_local": f"{EQUIPE}_01-collecte_{DEFI}_engineer_unesco-bm-education-long-terme-brut_v1.csv",
        "feuilles_utilisees": "Table unique",
        "portee_geographique": "National (Burkina Faso)",
        "periode_couverte": "2007 à 2024",
        "usage_defi2": "Benchmark de cadrage macro-historique des indicateurs d'accès",
        "statut_retenu": "RETENU",
        "motif_si_ecarte": "N/A",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-04",
        "producteur": "DGESS / MENAPLN",
        "publication": "Annuaire statistique du post-primaire et du secondaire 2019-2020",
        "annee_publication": "2020",
        "fichier_brut_local": f"{EQUIPE}_01-collecte_{DEFI}_engineer_post-primaire-2019-2020-brut_v1.csv",
        "feuilles_utilisees": "Extraction PDF tabulaire",
        "portee_geographique": "National et régional",
        "periode_couverte": "2019-2020",
        "usage_defi2": "Simple cadrage contextuel qualitatif (hors analyse longitudinale)",
        "statut_retenu": "RETENU",
        "motif_si_ecarte": "N/A",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-05",
        "producteur": "INSD (5e RGPH 2019)",
        "publication": "Projections démographiques 2020-2035 & Fichier localités",
        "annee_publication": "2022",
        "fichier_brut_local": "DataPack_DCB_2026/data/02_Demographie_INSD/...",
        "feuilles_utilisees": "N/A",
        "portee_geographique": "National, régions, communes",
        "periode_couverte": "2019-2035",
        "usage_defi2": "Écarté pour le calcul de taux bruts autonomes car les taux DGESS sont déjà validés",
        "statut_retenu": "ECARTE",
        "motif_si_ecarte": "Format extraction PDF semi-structuré non fiable pour un calcul direct de dénominateur en 5 jours ; les TBS officiels de la DGESS sont préférés",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-06",
        "producteur": "INSD / ICF",
        "publication": "Enquête Démographique et de Santé (EDS 2021, DHS FR378)",
        "annee_publication": "2022",
        "fichier_brut_local": "DataPack_DCB_2026/data/03_Conditions_de_Vie_et_Emploi/EDS_2021_...",
        "feuilles_utilisees": "N/A",
        "portee_geographique": "National et milieux",
        "periode_couverte": "2021",
        "usage_defi2": "Écarté des traitements quantitatifs du panel",
        "statut_retenu": "ECARTE",
        "motif_si_ecarte": "Données transversales d'enquête ponctuelle, non comparables temporellement avec la série administrative annuelle 10 ans DGESS",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-07",
        "producteur": "CONASUR",
        "publication": "Tableaux de bord mensuels des Personnes Déplacées Internes (PDI)",
        "annee_publication": "2020-2021",
        "fichier_brut_local": "DataPack_DCB_2026/data/03_Conditions_de_Vie_et_Emploi/PDI_CONASUR/...",
        "feuilles_utilisees": "N/A",
        "portee_geographique": "Régions et communes",
        "periode_couverte": "2020-2021",
        "usage_defi2": "Cadrage qualitatif de l'impact des fermetures d'écoles",
        "statut_retenu": "ECARTE",
        "motif_si_ecarte": "Couverture temporelle limitée à 2020-2021 ne permettant pas de panel continu sur 2015-2025",
        "date_acces": "2026-11-14"
    },
    {
        "id_source": "SRC-08",
        "producteur": "Secteur minier / Orpaillage",
        "publication": "NON TROUVÉ dans le DataPack",
        "annee_publication": "NON TROUVÉ",
        "fichier_brut_local": "AUCUN",
        "feuilles_utilisees": "AUCUNE",
        "portee_geographique": "NON TROUVÉ",
        "periode_couverte": "NON TROUVÉ",
        "usage_defi2": "Facteur explicatif exploratoire",
        "statut_retenu": "ECARTE",
        "motif_si_ecarte": "Aucun registre officiel géolocalisé d'orpaillage présent dans le DataPack ; traitement obligatoirement qualitatif via littérature externe",
        "date_acces": "2026-11-14"
    }
]

with open(REF_SOURCES_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(SOURCES[0].keys()), delimiter=";")
    writer.writeheader()
    writer.writerows(SOURCES)

print(f"OK: Table ref_sources générée -> {os.path.basename(REF_SOURCES_PATH)}")
