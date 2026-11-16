// Exemple de requête Power Query M pour le panel régional.
// Dans chaque requête, remplacez le chemin absolu par celui de votre dossier Data.
let
    Source = Csv.Document(
        File.Contents("C:\Users\VotreNom\Desktop\Data\03_transformation\TEAMDATALYS_03-transformation_D2_architect_panel-regional-education-10ans_v1.csv"),
        [Delimiter=";", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    EnTetes = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(
        EnTetes,
        {
            {"region", type text},
            {"annee_scolaire", type text},
            {"annee_debut", Int64.Type},
            {"annee_fin", Int64.Type},
            {"primaire_garcons", Int64.Type},
            {"primaire_filles", Int64.Type},
            {"primaire_total", Int64.Type},
            {"ips_tbs", type number}
        },
        "fr-FR"
    )
in
    Types

// Deuxième requête : PanelNationalMilieu.
// Créez une requête vide distincte, puis adaptez le nom de fichier et les types.
let
    Source = Csv.Document(
        File.Contents("C:\Users\VotreNom\Desktop\Data\03_transformation\TEAMDATALYS_03-transformation_D2_engineer_panel-national-milieu-10ans_v1.csv"),
        [Delimiter=";", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    EnTetes = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(EnTetes, {{"annee_scolaire", type text}}, "fr-FR")
in
    Types
