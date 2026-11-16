# « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
"""
Script d'exécution Étape 3 : Transformation, modélisation panel et référentiels.
1. Génère le référentiel géographique des 13 régions avec mapping vers les 17 nouvelles régions SIG.
2. Fusionne les tables nettoyées en un panel régional maître (13 régions x 10 ans) avec classification UNESCO.
3. Produit le panel national comparatif urbain/rural et le dictionnaire de données complet.
"""

import os
import csv

BASE_DIR = r"c:\Users\kosac\Desktop\Data"
COLLECTE_DIR = os.path.join(BASE_DIR, "01_collecte")
NETTOYAGE_DIR = os.path.join(BASE_DIR, "02_nettoyage")
TRANSFO_DIR = os.path.join(BASE_DIR, "03_transformation")
os.makedirs(TRANSFO_DIR, exist_ok=True)

EQUIPE = "TEAMDATALYS"
DEFI = "D2"

print("=== 1. GÉNÉRATION DU RÉFÉRENTIEL DES 13 RÉGIONS ET PASSAGE 17 RÉGIONS ===")
SIG_PATH = os.path.join(COLLECTE_DIR, f"{EQUIPE}_01-collecte_{DEFI}_engineer_sig-admin1-limites-brut_v1.csv")

# Référentiel des 13 régions avec codes historiques et correspondances R17
R13_DATA = [
    {"region": "BOUCLE DU MOUHOUN", "pcode_13": "BF46", "chef_lieu": "Dédougou", "nouvelles_regions_17": "Bankui (BF62), Sourou (BF61)"},
    {"region": "CASCADES", "pcode_13": "BF47", "chef_lieu": "Banfora", "nouvelles_regions_17": "Tannounyan (BF47)"},
    {"region": "CENTRE", "pcode_13": "BF13", "chef_lieu": "Ouagadougou", "nouvelles_regions_17": "Kadiogo (BF13)"},
    {"region": "CENTRE-EST", "pcode_13": "BF48", "chef_lieu": "Tenkodogo", "nouvelles_regions_17": "Nakambe (BF48)"},
    {"region": "CENTRE-NORD", "pcode_13": "BF49", "chef_lieu": "Kaya", "nouvelles_regions_17": "Koulse (BF49)"},
    {"region": "CENTRE-OUEST", "pcode_13": "BF50", "chef_lieu": "Koudougou", "nouvelles_regions_17": "Nando (BF50)"},
    {"region": "CENTRE-SUD", "pcode_13": "BF51", "chef_lieu": "Manga", "nouvelles_regions_17": "Nazinon (BF51)"},
    {"region": "EST", "pcode_13": "BF52", "chef_lieu": "Fada N'Gourma", "nouvelles_regions_17": "Goulmou (BF63), Sirba (BF58), Tapoa (BF60)"},
    {"region": "HAUTS-BASSINS", "pcode_13": "BF53", "chef_lieu": "Bobo-Dioulasso", "nouvelles_regions_17": "Guiriko (BF53)"},
    {"region": "NORD", "pcode_13": "BF54", "chef_lieu": "Ouahigouya", "nouvelles_regions_17": "Yaadga (BF54)"},
    {"region": "PLATEAU-CENTRAL", "pcode_13": "BF55", "chef_lieu": "Ziniaré", "nouvelles_regions_17": "Oubri (BF55)"},
    {"region": "SAHEL", "pcode_13": "BF56", "chef_lieu": "Dori", "nouvelles_regions_17": "Liptako (BF64), Soum (BF59)"},
    {"region": "SUD-OUEST", "pcode_13": "BF57", "chef_lieu": "Gaoua", "nouvelles_regions_17": "Djoro (BF57)"}
]

REF_REGIONS_PATH = os.path.join(TRANSFO_DIR, f"{EQUIPE}_03-transformation_{DEFI}_architect_referentiel-13-regions_v1.csv")
with open(REF_REGIONS_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(R13_DATA[0].keys()), delimiter=";")
    writer.writeheader()
    writer.writerows(R13_DATA)
