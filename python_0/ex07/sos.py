import sys


# Dictionnaire de correspondance Morse
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. "
}


def validate_arguments():
    """
    Valide les arguments de ligne de commande.

    Vérifie qu'il y a exactement 1 argument (chaîne à encoder).

    Returns:
        str: La chaîne à encoder en Morse

    Raises:
        AssertionError: Si les arguments sont invalides
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    return sys.argv[1]


def validate_string_content(text):
    """
    Valide que la chaîne ne contient que des caractères supportés.

    Vérifie que tous les caractères sont alphanumériques ou des espaces.

    Args:
        text (str): La chaîne à valider

    Raises:
        AssertionError: Si la chaîne contient des caractères non supportés
    """
    for char in text:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")


def encode_to_morse(text):
    """
    Encode une chaîne en code Morse.

    Convertit chaque caractère selon le dictionnaire NESTED_MORSE.
    Les caractères sont automatiquement convertis en majuscules.

    Args:
        text (str): La chaîne à encoder

    Returns:
        str: La chaîne encodée en Morse (sans espace final)
    """
    morse_parts = []

    for char in text.upper():
        morse_code = NESTED_MORSE[char]
        morse_parts.append(morse_code)

    # Joindre tous les codes et supprimer l'espace final
    result = "".join(morse_parts).rstrip()
    return result


def main():
    """
    Fonction principale du programme.

    Encode une chaîne fournie en argument en code Morse et affiche le résultat.
    """
    try:
        # Validation des arguments
        text = validate_arguments()

        # Validation du contenu
        validate_string_content(text)

        # Encodage en Morse
        morse_result = encode_to_morse(text)

        # Affichage du résultat
        print(morse_result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
