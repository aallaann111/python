import pandas as pd
import os

def filter_and_rename_csv(input_csv, rename_dict):
    df = pd.read_csv(input_csv)
    missing_columns = [col for col in rename_dict.keys() if col not in df.columns]
    if missing_columns:
        print(f"Les colonnes suivantes sont manquantes dans le fichier d'entrée : {missing_columns}")
        return

    df_filtered = df[rename_dict.keys()].rename(columns=rename_dict)
    output_csv = f"{os.path.splitext(input_csv)[0]}_filtered.csv"
    df_filtered.to_csv(output_csv, index=False)
    print(f"Le fichier CSV filtré et renommé a été sauvegardé avec succès sous : {output_csv}")