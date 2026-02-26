"""
Module de zoom et affichage d'images.

Ce module charge une image, effectue un zoom sur une zone spécifique,
convertit en niveaux de gris et affiche le résultat avec matplotlib.

Utilise la fonction ft_load de l'exercice 02 pour le chargement d'images.
"""
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(image: np.ndarray, zoom_size: tuple = (400, 400)) -> np.ndarray:
    """
    Effectue un zoom sur une zone spécifique de l'image.

    Extrait une zone rectangulaire de l'image avec les dimensions
    spécifiées à partir d'une position prédéfinie. La zone est optimisée
    pour correspondre aux spécifications du sujet.

    Args:
        image (np.ndarray): Image source (hauteur, largeur, canaux).
        zoom_size (tuple): Taille de la zone de zoom (hauteur, largeur).
                          Par défaut: (400, 400).

    Returns:
        np.ndarray: Zone zoomée de l'image.
                   Shape: (zoom_height, zoom_width, canaux)

    Raises:
        ValueError: Si zoom_size contient des valeurs non-positives.
        TypeError: Si les paramètres ne sont pas du bon type.

    Example:
        >>> image = np.random.randint(0, 256, (768, 1024, 3), dtype=np.uint8)
        >>> zoomed = zoom_image(image, (400, 400))
        >>> print(zoomed.shape)
        (400, 400, 3)
    """
    # Validation des paramètres
    if not isinstance(image, np.ndarray):
        raise TypeError("image doit être un tableau NumPy")

    if not isinstance(zoom_size, tuple) or len(zoom_size) != 2:
        raise TypeError("zoom_size doit être un tuple de 2 éléments")

    zoom_h, zoom_w = zoom_size
    if zoom_h <= 0 or zoom_w <= 0:
        raise ValueError("Les dimensions de zoom doivent être positives")

    # Dimensions de l'image
    img_h, img_w = image.shape[:2]

    # Calculer les coordonnées de début pour centrer le zoom
    start_h = 100
    start_w = 450

    # Calculer les coordonnées de fin
    end_h = min(img_h, start_h + zoom_h)
    end_w = min(img_w, start_w + zoom_w)

    # Extraire la zone zoomée
    zoomed = image[start_h:end_h, start_w:end_w]

    return zoomed


def rgb_to_grayscale(image: np.ndarray, method: str = "green") -> np.ndarray:
    """
    Convertit une image RGB en niveaux de gris.

    Plusieurs méthodes de conversion sont disponibles :
    - "red" : Utilise uniquement le canal rouge
    - "green" : Utilise uniquement le canal vert
    - "blue" : Utilise uniquement le canal bleu
    - "average" : Moyenne des trois canaux RGB
    - "weighted" : Formule pondérée (0.299*R + 0.587*G + 0.114*B)

    Args:
        image (np.ndarray): Image RGB (hauteur, largeur, 3).
        method (str): Méthode de conversion ("red", "green", "blue", "average", "weighted").

    Returns:
        np.ndarray: Image en niveaux de gris.
                   Shape: (hauteur, largeur, 1) ou (hauteur, largeur)

    Raises:
        ValueError: Si la méthode n'est pas supportée
        ou si l'image n'a pas 3 canaux.
        TypeError: Si les paramètres ne sont pas du bon type.
    """
    # Validation des paramètres
    if not isinstance(image, np.ndarray):
        raise TypeError("image doit être un tableau NumPy")

    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("L'image doit avoir 3 canaux RGB")

    if method not in ["red", "green", "blue", "average", "weighted"]:
        raise ValueError("Méthodes supportées: 'red', 'green', 'blue', 'average', 'weighted'")

    # Conversion selon la méthode choisie
    if method == "red":
        # Utiliser seulement le canal rouge (index 0)
        gray = image[:, :, 0:1]  # Garder la dimension canal
        
    elif method == "green":
        # Utiliser seulement le canal vert (index 1)
        gray = image[:, :, 1:2]  # Garder la dimension canal
        
    elif method == "blue":
        # Utiliser seulement le canal bleu (index 2)
        gray = image[:, :, 2:3]  # Garder la dimension canal

    elif method == "average":
        # Moyenne simple des trois canaux
        gray = np.mean(image, axis=2, keepdims=True)

    elif method == "weighted":
        # Formule pondérée standard (luminance)
        gray = (0.299 * image[:, :, 0] +
                0.587 * image[:, :, 1] +
                0.114 * image[:, :, 2])
        gray = gray[:, :, np.newaxis]  # Ajouter dimension canal

    return gray.astype(np.uint8)


def display_image(image: np.ndarray, title: str = "Image",
                  show_axes: bool = True) -> None:
    """
    Affiche une image avec matplotlib.

    Args:
        image (np.ndarray): Image à afficher (2D ou 3D).
        title (str): Titre de l'image.
        show_axes (bool): Afficher les axes avec échelles.

    Raises:
        ValueError: Si l'image n'a pas le bon format.
    """
    # Validation de l'image
    if not isinstance(image, np.ndarray):
        raise TypeError("image doit être un tableau NumPy")

    if image.ndim not in [2, 3]:
        raise ValueError("L'image doit être 2D ou 3D")

    # Configuration de l'affichage
    plt.figure(figsize=(8, 8))

    # Affichage selon le type d'image
    if image.ndim == 3 and image.shape[2] == 1:
        # Image en niveaux de gris avec dimension canal
        plt.imshow(image[:, :, 0], cmap='gray')
    elif image.ndim == 2:
        # Image en niveaux de gris 2D
        plt.imshow(image, cmap='gray')
    else:
        # Image RGB
        plt.imshow(image)

    # Configuration des axes
    if show_axes:
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.title(title)

        # Afficher la grille pour mieux voir les échelles
        plt.grid(True, alpha=0.3)
    else:
        plt.axis('off')

    # Afficher l'image
    plt.tight_layout()
    plt.show()


def main():
    """
    Fonction principale - Charge, zoome et affiche l'image animal.jpeg.
    """
    try:
        # 1. Charger l'image (ft_load affiche automatiquement shape + contenu)
        image = ft_load("animal.jpeg")

        print(image)

        # 2. Effectuer le zoom et conversion (silencieux)
        zoomed_image = zoom_image(image, (400, 400))
        gray_image = rgb_to_grayscale(zoomed_image, method="weighted")
        
        # 3. Afficher les résultats du zoom
        print(f"New shape after slicing: {gray_image.shape} or {gray_image.shape[:2]}")
        print(gray_image)
        
        # 4. Afficher l'image avec matplotlib
        display_image(gray_image, "Zoomed Animal Image", show_axes=True)

    except FileNotFoundError as e:
        print(f"Erreur: Fichier image non trouvé - {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")


if __name__ == "__main__":
    main()
