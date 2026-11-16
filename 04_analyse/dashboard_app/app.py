# « On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo
"""
Application Interactive Streamlit — Défi 2 : Disparités d'accès à l'éducation au Burkina Faso.
Équipe : TEAMDATALYS (Data Challenge Burkina 2026)
Livrable réexécutable en environnement local autonome.
"""

import os
import streamlit as st
import pandas as pd
import altair as alt

# Configuration de la page
st.set_page_config(
    page_title="Disparités Éducatives Burkina Faso (2015-2025)",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Chargement des données
@st.cache_data
def charger_donnees():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    transfo_dir = os.path.join(os.path.dirname(base_dir), "03_transformation")
    analyse_dir = base_dir
    
    panel_reg = pd.read_csv(
        os.path.join(transfo_dir, "TEAMDATALYS_03-transformation_D2_architect_panel-regional-education-10ans_v1.csv"),
        sep=";"
    )
    panel_mil = pd.read_csv(
        os.path.join(transfo_dir, "TEAMDATALYS_03-transformation_D2_engineer_panel-national-milieu-10ans_v1.csv"),
        sep=";"
    )
    pentes = pd.read_csv(
        os.path.join(analyse_dir, "TEAMDATALYS_04-analyse_D2_scientist_pentes-evolution-convergence_v1.csv"),
        sep=";"
    )
    classement = pd.read_csv(
        os.path.join(analyse_dir, "TEAMDATALYS_04-analyse_D2_analyst_classement-regions-parite_v1.csv"),
        sep=";"
    )
    return panel_reg, panel_mil, pentes, classement

panel_reg, panel_mil, pentes, classement = charger_donnees()

# 2. Barre latérale (Filtres)
st.sidebar.title("Paramètres et filtres")
st.sidebar.markdown("**Équipe :** TEAMDATALYS  \n**Défi :** DÉFI 2 (Parité F/G & Milieu)")

OPTION_PERIODE = "Total 2015–2025"
annees_dispos = sorted(panel_reg["annee_scolaire"].unique().tolist()) + [OPTION_PERIODE]
annee_selectionnee = st.sidebar.selectbox(
    "Sélectionnez l'année scolaire :",
    annees_dispos,
    index=len(annees_dispos) - 2,
    key="filtre_annee",
)
if annee_selectionnee == OPTION_PERIODE:
    st.sidebar.caption(
        "Sur la période, les effectifs sont cumulés et les taux/indices sont "
        "des moyennes annuelles."
    )

regions_dispos = ["TOUTES LES RÉGIONS"] + sorted(panel_reg["region"].unique().tolist())
region_selectionnee = st.sidebar.selectbox(
    "Focus régional :", regions_dispos, index=0, key="filtre_region"
)

# Appliquer les filtres avant l'affichage des onglets : chaque widget Streamlit
# relance le script, et les vues doivent toutes utiliser la même sélection.
if annee_selectionnee == OPTION_PERIODE:
    # Les effectifs sont cumulés sur les 10 années; les taux et indices sont
    # moyennés sur la période afin de ne pas additionner des pourcentages.
    colonnes_somme = [
        "primaire_garcons", "primaire_filles", "primaire_total",
        "ecoles_public", "ecoles_prive", "ecoles_total",
        "prescolaire_garcons", "prescolaire_filles", "prescolaire_total",
    ]
    colonnes_moyenne = [
        col for col in panel_reg.select_dtypes(include="number").columns
        if col not in colonnes_somme and col not in {"annee_debut", "annee_fin"}
    ]
    aggregation = {col: "sum" for col in colonnes_somme if col in panel_reg.columns}
    aggregation.update({col: "mean" for col in colonnes_moyenne})
    df_annee = panel_reg.groupby("region", as_index=False).agg(aggregation)
    df_annee["annee_scolaire"] = OPTION_PERIODE
    df_annee["primaire_ratio_f_g"] = (
        df_annee["primaire_filles"] / df_annee["primaire_garcons"]
    )
    for col_ips, col_profil in [
        ("ips_tba", "profil_parite_tba"),
        ("ips_tbs", "profil_parite_tbs"),
        ("ips_tap", "profil_parite_tap"),
    ]:
        df_annee[col_profil] = "Parité atteinte"
        df_annee.loc[df_annee[col_ips] < 0.97, col_profil] = "Filles défavorisées"
        df_annee.loc[df_annee[col_ips] > 1.03, col_profil] = "Garçons défavorisés"
else:
    df_annee = panel_reg[panel_reg["annee_scolaire"] == annee_selectionnee].copy()
if region_selectionnee != "TOUTES LES RÉGIONS":
    df_annee = df_annee[df_annee["region"] == region_selectionnee]

if annee_selectionnee == OPTION_PERIODE:
    colonnes_mil_moyenne = panel_mil.select_dtypes(include="number").columns
    df_mil_annee = pd.DataFrame([panel_mil[colonnes_mil_moyenne].mean()])
else:
    df_mil_annee = panel_mil[panel_mil["annee_scolaire"] == annee_selectionnee]
if df_annee.empty or df_mil_annee.empty:
    st.error("Aucune donnée ne correspond à l'année et à la région sélectionnées.")
    st.stop()

st.sidebar.markdown("---")
st.sidebar.markdown("""
### Norme de parité UNESCO
- **IPS < 0,97** : *Filles défavorisées*
- **0,97 ≤ IPS ≤ 1,03** : *Parité atteinte*
- **IPS > 1,03** : *Garçons défavorisés*
""")

# 3. En-tête principal
st.title("Analyse des disparités d'accès à l'éducation au Burkina Faso")
st.markdown("#### *Évolution sur 10 cohortes scolaires (2015/2016 à 2024/2025) à partir des statistiques officielles de la DGESS*")

# 4. Onglets thématiques
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Vue d'ensemble et carte",
    "2. Parité dans les deux sens",
    "3. Écart urbain / rural",
    "4. Dynamique et convergence",
    "5. Cadrage orpaillage et limites"
])

