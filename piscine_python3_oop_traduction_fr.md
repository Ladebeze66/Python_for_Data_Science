# Training Piscine Python for Data Science - 3

## Oriented Object Programming --- Traduction française

**Résumé :** Aujourd'hui, vous allez découvrir les classes et l'héritage
en programmation orientée objet.\
Version : 1.00

------------------------------------------------------------------------

# Sommaire

-   I --- Règles générales
-   II --- Instructions spécifiques du jour
-   III --- Exercice 00
-   IV --- Exercice 01
-   V --- Exercice 02
-   VI --- Exercice 03
-   VII --- Exercice 04
-   VIII --- Rendu et peer-évaluation

------------------------------------------------------------------------

# Chapitre I --- Règles générales

-   Rendre les modules depuis le cluster ou une machine virtuelle
    configurée.
-   Tout doit être installé avant les évaluations.
-   Les fonctions ne doivent pas planter.
-   Seul le dépôt Git est évalué.
-   Python **3.10 obligatoire**.
-   Imports explicites.
-   Aucune variable globale.

------------------------------------------------------------------------

# Chapitre II --- Instructions spécifiques du jour

Objectif : écrire du code orienté objet propre et éviter le code non
structuré.

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
-   Toutes les classes, méthodes et fonctions doivent avoir une
    docstring.
-   Respecter flake8.

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## GOT S1E9

**Fichier :** S1E9.py

Créer :

-   Une classe abstraite `Character`
-   Paramètres :
    -   `first_name`
    -   `is_alive=True` par défaut
-   Méthode permettant de passer `is_alive` à False.
-   Classe `Stark` héritant de `Character`.

⚠️ Impossible d'instancier `Character` directement.

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## GOT S1E7

**Fichier :** S1E7.py

Créer deux familles héritant de `Character` :

-   `Baratheon`
-   `Lannister`

Exigences :

-   `__str__` et `__repr__` doivent retourner des chaînes.
-   Ajouter une méthode de classe pour créer un Lannister en chaîne.

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## Now it's weird!

**Fichier :** DiamondTrap.py

Créer une classe :

    class King(Baratheon, Lannister)

-   Héritage multiple.
-   Utiliser des Properties pour modifier :
    -   eyes
    -   hairs

Python utilise la **linéarisation C3** pour gérer l'héritage diamant.

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## Calculate my vector

**Fichier :** ft_calculator.py

Créer une classe :

    class calculator

Opérations avec un scalaire :

-   addition (`__add__`)
-   multiplication (`__mul__`)
-   soustraction (`__sub__`)
-   division (`__truediv__`)

Pas de gestion d'erreurs sauf division par zéro.

------------------------------------------------------------------------

# Chapitre VII --- Exercice 04

## Calculate my dot product

**Fichier :** ft_calculator.py

Créer des méthodes statiques ou décorées :

    dotproduct
    add_vec
    sous_vec

-   Calculs entre deux vecteurs.
-   Pas de gestion d'erreurs.
-   Les méthodes doivent être appelables sans instancier la classe.

------------------------------------------------------------------------

# Chapitre VIII --- Rendu et peer-évaluation

-   Déposer le projet dans le dépôt Git.
-   Vérifier noms fichiers et dossiers.
-   L'évaluation se fait sur la machine du groupe évalué.