print(f"OK: Référentiel des 13 régions -> {len(R13_DATA)} lignes")


print("=== 2. CRÉATION DU PANEL RÉGIONAL MAÎTRE (13 RÉGIONS x 10 ANS) ===")
# Chargement des fichiers propres de l'Étape 2
def load_csv(filename):
    p = os.path.join(NETTOYAGE_DIR, filename)
    with open(p, "r", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter=";"))

prim_list = load_csv(f"{EQUIPE}_02-nettoyage_{DEFI}_engineer_effectifs-primaire-region-propre_v1.csv")
pres_list = load_csv(f"{EQUIPE}_02-nettoyage_{DEFI}_engineer_effectifs-prescolaire-region-propre_v1.csv")
ind_list  = load_csv(f"{EQUIPE}_02-nettoyage_{DEFI}_architect_indicateurs-dgess-region-propre_v1.csv")
eco_list  = load_csv(f"{EQUIPE}_02-nettoyage_{DEFI}_engineer_ecoles-primaire-region-propre_v1.csv")

# Indexation par clé (region, annee_scolaire)
pres_dict = {(r["region"], r["annee_scolaire"]): r for r in pres_list}
ind_dict  = {(r["region"], r["annee_scolaire"]): r for r in ind_list}
eco_dict  = {(r["region"], r["annee_scolaire"]): r for r in eco_list}
pcode_map = {r["region"]: r["pcode_13"] for r in R13_DATA}

def classifier_parite_unesco(val_ips):
    """
    Règle officielle UNESCO / ISU :
    IPS < 0.97  -> Filles défavorisées
    0.97 <= IPS <= 1.03 -> Parité atteinte
    IPS > 1.03  -> Garçons défavorisés
    """
    if val_ips is None:
        return "Indéterminé"
    try:
        v = float(val_ips)
    except (ValueError, TypeError):
        return "Indéterminé"
    if v < 0.97:
        return "Filles défavorisées"
    elif v <= 1.03:
        return "Parité atteinte"
    else:
        return "Garçons défavorisés"

panel_regional = []