# --- ONGLET 1 : VUE D'ENSEMBLE ---
with tab1:
    libelle_perimetre = "national" if region_selectionnee == "TOUTES LES RÉGIONS" else region_selectionnee
    st.header(f"Bilan {libelle_perimetre} — {annee_selectionnee}")
    df_mil_annee = df_mil_annee.iloc[0]
    
    tot_nat = df_annee["primaire_total"].sum()
    tot_g = df_annee["primaire_garcons"].sum()
    tot_f = df_annee["primaire_filles"].sum()
    ips_moyen = df_annee["ips_tbs"].mean()
    
    reg_min_ips = df_annee.loc[df_annee["ips_tbs"].idxmin()]
    reg_max_ips = df_annee.loc[df_annee["ips_tbs"].idxmax()]
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Effectif Primaire Total", f"{tot_nat:,}".replace(",", " "))
    c2.metric("Part des Élèves en Milieu Rural", f"{df_mil_annee['part_rural_pct']:.1f} %")
    if region_selectionnee == "TOUTES LES RÉGIONS":
        c3.metric("Région la plus défavorable aux Filles", f"{reg_min_ips['region']} (IPS {reg_min_ips['ips_tbs']:.3f})")
        c4.metric("Région la plus défavorable aux Garçons", f"{reg_max_ips['region']} (IPS {reg_max_ips['ips_tbs']:.3f})")
    else:
        region_ligne = df_annee.iloc[0]
        c3.metric("IPS de la région sélectionnée", f"{region_ligne['ips_tbs']:.3f}")
        c4.metric("Profil de parité", str(region_ligne["profil_parite_tbs"]))
    
    st.markdown("---")
    st.subheader(f"Tableau de bord — {libelle_perimetre} ({annee_selectionnee})")
    
    cols_a_afficher = [
        "region", "primaire_total", "primaire_ratio_f_g", "ips_tbs", "profil_parite_tbs",
        "tbs_garcons", "tbs_filles", "eleves_par_ecole", "cep_reussite_total"
    ]
    df_table = df_annee[cols_a_afficher].copy()
    df_table.columns = [
        "Région", "Effectif Total", "Ratio F/G (Inscrits)", "IPS du TBS", "Diagnostic Parité",
        "TBS Garçons (%)", "TBS Filles (%)", "Élèves / École", "Taux CEP (%)"
    ]
    st.dataframe(df_table.sort_values(by="IPS du TBS", ascending=True), use_container_width=True)

