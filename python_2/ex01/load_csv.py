import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Charge un dataset CSV et affiche ses dimensions.

    Args:
        path (str): Chemin vers le fichier CSV

    Returns:
        pd.DataFrame: Le dataset chargé, ou None en cas d'erreur
    """
    try:
        # Tentative de chargement du fichier CSV
        dataset = pd.read_csv(path)

        # Affichage des dimensions
        rows, cols = dataset.shape
        print(f"Loading dataset of dimensions ({rows}, {cols})")

        # Retour du dataset
        return dataset

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{path}' n'existe pas.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Erreur : Le fichier '{path}' est vide.")
        return None
    except pd.errors.ParserError:
        print(f"Erreur : Le fichier '{path}' n'est pas un CSV valide.")
        return None
    except PermissionError:
        print(f"Erreur : Permissions insuffisantes pour lire '{path}'.")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None


def main():
    """
    Fonction principale pour tester la fonction load.
    """


if __name__ == "__main__":
    main()
