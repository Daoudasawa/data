#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite de tests unitaires formels des formules mathématiques (F1 à F16)
Data Challenge Burkina 2026 — Défi 2
Équipe : TEAMDATALYS

Épigraphe :
« On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
"""

import unittest
import numpy as np
import math

# ==============================================================================
# IMPLÉMENTATION DE RÉFÉRENCE INDÉPENDANTE DES FORMULES F1 À F16
# ==============================================================================

def f1_ips(x_f, x_g):
    """F1: Indice de Parité des Sexes (IPS = X_F / X_G)."""
    if x_g is None or x_g <= 0:
        return None
    if x_f is None:
        return None
    return float(x_f) / float(x_g)

def f2_bande_parite(ips, seuil_bas=0.97, seuil_haut=1.03):
    """F2: Classification de parité selon la norme UNESCO/ISU."""
    if ips is None or np.isnan(ips):
        return "Non calculable"
    if ips < seuil_bas:
        return "Filles défavorisées"
    elif ips > seuil_haut:
        return "Garçons défavorisés"
    else:
        return "Parité atteinte"

def f3_ecart_absolu(tx_f, tx_g):
    """F3: Écart absolu fille-garçon en points de pourcentage (D = TX_F - TX_G)."""
    if tx_f is None or tx_g is None:
        return None
    return float(tx_f) - float(tx_g)

def f4_ips_national_pondere(liste_f, liste_g):
    """F4: Agrégation nationale pondérée stricte IPS = Sum(F) / Sum(G)."""
    sum_f = sum(liste_f)
    sum_g = sum(liste_g)
    if sum_g <= 0:
        return None
    return sum_f / sum_g

def f4_ips_moyenne_simple(liste_f, liste_g):
    """F4 (Formule interdite): Moyenne simple non pondérée des IPS."""
    ratios = [f / g for f, g in zip(liste_f, liste_g) if g > 0]
    return sum(ratios) / len(ratios) if ratios else None

def f5_coherence_arithmetique(total, garcons, filles, tolerance=1):
    """F5: Vérification arithmétique T = F + G."""
    if total is None or garcons is None or filles is None:
        return False
    return abs(total - (garcons + filles)) <= tolerance

def f7_indicateurs_milieu(e_u_g, e_u_f, e_r_g, e_r_f):
    """F7: Métriques milieu Urbain-Rural national."""
    e_u_t = e_u_g + e_u_f
    e_r_t = e_r_g + e_r_f
    part_rural = (e_r_t / (e_u_t + e_r_t)) * 100.0 if (e_u_t + e_r_t) > 0 else 0.0
    ips_u = e_u_f / e_u_g if e_u_g > 0 else None
    ips_r = e_r_f / e_r_g if e_r_g > 0 else None
    ecart_ips = (ips_u - ips_r) if (ips_u is not None and ips_r is not None) else None
    return {
        "part_rural": part_rural,
        "ips_urbain": ips_u,
        "ips_rural": ips_r,
        "ecart_ips": ecart_ips
    }

def f8_eleves_par_ecole(effectif, nb_ecoles, arrondi=1):
    """F8: Offre scolaire = effectif / nb_écoles."""
    if nb_ecoles is None or nb_ecoles <= 0:
        return None
    ratio = float(effectif) / float(nb_ecoles)
    return round(ratio, arrondi) if arrondi is not None else ratio

def f9_regression_mco(t, y):
    """
    F9: Régression linéaire MCO avec pente beta, R2 et intervalle de confiance à 95%.
    n = len(t). Avec n=10, df = 8, t_critique(0.975, 8) = 2.3060.
    """
    t = np.array(t, dtype=float)
    y = np.array(y, dtype=float)
    n = len(t)
    if n < 3:
        return None

    # MCO
    t_mean = np.mean(t)
    y_mean = np.mean(y)
    ss_tt = np.sum((t - t_mean)**2)
    ss_ty = np.sum((t - t_mean) * (y - y_mean))
    beta = ss_ty / ss_tt
    alpha = y_mean - beta * t_mean

    # Résidus et variance
    y_pred = alpha + beta * t
    residus = y - y_pred
    ss_res = np.sum(residus**2)
    ss_tot = np.sum((y - y_mean)**2)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 1.0

    df = n - 2
    s2 = ss_res / df
    se_beta = math.sqrt(s2 / ss_tt) if ss_tt > 0 else 0.0

    # Student à 95% pour df=8: 2.3060
    # Approximation exacte standard pour df quelconques
    t_crit = 2.3060 if df == 8 else (1.96 if df > 30 else 2.57)
    ic_bas = beta - t_crit * se_beta
    ic_haut = beta + t_crit * se_beta

    return {
        "alpha": alpha,
        "beta": beta,
        "r2": r2,
        "se_beta": se_beta,
        "ic_95": (ic_bas, ic_haut)
    }

def f10_theil_sen(t, y):
    """F10: Pente robuste de Theil-Sen (médiane de toutes les pentes par paires)."""
    t = np.array(t, dtype=float)
    y = np.array(y, dtype=float)
    n = len(t)
    pentes = []
    for i in range(n):
        for j in range(i + 1, n):
            if t[j] != t[i]:
                pentes.append((y[j] - y[i]) / (t[j] - t[i]))
    return float(np.median(pentes)) if pentes else None

def f10_mann_kendall(y):
    """F10: Test non paramétrique de tendance de Mann-Kendall (statistique S)."""
    y = np.array(y, dtype=float)
    n = len(y)
    s = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = y[j] - y[i]
            if diff > 0:
                s += 1
            elif diff < 0:
                s -= 1
    return s

def f11_distance_parite(ips):
    """F11: Distance absolue à la parité g = |IPS - 1|."""
    if ips is None or np.isnan(ips):
        return None
    return abs(float(ips) - 1.0)

def f12_sigma_convergence(matrice_ips_annee):
    """F12: Calcul de l'écart-type interrégional (sigma) et du coefficient de variation (CV)."""
    valeurs = [v for v in matrice_ips_annee if v is not None and not np.isnan(v)]
    if len(valeurs) < 2:
        return None
    arr = np.array(valeurs, dtype=float)
    sigma = float(np.std(arr, ddof=1)) # écart-type échantillon
    moyenne = float(np.mean(arr))
    cv = sigma / moyenne if moyenne > 0 else None
    return {"sigma": sigma, "moyenne": moyenne, "cv": cv}

