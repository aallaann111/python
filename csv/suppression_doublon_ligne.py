import pandas as pd
import os

csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")

try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
    exit()

print("Colonnes disponibles :", ', '.join(data.columns))
attributes = input("Entrez les attributs pour identifier les doublons, séparés par des virgules (ex: nom,prenom): ")
attributes = [attr.strip() for attr in attributes.split(",")]

output_folder = "resultat"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for attribute in attributes:
    if attribute not in data.columns:
        print(f"Erreur : La colonne '{attribute}' n'existe pas dans le fichier.")
        exit()

deduplicated_data = data.drop_duplicates(subset=attributes)

output_file = output_folder + "/deduplicated_ligne_date_" + csv_file
deduplicated_data.to_csv(output_file, index=False)
print(f"Fichier sans doublons '{output_file}' créé avec succès.")