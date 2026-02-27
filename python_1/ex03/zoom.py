"""
Module de zoom et affichage d'images.

Ce module charge une image, effectue un zoom sur une zone spécifique,
convertit en niveaux de gris et affiche le résultat avec matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(image: np.ndarray, start_h: int = 100, start_w: int = 450, 
               zoom_size: int = 400) -> np.ndarray:
    """
    Effectue un zoom sur une zone spécifique de l'image.
    
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
        np.ndarray: Image en niveaux de gris.
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


def display_image(image: np.ndarray, title: str = "Zoomed Image") -> None:
    """
    Affiche une image avec matplotlib.
    
    Args:
        image (np.ndarray): Image à afficher.
        title (str): Titre de l'image.
    """
    plt.figure(figsize=(8, 8))
    
    if image.shape[2] == 1:
        # Image en niveaux de gris
        plt.imshow(image.squeeze(), cmap='gray')
    else:
        # Image RGB
        plt.imshow(image)
    
    plt.title(title)
    plt.xlabel("Pixels (largeur)")
    plt.ylabel("Pixels (hauteur)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    """
    Fonction principale - Charge, zoome et affiche l'image animal.jpeg.
    """
    try:
        # 1. Charger l'image (ft_load affiche automatiquement shape + contenu)
        image = ft_load("animal.jpeg")
        
        # 2. Effectuer le zoom et conversion
        zoomed_image = zoom_image(image)
        gray_image = rgb_to_grayscale(zoomed_image, method="red")
        
        # 3. Afficher les résultats du zoom
        shape_full = gray_image.shape
        shape_2d = gray_image.shape[:2]
        print(f"New shape after slicing: {shape_full} or {shape_2d}")
        
        # Affichage avec reshape temporaire pour correspondre au sujet
        print(gray_image.reshape(1, -1, 1))
        
        # 4. Afficher l'image avec matplotlib
        display_image(gray_image, "Zoomed Animal Image")
        
    except Exception as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    main()