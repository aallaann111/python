# Documentation

- [1. Filtrer Attribut Type](#1-filtrer_attribut_typefiltrer_attribut_typepy)
- [2. Suppression Doublon Colonne](#2-suppression_doublon_colonnesuppression_doublon_colonnepy)
- [3. Suppression Doublon Ligne](#3-suppression_doublon_lignesuppression_doublon_lignepy)
- [4. Suppression Doublon Ligne Date](#4-suppression_doublon_ligne_datesuppression_doublon_ligne_datepy)
- [5. Suppression Ligne](#5-suppression_lignesuppression_lignepy)
- [6. Suppression Colonne](#6-suppression_colonnesuppression_colonnepy)

## Prérequis

- La bibliothèque `pandas` pour manipuler les données.dossiers

Installez `pandas` avec la commande suivante si nécessaire :

```bash
pip install pandas
```


# 1. [filtrer_attribut_type](filtrer_attribut_type.py)

### Description

Ce script Python permet de lire un fichier CSV, de filtrer ses données en fonction d'une colonne choisie par l'utilisateur, puis de sauvegarder chaque sous-ensemble de données dans des fichiers CSV distincts. Le fichier de sortie est nommé en fonction de la valeur unique de l'attribut sélectionné. Ce script est utile pour organiser ou analyser des sous-ensembles spécifiques de données d'un CSV de manière structurée.

### Utilisation

1. **Préparez le fichier CSV** : Assurez-vous d'avoir un fichier CSV dans le même répertoire que le script ou notez son chemin d'accès.

2. **Exécution du script** :
   Exécutez le script avec la commande suivante dans votre terminal :
   ```bash
   python filtrer_attribut_type.py
   ```

3. **Instructions interactives** :
   - Le script vous demandera le **nom du fichier CSV** (par exemple `data.csv`). Entrez le nom du fichier.
   - Ensuite, le script affichera les colonnes disponibles dans le fichier.
   - Choisissez une **colonne** pour trier et filtrer les données. Par exemple, si votre fichier contient une colonne `catégorie`, saisissez `catégorie`.

4. **Résultat** :
   - Le script crée un dossier nommé `resultat` dans le même répertoire.
   - Pour chaque valeur unique dans la colonne sélectionnée, un fichier CSV sera créé dans le dossier `resultat`, avec uniquement les lignes correspondantes à cette valeur. Par exemple, pour un fichier avec une colonne `catégorie` contenant les valeurs `A`, `B`, et `C`, trois fichiers (`A.csv`, `B.csv`, `C.csv`) seront générés dans le dossier `resultat`.
   - Le nom de chaque fichier est basé sur la valeur unique de l'attribut choisi pour filtrer.

5. **Fin de l'opération** :
   Une fois l'opération terminée, le script affiche un message pour indiquer la fin du processus.

### Exemple

Supposons un fichier `produits.csv` avec la structure suivante :

| produit_id | nom      | catégorie |
|------------|----------|-----------|
| 1          | Chaise   | Meubles   |
| 2          | Table    | Meubles   |
| 3          | Crayon   | Bureau    |

- **Nom du fichier** : `produits.csv`
- **Colonne à trier** : `catégorie`

Le script créera deux fichiers dans le dossier `resultat` :
- `Meubles.csv` contenant les produits avec la catégorie "Meubles".
- `Bureau.csv` contenant les produits avec la catégorie "Bureau".

# test

# 2. [suppression_doublon_colonne](suppression_doublon_colonne.py)

### Description

Ce script Python permet de traiter un fichier CSV en supprimant les valeurs redondantes dans une colonne spécifique en fonction d'une colonne de référence. Lorsqu'une valeur dans la colonne de doublons est identique à celle de la colonne de référence pour une ligne donnée, cette valeur est remplacée par une chaîne vide, signalant une redondance dans les données.

### Utilisation

1. **Préparez le fichier CSV** : Assurez-vous d'avoir un fichier CSV dans le même répertoire que le script ou notez son chemin d'accès.

2. **Exécution du script** :
   Exécutez le script avec la commande suivante dans votre terminal :
   ```bash
   python suppression_doublon_colonne.py
   ```

3. **Instructions interactives** :
   - Le script vous demandera le **nom du fichier CSV** (par exemple `data.csv`). Entrez le nom du fichier.
   - Il affichera ensuite les colonnes disponibles dans le fichier.
   - Sélectionnez une **colonne de référence** qui sera comparée à une **colonne contenant les doublons**.
   - Le script vérifie l'existence de ces colonnes dans le fichier.

4. **Résultat** :
   - Le script crée un dossier nommé `resultat` dans le même répertoire.
   - Un fichier CSV nommé `deduplicated_colonne_<nom_du_fichier_original>.csv` sera généré dans le dossier `resultat`, avec les valeurs redondantes supprimées dans la colonne spécifiée.

5. **Fin de l'opération** :
   Une fois l'opération terminée, le script affiche un message confirmant la création du fichier sans doublons.

### Exemple

Supposons un fichier `ventes.csv` avec la structure suivante :

| id | produit   | nom_produit | prix |
|----|-----------|-------------|------|
| 1  | Chaise    | Chaise      | 50   |
| 2  | Table     | Table       | 100  |
| 3  | Canapé    | Sofa        | 300  |

- **Nom du fichier** : `ventes.csv`
- **Colonne de référence** : `produit`
- **Colonne contenant les doublons** : `nom_produit`

Le script créera un fichier `deduplicated_colonne_ventes.csv` dans le dossier `resultat`, où les redondances dans `nom_produit` sont remplacées par une chaîne vide :

| id | produit   | nom_produit | prix |
|----|-----------|-------------|------|
| 1  | Chaise    |             | 50   |
| 2  | Table     |             | 100  |
| 3  | Canapé    | Sofa        | 300  |

Dans cet exemple, les valeurs de `nom_produit` qui sont identiques aux valeurs de `produit` ont été supprimées, tandis que les autres valeurs ont été conservées.

# 3. [suppression_doublon_ligne](suppression_doublon_ligne.py)

### Description

Ce script Python permet de lire un fichier CSV, d’identifier et de supprimer les doublons en fonction d’une ou plusieurs colonnes choisies par l’utilisateur, puis de sauvegarder les données dédupliquées dans un nouveau fichier CSV. Ce script est utile pour nettoyer des jeux de données en éliminant les enregistrements redondants en fonction de critères de colonnes spécifiques.

### Utilisation

1. **Préparez le fichier CSV** : Assurez-vous d'avoir un fichier CSV dans le même répertoire que le script ou notez son chemin d'accès.

2. **Exécution du script** :
   Exécutez le script avec la commande suivante dans votre terminal :
   ```bash
   python suppression_doublon_ligne.py
   ```

3. **Instructions interactives** :
   - Le script vous demandera le **nom du fichier CSV** (par exemple `data.csv`). Entrez le nom du fichier.
   - Ensuite, il vous sera demandé d’indiquer les **colonnes à utiliser pour identifier les doublons**, en les séparant par des virgules (exemple : `nom,prenom`). Ces colonnes serviront de critères pour déterminer les lignes en double.
   - Le script vérifie l'existence des colonnes spécifiées dans le fichier CSV.

4. **Résultat** :
   - Le script crée un dossier nommé `resultat` dans le même répertoire.
   - Un fichier CSV nommé `deduplicated_<nom_du_fichier_original>.csv` sera généré dans le dossier `resultat`, contenant les données sans doublons, en fonction des colonnes spécifiées pour le filtrage.

5. **Fin de l'opération** :
   Une fois l'opération terminée, le script affiche un message confirmant la création du fichier dédupliqué.

### Exemple

Supposons un fichier `contacts.csv` avec la structure suivante :

| id | nom    | prenom | email               |
|----|--------|--------|---------------------|
| 1  | Dupont | Marie  | marie.dupont@mail.com |
| 2  | Durand | Jean   | jean.durand@mail.com |
| 3  | Dupont | Marie  | marie.dupont@mail.com |

- **Nom du fichier** : `contacts.csv`
- **Colonnes à utiliser pour les doublons** : `nom,prenom`

Le script créera un fichier `deduplicated_contacts.csv` dans le dossier `resultat`, contenant les données suivantes sans doublons :

| id | nom    | prenom | email               |
|----|--------|--------|---------------------|
| 1  | Dupont | Marie  | marie.dupont@mail.com |
| 2  | Durand | Jean   | jean.durand@mail.com | 

Dans cet exemple, seule la première occurrence du doublon `nom = Dupont` et `prenom = Marie` est conservée.

# 4. [suppression_doublon_ligne_date](suppression_doublon_ligne_date.py)

### Description

Ce script Python permet de lire un fichier CSV, de supprimer les doublons en fonction d'une ou plusieurs colonnes spécifiées par l'utilisateur, et de conserver uniquement la ligne avec la date la plus récente ou la plus ancienne dans chaque groupe de doublons. Ce script est particulièrement utile pour des données comportant des mises à jour répétées, permettant de conserver l'enregistrement le plus récent ou le plus ancien par groupe.

### Utilisation

1. **Préparez le fichier CSV** : Assurez-vous d'avoir un fichier CSV dans le même répertoire que le script ou notez son chemin d'accès.

2. **Exécution du script** :
   Exécutez le script avec la commande suivante dans votre terminal :
   ```bash
   python suppression_doublon_ligne_date.py
   ```

3. **Instructions interactives** :
   - Le script vous demandera le **nom du fichier CSV** (par exemple `data.csv`). Entrez le nom du fichier.
   - Il affichera ensuite les colonnes disponibles dans le fichier.
   - Sélectionnez un **attribut de type date** qui sera utilisé pour choisir la ligne la plus récente ou la plus ancienne dans chaque groupe de doublons.
   - Indiquez les **colonnes pour identifier les doublons** en les séparant par des virgules (exemple : `nom,prenom`). Ces colonnes détermineront les groupes de doublons à partir desquels le script conservera l’enregistrement le plus récent ou le plus ancien.
   - Précisez si vous souhaitez garder la ligne avec la **date la plus récente ou la plus ancienne** dans chaque groupe (en entrant `recent` ou `ancien`).

4. **Résultat** :
   - Le script crée un dossier nommé `resultat` dans le même répertoire.
   - Un fichier CSV nommé `deduplicated_<nom_du_fichier_original>.csv` sera généré dans le dossier `resultat`, contenant les données sans doublons, avec pour chaque groupe de doublons la ligne ayant la date la plus récente ou la plus ancienne selon le choix.

5. **Fin de l'opération** :
   Une fois l'opération terminée, le script affiche un message confirmant la création du fichier sans doublons.

### Exemple

Supposons un fichier `historique.csv` avec la structure suivante :

| id | nom    | prenom | date_modification |
|----|--------|--------|-------------------|
| 1  | Dupont | Marie  | 2023-05-01        |
| 2  | Durand | Jean   | 2023-06-01        |
| 3  | Dupont | Marie  | 2023-07-01        |

- **Nom du fichier** : `historique.csv`
- **Attribut de type date** : `date_modification`
- **Colonnes pour identifier les doublons** : `nom,prenom`
- **Choix de la date** : `recent`

Le script créera un fichier `deduplicated_historique.csv` dans le dossier `resultat`, contenant les données suivantes :

| id | nom    | prenom | date_modification |
|----|--------|--------|-------------------|
| 2  | Durand | Jean   | 2023-06-01        |
| 3  | Dupont | Marie  | 2023-07-01        |

Dans cet exemple, pour le doublon `nom = Dupont` et `prenom = Marie`, seule la ligne avec la date de modification la plus récente a été conservée.

# 5. [suppression_ligne](suppression_ligne.py)

### Description

Ce script Python permet de filtrer un fichier CSV en supprimant les lignes contenant des valeurs spécifiques dans des colonnes définies par l'utilisateur. Ce script est particulièrement utile pour nettoyer des données en éliminant des lignes non pertinentes ou indésirables en fonction de critères précis sur une ou plusieurs colonnes.

### Utilisation

1. **Préparez le fichier CSV** : Assurez-vous d'avoir un fichier CSV dans le même répertoire que le script ou notez son chemin d'accès.

2. **Exécution du script** :
   Exécutez le script avec la commande suivante dans votre terminal :
   ```bash
   python suppression_ligne.py
   ```

3. **Instructions interactives** :
   - Le script vous demandera le **nom du fichier CSV** (par exemple `data.csv`). Entrez le nom du fichier.
   - Il affichera ensuite les colonnes disponibles dans le fichier.
   - Sélectionnez les colonnes pour le filtrage en entrant le **nom de la colonne** puis en indiquant les valeurs spécifiques à supprimer dans cette colonne, séparées par des virgules (par exemple : `valeur1,valeur2`). Vous pouvez ajouter plusieurs colonnes de cette façon, en appuyant sur **Entrée** sans rien saisir pour terminer la sélection.

4. **Résultat** :
   - Le script crée un dossier nommé `resultat` dans le même répertoire.
   - Un fichier CSV filtré, nommé `delete_ligne_<nom_du_fichier_original>.csv`, sera généré dans le dossier `resultat`, avec les lignes contenant les valeurs indésirables supprimées.

5. **Fin de l'opération** :
   Une fois l'opération terminée, le script affiche un message confirmant la création du fichier filtré.

### Exemple

Supposons un fichier `inventaire.csv` avec la structure suivante :

| id | produit   | catégorie | stock |
|----|-----------|-----------|-------|
| 1  | Chaise    | Meubles   | 20    |
| 2  | Table     | Meubles   | 15    |
| 3  | Stylo     | Bureau    | 100   |
| 4  | Crayon    | Bureau    | 50    |

- **Nom du fichier** : `inventaire.csv`
- **Colonnes à filtrer** : 
  - Colonne `catégorie` avec les valeurs `Meubles`
  - Colonne `stock` avec la valeur `50`

Le script créera un fichier `delete_ligne_inventaire.csv` dans le dossier `resultat`, contenant les données suivantes :

| id | produit | catégorie | stock |
|----|---------|-----------|-------|
| 3  | Stylo   | Bureau    | 100   |

Dans cet exemple, toutes les lignes où `catégorie` est `Meubles` ou `stock` est `50` ont été supprimées du fichier.

# 6. [suppression_colonne](suppression_colonne.py)

### Description

Ce script Python permet de modifier un fichier CSV en supprimant soit une ou plusieurs colonnes entières, soit uniquement le contenu de certaines colonnes, en fonction des préférences de l'utilisateur. Ce script est utile pour préparer un jeu de données en supprimant des informations sensibles ou non pertinentes tout en conservant la structure du fichier.

### Utilisation

1. **Préparez le fichier CSV** : Assurez-vous d'avoir un fichier CSV dans le même répertoire que le script ou notez son chemin d'accès.

2. **Exécution du script** :
   Exécutez le script avec la commande suivante dans votre terminal :
   ```bash
   python suppression_colonne.py
   ```

3. **Instructions interactives** :
   - Le script vous demandera le **nom du fichier CSV** (par exemple `data.csv`). Entrez le nom du fichier.
   - Il affichera ensuite les colonnes disponibles dans le fichier.
   - Sélectionnez une ou plusieurs **colonnes à traiter**, en les séparant par des virgules (par exemple : `nom,adresse`).
   - Pour chaque colonne sélectionnée, vous devrez indiquer si vous souhaitez **supprimer la colonne entière** ou seulement **vider son contenu** :
     - **colonne** : La colonne entière est supprimée du fichier.
     - **contenu** : La colonne est conservée, mais son contenu est remplacé par des chaînes vides.

4. **Résultat** :
   - Le script crée un dossier nommé `resultat` dans le même répertoire.
   - Un fichier CSV modifié, nommé `delete_colonne_<nom_du_fichier_original>.csv`, sera généré dans le dossier `resultat`, selon les choix effectués pour chaque colonne.

5. **Fin de l'opération** :
   Une fois l'opération terminée, le script affiche un message confirmant la création du fichier modifié.

### Exemple

Supposons un fichier `employes.csv` avec la structure suivante :

| id | nom      | adresse        | salaire |
|----|----------|----------------|---------|
| 1  | Dupont   | 123 Rue A      | 3000    |
| 2  | Durand   | 456 Rue B      | 3200    |
| 3  | Martin   | 789 Rue C      | 2900    |

- **Nom du fichier** : `employes.csv`
- **Colonnes à traiter** : `adresse,salaire`
  - **Option pour `adresse`** : `contenu`
  - **Option pour `salaire`** : `colonne`

Le script créera un fichier `delete_colonne_employes.csv` dans le dossier `resultat`, avec le contenu suivant :

| id | nom      | adresse | 
|----|----------|---------|
| 1  | Dupont   |         |
| 2  | Durand   |         |
| 3  | Martin   |         |

Dans cet exemple, la colonne `salaire` a été entièrement supprimée, et le contenu de la colonne `adresse` a été vidé, mais la colonne elle-même est conservée.