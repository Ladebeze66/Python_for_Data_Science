"""
Module de chargement et manipulation d'images.

Ce module fournit des fonctions pour charger des images depuis des fichiers,
les convertir en tableaux NumPy et afficher leurs informations.

Supporte les formats JPG, JPEG, PNG et autres formats courants.
Utilise PIL/Pillow pour le chargement et NumPy pour la manipulation.
"""
import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis un fichier et la convertit en tableau NumPy RGB.

    Cette fonction charge une image, affiche ses informations
    (dimensions et format),
    et retourne le contenu des pixels sous forme de tableau NumPy 3D
    au format RGB.

    La fonction gère automatiquement la conversion vers le format RGB, même si
    l'image source est en niveaux de gris, RGBA, ou autre format.

    Args:
        path (str): Chemin vers le fichier image à charger.
                   Doit pointer vers un fichier image valide.
                   Formats supportés : JPG, JPEG, PNG, BMP, TIFF, etc.

    Returns:
        np.ndarray: Tableau NumPy 3D représentant l'image au format RGB.
                   Shape: (hauteur, largeur, 3)
                   Dtype: uint8 (valeurs 0-255)
                   Ordre des canaux: [Rouge, Vert, Bleu]

    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
        PermissionError: Si l'accès au fichier est refusé.
        PIL.UnidentifiedImageError: Si le fichier n'est pas une image valide.
        ValueError: Si l'image ne peut pas être convertie en RGB.
        OSError: Pour d'autres erreurs de lecture de fichier.

    Example:
        >>> image_array = ft_load("landscape.jpg")
        The shape of image is: (257, 450, 3)
        >>> print(image_array.shape)
        (257, 450, 3)
        >>> print(image_array.dtype)
        uint8

    Note:
        - La fonction affiche automatiquement la shape de l'image sur stdout
        - Les images en niveaux de gris sont automatiquement converties en RGB
        - Les images avec transparence (RGBA) perdent le canal alpha
        - Les valeurs des pixels sont dans la plage [0, 255]
    """
    # Validation du type du paramètre
    if not isinstance(path, str):
        raise TypeError(
            f"Le paramètre 'path' doit être une chaîne de caractères, "
            f"reçu: {type(path).__name__}"
        )

    # Validation que le chemin n'est pas vide
    if not path.strip():
        raise ValueError("Le chemin ne peut pas être vide")

    # Vérification de l'existence du fichier
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Le fichier '{path}' n'existe pas. "
            f"Vérifiez le chemin et le nom du fichier."
        )

    # Vérification que c'est bien un fichier (pas un dossier)
    if not os.path.isfile(path):
        raise ValueError(
            f"'{path}' n'est pas un fichier. "
            f"Veuillez spécifier un chemin vers un fichier image."
        )

    try:
        # Chargement de l'image avec PIL/Pillow
        with Image.open(path) as image:
            # Affichage des informations sur l'image originale
            # (optionnel pour debug)
            # print(f"Format original: {image.format}")
            # print(f"Mode original: {image.mode}")
            # print(f"Taille originale: {image.size}")

            # Conversion en mode RGB si nécessaire
            # Cela garantit 3 canaux (R, G, B) même
            # pour les images en niveaux de gris
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Conversion en tableau NumPy
            # PIL retourne (largeur, hauteur) mais NumPy utilise
            # (hauteur, largeur)
            image_array = np.array(image, dtype=np.uint8)

    except FileNotFoundError:
        # Re-lever l'exception déjà gérée plus haut
        raise

    except PermissionError as e:
        raise PermissionError(
            f"Accès refusé au fichier '{path}'. "
            f"Vérifiez les permissions du fichier."
        ) from e

    except Image.UnidentifiedImageError as e:
        raise ValueError(
            f"Le fichier '{path}' n'est pas une image valide ou "
            f"son format n'est pas supporté. "
            f"Formats supportés : JPG, JPEG, PNG, BMP, TIFF, etc."
        ) from e

    except OSError as e:
        raise OSError(
            f"Erreur lors de la lecture du fichier '{path}': {str(e)}"
        ) from e

    except Exception as e:
        raise RuntimeError(
            f"Erreur inattendue lors du chargement '{path}': {str(e)}"
        ) from e

    # Validation du résultat (sécurité supplémentaire)
    if image_array.ndim != 3:
        raise ValueError(
            f"L'image chargée n'a pas le bon nombre de dimensions. "
            f"Attendu: 3D (hauteur, largeur, canaux): {image_array.ndim}D"
        )

    if image_array.shape[2] != 3:
        raise ValueError(
            f"L'image chargée n'a pas 3 canaux RGB. "
            f"Canaux détectés: {image_array.shape[2]}"
        )

    # Affichage de la shape (requis par le sujet)
    print(f"The shape of image is: {image_array.shape}")

    # vérification de la configuration de l'affichage
    # print(np.get_printoptions())

    return image_array


def main():
    """
    Fonction principale du module (obligatoire selon les règles du jour).

    Cette fonction reste vide car les tests sont effectués dans tester.py.
    Le module est conçu pour être importé et utilisé par d'autres programmes.
    """
    # Code de test optionnel pour développement
    # try:
    #     print("Test de développement:")
    #     # Créer une image de test simple si pas d'image disponible
    #     test_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    #     print(f"Image de test créée: {test_image.shape}")
    # except Exception as e:
    #     print(f"Erreur: {e}")
    pass


if __name__ == "__main__":
    main()
