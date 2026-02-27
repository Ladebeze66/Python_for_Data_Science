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

• Vous devez rendre vos modules depuis un ordinateur du cluster en utilisant soit une machine virtuelle :
  ◦ Vous pouvez choisir le système d'exploitation à utiliser pour votre machine virtuelle
  ◦ Votre machine virtuelle doit avoir tous les logiciels nécessaires pour réaliser votre projet. Ces logiciels doivent être configurés et installés.
• Ou vous pouvez utiliser l'ordinateur directement si les outils sont disponibles.
  ◦ Assurez-vous d'avoir l'espace sur votre session pour installer ce dont vous avez besoin pour tous les modules (utilisez le goinfre si votre campus en a un)
  ◦ Vous devez avoir tout installé avant les évaluations
• Vos fonctions ne doivent pas quitter de manière inattendue (segmentation fault, bus error, double free, etc) en dehors des comportements non définis. Si cela arrive, votre projet sera considéré comme non fonctionnel et recevra un 0 pendant l'évaluation.
• Nous vous encourageons à créer des programmes de test pour votre projet même si ce travail n'aura pas à être rendu et ne sera pas noté. Cela vous donnera une chance de tester facilement votre travail et celui de vos pairs. Vous trouverez ces tests particulièrement utiles pendant votre soutenance. En effet, pendant la soutenance, vous êtes libre d'utiliser vos tests et/ou les tests du pair que vous évaluez.
• Rendez votre travail dans votre dépôt git assigné. Seul le travail dans le dépôt git sera noté. Si Deepthought est assigné pour noter votre travail, cela sera fait après vos peer-évaluations. Si une erreur arrive dans n'importe quelle section de votre travail pendant la notation de Deepthought, l'évaluation s'arrêtera.
• Vous devez utiliser la version Python 3.10
• Vos imports de lib doivent être explicites, par exemple vous devez "import numpy as np". Importer "from pandas import *" n'est pas autorisé, et vous aurez 0 à l'exercice.
• Il n'y a pas de variable globale.
• Par Odin, par Thor ! Utilisez votre cerveau !!!

------------------------------------------------------------------------

# Chapitre II --- Instructions spécifiques du jour

• Aucun code dans le scope global. Utilisez des fonctions !
• Chaque programme doit avoir son main et ne pas être un simple script :

```python
def main():
    # vos tests et votre gestion d'erreur
    
if __name__ == "__main__":
    main()
```

• Toute exception non gérée invalidera les exercices, même dans le cas d'une erreur que vous étiez censé tester.
• Vous pouvez utiliser n'importe quelle fonction built-in si elle n'est pas interdite dans l'exercice.
• Toutes vos fonctions doivent avoir une documentation (__doc__)
• Votre code doit être à la norme
  ◦ pip install flake8
  ◦ alias norminette=flake8

Pour ce module, nous utiliserons des données de FREE SCHOOL MATERIALS FROM GAPMINDER.ORG, CC-BY LICENSE.
Nous vous encourageons à jeter un œil aux données disponibles si vous voulez vous entraîner à manipuler des données ou faire de la visualisation de données.

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Exercice 00: Load my Dataset

**Répertoire de rendu :** ex00/  
**Fichiers à rendre :** load_csv.py  
**Fonctions autorisées :** pandas ou toute lib pour la manipulation de dataset  

Créez une fonction qui prend un chemin en argument, écrit les dimensions du dataset et le retourne. Vous devez gérer les cas d'erreur et retourner None si le chemin est mauvais, mauvais format...

```python
def load(path: str) -> Dataset:  # (Vous devez adapter le type de retour selon votre librairie)
    # votre code ici
```

Votre script de test :

```python
from load_csv import load
print(load("life_expectancy_years.csv"))
```

```bash
$> python tester.py
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
$>
```

Vous pouvez afficher le Dataset dans n'importe quel format que vous aimez, le format donné n'est pas restrictif.

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## Exercice 01: draw my country

**Répertoire de rendu :** ex01/  
**Fichiers à rendre :** load_csv.py, aff_life.py  
**Fonctions autorisées :** matplotlib, seaborn ou toute lib pour la visualisation de données  

Créez un programme qui appelle la fonction load de l'exercice précédent, charge le fichier life_expectancy_years.csv, et affiche les informations du pays de votre campus. Votre graphique doit avoir un titre et une légende pour chaque axe.

Par exemple, pour les campus 42 en France nous aurons ce résultat.

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## Exercice 02: compare my country

**Répertoire de rendu :** ex02/  
**Fichiers à rendre :** load_csv.py, aff_pop.py  
**Fonctions autorisées :** matplotlib, seaborn ou toute lib pour la visualisation de données  

Créez un programme qui appelle la fonction load du premier exercice, charge le fichier population_total.csv, et affiche les informations du pays de votre campus versus un autre pays de votre choix. Votre graphique doit avoir un titre, une légende pour chaque axe et une légende pour chaque graphique.

Vous devez afficher les années de 1800 à 2050.

Par exemple, pour les campus 42 en France nous aurons ce résultat.

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## Exercice 03: draw my year

**Répertoire de rendu :** ex03/  
**Fichiers à rendre :** load_csv.py, projection_life.py  
**Fonctions autorisées :** matplotlib, seaborn ou toute lib pour la visualisation de données et votre lib de l'ex00  

Créez un programme qui appelle la fonction load du premier exercice, charge les fichiers "income_per_person_gdppercapita_ppp_inflation_adjusted.csv" et "life_expectancy_years.csv", et affiche la projection de l'espérance de vie en relation avec le produit national brut de l'année 1900 pour chaque pays.

Votre graphique doit avoir un titre, une légende pour chaque axe et une légende pour chaque graphique.

Vous devez afficher l'année 1900.

**Voyez-vous une corrélation entre l'espérance de vie et le produit intérieur brut ?**

------------------------------------------------------------------------

# Chapitre VII --- Rendu et peer-évaluation

Rendez votre travail dans votre dépôt Git comme d'habitude. Seul le travail à l'intérieur de votre dépôt sera évalué pendant la soutenance. N'hésitez pas à vérifier deux fois les noms de vos dossiers et fichiers pour vous assurer qu'ils sont corrects.

**Le processus d'évaluation se déroulera sur l'ordinateur du groupe évalué.**
