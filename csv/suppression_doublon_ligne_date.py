import pandas as pd
import os

csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")

try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
    exit()

print("Colonnes disponibles :", ', '.join(data.columns))

date_attribute = input("Entrez l'attribut de type date pour sélectionner le plus récent ou le plus ancien: ")

if date_attribute not in data.columns:
    print(f"Erreur : La colonne '{date_attribute}' n'existe pas dans le fichier.")
    exit()

attributes = input("Entrez les attributs pour identifier les doublons, séparés par des virgules (ex: nom,prenom): ")
attributes = [attr.strip() for attr in attributes.split(",")]

for attribute in attributes:
    if attribute not in data.columns:
        print(f"Erreur : La colonne '{attribute}' n'existe pas dans le fichier.")
        exit()

date_choice = input("Voulez-vous garder la ligne avec la date la plus récente ou la plus ancienne ? (entrez 'recent' ou 'ancien'): ").strip().lower()

if date_choice not in ['recent', 'ancien']:
    print("Erreur : Veuillez entrer 'récent' pour la date la plus récente ou 'ancien' pour la plus ancienne.")
    exit()

try:
    data[date_attribute] = pd.to_datetime(data[date_attribute])
except Exception as e:
    print(f"Erreur lors de la conversion de '{date_attribute}' en format date : {e}")
    exit()

output_folder = "resultat"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
data_sorted = data.sort_values(by=attributes + [date_attribute], ascending=(date_choice == 'ancien'))

deduplicated_data = data_sorted.drop_duplicates(subset=attributes, keep='first')

output_file = output_folder + "/deduplicated_" + csv_file
deduplicated_data.to_csv(output_file, index=False)
print(f"Fichier sans doublons '{output_file}' créé avec succès.")