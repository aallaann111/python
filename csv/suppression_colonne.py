import pandas as pd
import os

csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")

try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
    exit()

print("Colonnes disponibles :", ', '.join(data.columns))
columns_to_process = input("Entrez les noms des colonnes à traiter, séparés par des virgules : ")
columns_to_process = [col.strip() for col in columns_to_process.split(",")]

for column in columns_to_process:
    if column not in data.columns:
        print(f"Erreur : La colonne '{column}' n'existe pas dans le fichier.")
        exit()
        
for column in columns_to_process:
    choice = input(f"Voulez-vous supprimer entièrement la colonne '{column}' ou seulement son contenu ? (entrez 'colonne' ou 'contenu'): ").strip().lower()
    
    if choice == 'colonne':
        data = data.drop(columns=[column])
    elif choice == 'contenu':
        data[column] = ''
    else:
        print(f"Option invalide pour la colonne '{column}'. Aucune action prise pour cette colonne.")

output_folder = "resultat"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, "delete_colonne_" + csv_file)
data.to_csv(output_file, index=False)
print(f"Fichier modifié '{output_file}' créé avec succès.")
