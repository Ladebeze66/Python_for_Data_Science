"""
Module de rotation d'images par transposition manuelle.

Ce module charge une image, effectue un zoom, convertit en niveaux de gris,
puis applique une transposition manuelle pour simuler une rotation.
"""
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(image: np.ndarray, start_h: int = 100, start_w: int = 450,
               zoom_size: int = 400) -> np.ndarray:
    """
    Extrait une zone carrée de l'image.

    Args:
        image (np.ndarray): Image source (hauteur, largeur, canaux).
        start_h (int): Position de départ en hauteur.
        start_w (int): Position de départ en largeur.
        zoom_size (int): Taille du carré de zoom.

    Returns:
        np.ndarray: Zone zoomée de l'image.
    """
    end_h = start_h + zoom_size
    end_w = start_w + zoom_size
    return image[start_h:end_h, start_w:end_w]


def rgb_to_grayscale(image: np.ndarray, method: str = "red") -> np.ndarray:
    """
    Convertit une image RGB en niveaux de gris.

    Args:
        image (np.ndarray): Image RGB (hauteur, largeur, 3).
        method (str): Méthode de conversion ("red", "green", "blue").

    Returns:
        np.ndarray: Image en niveaux de gris (hauteur, largeur, 1).
    """
    if method == "red":
        return image[:, :, 0:1]
    elif method == "green":
        return image[:, :, 1:2]
    elif method == "blue":
        return image[:, :, 2:3]
    else:
        # Méthode par défaut : moyenne
        return np.mean(image, axis=2, keepdims=True).astype(np.uint8)


def ft_transpose(matrix: np.ndarray) -> np.ndarray:
    """
    Transpose une matrice 2D manuellement.

    IMPORTANT: Implémentation manuelle obligatoire selon le sujet.
    Aucune fonction de librairie (.T, .transpose(), np.rot90()) autorisée.

    Args:
        matrix (np.ndarray): Matrice 2D à transposer.

    Returns:
        np.ndarray: Matrice transposée.

    Algorithm:
        Pour chaque élément matrix[i][j], le placer à transposed[j][i].

    Example:
        >>> matrix = np.array([[1, 2, 3], [4, 5, 6]])
        >>> result = ft_transpose(matrix)
        >>> print(result)
        [[1 4]
         [2 5]
         [3 6]]
    """
    height, width = matrix.shape

    # Créer une nouvelle matrice avec dimensions inversées
    transposed = np.zeros((width, height), dtype=matrix.dtype)

    # Algorithme de transposition manuelle
    for i in range(height):
        for j in range(width):
            transposed[j][i] = matrix[i][j]

    return transposed


def display_image(image: np.ndarray, title: str = "Transposed Image") -> None:
    """
    Affiche une image avec matplotlib.

    Args:
        image (np.ndarray): Image à afficher.
        title (str): Titre de l'image.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.xlabel("Pixels (largeur)")
    plt.ylabel("Pixels (hauteur)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    """
    Fonction principale - Charge, zoome, convertit et transpose l'image.

    Reproduit exactement la sortie attendue du sujet :
    1. Affiche la shape de l'image zoomée en grayscale
    2. Affiche le contenu de l'image avant transposition
    3. Effectue la transposition manuelle
    4. Affiche la shape et le contenu après transposition
    """
    try:
        # 1. Charger l'image RGB originale (silencieux maintenant)
        original_image = ft_load("animal.jpeg")

        # 2. Effectuer zoom + conversion grayscale
        zoomed_image = zoom_image(original_image)
        gray_image = rgb_to_grayscale(zoomed_image, method="red")

        # 3. Affichage AVANT transposition (exactement comme le sujet)
        shape_full = gray_image.shape
        shape_2d = gray_image.shape[:2]
        print(f"The shape of image is: {shape_full} or {shape_2d}")

        # Affichage du contenu 3D avec reshape pour format compact
        print(gray_image.reshape(1, -1, 1))

        # 4. Conversion 3D → 2D pour la transposition
        gray_2d = gray_image.squeeze()  # (400, 400, 1) → (400, 400)

        # 5. Transposition manuelle (cœur de l'exercice)
        transposed = ft_transpose(gray_2d)

        # 6. Affichage APRÈS transposition (exactement comme le sujet)
        print(f"New shape after Transpose: {transposed.shape}")

        # Affichage du contenu 2D avec reshape pour format compact
        # Utiliser la troncature automatique de NumPy sur chaque ligne
        reshaped = transposed.reshape(2, -1)
        np.set_printoptions(threshold=1000, edgeitems=3)
        first_line = str(reshaped[0])[1:-1]  # Enlever [ ]
        last_line = str(reshaped[1])[1:-1]   # Enlever [ ]
        print(f"[{first_line}")
        print(" ...")
        print(f" {last_line}]")

        # 7. Affichage graphique (optionnel selon le sujet)
        display_image(transposed, "Transposed Animal Image")

    except Exception as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    main()