# --- ONGLET 2 : PARITÉ DANS LES DEUX SENS ---
with tab2:
    st.header("Analyse de la Parité Fille-Garçon dans les DEUX SENS")
    st.markdown("""
    L'analyse conventionnelle se borne à dénoncer le déficit de scolarisation féminin. 
    Notre approche met en lumière les **deux visages de l'inégalité** :
    1. **Filles défavorisées** (IPS < 0,97) : Contraintes socioculturelles, mariage précoce, vulnérabilité sahélienne.
    2. **Garçons défavorisés** (IPS > 1,03) : Décrochage précoce, attraction vers les travaux manuels, agricoles ou l'orpaillage.
    """)
    
    # Graphique barres horizontales IPS par région
    chart_parite = alt.Chart(df_annee).mark_bar().encode(
        x=alt.X("ips_tbs:Q", title="Indice de Parité des Sexes (TBS)", scale=alt.Scale(domain=[0.85, 1.15])),
        y=alt.Y("region:N", title="Région", sort="-x"),
        color=alt.Color("profil_parite_tbs:N", scale=alt.Scale(
            domain=["Filles défavorisées", "Parité atteinte", "Garçons défavorisés"],
            range=["#d9534f", "#5cb85c", "#0275d8"]
        ), title="Profil de Parité (UNESCO)"),
        tooltip=["region", "ips_tbs", "profil_parite_tbs", "tbs_garcons", "tbs_filles"]
    ).properties(
        height=max(140, 32 * len(df_annee)),
        title=f"Situation de {libelle_perimetre} en {annee_selectionnee}",
    )
    
    # Lignes de seuils
    ligne_basse = alt.Chart(pd.DataFrame({'x': [0.97]})).mark_rule(strokeDash=[4, 4], color="#d9534f").encode(x='x:Q')
    ligne_haute = alt.Chart(pd.DataFrame({'x': [1.03]})).mark_rule(strokeDash=[4, 4], color="#0275d8").encode(x='x:Q')
    
    st.altair_chart(chart_parite + ligne_basse + ligne_haute, use_container_width=True)
    
    st.info("**Observation clé :** Les lignes pointillées délimitent le couloir d'équité UNESCO [0,97 ; 1,03]. Toute région située à gauche présente un déficit féminin ; toute région située à droite présente un déficit masculin.")