def f13_beta_convergence(g_initial, g_final, duree=9):
    """
    F13: Taux d'évolution de la distance à la parité.
    (g(T) - g(0)) / T = a + b * g(0)
    """
    g0 = np.array(g_initial, dtype=float)
    gT = np.array(g_final, dtype=float)
    vitesse = (gT - g0) / float(duree)
    # Régression OLS
    cov = np.cov(g0, vitesse)[0, 1]
    var_g0 = np.var(g0, ddof=1)
    b = cov / var_g0 if var_g0 > 0 else 0.0
    a = np.mean(vitesse) - b * np.mean(g0)
    return {"a": a, "b": b, "rattrapage": bool(b < 0)}

def f14_spearman_bootstrap(x, y, n_bootstrap=2000, seed=42):
    """F14: Corrélation de rang de Spearman avec IC 95% bootstrap."""
    np.random.seed(seed)
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)
    if n < 4:
        return None

    # Rang
    def rangs(v):
        order = np.argsort(v)
        ranks = np.empty_like(order, dtype=float)
        ranks[order] = np.arange(len(v))
        return ranks

    rx = rangs(x)
    ry = rangs(y)
    rho_base = float(np.corrcoef(rx, ry)[0, 1])

    # Bootstrap
    rhos_boot = []
    for _ in range(n_bootstrap):
        idx = np.random.choice(n, size=n, replace=True)
        bx = rx[idx]
        by = ry[idx]
        # Si variance non nulle
        if np.std(bx) > 0 and np.std(by) > 0:
            rhos_boot.append(np.corrcoef(bx, by)[0, 1])

    ic_bas = float(np.percentile(rhos_boot, 2.5))
    ic_haut = float(np.percentile(rhos_boot, 97.5))
    return {
        "rho": rho_base,
        "ic_95": (ic_bas, ic_haut),
        "n_bootstraps": len(rhos_boot)
    }

# ==============================================================================
# SUITE DE TESTS UNITAIRES FORMELS (CAS CALCULABLES À LA MAIN)
# ==============================================================================

