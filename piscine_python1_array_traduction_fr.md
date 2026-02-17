# Training Piscine Python for Data Science - 1

## Array --- Traduction française

**Résumé :** Aujourd'hui, vous découvrirez les tableaux (arrays), leurs
manipulations et le travail sur les images.\
Version : 1.1

------------------------------------------------------------------------

# Sommaire

-   I --- Règles générales
-   II --- Instructions spécifiques du jour
-   III --- Exercice 00
-   IV --- Exercice 01
-   V --- Exercice 02
-   VI --- Exercice 03
-   VII --- Exercice 04
-   VIII --- Exercice 05
-   IX --- Rendu et peer-évaluation

------------------------------------------------------------------------

# Chapitre I --- Règles générales

-   Soumettre les modules depuis le cluster ou une machine virtuelle
    configurée.
-   Tout doit être installé avant les évaluations.
-   Les fonctions ne doivent jamais planter.
-   Créer vos propres tests est fortement conseillé.
-   Seul le dépôt Git est évalué.
-   Python **3.10 obligatoire**.
-   Imports explicites (`import numpy as np`).
-   Aucune variable globale.
-   Par Odin, par Thor... utilisez votre cerveau !

------------------------------------------------------------------------

# Chapitre II --- Instructions spécifiques du jour

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
-   Les fonctions doivent avoir une docstring.
-   Respecter la norme flake8.

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Give my BMI

**Fichier :** give_bmi.py\
Créer :

    def give_bmi(height, weight) -> list:
    def apply_limit(bmi, limit) -> list:

-   Calculer les BMI.
-   Retourner une liste de booléens selon une limite.
-   Gérer les erreurs (types, tailles).

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## 2D array

**Fichier :** array2D.py

Créer :

    def slice_me(family, start, end) -> list:

-   Afficher la shape.
-   Retourner un slice du tableau 2D.
-   Utiliser le slicing.

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## load my image

**Fichier :** load_image.py

Créer :

    def ft_load(path: str):

-   Charger une image JPG/JPEG.
-   Afficher shape et pixels RGB.
-   Gérer les erreurs clairement.

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## zoom on me

**Fichiers :** - load_image.py - zoom.py

Programme qui :

-   Charge "animal.jpeg"
-   Affiche dimensions, channels, pixels
-   Effectue un zoom (slice)
-   Affiche les axes X/Y

------------------------------------------------------------------------

# Chapitre VII --- Exercice 04

## rotate me

**Fichiers :** - load_image.py - rotate.py

-   Découper un carré dans l'image
-   Faire une transpose
-   Afficher nouvelle shape

⚠️ La transpose doit être faite **sans librairie**.

------------------------------------------------------------------------

# Chapitre VIII --- Exercice 05

## Pimp my image

**Fichiers :** - load_image.py - pimp_image.py

Créer 5 fonctions :

    ft_invert
    ft_red
    ft_green
    ft_blue
    ft_grey

-   Appliquer des filtres couleur.
-   Conserver la même shape.
-   Respecter les opérateurs autorisés.

------------------------------------------------------------------------

# Chapitre IX --- Rendu et peer-évaluation

-   Déposer dans le dépôt Git.
-   Vérifier noms fichiers et dossiers.
-   L'évaluation se fait sur la machine du groupe évalué.
