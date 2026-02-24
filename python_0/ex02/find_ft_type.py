def all_thing_is_obj(object: any) -> int:
    """
    Analyse le type d'un objet et affiche un message formaté.
    
    Cette fonction examine le type de l'objet passé en paramètre et affiche
    un message personnalisé selon le type détecté :
    - Les conteneurs (list, tuple, set, dict) : "Type : <class 'type'>"
    - Les chaînes : "contenu is in the kitchen : <class 'str'>"
    - Autres types : "Type not found"
    
    Args:
        object (any): L'objet à analyser
        
    Returns:
        int: Retourne toujours 42
    """
    if isinstance(object, list):
        print("List :", type(object))
    elif isinstance(object, tuple):
        print("Tuple :", type(object))
    elif isinstance(object, set):
        print("Set :", type(object))
    elif isinstance(object, dict):
        print("Dict :", type(object))
    elif isinstance(object, str):
        print(f"{object} is in the kitchen :", type(object))
    else:
        print("Type not found")
    
    return 42

# IMPORTANT : Aucun code d'exécution ici !
# Le fichier doit être un module pur, importable sans effet de bord.