import pandas as pd

csv_path = input("Entrez le chemin de votre fichier CSV : ")

try:
    data = pd.read_csv(csv_path)
    
    print("Colonnes disponibles :")
    for col in data.columns:
        print(f"- {col}")
    
    column_name = input("Entrez le nom de la colonne où chercher les doublons : ")
    
    if column_name not in data.columns:
        print("La colonne spécifiée n'existe pas dans le fichier.")
    else:
        duplicate_counts = data[column_name].value_counts()
        duplicates = duplicate_counts[duplicate_counts > 1]
        
        output_file = "doublons.txt"
        with open(output_file, "w") as f:
            f.write("Valeurs en doublon et leur nombre d'occurrences :\n")
            for value, count in duplicates.items():
                f.write(f"{value} : {count} fois\n")
        
        print(f"Le fichier '{output_file}' a été créé avec les valeurs en doublons et leurs occurrences.")
except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")
except pd.errors.EmptyDataError:
    print("Le fichier spécifié est vide ou invalide.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
