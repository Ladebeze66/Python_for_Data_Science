import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image et retourne un tableau NumPy avec les valeurs RGB.

    Args:
        path (str): Chemin vers le fichier image.

    Returns:
        np.ndarray: Tableau contenant les valeurs RGB de l'image.
                   Shape: (1, pixels_total, 3) pour affichage optimal

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        ValueError: Si le fichier n'est pas une image valide.
        PermissionError: Si l'accès au fichier est refusé.
    """
    try:
        # Charger et convertir l'image en RGB
        image = Image.open(path).convert('RGB')
        image_array = np.array(image, dtype=np.uint8)

        # Affichage requis par le sujet (shape originale)
        print(f"The shape of image is: {image_array.shape}")
        print(image_array.reshape(1, -1, 3))  # Affichage seulement
        print(" ...")
        # Reshape pour obtenir l'affichage tronqué du sujet
        return image_array

    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{path}' n'existe pas.")
    except Image.UnidentifiedImageError:
        raise ValueError(f"Le fichier '{path}' n'est pas une image valide.")
    except PermissionError:
        raise PermissionError(f"Accès refusé au fichier '{path}'.")
    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement de '{path}': {str(e)}")


def main():
    """
    Fonction principale du module (obligatoire selon les règles du jour).

    Cette fonction reste vide car les tests sont effectués dans tester.py.
    Le module est conçu pour être importé et utilisé par d'autres programmes.
    """
    pass


if __name__ == "__main__":
    main()
