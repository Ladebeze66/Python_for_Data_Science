import sys
from ft_filter import ft_filter


def validate_arguments():
    """
    Valide les arguments de ligne de commande.
    Vérifie qu'il y a exactement 2 arguments : une chaîne et un entier.

    Returns:
        tuple: (string, int) les arguments validés

    Raises:
        AssertionError: Si les arguments sont invalides
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        text = sys.argv[1]

        # Vérifier que le 1er argument n'est pas un nombre
        try:
            int(text)
            # Si on arrive ici, c'est un nombre → erreur !
            raise AssertionError("the arguments are bad")
        except ValueError:
            # Parfait, ce n'est pas un nombre
            pass

        # Le 2ème argument doit être convertible en entier
        length_threshold = int(sys.argv[2])

        return text, length_threshold

    except ValueError:
        raise AssertionError("the arguments are bad")


def filter_words_by_length(text, min_length):
    """
    Filtre les mots d'un texte par longueur minimale.

    Utilise list comprehension et lambda comme requis par l'énoncé.

    Args:
        text (str): Texte contenant les mots séparés par des espaces
        min_length (int): Longueur minimale (exclusive)

    Returns:
        list: Liste des mots ayant une longueur > min_length
    """
    # Séparer le texte en mots (par espaces)
    words = text.split()

    # Utiliser ft_filter avec lambda (requis par l'énoncé)
    filtered_words = ft_filter(lambda word: len(word) > min_length, words)

    # Convertir en liste avec list comprehension (requis par l'énoncé)
    return [word for word in filtered_words]


def main():
    """
    Fonction principale du programme.

    Filtre les mots d'une chaîne selon leur longueur et affiche le résultat.
    """
    try:
        # Validation des arguments
        text, min_length = validate_arguments()

        # Filtrage des mots
        result = filter_words_by_length(text, min_length)

        # Affichage du résultat
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
