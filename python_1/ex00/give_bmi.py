"""
Module de calcul d'IMC (BMI) et application de limites utilisant NumPy.

Ce module fournit des fonctions pour calculer l'Indice de Masse Corporelle
à partir de listes de tailles et de poids, ainsi que pour appliquer des seuils
de comparaison sur les valeurs calculées.

Utilise NumPy pour des calculs vectorisés optimisés.
"""
import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calcule l'Indice de Masse Corporelle (BMI) pour chaque paire taille/poids.

    Utilise la formule : BMI = poids(kg) / taille(m)²

    Args:
        height (list[int | float]): Liste des tailles en mètres.
                                   Chaque valeur doit être un nombre positif.
        weight (list[int | float]): Liste des poids en kilogrammes.
                                   Chaque valeur doit être un nombre positif.

    Returns:
        list[int | float]: Liste des valeurs BMI calculées.
            Chaque BMI correspond à la paire (height[i], weight[i]).

    Raises:
        TypeError: Si les paramètres ne sont pas des listes ou si les éléments
                  ne sont pas des nombres convertibles.
        ValueError: Si les listes ont des tailles différentes, sont vides,
                   ou contiennent des valeurs non-positives.

    Note:
        Les calculs sont effectués en virgule flottante pour une précision
        maximale, même si les entrées sont des entiers.
    """
    # Validation des types de paramètres
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Les paramètres doivent être des listes")

    # Validation des tailles des listes
    if len(height) != len(weight):
        raise ValueError(
            f"Les listes doivent avoir la même taille: "
            f"height={len(height)}, weight={len(weight)}"
        )

    # Validation des listes vides
    if len(height) == 0:
        raise ValueError("Les listes ne peuvent pas être vides")

    # Conversion en arrays NumPy avec gestion d'erreurs
    try:
        height_array = np.array(height, dtype=np.float64)
        weight_array = np.array(weight, dtype=np.float64)
    except (ValueError, TypeError) as e:
        raise TypeError(
            "Tous les éléments doivent être des nombres convertibles en float"
        ) from e

    # vérification que toutes les tailles sont positives
    if np.any(height_array <= 0):
        invalid_indices = np.where(height_array <= 0)[0]
        raise ValueError(
            f"Toutes les tailles doivent être positives. "
            f"Valeurs invalides aux indices: {invalid_indices.tolist()}"
        )

    # Validation des valeurs : vérification que tous les poids sont positifs
    if np.any(weight_array <= 0):
        invalid_indices = np.where(weight_array <= 0)[0]
        raise ValueError(
            f"Tous les poids doivent être positifs. "
            f"Valeurs invalides aux indices: {invalid_indices.tolist()}"
        )

    # Calcul vectorisé du BMI : BMI = poids / taille²
    bmi_array = weight_array / np.square(height_array)

    # Conversion du résultat en liste Python (selon la signature de retour)
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applique un seuil de comparaison aux valeurs d'IMC.

    Compare chaque valeur BMI avec une limite donnée et retourne un masque
    booléen indiquant quelles valeurs dépassent cette limite.

    Args:
        bmi (list[int | float]): Liste des valeurs BMI à comparer.
                                Chaque élément doit être un nombre.
        limit (int): Seuil de comparaison (valeur entière).
                    Les valeurs BMI strictement supérieures à ce seuil
                    donneront True dans le résultat.

    Returns:
        list[bool]: Liste de booléens de même longueur que bmi.
                   True si bmi[i] > limit, False sinon.

    Raises:
        TypeError: Si bmi n'est pas une liste, si limit n'est pas un entier,
                  ou si les éléments de bmi ne sont pas des nombres.
    """
    # Validation du type du paramètre bmi
    if not isinstance(bmi, list):
        raise TypeError(
            f"Le paramètre 'bmi' doit être une liste: {type(bmi).__name__}"
        )

    # Validation du type du paramètre limit
    if not isinstance(limit, int):
        raise TypeError(
            f"Le paramètre 'limit' doit être un entier: {type(limit).__name__}"
        )

    # Gestion du cas d'une liste vide (retour d'une liste vide)
    if len(bmi) == 0:
        return []

    # Conversion en array NumPy avec validation des types
    try:
        bmi_array = np.array(bmi, dtype=np.float64)
    except (ValueError, TypeError) as e:
        raise TypeError(
            "Tous les éléments de 'bmi' doivent être des nombres convertibles"
        ) from e

    # Vérification explicite que tous les éléments sont des nombres finis
    if not np.all(np.isfinite(bmi_array)):
        invalid_indices = np.where(~np.isfinite(bmi_array))[0]
        raise TypeError(
            f"Tous les éléments doivent être des nombres finis. "
            f"Valeurs invalides aux indices: {invalid_indices.tolist()}"
        )

    # Comparaison vectorisée : chaque élément > limit
    comparison_result = bmi_array > limit

    # Conversion du résultat booléen NumPy en liste Python
    return comparison_result.tolist()


def main():
    """
    Fonction principale du module
    """


if __name__ == "__main__":
    main()
