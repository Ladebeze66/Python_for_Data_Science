# whatis.py
import sys # pour recevoir les arguments de la ligne de commande

def check_even_odd(number):
    """
    Détermine si un nombre est pair ou impair et affiche le résultat.
    
    Args:
        number (int): Le nombre à analyser
    """
    if number %2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
        
def process_argument(arg_str):
    """
    Valide et convertit l'argument string en entier, puis l'analyse.
    
    Args:
        arg_str (str): L'argument à traiter
        
    Raises:
        AssertionError: Si l'argument n'est pas un entier valide
    """
    try:
        number = int(arg_str)
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    check_even_odd(number)
    
def main():
    """
    Fonction principale qui gère les arguments de ligne de commande.
    
    Raises:
        AssertionError: Si le nombre d'arguments est invalide
    """
    try:
        argc = len(sys.argv)
    
        if argc == 1:
            # 0 argument - comportement silencieux
            return
        elif argc == 2:
            # 1 argument - triatement normal
            process_argument(sys.argv[1])
        else:
            # Plus de 2 arguments - erreur
            raise AssertionError("more than one argument is provided")
    
    except AssertionError as e:
        # Capture l'AssertionError et afficher seulement le message
        print(f"AssertionError: {e}")
        
if __name__ == "__main__":
    main()