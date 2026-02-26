# ft_package/count.py
def count_in_list(lst, item):
    """
    Compte le nombre d'occurrences d'un élément dans une liste.

    Args:
        lst (list): La liste dans laquelle chercher
        item: L'élément à compter

    Returns:
        int: Le nombre d'occurrences de l'élément
    """
    return lst.count(item)
