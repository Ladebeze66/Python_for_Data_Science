# NULL_not_found.py

def NULL_not_found(object: any) -> int:
    """
    Identifie et affiche les types d'objets considérés comme "Null".
    
    Cette fonction examine si l'objet passé correspond à l'un des 5 types
    de valeurs "Null" reconnus :
    - None (NoneType)
    - float("NaN") (float NaN)  
    - 0 (int zéro)
    - "" (str chaîne vide)
    - False (bool faux)
    
    Args:
        object (any): L'objet à analyser
        
    Returns:
        int: 0 si l'objet est un type "Null", 1 sinon
    """
    if object is None:
        print("Nothing: None", type(object)) 
        return 0
    elif type(object) == float and str(object) == "nan":
        print("Cheese: nan", type(object))
        return 0
    elif type(object) == int and object == 0:
        print("Zero: 0", type(object))
        return 0
    elif type(object) == str and object == "":
        print("Empty:", type(object))
        return 0
    elif type(object) == bool and object is False:
        print("Fake: False", type(object))
        return 0
    else:
        print("Type not Found")
        return 1