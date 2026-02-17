# Training Piscine Python for Data Science - 4

## Data Oriented Design --- Traduction française

**Résumé :** Aujourd'hui, vous allez découvrir des principes de
conception orientée données et des structures avancées.\
Version : 1.00

------------------------------------------------------------------------

# Sommaire

-   I --- Règles générales
-   II --- Instructions spécifiques du jour
-   III --- Exercice 00
-   IV --- Exercice 01
-   V --- Exercice 02
-   VI --- Exercice 03
-   VII --- Rendu et peer-évaluation

------------------------------------------------------------------------

# Chapitre I --- Règles générales

-   Rendre les modules depuis le cluster ou une machine virtuelle
    configurée.
-   Tout doit être installé avant les évaluations.
-   Les fonctions ne doivent pas planter.
-   Seul le dépôt Git est évalué.
-   Python **3.10 obligatoire**.
-   Imports explicites (`import numpy as np`).
-   Aucune variable globale.
-   Par Odin, par Thor... utilisez votre cerveau !

------------------------------------------------------------------------

# Chapitre II --- Instructions spécifiques du jour

Un reproche fréquent envers les data scientists est d'écrire du code peu
structuré. L'objectif de ce module est d'éviter le code inefficace et
les variables codées en dur.

-   Aucun code dans le scope global.
-   Chaque programme doit contenir :

```{=html}
<!-- -->
```
    def main():
        pass

    if __name__ == "__main__":
        main()

-   Toute exception non gérée invalide l'exercice.
-   Toutes les fonctions, classes et méthodes doivent avoir une
    docstring.
-   Respecter la norme flake8.

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Calculate my statistics

**Dossier :** ex00/\
**Fichier :** statistics.py\
**Fonctions autorisées :** aucune

Créer :

    def ft_statistics(*args: Any, **kwargs: Any) -> None:

Objectif :

-   Calculer :
    -   Mean (moyenne)
    -   Median (médiane)
    -   Quartiles (25% et 75%)
    -   Standard deviation (écart-type)
    -   Variance
-   Les calculs dépendent des kwargs demandés.
-   Gérer les erreurs correctement.

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## Outer_inner

**Dossier :** ex01/\
**Fichier :** in_out.py

Créer :

    def square(x)
    def pow(x)
    def outer(x, function)

Objectif :

-   Retourner un objet fonction.
-   Chaque appel applique une transformation successive.
-   Utiliser une fonction interne (`inner`) avec fermeture (closure).

⚠️ Les variables globales sont interdites.

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## my first decorating

**Dossier :** ex02/\
**Fichier :** callLimit.py

Créer un décorateur :

    def callLimit(limit: int):

Objectif :

-   Limiter le nombre d'appels d'une fonction.
-   Afficher une erreur si la limite est dépassée.
-   Utiliser des wrappers.

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## data class

**Dossier :** ex03/\
**Fichier :** new_student.py\
Librairies autorisées : dataclasses, random, string

Créer une dataclass :

    @dataclass
    class Student:

Exigences :

-   Champs :
    -   name
    -   surname
    -   active = True
-   Générer :
    -   login automatiquement
    -   id aléatoire via `generate_id()`
-   login et id ne doivent pas être initialisables.
-   Ne pas utiliser `__str__` ni `__repr__`.

------------------------------------------------------------------------

# Chapitre VII --- Rendu et peer-évaluation

-   Déposer le projet dans le dépôt Git.
-   Vérifier noms fichiers et dossiers.
-   L'évaluation se fait sur la machine du groupe évalué.
