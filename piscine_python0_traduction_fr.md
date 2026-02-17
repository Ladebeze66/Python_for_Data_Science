# Training Piscine Python for Data Science - 0

## Starting --- Traduction française

**Résumé :** Aujourd'hui, vous apprendrez les bases du langage Python.\
Version : 1.3

------------------------------------------------------------------------

# Sommaire

-   I --- Règles générales
-   II --- Exercice 00
-   III --- Exercice 01
-   IV --- Exercice 02
-   V --- Exercice 03
-   VI --- Exercice 04
-   VII --- Règles supplémentaires
-   VIII --- Exercice 05
-   IX --- Exercice 06
-   X --- Exercice 07
-   XI --- Exercice 08
-   XII --- Exercice 09
-   XIII --- Rendu et peer‑évaluation

------------------------------------------------------------------------

# Chapitre I --- Règles générales

-   Vous devez soumettre vos modules depuis un ordinateur du cluster ou
    via une machine virtuelle.
-   Vous pouvez choisir le système de votre VM, mais elle doit être
    correctement configurée.
-   Tout doit être installé avant les évaluations.
-   Vos fonctions ne doivent jamais planter.
-   Créez vos propres tests pour faciliter la validation.
-   Seul le contenu du dépôt Git sera évalué.
-   Python **3.10 obligatoire**.
-   Les imports doivent être explicites (`import numpy as np`).
-   Les variables globales sont interdites.
-   Par Odin, par Thor... utilisez votre cerveau !

------------------------------------------------------------------------

# Chapitre II --- Exercice 00

## First python script

**Dossier :** ex00/\
**Fichier :** Hello.py\
**Fonctions autorisées :** aucune

Modifier les structures pour afficher :

-   Hello World
-   Hello pays
-   Hello ville
-   Hello campus

Sortie attendue :

    ['Hello', 'World!']
    ('Hello', 'France!')
    {'Hello', 'Paris!'}
    {'Hello': '42Paris!'}

------------------------------------------------------------------------

# Chapitre III --- Exercice 01

## First use of package

**Fichier :** format_ft_time.py\
**Librairies autorisées :** time, datetime

Créer un script qui affiche :

-   le timestamp depuis 1970
-   la notation scientifique
-   la date formatée

------------------------------------------------------------------------

# Chapitre IV --- Exercice 02

## First function python

**Fichier :** find_ft_type.py

Créer une fonction :

    def all_thing_is_obj(object: any) -> int:

-   Affiche le type d'objet
-   Retourne 42

------------------------------------------------------------------------

# Chapitre V --- Exercice 03

## NULL not found

**Fichier :** NULL_not_found.py

Créer :

    def NULL_not_found(object: any) -> int:

-   Affiche les types Null (`None`, `NaN`, etc.)
-   Retourne 0 si OK, sinon 1

------------------------------------------------------------------------

# Chapitre VI --- Exercice 04

## The Even and the Odd

**Fichier :** whatis.py\
Utiliser `sys`.

-   Prend un nombre en argument
-   Affiche pair ou impair
-   AssertionError si invalide

------------------------------------------------------------------------

# Chapitre VII --- Règles supplémentaires

-   Pas de code global.
-   Chaque programme doit avoir :

```{=html}
<!-- -->
```
    def main():
        pass

    if __name__ == "__main__":
        main()

-   Toutes les fonctions doivent avoir une docstring.
-   Respecter la norme flake8.

------------------------------------------------------------------------

# Chapitre VIII --- Exercice 05

## Programme autonome

**Fichier :** building.py

Créer un programme qui analyse une chaîne :

-   Majuscules
-   Minuscules
-   Ponctuation
-   Espaces
-   Chiffres

Demande une entrée si aucun argument.

------------------------------------------------------------------------

# Chapitre IX --- Exercice 06

## Recode filter

**Fichiers :** - ft_filter.py - filterstring.py

### Partie 1

Recréer `filter` avec :

-   list comprehension
-   lambda

Utilisation du vrai filter interdite.

### Partie 2

Programme qui retourne les mots d'une longueur \> N.

------------------------------------------------------------------------

# Chapitre X --- Exercice 07

## Dictionaries SoS

**Fichier :** sos.py

Encoder une chaîne en Morse.

-   Utiliser un dictionnaire.
-   `.` et `-`
-   espace → `/`

------------------------------------------------------------------------

# Chapitre XI --- Exercice 08

## Loading ...

**Fichier :** Loading.py

Créer une fonction `ft_tqdm` qui imite tqdm avec `yield`.

Possibilité d'utiliser `get_terminal_size`.

------------------------------------------------------------------------

# Chapitre XII --- Exercice 09

## Création de package Python

Créer un package installable via pip.

Il doit :

-   apparaître dans `pip list`
-   fonctionner avec :

```{=html}
<!-- -->
```
    from ft_package import count_in_list

------------------------------------------------------------------------

# Chapitre XIII --- Rendu et peer‑évaluation

-   Déposer dans le dépôt Git.
-   Vérifier noms des dossiers et fichiers.
-   L'évaluation se fait sur l'ordinateur du groupe évalué.
