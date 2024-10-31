import pandas as pd
import os

def process_csv_columns(csv_file, columns_to_process, actions):
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{csv_file}' n'a pas été trouvé.")
        return None

    # Vérification des colonnes
    for column in columns_to_process:
        if column not in data.columns:
            print(f"Erreur : La colonne '{column}' n'existe pas dans le fichier.")
            return None

    # Traitement des colonnes
    for column, action in actions.items():
        if action == 'colonne':
            data = data.drop(columns=[column])
        elif action == 'contenu':
            data[column] = ''
        else:
            print(f"Option invalide pour la colonne '{column}'. Aucune action prise pour cette colonne.")

    # Création du fichier de sortie
    base_filename = os.path.splitext(os.path.basename(csv_file))[0]
    output_folder = "resultat"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, f"delete_colonne_{base_filename}.csv")
    data.to_csv(output_file, index=False)
    return output_file

# Exemple d'utilisation:
if __name__ == "__main__":
    csv_file = input("Entrez le nom du fichier CSV (ex: fichier.csv): ")
    print("Colonnes disponibles :", ', '.join(pd.read_csv(csv_file).columns))
    
    columns_to_process = input("Entrez les noms des colonnes à traiter, séparés par des virgules : ")
    columns_to_process = [col.strip() for col in columns_to_process.split(",")]
    
    actions = {}
    for column in columns_to_process:
        action = input(f"Pour '{column}', entrez 'colonne' ou 'contenu': ").strip().lower()
        actions[column] = action
    
    result = process_csv_columns(csv_file, columns_to_process, actions)
    if result:
        print(f"Fichier modifié '{result}' créé avec succès.")
