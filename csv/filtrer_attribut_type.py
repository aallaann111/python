import pandas as pd
import os

csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")

try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
    exit()

print("Colonnes disponibles :", ', '.join(data.columns))
attribute = input("Entrez l'attribut selon lequel vous voulez trier: ")

if attribute not in data.columns:
    print(f"Erreur : La colonne '{attribute}' n'existe pas dans le fichier.")
    exit()

output_folder = "resultat"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

unique_values = data[attribute].unique()
for value in unique_values:
    filtered_data = data[data[attribute] == value]
    
    output_file = f"{output_folder}/{value}.csv"
    
    filtered_data.to_csv(output_file, index=False)
    print(f"Fichier '{output_file}' créé avec les lignes ayant '{attribute}' = '{value}'.")

print("Opération terminée !")
