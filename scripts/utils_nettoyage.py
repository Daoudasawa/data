# « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
"""
Utilitaires de nettoyage et de normalisation pour le Défi 2 (Data Challenge Burkina 2026).
Fournit les fonctions canoniques :
- Normalisation des 13 régions historiques
- Normalisation des années scolaires (ex: 2015-2016, 2015/16, 2016 -> '2015-2016')
- Contrôle de cohérence arithmétique T = F + G et détection des lignes totales
"""

import re

# 1. Dictionnaire canonique des 13 régions du Burkina Faso
REGIONS_CANONIQUES = {
    "BOUCLE DU MOUHOUN": "BOUCLE DU MOUHOUN",
    "BOUCLE-DU-MOUHOUN": "BOUCLE DU MOUHOUN",
    "MOUHOUN": "BOUCLE DU MOUHOUN",
    "CASCADES": "CASCADES",
    "CASCADE": "CASCADES",
    "CENTRE": "CENTRE",
    "CENTRE-EST": "CENTRE-EST",
    "CENTRE EST": "CENTRE-EST",
    "CENTRE-NORD": "CENTRE-NORD",
    "CENTRE NORD": "CENTRE-NORD",
    "CENTRE-OUEST": "CENTRE-OUEST",
    "CENTRE OUEST": "CENTRE-OUEST",
    "CENTRE-SUD": "CENTRE-SUD",
    "CENTRE SUD": "CENTRE-SUD",
    "EST": "EST",
    "HAUTS-BASSINS": "HAUTS-BASSINS",
    "HAUTS BASSINS": "HAUTS-BASSINS",
    "NORD": "NORD",
    "PLATEAU CENTRAL": "PLATEAU-CENTRAL",
    "PLATEAU-CENTRAL": "PLATEAU-CENTRAL",
    "PLATEAU_CENTRAL": "PLATEAU-CENTRAL",
    "SAHEL": "SAHEL",
    "SUD-OUEST": "SUD-OUEST",
    "SUD OUEST": "SUD-OUEST"
}

# Lignes agrégées / Totaux
LIGNES_TOTALES = {
    "NATIONAL", "BURKINA FASO", "TOTAL", "TOTAL GENERAL", "TOTAL GÉNÉRAL", "TOTAL NATIONAL"
}

def normaliser_region(nom):
    """Retourne le nom canonique de la région ou None si ligne totale ou inconnue."""
    if nom is None:
        return None
    propre = str(nom).strip().upper()
    propre = re.sub(r"\s+", " ", propre)
    if propre in LIGNES_TOTALES or propre.startswith("TOTAL"):
        return "TOTAL_AGREGE"
    return REGIONS_CANONIQUES.get(propre, propre)

def est_ligne_totale(nom):
    """Vérifie si le libellé correspond à un total ou agrégat national."""
    if nom is None:
        return False
    propre = str(nom).strip().upper()
    if propre in LIGNES_TOTALES or propre.startswith("TOTAL") or "BURKINA" in propre:
        return True
    return False

def normaliser_annee_scolaire(annee_brute):
    """
    Normalise les différents formats d'années scolaires en format canonique 'AAAA-AAAA'.
    Exemples:
    - '2015-2016' -> '2015-2016', 2015, 2016
    - '2015/2016' -> '2015-2016', 2015, 2016
    - '2015/16'   -> '2015-2016', 2015, 2016
    - '2015-16'   -> '2015-2016', 2015, 2016
    - 2016        -> '2015-2016', 2015, 2016 (fin d'année scolaire)
    - '2024/25'   -> '2024-2025', 2024, 2025
    """
    s = str(annee_brute).strip()
    # Nettoyer d'éventuelles notes de traçabilité dans l'en-tête
    s = s.split("\n")[0].strip()

    # Format AAAA-AAAA ou AAAA/AAAA
    m = re.match(r"^(\d{4})[-/](\d{4})$", s)
    if m:
        debut, fin = int(m.group(1)), int(m.group(2))
        return f"{debut}-{fin}", debut, fin

    # Format AAAA-AA ou AAAA/AA
    m = re.match(r"^(\d{4})[-/](\d{2})$", s)
    if m:
        debut = int(m.group(1))
        fin = int(str(debut)[:2] + m.group(2))
        return f"{debut}-{fin}", debut, fin

    # Format AAAA (année civile de fin de session scolaire)
    m = re.match(r"^(\d{4})$", s)
    if m:
        fin = int(m.group(1))
        debut = fin - 1
        return f"{debut}-{fin}", debut, fin

    raise ValueError(f"Format d'année scolaire non reconnu : {annee_brute}")

def verifier_somme_t_f_g(total, garcons, filles, tolerance=0):
    """Vérifie la relation arithmétique Total = Filles + Garçons."""
    if total is None or garcons is None or filles is None:
        return False, None
    diff = total - (garcons + filles)
    return abs(diff) <= tolerance, diff
