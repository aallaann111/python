import pandas as pd
import os

csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")

try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
    exit()

print("Colonnes disponibles :", ', '.join(data.columns))

reference_column = input("Entrez le nom de la colonne de référence : ")
duplicate_column = input("Entrez le nom de la colonne contenant les doublons : ")

if reference_column not in data.columns or duplicate_column not in data.columns:
    print("Erreur : Une des colonnes spécifiées n'existe pas dans le fichier.")
    exit()

output_folder = "resultat"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

data[duplicate_column] = data.apply(
    lambda row: '' if row[duplicate_column] == row[reference_column] else row[duplicate_column],
    axis=1
)

output_file = os.path.join(output_folder, "deduplicated_colonne_" + csv_file)
data.to_csv(output_file, index=False)
print(f"Fichier sans doublons '{output_file}' créé avec succès.")
