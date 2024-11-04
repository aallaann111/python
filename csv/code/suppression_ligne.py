import pandas as pd
import os

csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")

try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
    exit()

print("Colonnes disponibles :", ', '.join(data.columns))

columns_to_filter = {}

while True:
    column = input("Entrez le nom de la colonne pour filtrer (ou appuyez sur Entrée pour terminer) : ").strip()
    if column == "":
        break
    if column not in data.columns:
        print(f"Erreur : La colonne '{column}' n'existe pas dans le fichier.")
        continue
    values = input(f"Entrez les valeurs à supprimer dans '{column}', séparées par des virgules : ")
    values = [value.strip() for value in values.split(",")]
    columns_to_filter[column] = values

for column, values in columns_to_filter.items():
    data = data[~data[column].isin(values)]

base_filename = os.path.splitext(os.path.basename(csv_file))[0]

output_folder = "resultat"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, f"delete_ligne_{base_filename}.csv")
data.to_csv(output_file, index=False)
print(f"Fichier filtré '{output_file}' créé avec succès.")