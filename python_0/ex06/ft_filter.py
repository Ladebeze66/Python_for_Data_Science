def ft_filter(function, iterable):
    """
    Réimplémentation de filter() avec list comprehensions.

    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.

    Args:
        function: Fonction de prédicat ou None
        iterable: Séquence à filtrer

    Returns:
        generator: Générateur des éléments filtrés
    """
    if function is None:
        # Cas None : filtrer les valeurs truthy
        return (item for item in iterable if item)
    else:
        # Cas fonction : appliquer le prédicat
        return (item for item in iterable if function(item))
        # list comprehension
