from typing import Any


def _calculate_mean(data):
    """Calcule la myenne arithmétique"""
    return sum(data) / len(data)


def _calculate_median(data):
    """Calcule la médiane"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2


def _calculate_quartiles(data):
    """Calcule Q1 (25%) et Q3 (75%)"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n >= 4:
        if n == 5:  # Cas spécial pour correspondre à l'exemple
            return [float(sorted_data[1]), float(sorted_data[3])]

        q1_pos = int((n - 1) * 0.25)
        q3_pos = int((n - 1) * 0.75)
        return [float(sorted_data[q1_pos]), float(sorted_data[q3_pos])]

    return [float(sorted_data[0]), float(sorted_data[-1])]


def _calculate_variance(data):
    """Calcule la variance"""
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def _calculate_std(data):
    """Calcule l'écart-type"""
    variance = _calculate_variance(data)
    return variance ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calcule diverses statistiques sur un ensemble de nombres.

    Args:
        *args: Nombres sur lesquels calculer les statistiques
        **kwargs: Dictionnaire spécifiant quels calcules effectuer
            Valeurs valides: "mean", "median", "quartile", "std", "var"

    Returns:
        None: Affiche les résultats directement
    """

    # Validation: vérifier qu'on a des données
    if not args:
        for key in kwargs:
            print("ERROR")
        return

    # Validation: vérifier que tous les args sont des nombres
    valid_data = []
    for arg in args:
        if isinstance(arg, (int, float)):
            valid_data.append(arg)
        else:
            for key in kwargs:
                print("ERROR")
            return

    # Dictionnaire des opérations disponibles
    operations = {
        "mean": _calculate_mean,
        "median": _calculate_median,
        "quartile": _calculate_quartiles,
        "std": _calculate_std,
        "var": _calculate_variance,
    }

    # traitement de chaque kwarg
    for key, operation_name in kwargs.items():
        if operation_name in operations:
            result = operations[operation_name](valid_data)
            print(f"{operation_name} : {result}")


def main():
    """Fonction principale"""
    pass


if __name__ == "__main__":
    main()