for row in prim_list:
    reg = row["region"]
    an = row["annee_scolaire"]
    key = (reg, an)
    
    pre = pres_dict.get(key, {})
    ind = ind_dict.get(key, {})
    eco = eco_dict.get(key, {})
    
    tot_prim = int(row["effectif_total"])
    tot_eco = int(eco.get("ecoles_total", 0)) if eco.get("ecoles_total") else 0
    eleves_par_ecole = round(tot_prim / tot_eco, 1) if tot_eco > 0 else None
    
    ratio_prim_fg = float(row["ratio_f_g"]) if row.get("ratio_f_g") else None
    ips_tbs_val = float(ind.get("ips_tbs")) if ind.get("ips_tbs") else None
    
    record = {
        "region": reg,
        "pcode_13": pcode_map.get(reg, "N/A"),
        "annee_scolaire": an,
        "annee_debut": int(row["annee_debut"]),
        "annee_fin": int(row["annee_fin"]),
        
        # Effectifs Primaire
        "primaire_garcons": int(row["effectif_garcons"]),
        "primaire_filles": int(row["effectif_filles"]),
        "primaire_total": tot_prim,
        "primaire_ecart_f_g": int(row["ecart_f_g"]),
        "primaire_ratio_f_g": ratio_prim_fg,
        "profil_parite_effectifs": classifier_parite_unesco(ratio_prim_fg),
        
        # Écoles
        "ecoles_public": int(eco.get("ecoles_public", 0)),
        "ecoles_prive": int(eco.get("ecoles_prive", 0)),
        "ecoles_total": tot_eco,
        "eleves_par_ecole": eleves_par_ecole,
        
        # Préscolaire
        "prescolaire_garcons": int(pre.get("effectif_garcons", 0)),
        "prescolaire_filles": int(pre.get("effectif_filles", 0)),
        "prescolaire_total": int(pre.get("effectif_total", 0)),
        "prescolaire_ratio_f_g": float(pre["ratio_f_g"]) if pre.get("ratio_f_g") else None,
        
        # Indicateurs officiels DGESS
        "tba_garcons": float(ind["tba_garcons"]) if ind.get("tba_garcons") else None,
        "tba_filles": float(ind["tba_filles"]) if ind.get("tba_filles") else None,
        "tba_total": float(ind["tba_total"]) if ind.get("tba_total") else None,
        "ips_tba": float(ind["ips_tba"]) if ind.get("ips_tba") else None,
        "profil_parite_tba": classifier_parite_unesco(ind.get("ips_tba")),
        
        "tbs_garcons": float(ind["tbs_garcons"]) if ind.get("tbs_garcons") else None,
        "tbs_filles": float(ind["tbs_filles"]) if ind.get("tbs_filles") else None,
        "tbs_total": float(ind["tbs_total"]) if ind.get("tbs_total") else None,
        "ips_tbs": ips_tbs_val,
        "profil_parite_tbs": classifier_parite_unesco(ips_tbs_val),
        
        "tap_garcons": float(ind["tap_garcons"]) if ind.get("tap_garcons") else None,
        "tap_filles": float(ind["tap_filles"]) if ind.get("tap_filles") else None,
        "tap_total": float(ind["tap_total"]) if ind.get("tap_total") else None,
        "ips_tap": float(ind["ips_tap"]) if ind.get("ips_tap") else None,
        "profil_parite_tap": classifier_parite_unesco(ind.get("ips_tap")),
        
        "cep_reussite_garcons": float(ind["cep_reussite_garcons"]) if ind.get("cep_reussite_garcons") else None,
        "cep_reussite_filles": float(ind["cep_reussite_filles"]) if ind.get("cep_reussite_filles") else None,
        "cep_reussite_total": float(ind["cep_reussite_total"]) if ind.get("cep_reussite_total") else None
    }
    panel_regional.append(record)

PANEL_REG_PATH = os.path.join(TRANSFO_DIR, f"{EQUIPE}_03-transformation_{DEFI}_architect_panel-regional-education-10ans_v1.csv")
with open(PANEL_REG_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(panel_regional[0].keys()), delimiter=";")
    writer.writeheader()
    writer.writerows(panel_regional)
print(f"OK: Panel régional maître généré -> {len(panel_regional)} lignes (13 régions x 10 ans)")


print("=== 3. CRÉATION DU PANEL COMPARATIF URBAIN / RURAL (NATIONAL) ===")
mil_list = load_csv(f"{EQUIPE}_02-nettoyage_{DEFI}_engineer_effectifs-primaire-milieu-propre_v1.csv")

# Indexer par année et milieu
mil_dict = {}
for m in mil_list:
    an = m["annee_scolaire"]
    mil = m["milieu"]
    if an not in mil_dict:
        mil_dict[an] = {}
    mil_dict[an][mil] = m

panel_milieu = []
for an, d in mil_dict.items():
    urb = d["URBAIN"]
    rur = d["RURAL"]
    
    u_g = int(urb["effectif_garcons"])
    u_f = int(urb["effectif_filles"])
    u_t = int(urb["effectif_total"])
    u_ips = round(u_f / u_g, 4) if u_g > 0 else None
    
    r_g = int(rur["effectif_garcons"])
    r_f = int(rur["effectif_filles"])
    r_t = int(rur["effectif_total"])
    r_ips = round(r_f / r_g, 4) if r_g > 0 else None
    
    nat_g = u_g + r_g
    nat_f = u_f + r_f
    nat_t = u_t + r_t
    nat_ips = round(nat_f / nat_g, 4) if nat_g > 0 else None
    
    part_rural_pct = round(r_t / nat_t * 100, 2)
    part_filles_rural_pct = round(r_f / nat_f * 100, 2)
    ecart_ips_urb_rur = round(u_ips - r_ips, 4)
    
    panel_milieu.append({
        "annee_scolaire": an,
        "annee_debut": int(urb["annee_debut"]),
        "annee_fin": int(urb["annee_fin"]),
        "urbain_garcons": u_g,
        "urbain_filles": u_f,
        "urbain_total": u_t,
        "ips_urbain": u_ips,
        "profil_parite_urbain": classifier_parite_unesco(u_ips),
        "rural_garcons": r_g,
        "rural_filles": r_f,
        "rural_total": r_t,
        "ips_rural": r_ips,
        "profil_parite_rural": classifier_parite_unesco(r_ips),
        "national_garcons": nat_g,
        "national_filles": nat_f,
        "national_total": nat_t,
        "ips_national": nat_ips,
        "part_rural_pct": part_rural_pct,
        "part_filles_rural_pct": part_filles_rural_pct,
        "ecart_ips_urbain_rural": ecart_ips_urb_rur
    })

