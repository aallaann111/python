import pandas as pd
import os

def filter_csv_by_attribute(csv_file, attribute, output_folder="resultat"):
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
        return

    if attribute not in data.columns:
        print(f"Erreur : La colonne '{attribute}' n'existe pas dans le fichier.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    unique_values = data[attribute].unique()
    for value in unique_values:
        filtered_data = data[data[attribute] == value]
        output_file = f"{output_folder}/{value}.csv"
        filtered_data.to_csv(output_file, index=False)
        print(f"Fichier '{output_file}' créé avec les lignes ayant '{attribute}' = '{value}'.")

    print("Opération terminée !")
