import sys


def is_punctuation(char):
    """
    Vérifie si un caractère est de la ponctuation.

    Utilise la définition standard ASCII de la ponctuation sans
    dépendre du module string, conformément aux contraintes de l'exercice.

    Args:
        char(str): Le caractère à vérifier (doit être de longeur 1)

    Returns:
        bool: True si le caractère est de la ponctuation, False sinon
    """
    # Défintion manuelle des caractères de ponctuation ASCII
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return char in punctuation_chars


def analyze_text(text):
    """
    Analyse une chaîne de caractères et compte les différents types.

    Parcourt chaque caractère du texte et le classe dans une des
    5 catégories : majuscules, minuscules, chiffres, espaces, ponctuation.
    Les caractères qui ne correspondent à aucune catégorie sont ignorés.

    Args:
        text(str): Le texte à analyser

    Returns:
        dict: Dictionnaire contenant les compteurs pour chaque catégorie:
        - "upper": Nombre de lettres majuscules
        - "lower": Nombre de lettres minuscules
        - "digits": Nombre de chiffres
        - "spaces": Nombre d'espaces (incluant tabs, newlines)
        _ "punctuation": nombre de signes de ponctuation
    """
    counts = {
        'upper': 0,
        'lower': 0,
        'digits': 0,
        'spaces': 0,
        'punctuation': 0,
    }

    for char in text:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif is_punctuation(char):
            counts['punctuation'] += 1
        # Note: les caractères non-ASCII ou autres sont ignorés

    return counts


def display_results(text, counts):
    """
    Affiche les résultats de l'analyse de texte au format requis.

    Formate et affiche le nombre total de caractères suivi du détail
    par catégorie selon format exact spécifié dans l'énoncé.

    Args:
        text(str): Le texte original analysé
        counts(dict): Dictionnaire des compteurs par catégorie
    """
    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def get_user_input():
    """
    Demande une saisie à l'utilisateur de manière interactive.

    Gère automatiquement les deux cas selon l'énoncé :
    - Entrée normale : le retour chariot compte comme un espace
    - Ctrl+D : pas de retour chariot, donc pas d'espace supplémentaire

    Returns:
        tuple: (text, has_carriage_return) où has_carriage_return
               indique si un retour chariot doit être ajouté comme espace

    Raises:
        KeyboardInterrupt: Si l'utilisateur interrompt avec Ctrl+C
        EOFError: Si l'utilisateur utilise Ctrl+D sans texte
    """
    print("What is the text to count?", flush=True)
    # flush=True pour garantir l'affichage immédiat

    try:
        # Utiliser sys.stdin.readline() pour capturer le comportement exact
        text = sys.stdin.readline()

        if text.endswith('\n'):
            # Entrée normale : supprimer le \n et ajouter un espace
            return text[:-1], True
        else:
            # Ctrl+D après du texte : pas de \n, pas d'espace supplémentaire
            return text, False

    except EOFError:
        # Ctrl+D sans texte : re-lever l'exception
        raise


def validate_arguments():
    """
    Valide le nombre d'arguments de ligne de commande.

    Vérifie que le programme reçoit 0 ou 1 argument (en plus du nom
    du script). Lève une exception si plus d'un argument est fourni.

    Returns:
        str ou None: Le texte à analyser si fourni en argument,
        None si aucun argument (mode interactif)

    Raises:
        AssertionError: Si plus d'un argument est fourni
    """
    argc = len(sys.argv)

    if argc == 1:
        # Aucun argument - mode interactif
        return None
    elif argc == 2:
        # un argument - mode direct
        return sys.argv[1]
    else:
        # Trop d'arguments - erreur
        raise AssertionError("more than one argument is provided")


def main():
    """
    Fonction principale du programme.

    Orchestre l'exécution complète : validation des arguments,
    obtention du texte (argument ou saisie), analyse et affichage
    des résultats. Gère toutes les exceptions possibles selon
    les nouvelles règles.
    """
    try:
        # Validation et récupération des arguments
        text_from_arg = validate_arguments()

        if text_from_arg is None:
            # Mode interactif - demander saisie utilisateur
            text, has_carriage_return = get_user_input()

            # Ajouter l'espace du retour chariot si nécessaire
            if has_carriage_return:
                text = text + " "
        else:
            # Mode direct - utiliser l'argument fourni
            text = text_from_arg

        # Analyser le texte
        counts = analyze_text(text)

        # Afficher les résultats
        display_results(text, counts)

    except AssertionError as e:
        # Erreurs de validation des arguments
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        # Interruption par Ctrl+C
        print("\nProgram interrupted by user")
    except EOFError:
        # Ctrl+D sans texte
        print("\nEnd of input reached")
    except Exception as e:
        # Toute autre erreur inattendue
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
