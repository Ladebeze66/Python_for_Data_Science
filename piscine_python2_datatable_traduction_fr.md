# Training Piscine Python for Data Science - 2

## DataTable --- Traduction française

**Résumé :** Aujourd'hui, vous apprendrez à charger, manipuler et
afficher des DataTables.\
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
-   Créer vos propres tests est conseillé.
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
-   Toutes les fonctions doivent avoir une docstring.
-   Respecter la norme flake8.
-   Les datasets utilisés proviennent de GAPMINDER (CC-BY).

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Load my Dataset

**Fichier :** load_csv.py\
Librairies autorisées : pandas ou équivalent.

Créer :

    def load(path: str):

-   Charger un dataset CSV.
-   Afficher ses dimensions.
-   Retourner le dataset.
-   Retourner `None` en cas d'erreur.

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## draw my country

**Fichiers :** - load_csv.py - aff_life.py

Créer un programme qui :

-   Charge `life_expectancy_years.csv`
-   Affiche l'évolution pour le pays de ton campus
-   Graph avec titre et axes légendés

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## compare my country

**Fichiers :** - load_csv.py - aff_pop.py

Créer un programme qui :

-   Charge `population_total.csv`
-   Compare ton pays avec un autre
-   Affiche les années **1800 à 2050**
-   Graph avec titre et légendes

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## draw my year

**Fichiers :** - load_csv.py - projection_life.py

Créer un programme qui :

-   Charge :
    -   income_per_person_gdppercapita_ppp_inflation_adjusted.csv
    -   life_expectancy_years.csv
-   Affiche la projection espérance de vie vs PIB pour **1900**
-   Graph avec titres et axes légendés

Objectif : observer la corrélation entre espérance de vie et PIB.

------------------------------------------------------------------------

# Chapitre VII --- Rendu et peer-évaluation

-   Déposer le projet dans le dépôt Git.
-   Vérifier noms fichiers et dossiers.
-   L'évaluation se fait sur la machine du groupe évalué.
