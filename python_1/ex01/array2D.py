"""
Module de manipulation de tableaux 2D avec slicing.

Ce module fournit des fonctions pour manipuler des tableaux 2D,
afficher leurs dimensions et effectuer des opérations de slicing.

Utilise NumPy pour une gestion robuste des tableaux multidimensionnels.
"""
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Découpe un tableau 2D selon les indices start et end.

    Affiche la forme (shape) du tableau original et du tableau résultant,
    puis retourne la portion découpée sous forme de liste Python.

    Utilise NumPy pour une validation robuste et des opérations de slicing
    optimisées sur les tableaux multidimensionnels.

    Args:
        family (list): Tableau 2D sous forme de liste de listes.
                      Chaque sous-liste doit avoir la même longueur.
                      Exemple: [[1.80, 78.4], [2.15, 102.7]]
        start (int): Index de début (inclus). Peut être négatif.
        end (int): Index de fin (exclu). Peut être négatif.

    Returns:
        list: Portion du tableau découpée, convertie en liste Python.
              Conserve la structure 2D originale.

    Raises:
        TypeError: Si family n'est pas une liste ou si start/end
        ne sont pas des entiers.
        ValueError: Si family n'est pas un tableau 2D valide
        (lignes de tailles différentes).

    Example:
        >>> family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5]]
        >>> slice_me(family, 0, 2)
        My shape is : (3, 2)
        My new shape is : (2, 2)
        [[1.8, 78.4], [2.15, 102.7]]

    Note:
        - Les indices négatifs comptent depuis la fin (-1 = dernier élément)
        - Le slicing suit la convention Python [start:end) (end exclu)
        - La fonction affiche les shapes sur stdout avant
            de retourner le résultat.
    """
    # Validation du type du paramètre family
    if not isinstance(family, list):
        raise TypeError(
            f"'family' doit être une liste: {type(family).__name__}"
        )

    # Validation du type des paramètres start et end
    if not isinstance(start, int):
        raise TypeError(
            f"Le paramètre 'start' doit être un entier: {type(start).__name__}"
        )

    if not isinstance(end, int):
        raise TypeError(
            f"Le paramètre 'end' doit être un entier: {type(end).__name__}"
        )

    # Validation que family n'est pas vide
    if len(family) == 0:
        raise ValueError("Le tableau ne peut pas être vide")

    # Validation que chaque élément de family est une liste
    for i, row in enumerate(family):
        if not isinstance(row, list):
            raise TypeError(
                f"Ligne {i}: chaque élément doit être une liste, "
                f"reçu: {type(row).__name__}"
            )

    # Conversion en array NumPy avec validation automatique de la forme 2D
    try:
        family_array = np.array(family, dtype=np.float64)
    except ValueError as e:
        # NumPy lève ValueError si les lignes n'ont pas la même taille
        raise ValueError(
            "Toutes les lignes du tableau doivent avoir la même longueur. "
            "Vérifiez que c'est bien un tableau 2D rectangulaire."
        ) from e
    except (TypeError, OverflowError) as e:
        raise TypeError(
            "Tous les éléments doivent être des nombres convertibles en float"
        ) from e

    # Validation que c'est bien un tableau 2D (pas 1D ou 3D+)
    if family_array.ndim != 2:
        raise ValueError(
            f"Dimensions détectées: {family_array.ndim}D"
        )

    # Affichage de la forme originale
    original_shape = family_array.shape
    print(f"My shape is : {original_shape}")

    # Application du slicing avec NumPy
    # NumPy gère automatiquement les indices négatifs et les bornes
    try:
        sliced_array = family_array[start:end]
    except IndexError as e:
        raise ValueError(
            f"Indices de slicing invalides: start={start}, end={end}, "
            f"taille du tableau={len(family_array)}"
        ) from e

    # Affichage de la nouvelle forme
    new_shape = sliced_array.shape
    print(f"My new shape is : {new_shape}")

    # Conversion du résultat en liste Python (selon le type de retour spécifié)
    return sliced_array.tolist()


def main():
    """
    Fonction principale du module (obligatoire selon les règles du jour).

    Cette fonction reste vide car les tests sont effectués dans tester.py.
    Le module est conçu pour être importé et utilisé par d'autres programmes.
    """
    # Code de test optionnel pour développement
    # try:
    #     print("Test de développement:")
    #     test_family = [[1.75, 70], [1.80, 75], [1.65, 60]]
    #     result = slice_me(test_family, 0, 2)
    #     print(f"Résultat: {result}")
    # except Exception as e:
    #     print(f"Erreur: {e}")
    pass


if __name__ == "__main__":
    main()
