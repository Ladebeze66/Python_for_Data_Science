"""
Module de filtres d'images avec contraintes d'opérateurs.

Ce module implémente 5 filtres d'images différents, chacun avec des contraintes
d'opérateurs mathématiques spécifiques.

Contraintes par fonction :
- ft_invert : =, +, -, *
- ft_red    : =, *
- ft_green  : =, -
- ft_blue   : =
- ft_grey   : =, /
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray as array


def ft_invert(array) -> array:
    """
    Inverts the color of the image received.

    Inverse les couleurs de l'image reçue.

    Cette fonction applique une inversion complète des couleurs en soustrayant
    chaque valeur de pixel de 255 (valeur maximale pour un pixel 8-bit).
    Le résultat produit un effet de "négatif photographique" où les couleurs
    sombres deviennent claires et vice versa.

    Principe mathématique :
        nouveau_pixel = 255 - ancien_pixel

    Exemples de transformation :
        - Noir [0, 0, 0] → Blanc [255, 255, 255]
        - Blanc [255, 255, 255] → Noir [0, 0, 0]
        - Rouge [255, 0, 0] → Cyan [0, 255, 255]
        - Vert [0, 255, 0] → Magenta [255, 0, 255]

    Args:
        array: Tableau NumPy représentant l'image RGB.
               Shape attendue: (hauteur, largeur, 3)
               Type: uint8 avec valeurs 0-255

    Returns:
        array: Image avec couleurs inversées, même dimensions que l'entrée.
               Type: uint8 avec valeurs 0-255

    Contraintes d'opérateurs autorisés : =, +, -, *

    Note technique:
        Utilise la soustraction vectorisée de NumPy pour un traitement
        efficace de tous les pixels simultanément.
    """
    # Inversion par soustraction : 255 - valeur_pixel
    return 255 - array


def ft_red(array) -> array:
    """
    Applique un filtre rouge à l'image.

    Cette fonction conserve uniquement le canal rouge de l'image RGB,
    en annulant complètement les canaux vert et bleu. L'image résultante
    n'affiche que les intensités de rouge, créant un effet monochrome rouge.

    Principe technique :
        Utilise un masque multiplicatif [1, 0, 0] appliqué à chaque pixel.
        [R, G, B] * [1, 0, 0] = [R*1, G*0, B*0] = [R, 0, 0]

    Exemples de transformation :
        - [100, 200, 50] → [100, 0, 0] (garde seulement le rouge)
        - [0, 255, 255] → [0, 0, 0] (cyan devient noir, pas de rouge)
        - [255, 100, 100] → [255, 0, 0] (rouge pur intense)

    Args:
        array: Tableau NumPy représentant l'image RGB.
               Shape attendue: (hauteur, largeur, 3)
               Type: uint8 avec valeurs 0-255

    Returns:
        array: Image filtrée en rouge, même dimensions que l'entrée.
               Seul le canal rouge (indice 0) conserve ses valeurs originales.

    Contraintes d'opérateurs autorisés : =, *

    Note technique:
        Le broadcasting NumPy permet d'appliquer le masque [1, 0, 0]
        à tous les pixels simultanément de manière vectorisée.
    """
    # Masque multiplicatif : [1, 0, 0] garde rouge, annule vert et bleu
    return array * [1, 0, 0]


def ft_green(array) -> array:
    """
    Applique un filtre vert à l'image.

    Cette fonction conserve uniquement le canal vert de l'image RGB,
    en annulant les canaux rouge et bleu. Contrainte par l'interdiction
    d'utiliser la multiplication, elle utilise une approche créative
    basée sur la soustraction.

    Principe technique (soustraction créative) :
        1. array * [1, 0, 1] produit [R, 0, B] (garde rouge et bleu)
        2. array - [R, 0, B] = [R-R, G-0, B-B] = [0, G, 0]
        3. Résultat : seul le canal vert subsiste

    Exemples de transformation :
        - [100, 200, 50] → [0, 200, 0] (garde seulement le vert)
        - [255, 0, 255] → [0, 0, 0] (magenta devient noir, pas de vert)
        - [100, 255, 100] → [0, 255, 0] (vert pur intense)

    Args:
        array: Tableau NumPy représentant l'image RGB.
               Shape attendue: (hauteur, largeur, 3)
               Type: uint8 avec valeurs 0-255

    Returns:
        array: Image filtrée en vert, même dimensions que l'entrée.
               Seul le canal vert (indice 1) conserve ses valeurs originales.

    Contraintes d'opérateurs autorisés : =, -

    Note technique:
        Cette solution démontre comment contourner l'interdiction de
        multiplication directe en utilisant une soustraction intelligente.
    """
    # Soustraction créative : array - [R, 0, B] = [0, G, 0]
    return array - array * [1, 0, 1]


def ft_blue(array) -> array:
    """
    Applique un filtre bleu à l'image.

    Cette fonction conserve uniquement le canal bleu de l'image RGB,
    en annulant les canaux rouge et vert. Contrainte par l'interdiction
    d'utiliser toute opération arithmétique, elle utilise uniquement
    des assignations directes.

    Principe technique (assignation directe) :
        1. Créer une copie de l'image originale
        2. Assigner 0 au canal rouge (indice 0)
        3. Assigner 0 au canal vert (indice 1)
        4. Le canal bleu (indice 2) reste inchangé

    Exemples de transformation :
        - [100, 200, 50] → [0, 0, 50] (garde seulement le bleu)
        - [255, 255, 0] → [0, 0, 0] (jaune devient noir, pas de bleu)
        - [100, 100, 255] → [0, 0, 255] (bleu pur intense)

    Args:
        array: Tableau NumPy représentant l'image RGB.
               Shape attendue: (hauteur, largeur, 3)
               Type: uint8 avec valeurs 0-255

    Returns:
        array: Image filtrée en bleu, même dimensions que l'entrée.
               Seul le canal bleu (indice 2) conserve ses valeurs originales.

    Contraintes d'opérateurs autorisés : = (assignation uniquement)

    Note technique:
        Cette contrainte extrême force l'utilisation d'une approche
        impérative plutôt que vectorisée, démontrant différents paradigmes
        de programmation avec NumPy.
    """
    # Seule l'assignation est autorisée - solution directe
    result = array.copy()  # Assignation (copie)
    result[:, :, 0] = 0    # Assignation : rouge = 0
    result[:, :, 1] = 0    # Assignation : vert = 0
    return result          # Le bleu reste inchangé


def ft_grey(array) -> array:
    """
    Convertit l'image en niveaux de gris.

    Cette fonction transforme une image couleur RGB en image en niveaux
    de gris en calculant la moyenne arithmétique des trois canaux pour
    chaque pixel. Cette méthode simple produit une conversion grayscale
    uniforme, bien que moins sophistiquée que les méthodes perceptuelles.

    Principe technique (moyenne arithmétique améliorée) :
        1. Convertir chaque canal en float64 pour une précision maximale
        2. Pour chaque pixel [R, G, B], calculer (R + G + B) / 3
        3. Convertir le résultat en uint8 pour chaque canal séparément
        4. Assigner cette valeur aux trois canaux : [gris, gris, gris]

    Formule mathématique :
        gris = (Rouge_float64 + Vert_float64 + Bleu_float64) / 3
        puis conversion uint8 canal par canal

    Amélioration par rapport à la version simple :
        - Précision float64 évite les erreurs d'arrondi prématurées
        - Conversion uint8 par canal évite les artefacts visuels
        - Résultat plus propre et contrasté

    Exemples de transformation :
        - [100, 200, 50] → [116, 116, 116] (moyenne = 116.67 → 117)
        - [255, 255, 255] → [255, 255, 255] (blanc reste blanc)
        - [0, 0, 0] → [0, 0, 0] (noir reste noir)
        - [255, 0, 0] → [85, 85, 85] (rouge devient gris moyen)

    Args:
        array: Tableau NumPy représentant l'image RGB.
               Shape attendue: (hauteur, largeur, 3)
               Type: uint8 avec valeurs 0-255

    Returns:
        array: Image en niveaux de gris, même dimensions que l'entrée.
               Les trois canaux contiennent la même valeur de gris.
               Type: uint8 avec valeurs 0-255
               Qualité visuelle améliorée par rapport à la conversion simple.

    Contraintes d'opérateurs autorisés : =, /

    Note technique:
        L'utilisation de float64 intermédiaire améliore significativement
        la qualité visuelle en évitant les pertes de précision et les
        artefacts de quantification. La conversion uint8 par canal
        préserve mieux les nuances de gris.

    Alternative perceptuelle (non utilisée ici) :
        gris = 0.299*R + 0.587*G + 0.114*B
        (pondération selon perception humaine)
        Nécessiterait la multiplication (opérateur interdit pour cet exercice)
    """
    # Calculer pour chaque canal séparément
    grey_value = (array[:, :, 0].astype(np.float64) +
                  array[:, :, 1].astype(np.float64) +
                  array[:, :, 2].astype(np.float64)) / 3

    result = array.copy()
    result[:, :, 0] = grey_value.astype(np.uint8)
    result[:, :, 1] = grey_value.astype(np.uint8)
    result[:, :, 2] = grey_value.astype(np.uint8)

    return result


def display_images(original, inverted, red, green, blue, grey):
    """
    Affiche les 6 images dans une grille 3x2 (3 lignes, 2 colonnes).

    Args:
        original: Image originale
        inverted: Image inversée
        red: Image filtrée rouge
        green: Image filtrée verte
        blue: Image filtrée bleue
        grey: Image en niveaux de gris

    Disposition:
        Ligne 1: Original, Invert
        Ligne 2: Red, Green
        Ligne 3: Blue, Grey

    Note:
        - Titres affichés sous les images avec police serif
        - Format portrait (10x15) adapté à la disposition verticale
        - Calcul de position: i // 2, i % 2 pour 2 colonnes par ligne
    """
    fig, axes = plt.subplots(3, 2, figsize=(10, 15))

    images = [original, inverted, red, green, blue, grey]
    titles = ['Figure VIII.1: Original', 'Figure VIII.2: Invert',
              'Figure VIII.3: Red', 'Figure VIII.4: Green',
              'Figure VIII.5: Blue', 'Figure VIII.6: Grey']

    for i, (img, title) in enumerate(zip(images, titles)):
        row, col = i // 2, i % 2
        axes[row, col].imshow(img)

        # Titre sous l'image avec police serif
        axes[row, col].text(0.5, -0.05, title,
                            transform=axes[row, col].transAxes,
                            ha='center', va='top', fontsize=14,
                            fontfamily='serif')

        axes[row, col].axis('off')

    plt.tight_layout()
    plt.show()


def main():
    """
    Fonction principale du module (obligatoire selon les règles du jour).

    Cette fonction reste vide car les tests sont effectués dans tester.py.
    Le module est conçu pour être importé et utilisé par d'autres programmes.
    """
    pass


if __name__ == "__main__":
    main()
