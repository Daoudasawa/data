#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de vérification automatique du nommage des livrables
Data Challenge Burkina 2026 - Défi 2
Équipe: TEAMDATALYS (Membre 1: engineer/analyst, Membre 2: architect/scientist)

Epigraphe:
« On ne développe pas, on se développe » — l'éthique de l'éducation en Afrique : sur les traces de Joseph Ki-Zerbo
"""

import os
import re
import sys

ALLOWED_ETAPES = {
    '01_collecte': '01-collecte',
    '02_nettoyage': '02-nettoyage',
    '03_transformation': '03-transformation',
    '04_analyse': '04-analyse',
    '05_interpretation': '05-interpretation'
}

ALLOWED_ROLES = {'engineer', 'architect', 'analyst', 'scientist'}
EQUIPE = 'TEAMDATALYS'
DEFI = 'D2'

PATTERN = re.compile(
    r'^(?P<equipe>[A-Z0-9]+)_(?P<etape>0[1-5]-[a-z]+)_(?P<defi>D[1-3])_(?P<role>[a-z]+)_(?P<desc>[a-z0-9\-]+)_(?P<version>v[0-9]+)\.(?P<ext>[a-z0-9]+)$'
)

def check_naming():
    total_files = 0
    errors = []
    warnings = []
    valid_files = []

    print("=" * 70)
    print("AUDIT DE CONFORMITÉ DU NOMMAGE DES FICHIERS (Dossiers 01 à 05)")
    print("=" * 70)

    for folder, etape_code in ALLOWED_ETAPES.items():
        if not os.path.exists(folder):
            errors.append(f"Dossier obligatoire manquant : {folder}")
            continue

        for root, dirs, files in os.walk(folder):
            # Ignore cache
            if '__pycache__' in root:
                continue

            rel_root = os.path.relpath(root, ".")
            for f in files:
                total_files += 1
                f_path = os.path.join(rel_root, f)

                # Special case: LISEZ-MOI at the root of step folders
                if f in ('LISEZ-MOI.txt', 'LISEZ-MOI.md'):
                    valid_files.append((f_path, "FICHIER DESCRIPTIF ÉTAPE (LISEZ-MOI) - OK"))
                    continue

                # Special case: dashboard application files in 04_analyse/dashboard_app
                if 'dashboard_app' in rel_root:
                    if f in ('app.py', 'requirements.txt', 'lancer_dashboard.bat'):
                        valid_files.append((f_path, "APPLICATION EXÉCUTABLE (DASHBOARD) - OK"))
                        continue

                # Check strict naming
                m = PATTERN.match(f)
                if not m:
                    # Diagnose error
                    err_reasons = []
                    if " " in f:
                        err_reasons.append("contient des espaces")
                    if any(ord(c) > 127 for c in f):
                        err_reasons.append("contient des caractères accentués ou non-ASCII")
                    if "EXX" in f:
                        err_reasons.append("contient le placeholder EXX non substitué")
                    if not err_reasons:
                        err_reasons.append("structure non conforme au gabarit EQUIPE_ÉTAPE_DÉFI_RÔLE_desc_vN.ext")
                    errors.append(f"{f_path} : REJETÉ -> {', '.join(err_reasons)}")
                    continue

                d = m.groupdict()
                file_errors = []

                if d['equipe'] != EQUIPE:
                    file_errors.append(f"Équipe '{d['equipe']}' au lieu de '{EQUIPE}'")
                if d['etape'] != etape_code:
                    file_errors.append(f"Étape '{d['etape']}' ne correspond pas au dossier '{folder}' (attendu: '{etape_code}')")
                if d['defi'] != DEFI:
                    file_errors.append(f"Défi '{d['defi']}' au lieu de '{DEFI}'")
                if d['role'] not in ALLOWED_ROLES:
                    file_errors.append(f"Rôle '{d['role']}' invalide (autorisés: {ALLOWED_ROLES})")

                if file_errors:
                    errors.append(f"{f_path} : {'; '.join(file_errors)}")
                else:
                    valid_files.append((f_path, f"CONFORME (Rôle: {d['role']}, Version: {d['version']})"))

    print(f"\nTotal des fichiers inspectés : {total_files}")
    print(f"Fichiers conformes : {len(valid_files)}")
    print(f"Anomalies détectées : {len(errors)}")

    print("\n--- DETAIL DES FICHIERS CONFORMES ---")
    for path, status in valid_files:
        print(f" [OK] {path} -> {status}")

    if errors:
        print("\n--- ANOMALIES À CORRIGER ---")
        for err in errors:
            print(f" [ERREUR] {err}")
        return False
    else:
        print("\n>>> TOUS LES FICHIERS SONT 100% CONFORMES AUX EXIGENCES OFFICIELLES <<<")
        return True

if __name__ == '__main__':
    ok = check_naming()
    sys.exit(0 if ok else 1)
