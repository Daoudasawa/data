-- ============================================================================
-- SCHÉMA RELATIONNEL POSTGRESQL — DÉFI 2 : DISPARITÉS D'ACCÈS À L'ÉDUCATION
-- Data Challenge Burkina 2026 (Édition Éducation)
-- Équipe : TEAMDATALYS | Rôle : Data Architect
-- Version : v2 (Compatible PostgreSQL 12+, exécutable et réinitialisable à blanc)
-- ============================================================================
--
-- « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo

BEGIN;

-- 1. NETTOYAGE PRÉALABLE (IDEMPOTENCE)
DROP VIEW IF EXISTS vue_comparaison_urbain_rural CASCADE;
DROP VIEW IF EXISTS vue_disparites_regionales_parite CASCADE;
DROP TABLE IF EXISTS fait_education_regionale CASCADE;
DROP TABLE IF EXISTS fait_education_milieu_national CASCADE;
DROP TABLE IF EXISTS fait_controle_totaux CASCADE;
DROP TABLE IF EXISTS ref_annee_scolaire CASCADE;
DROP TABLE IF EXISTS ref_region CASCADE;

-- 2. TABLES DE RÉFÉRENCE (DIMENSIONS)

CREATE TABLE ref_region (
    code_region_13       VARCHAR(10) PRIMARY KEY,
    nom_region_canonique VARCHAR(50) NOT NULL UNIQUE,
    chef_lieu            VARCHAR(50) NOT NULL,
    nouvelles_regions_17 TEXT NOT NULL,
    created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE ref_region IS 'Référentiel des 13 régions statistiques historiques du Burkina Faso avec mapping vers les 17 nouvelles régions (loi 2024/2025).';

CREATE TABLE ref_annee_scolaire (
    annee_scolaire VARCHAR(9) PRIMARY KEY, -- Format AAAA-AAAA
    annee_debut    INTEGER NOT NULL,
    annee_fin      INTEGER NOT NULL,
    session_label  VARCHAR(20) NOT NULL,
    CONSTRAINT chk_annee_chronologie CHECK (annee_fin = annee_debut + 1)
);

COMMENT ON TABLE ref_annee_scolaire IS 'Nomenclature temporelle des 10 années scolaires de 2015-2016 à 2024-2025.';

-- 3. TABLES DE FAITS

CREATE TABLE fait_education_regionale (
    id_fait                   SERIAL PRIMARY KEY,
    code_region_13            VARCHAR(10) NOT NULL REFERENCES ref_region(code_region_13) ON DELETE RESTRICT,
    annee_scolaire            VARCHAR(9) NOT NULL REFERENCES ref_annee_scolaire(annee_scolaire) ON DELETE RESTRICT,
    
    -- Effectifs Primaire
    primaire_garcons          INTEGER NOT NULL CHECK (primaire_garcons >= 0),
    primaire_filles           INTEGER NOT NULL CHECK (primaire_filles >= 0),
    primaire_total            INTEGER NOT NULL CHECK (primaire_total >= 0),
    primaire_ecart_f_g        INTEGER NOT NULL, -- Filles - Garçons
    primaire_ratio_f_g        NUMERIC(6,4) CHECK (primaire_ratio_f_g >= 0),
    profil_parite_effectifs   VARCHAR(30) NOT NULL,
    
    -- Infrastructure scolaire
    ecoles_public             INTEGER NOT NULL CHECK (ecoles_public >= 0),
    ecoles_prive              INTEGER NOT NULL CHECK (ecoles_prive >= 0),
    ecoles_total              INTEGER NOT NULL CHECK (ecoles_total >= 0),
    eleves_par_ecole          NUMERIC(6,1) CHECK (eleves_par_ecole >= 0),
    
    -- Préscolaire
    prescolaire_garcons       INTEGER NOT NULL CHECK (prescolaire_garcons >= 0),
    prescolaire_filles        INTEGER NOT NULL CHECK (prescolaire_filles >= 0),
    prescolaire_total         INTEGER NOT NULL CHECK (prescolaire_total >= 0),
    prescolaire_ratio_f_g     NUMERIC(6,4),
    
    -- Indicateurs officiels DGESS (taux et parité)
    tba_garcons               NUMERIC(5,2),
    tba_filles                NUMERIC(5,2),
    tba_total                 NUMERIC(5,2),
    ips_tba                   NUMERIC(6,4),
    profil_parite_tba         VARCHAR(30),
    
    tbs_garcons               NUMERIC(5,2),
    tbs_filles                NUMERIC(5,2),
    tbs_total                 NUMERIC(5,2),
    ips_tbs                   NUMERIC(6,4),
    profil_parite_tbs         VARCHAR(30),
    
    tap_garcons               NUMERIC(5,2),
    tap_filles                NUMERIC(5,2),
    tap_total                 NUMERIC(5,2),
    ips_tap                   NUMERIC(6,4),
    profil_parite_tap         VARCHAR(30),
    
    cep_reussite_garcons      NUMERIC(5,2),
    cep_reussite_filles       NUMERIC(5,2),
    cep_reussite_total        NUMERIC(5,2),
    
    CONSTRAINT uq_region_annee UNIQUE (code_region_13, annee_scolaire),
    CONSTRAINT chk_primaire_somme CHECK (primaire_total = primaire_garcons + primaire_filles),
    CONSTRAINT chk_ecoles_somme CHECK (ecoles_total = ecoles_public + ecoles_prive),
    CONSTRAINT chk_prescolaire_somme CHECK (prescolaire_total = prescolaire_garcons + prescolaire_filles)
);

COMMENT ON TABLE fait_education_regionale IS 'Panel annuel régional (13 régions x 10 ans) intégrant effectifs, parité dans les deux sens et indicateurs officiels.';

CREATE TABLE fait_education_milieu_national (
    annee_scolaire            VARCHAR(9) PRIMARY KEY REFERENCES ref_annee_scolaire(annee_scolaire) ON DELETE RESTRICT,
    urbain_garcons            INTEGER NOT NULL CHECK (urbain_garcons >= 0),
    urbain_filles             INTEGER NOT NULL CHECK (urbain_filles >= 0),
    urbain_total              INTEGER NOT NULL CHECK (urbain_total >= 0),
    ips_urbain                NUMERIC(6,4) NOT NULL,
    profil_parite_urbain      VARCHAR(30) NOT NULL,
    
    rural_garcons             INTEGER NOT NULL CHECK (rural_garcons >= 0),
    rural_filles              INTEGER NOT NULL CHECK (rural_filles >= 0),
    rural_total               INTEGER NOT NULL CHECK (rural_total >= 0),
    ips_rural                 NUMERIC(6,4) NOT NULL,
    profil_parite_rural       VARCHAR(30) NOT NULL,
    
    national_garcons          INTEGER NOT NULL CHECK (national_garcons >= 0),
    national_filles           INTEGER NOT NULL CHECK (national_filles >= 0),
    national_total            INTEGER NOT NULL CHECK (national_total >= 0),
    ips_national              NUMERIC(6,4) NOT NULL,
    
    part_rural_pct            NUMERIC(5,2) NOT NULL,
    part_filles_rural_pct     NUMERIC(5,2) NOT NULL,
    ecart_ips_urbain_rural    NUMERIC(6,4) NOT NULL,
    
    CONSTRAINT chk_urbain_somme CHECK (urbain_total = urbain_garcons + urbain_filles),
    CONSTRAINT chk_rural_somme CHECK (rural_total = rural_garcons + rural_filles),
    CONSTRAINT chk_national_somme CHECK (national_total = national_garcons + national_filles),
    CONSTRAINT chk_milieu_consolidation CHECK (national_total = urbain_total + rural_total)
);

COMMENT ON TABLE fait_education_milieu_national IS 'Série temporelle nationale consolidant les écarts d''accès entre milieu urbain et milieu rural.';

CREATE TABLE fait_controle_totaux (
    annee_scolaire            VARCHAR(9) PRIMARY KEY REFERENCES ref_annee_scolaire(annee_scolaire),
    primaire_total_officiel   INTEGER NOT NULL,
    milieu_total_officiel     INTEGER NOT NULL,
    prescolaire_total_officiel INTEGER NOT NULL,
    ecoles_total_officiel     INTEGER NOT NULL,
    ecart_controle            INTEGER DEFAULT 0
);

-- 4. VUES ANALYTIQUES POUR LE TABLEAU DE BORD ET L'ÉVALUATION

CREATE VIEW vue_disparites_regionales_parite AS
SELECT 
    f.annee_scolaire,
    r.nom_region_canonique AS region,
    r.chef_lieu,
    f.primaire_total,
    f.primaire_ratio_f_g AS ratio_effectifs_f_g,
    f.ips_tbs AS ips_tbs_officiel,
    f.profil_parite_tbs,
    CASE 
        WHEN f.ips_tbs < 0.97 THEN 'Déficit filles (accès scolaire compromis)'
        WHEN f.ips_tbs > 1.03 THEN 'Déficit garçons (décrochage/non-inscription garçons)'
        ELSE 'Zone de parité équilibrée (0.97 - 1.03)'
    END AS diagnostic_analytique,
    f.eleves_par_ecole,
    f.cep_reussite_total,
    r.nouvelles_regions_17 AS correspondance_decoupage_2024
FROM fait_education_regionale f
JOIN ref_region r ON f.code_region_13 = r.code_region_13;

COMMENT ON VIEW vue_disparites_regionales_parite IS 'Vue analytique restituant le profil de parité fille-garçon dans les deux sens pour chaque région.';

CREATE VIEW vue_comparaison_urbain_rural AS
SELECT
    annee_scolaire,
    ips_urbain,
    profil_parite_urbain,
    ips_rural,
    profil_parite_rural,
    ecart_ips_urbain_rural,
    part_rural_pct,
    national_total
FROM fait_education_milieu_national;

COMMENT ON VIEW vue_comparaison_urbain_rural IS 'Vue comparant l''évolution des ratios de genre entre les villes et les campagnes burkinabè.';

COMMIT;
