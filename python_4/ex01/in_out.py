def square(x: int | float) -> int | float:
    """
    Calcule le carré d'un nombre.

    Args:
        x: Nombre à élever au carré

    Returns:
        Le carré de x (x^2)
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calcule l'exponentiation d'un nombre par lui-même.

    Args:
        x: Nombre à élever à sa propre puissance

    Returns:
        x élevé à la puissance x (x^x)
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Crée une closure qui applique successivment une fonction.

    Args:
        x: Valeur initiale
        function: Fonction à appliquer (square ou pow)

    Returns:
        Résultat du calcul après application de la fonction
    """
    count = 0

    def inner() -> float:
        """
        Applique la fonction sur la valeur courante et met à jour l'état.

        Returns:
            Résultat du calcul après application de la fonction
        """
        nonlocal count, x
        count += 1
        x = function(x)
        return x
    return inner


def main():
    """Fonction principale"""
    pass


if __name__ == "__main__":
    main()