# Trier par ordre chronologique
panel_milieu.sort(key=lambda x: x["annee_debut"])

PANEL_MIL_PATH = os.path.join(TRANSFO_DIR, f"{EQUIPE}_03-transformation_{DEFI}_engineer_panel-national-milieu-10ans_v1.csv")
with open(PANEL_MIL_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(panel_milieu[0].keys()), delimiter=";")
    writer.writeheader()
    writer.writerows(panel_milieu)
print(f"OK: Panel milieu national généré -> {len(panel_milieu)} années scolaires")


print("=== 4. CRÉATION DU DICTIONNAIRE DES VARIABLES ===")
DICT_VARS = [
    {"table": "panel-regional-education-10ans", "colonne": "region", "type_sql": "VARCHAR(50)", "description": "Nom canonique de la région (13 régions historiques)", "unite": "Texte", "source": "Feuil1 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "pcode_13", "type_sql": "VARCHAR(10)", "description": "Code géographique normalisé COD-AB de l'ancienne région", "unite": "Code (ex: BF13)", "source": "bfa_admin1 OCHA"},
    {"table": "panel-regional-education-10ans", "colonne": "annee_scolaire", "type_sql": "VARCHAR(9)", "description": "Année scolaire au format AAAA-AAAA", "unite": "Format AAAA-AAAA", "source": "Normalisation DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "annee_debut", "type_sql": "INTEGER", "description": "Année civile d'ouverture de l'année scolaire", "unite": "Année (ex: 2015)", "source": "Calcul"},
    {"table": "panel-regional-education-10ans", "colonne": "annee_fin", "type_sql": "INTEGER", "description": "Année civile de clôture de l'année scolaire", "unite": "Année (ex: 2016)", "source": "Calcul"},
    {"table": "panel-regional-education-10ans", "colonne": "primaire_garcons", "type_sql": "INTEGER", "description": "Effectif des garçons scolarisés au primaire", "unite": "Nombre d'élèves", "source": "Feuil1 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "primaire_filles", "type_sql": "INTEGER", "description": "Effectif des filles scolarisées au primaire", "unite": "Nombre d'élèves", "source": "Feuil1 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "primaire_total", "type_sql": "INTEGER", "description": "Effectif total scolarisé au primaire (Filles + Garçons)", "unite": "Nombre d'élèves", "source": "Feuil1 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "primaire_ecart_f_g", "type_sql": "INTEGER", "description": "Différence brute Filles - Garçons", "unite": "Nombre d'élèves (+ ou -)", "source": "Calcul (F - G)"},
    {"table": "panel-regional-education-10ans", "colonne": "primaire_ratio_f_g", "type_sql": "NUMERIC(6,4)", "description": "Ratio filles/garçons calculé sur les effectifs inscrits", "unite": "Ratio", "source": "Calcul (F / G)"},
    {"table": "panel-regional-education-10ans", "colonne": "profil_parite_effectifs", "type_sql": "VARCHAR(30)", "description": "Typologie de parité sur effectifs (<0.97 Filles défavorisées, >1.03 Garçons défavorisés)", "unite": "Catégorie UNESCO", "source": "Classification"},
    {"table": "panel-regional-education-10ans", "colonne": "ecoles_total", "type_sql": "INTEGER", "description": "Nombre total d'écoles primaires (public + privé)", "unite": "Établissements", "source": "Feuil13 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "eleves_par_ecole", "type_sql": "NUMERIC(6,1)", "description": "Nombre moyen d'élèves par école primaire", "unite": "Élèves / école", "source": "Calcul (primaire_total / ecoles_total)"},
    {"table": "panel-regional-education-10ans", "colonne": "prescolaire_total", "type_sql": "INTEGER", "description": "Effectif total scolarisé au préscolaire", "unite": "Nombre d'élèves", "source": "PRESCOLAIRE DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "tba_total", "type_sql": "NUMERIC(5,2)", "description": "Taux Brut d'Admission au primaire (%)", "unite": "%", "source": "Feuil6 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "ips_tba", "type_sql": "NUMERIC(6,4)", "description": "Indice de Parité des Sexes officiel du TBA", "unite": "Indice", "source": "Feuil10 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "tbs_total", "type_sql": "NUMERIC(5,2)", "description": "Taux Brut de Scolarisation au primaire (%)", "unite": "%", "source": "Feuil7 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "ips_tbs", "type_sql": "NUMERIC(6,4)", "description": "Indice de Parité des Sexes officiel du TBS", "unite": "Indice", "source": "Feuil11 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "profil_parite_tbs", "type_sql": "VARCHAR(30)", "description": "Typologie officielle de parité sur TBS (<0.97 F, >1.03 G)", "unite": "Catégorie UNESCO", "source": "Classification"},
    {"table": "panel-regional-education-10ans", "colonne": "tap_total", "type_sql": "NUMERIC(5,2)", "description": "Taux d'Achèvement du Primaire (%)", "unite": "%", "source": "Feuil8 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "ips_tap", "type_sql": "NUMERIC(6,4)", "description": "Indice de Parité des Sexes officiel du TAP", "unite": "Indice", "source": "Feuil12 DGESS"},
    {"table": "panel-regional-education-10ans", "colonne": "cep_reussite_total", "type_sql": "NUMERIC(5,2)", "description": "Taux de réussite à l'examen du CEP (%)", "unite": "%", "source": "Feuil9 DGESS"},
    {"table": "panel-national-milieu-10ans", "colonne": "annee_scolaire", "type_sql": "VARCHAR(9)", "description": "Année scolaire au format AAAA-AAAA", "unite": "Format AAAA-AAAA", "source": "Feuil3 DGESS"},
    {"table": "panel-national-milieu-10ans", "colonne": "ips_urbain", "type_sql": "NUMERIC(6,4)", "description": "Indice de parité filles/garçons en milieu urbain national", "unite": "Ratio F/G", "source": "Calcul Feuil3"},
    {"table": "panel-national-milieu-10ans", "colonne": "ips_rural", "type_sql": "NUMERIC(6,4)", "description": "Indice de parité filles/garçons en milieu rural national", "unite": "Ratio F/G", "source": "Calcul Feuil3"},
    {"table": "panel-national-milieu-10ans", "colonne": "part_rural_pct", "type_sql": "NUMERIC(5,2)", "description": "Part des effectifs du primaire scolarisés en milieu rural", "unite": "%", "source": "Calcul Feuil3"},
    {"table": "panel-national-milieu-10ans", "colonne": "ecart_ips_urbain_rural", "type_sql": "NUMERIC(6,4)", "description": "Différence IPS Urbain - IPS Rural", "unite": "Différence de ratio", "source": "Calcul"}
]

DICT_PATH = os.path.join(TRANSFO_DIR, f"{EQUIPE}_03-transformation_{DEFI}_architect_dictionnaire-variables_v1.csv")
with open(DICT_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(DICT_VARS[0].keys()), delimiter=";")
    writer.writeheader()
    writer.writerows(DICT_VARS)
print(f"OK: Dictionnaire des variables généré -> {len(DICT_VARS)} variables décrites")