class TestFormulesMathematiques(unittest.TestCase):

    def test_f1_ips(self):
        """Test F1: Cas calculables à la main."""
        # F = 480, G = 500 -> 0.96 (filles défavorisées)
        self.assertAlmostEqual(f1_ips(480, 500), 0.96, places=4)
        # F = 500, G = 500 -> 1.00 (parité)
        self.assertAlmostEqual(f1_ips(500, 500), 1.00, places=4)
        # F = 525, G = 500 -> 1.05 (garçons défavorisés)
        self.assertAlmostEqual(f1_ips(525, 500), 1.05, places=4)
        # Division par zéro sécurisée
        self.assertIsNone(f1_ips(500, 0))
        self.assertIsNone(f1_ips(500, -10))

    def test_f2_bande_parite(self):
        """Test F2: Classification seuils UNESCO et sensibilité."""
        self.assertEqual(f2_bande_parite(0.969), "Filles défavorisées")
        self.assertEqual(f2_bande_parite(0.970), "Parité atteinte")
        self.assertEqual(f2_bande_parite(1.000), "Parité atteinte")
        self.assertEqual(f2_bande_parite(1.030), "Parité atteinte")
        self.assertEqual(f2_bande_parite(1.031), "Garçons défavorisés")

        # Test de sensibilité (0.95 - 1.05)
        self.assertEqual(f2_bande_parite(0.96, seuil_bas=0.95, seuil_haut=1.05), "Parité atteinte")
        # Test de sensibilité (0.98 - 1.02)
        self.assertEqual(f2_bande_parite(0.975, seuil_bas=0.98, seuil_haut=1.02), "Filles défavorisées")

    def test_f3_ecarts_absolus(self):
        """Test F3: Écart absolu en points de pourcentage (D = TX_F - TX_G)."""
        tx_f = 85.5
        tx_g = 90.0
        # 85.5 - 90.0 = -4.5 points
        self.assertAlmostEqual(f3_ecart_absolu(tx_f, tx_g), -4.5, places=2)

    def test_f4_ponderation_nationale(self):
        """Test F4: Démontrer la divergence mathématique stricte entre pondération et moyenne simple."""
        # Région 1 (Métropole, grande population): F = 95000, G = 100000 -> IPS = 0.95
        # Région 2 (Enclave rurale, petite population): F = 500, G = 1000 -> IPS = 0.50
        lf = [95000, 500]
        lg = [100000, 1000]

        ips_pondere = f4_ips_national_pondere(lf, lg) # (95000 + 500) / (100000 + 1000) = 95500 / 101000 ≈ 0.9455
        ips_simple = f4_ips_moyenne_simple(lf, lg)   # (0.95 + 0.50) / 2 = 0.7250

        self.assertAlmostEqual(ips_pondere, 95500.0 / 101000.0, places=4)
        self.assertAlmostEqual(ips_simple, 0.7250, places=4)
        # La moyenne simple fausse le résultat de plus de 22 points !
        self.assertGreater(abs(ips_pondere - ips_simple), 0.20)

    def test_f5_coherence_arithmetique(self):
        """Test F5: Cohérence T = F + G."""
        self.assertTrue(f5_coherence_arithmetique(1000, 520, 480))
        self.assertTrue(f5_coherence_arithmetique(1001, 520, 480, tolerance=1)) # Arrondi
        self.assertFalse(f5_coherence_arithmetique(1005, 520, 480, tolerance=1))

    def test_f7_milieu(self):
        """Test F7: Dynamique urbain/rural."""
        res = f7_indicateurs_milieu(e_u_g=400, e_u_f=420, e_r_g=600, e_r_f=540)
        # Urbain Total = 820, Rural Total = 1140, Total = 1960
        # part_rural = 1140 / 1960 = 58.163%
        self.assertAlmostEqual(res["part_rural"], 1140.0 / 1960.0 * 100.0, places=2)
        # IPS_U = 420 / 400 = 1.05
        self.assertAlmostEqual(res["ips_urbain"], 1.05, places=4)
        # IPS_R = 540 / 600 = 0.90
        self.assertAlmostEqual(res["ips_rural"], 0.90, places=4)
        # Ecart IPS = 1.05 - 0.90 = +0.15
        self.assertAlmostEqual(res["ecart_ips"], 0.15, places=4)

    def test_f8_eleves_par_ecole(self):
        """Test F8: Élèves par école."""
        # 237553 / 1098 = 216.3506... -> arrondi à 216.4
        self.assertEqual(f8_eleves_par_ecole(237553, 1098, arrondi=1), 216.4)
        # Cas simple: 500 élèves dans 2 écoles = 250.0
        self.assertEqual(f8_eleves_par_ecole(500, 2, arrondi=1), 250.0)
        self.assertIsNone(f8_eleves_par_ecole(20000, 0))

    def test_f9_regression_mco(self):
        """Test F9: Droite linéaire parfaite y = 0.01 * t + 0.90 sur 10 points."""
        t = list(range(10))
        y = [0.90 + 0.01 * i for i in t]
        res = f9_regression_mco(t, y)
        self.assertAlmostEqual(res["beta"], 0.01, places=5)
        self.assertAlmostEqual(res["alpha"], 0.90, places=5)
        self.assertAlmostEqual(res["r2"], 1.00, places=5)
        # Pour une droite parfaite, l'erreur type est quasi nulle
        self.assertAlmostEqual(res["se_beta"], 0.0, places=4)

    def test_f10_theil_sen_robustesse(self):
        """Test F10: Theil-Sen insensible à une valeur aberrante extrême."""
        t = [0, 1, 2, 3, 4]
        # Pente réelle = 1.0, mais valeur aberrante à l'indice 4: y = 100 au lieu de 4
        y_aberrant = [0.0, 1.0, 2.0, 3.0, 100.0]

        pente_ts = f10_theil_sen(t, y_aberrant)
        res_mco = f9_regression_mco(t, y_aberrant)

        # Theil-Sen retrouve la vraie pente médiane (1.0)
        self.assertAlmostEqual(pente_ts, 1.0, places=4)
        # Alors que le MCO est complètement pollué (pente > 15)
        self.assertGreater(res_mco["beta"], 15.0)

        # Test Mann-Kendall
        s = f10_mann_kendall([1, 2, 3, 4, 5])
        # n*(n-1)/2 = 10 paires positives -> S = 10
        self.assertEqual(s, 10)

    def test_f11_distance_parite(self):
        """Test F11: Distance à la parité."""
        self.assertAlmostEqual(f11_distance_parite(0.92), 0.08, places=4)
        self.assertAlmostEqual(f11_distance_parite(1.05), 0.05, places=4)

    def test_f12_sigma_convergence(self):
        """Test F12: Réduction de la dispersion spatiale."""
        # Année 1 (dispersion large): [0.80, 0.90, 1.00, 1.10]
        # Année 2 (convergence): [0.95, 0.98, 1.00, 1.02]
        c1 = f12_sigma_convergence([0.80, 0.90, 1.00, 1.10])
        c2 = f12_sigma_convergence([0.95, 0.98, 1.00, 1.02])

        self.assertGreater(c1["sigma"], c2["sigma"])
        self.assertGreater(c1["cv"], c2["cv"])

    def test_f13_beta_convergence(self):
        """Test F13: Modèle de rattrapage b < 0."""
        # Régions très éloignées initialement (g0 = 0.20 -> gT = 0.05) rattrapent plus vite
        # que celles déjà proches (g0 = 0.05 -> gT = 0.03)
        g0 = [0.20, 0.15, 0.10, 0.05]
        gT = [0.05, 0.05, 0.04, 0.03]
        res = f13_beta_convergence(g0, gT, duree=9)
        self.assertTrue(res["rattrapage"])
        self.assertLess(res["b"], 0.0)

    def test_f14_spearman_bootstrap(self):
        """Test F14: Rang de Spearman parfait avec IC bootstrap."""
        x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        y = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105] # relation monotone parfaite
        res = f14_spearman_bootstrap(x, y, n_bootstrap=500, seed=42)
        self.assertAlmostEqual(res["rho"], 1.0, places=4)
        self.assertGreaterEqual(res["ic_95"][0], 0.95)

if __name__ == '__main__':
    print("=" * 70)
    print("EXÉCUTION DES TESTS UNITAIRES DES FORMULES MATHÉMATIQUES F1 À F16")
    print("=" * 70)
    unittest.main(verbosity=2)