# --- ONGLET 3 : ÉCART URBAIN / RURAL ---
with tab3:
    st.header("Dynamique Comparative : Villes vs Campagnes (National)")
    st.warning("**Rappel méthodologique :** Les statistiques scolaires de la DGESS ventilent le milieu au niveau national uniquement (Feuil3). Aucun croisement région × milieu n'existe dans le jeu de données officiel.")
    
    # Graphique d'évolution comparée IPS Urbain vs Rural
    df_mil_long = pd.melt(
        panel_mil,
        id_vars=["annee_scolaire", "annee_debut"],
        value_vars=["ips_urbain", "ips_rural"],
        var_name="Milieu",
        value_name="IPS"
    )
    df_mil_long["Milieu"] = df_mil_long["Milieu"].map({"ips_urbain": "Milieu Urbain", "ips_rural": "Milieu Rural"})
    
    chart_mil = alt.Chart(df_mil_long).mark_line(point=True).encode(
        x=alt.X("annee_scolaire:N", title="Année Scolaire"),
        y=alt.Y("IPS:Q", title="Indice de Parité des Sexes (F/G)", scale=alt.Scale(domain=[0.90, 1.05])),
        color=alt.Color("Milieu:N", scale=alt.Scale(domain=["Milieu Urbain", "Milieu Rural"], range=["#e67e22", "#27ae60"])),
        tooltip=["annee_scolaire", "Milieu", "IPS"]
    ).properties(height=400, title="Convergence spectaculaire du monde rural vers la parité (2015-2025)")
    
    st.altair_chart(chart_mil, use_container_width=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        #### Enseignements majeurs sur le milieu :
        - **En 2015-2016** : Le milieu rural accusait un retard critique (**IPS = 0,920** contre 1,011 en ville, soit un fossé de **0,091 point**).
        - **En 2024-2025** : Le milieu rural a comblé l'essentiel de son retard pour atteindre **0,972**, entrant dans la zone de parité équilibrée.
        - **Érosion du poids rural** : La part des élèves scolarisés en milieu rural est passée de **72,8 %** en 2015 à **63,5 %** en 2025, traduisant l'urbanisation et les flux de déplacement.
        """)
    with c2:
        st.dataframe(panel_mil[["annee_scolaire", "ips_urbain", "ips_rural", "ecart_ips_urbain_rural", "part_rural_pct"]], use_container_width=True)

# --- ONGLET 4 : DYNAMIQUE & CONVERGENCE ---
with tab4:
    st.header("Trajectoires Régionales sur 10 ans et Test de Convergence")
    
    st.subheader(r"1. Test formel de $\sigma$-convergence (Dispersion interrégionale)")
    st.markdown("""
    L'écart-type de l'IPS entre les 13 régions mesure l'inégalité spatiale globale à chaque rentrée scolaire.
    """)
    
    pentes_affichees = pentes
    if region_selectionnee != "TOUTES LES RÉGIONS":
        pentes_affichees = pentes_affichees[pentes_affichees["region"] == region_selectionnee]
    st.dataframe(
        pentes_affichees[["region", "ips_2015_2016", "ips_2024_2025", "delta_total_10ans", "pente_annuelle_ips", "trajectoire_ips"]]
        .sort_values(by="pente_annuelle_ips", ascending=False),
        use_container_width=True,
    )
    
    # Courbe d'évolution pour la région sélectionnée
    if region_selectionnee != "TOUTES LES RÉGIONS":
        df_reg_sel = panel_reg[panel_reg["region"] == region_selectionnee]
        st.subheader(f"Trajectoire détaillée pour la région : {region_selectionnee}")
        chart_reg = alt.Chart(df_reg_sel).mark_line(point=True, color="#2980b9").encode(
            x=alt.X("annee_scolaire:N", title="Année"),
            y=alt.Y("ips_tbs:Q", title="IPS du TBS", scale=alt.Scale(domain=[0.85, 1.15])),
            tooltip=["annee_scolaire", "ips_tbs", "tbs_garcons", "tbs_filles", "profil_parite_tbs"]
        ).properties(height=350)
        st.altair_chart(chart_reg, use_container_width=True)

# --- ONGLET 5 : ORPAILLAGE & LIMITES ---
with tab5:
    st.header("Cadrage Contextuel : Orpaillage, Sécurité et Limites Scientifiques")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Orpaillage artisanal : hypothèse exploratoire")
        st.markdown("""
        - **Absence de registre dans les données** : Le DataPack ne comporte aucun recensement géolocalisé d'orpaillage.
        - **Hypothèse documentée** : Dans les régions minières artisanales (Sud-Ouest, Cascades, Centre-Ouest), les garçons sont précocement retirés de l'école pour travailler sur les sites d'extraction.
        - **Confrontation empirique** : Le Sud-Ouest affichait en 2015 un IPS record de **1,063** (déficit de garçons).
        - **Prudence méthodologique** : Il s'agit d'une association qualitative documentée par les rapports du MENAPLN et de l'INSD, jamais d'une causalité prouvée.
        """)
    with col_b:
        st.subheader("Limites méthodologiques formelles")
        st.markdown("""
        1. **Échelle géographique** : Analyse menée à l'échelle des 13 régions historiques (impossible d'avoir les 45 provinces de façon continue sans extraire des centaines de PDF).
        2. **Absence de croisement Région × Milieu** : La DGESS fournit le milieu uniquement au niveau national consolidé.
        3. **Cycle d'enseignement** : Analyse restreinte au préscolaire et au primaire (post-primaire et secondaire non documentés en série temporelle).
        4. **Taux officiels** : Les TBS/TBA reposent sur les projections démographiques de l'INSD, non recalculées par nous-mêmes.
        """)

# 5. Pied de page obligatoire
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #555; padding: 15px; font-style: italic;">
« On ne développe pas, on se développe » — l’éthique de l’éducation en Afrique : sur les traces de Joseph Ki-Zerbo<br>
<strong>Data Challenge Burkina (Édition Éducation 2026) — Solution développée par Team Datalys (Défi 2)</strong>
</div>
""", unsafe_allow_html=True)
