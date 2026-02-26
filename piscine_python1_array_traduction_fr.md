# Training Piscine Python for datascience - 1

## Array

**Résumé :** Aujourd'hui, vous découvrirez les tableaux (arrays), leurs manipulations et le travail sur les images.\
**Version :** 1.1

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

• Vous devez rendre vos modules depuis un ordinateur du cluster soit en utilisant une machine virtuelle :
  ◦ Vous pouvez choisir le système d'exploitation à utiliser pour votre machine virtuelle
  ◦ Votre machine virtuelle doit avoir tous les logiciels nécessaires pour réaliser votre projet. Ces logiciels doivent être configurés et installés.
• Ou vous pouvez utiliser l'ordinateur directement au cas où les outils sont disponibles.
  ◦ Assurez-vous d'avoir l'espace sur votre session pour installer ce dont vous avez besoin pour tous les modules (utilisez le goinfre si votre campus en a un)
  ◦ Vous devez avoir tout installé avant les évaluations
• Vos fonctions ne doivent pas quitter de manière inattendue (segmentation fault, bus error, double free, etc.) en dehors des comportements indéfinis. Si cela arrive, votre projet sera considéré comme non fonctionnel et recevra un 0 pendant l'évaluation.
• Nous vous encourageons à créer des programmes de test pour votre projet même si ce travail n'aura pas à être soumis et ne sera pas noté. Cela vous donnera une chance de tester facilement votre travail et celui de vos pairs. Vous trouverez ces tests particulièrement utiles pendant votre défense. En effet, pendant la défense, vous êtes libre d'utiliser vos tests et/ou les tests du pair que vous évaluez.
• Soumettez votre travail à votre dépôt git assigné. Seul le travail dans le dépôt git sera noté. Si Deepthought est assigné pour noter votre travail, cela se fera après vos peer-évaluations. Si une erreur arrive dans n'importe quelle section de votre travail pendant la notation de Deepthought, l'évaluation s'arrêtera.
• Vous devez utiliser Python version 3.10
• Vos imports de librairie doivent être explicites, par exemple vous devez "import numpy as np". Importer "from pandas import *" n'est pas autorisé, et vous aurez 0 à l'exercice.
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
• Vous pouvez utiliser toute fonction built-in si elle n'est pas interdite dans l'exercice.
• Toutes vos fonctions doivent avoir une documentation (__doc__)
• Votre code doit être à la norme :
  ◦ pip install flake8
  ◦ alias norminette=flake8

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Give my BMI

**Dossier :** ex00/\
**Fichiers :** give_bmi.py\
**Fonctions autorisées :** numpy ou toute librairie de manipulation de tableaux

Votre fonction `give_bmi` prend 2 listes d'entiers ou de flottants en entrée et retourne une liste de valeurs BMI.

Votre fonction `apply_limit` accepte une liste d'entiers ou de flottants et un entier représentant une limite comme paramètres. Elle retourne une liste de booléens (True si au-dessus de la limite).

Vous devez gérer les cas d'erreur si les listes ne sont pas de la même taille, ne sont pas des int ou float...

**Le prototype des fonctions est :**
```python
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #your code here

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    #your code here
```

**Votre tester.py :**
```python
from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

**Sortie attendue :**
```
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
$>
```

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## 2D array

**Dossier :** ex01/\
**Fichiers :** array2D.py\
**Fonctions autorisées :** numpy ou toute librairie de manipulation de tableaux

Écrivez une fonction qui prend comme paramètres un tableau 2D, affiche sa forme (shape), et retourne une version tronquée du tableau basée sur les arguments start et end fournis.

Vous devez utiliser la méthode de slicing.

Vous devez gérer les cas d'erreur si les listes ne sont pas de la même taille, ne sont pas des listes...

**Le prototype de la fonction est :**
```python
def slice_me(family: list, start: int, end: int) -> list:
    #your code here
```

**Votre tester.py :**
```python
from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

**Sortie attendue :**
```
$> python test_array2D.py
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
$>
```

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## load my image

**Dossier :** ex02/\
**Fichiers :** load_image.py\
**Fonctions autorisées :** toutes les librairies pour charger des images et manipuler des tableaux

Vous devez écrire une fonction qui charge une image, affiche son format, et son contenu de pixels au format RGB.

Vous devez gérer, au minimum, les formats JPG et JPEG.

Vous devez gérer toute erreur avec un message d'erreur clair.

**Voici comment elle doit être prototypée :**
```python
def ft_load(path: str) -> array:  # (vous pouvez retourner le format désiré)
    #your code here
```

**Votre tester.py :**
```python
from load_image import ft_load

print(ft_load("landscape.jpg"))
```

**Sortie attendue :**
```
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
  [23 42 84]
  [28 43 84]
  ...
  [ 0  0  0]
  [ 1  1  1]
  [ 1  1  1]]]
$>
```

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## zoom on me

**Dossier :** ex03/\
**Fichiers :** load_image.py, zoom.py\
**Fonctions autorisées :** toutes les librairies pour charger, manipuler, afficher des images et manipuler des tableaux

Créez un programme qui doit charger l'image "animal.jpeg", afficher des informations à son sujet et l'afficher après "zoom".

• La taille en pixels sur les axes X et Y
• Le nombre de canaux
• Le contenu en pixels de l'image
• Afficher l'échelle sur les axes x et y sur l'image

Si quelque chose se passe mal, le programme ne doit pas s'arrêter brutalement et gérer toute erreur avec un message clair.

**Sortie attendue :**
```
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
  [139 130 151]
  [155 146 167]
  ...
  [120 156  94]
  [119 154  90]
  [118 153  89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
  [180]
  [194]
  ...
  [102]
  [104]
  [103]]]
$>
```

**Sortie attendue :**
Votre tableau après slicing et la zone de zoom peuvent être différents.

------------------------------------------------------------------------

# Chapitre VII --- Exercice 04

## rotate me

**Dossier :** ex04/\
**Fichiers :** load_image.py, rotate.py\
**Fonctions autorisées :** toutes les librairies pour charger, manipuler, afficher des images et manipuler des tableaux

Créez un programme qui doit charger l'image "animal.jpeg", découper une partie carrée de celle-ci et la transposer pour produire l'image ci-dessous. Il doit l'afficher, imprimer la nouvelle forme et les données de l'image après la transposition.

**Sortie attendue :**
```
$> python rotate.py
The shape of image is: (400, 400, 1) or (400, 400)
[[[167]
  [180]
  [194]
  ...
  [102]
  [104]
  [103]]]
New shape after Transpose: (400, 400)
[[167 180 194 ... 64 50 72]
 ...
 [115 116 119 ... 102 104 103]]
$>
```

Votre tableau après la transposition peut être différent.
Vous pouvez chercher la méthode transpose, cela pourrait vous aider...

**Vous devez faire la transposition vous-même, aucune librairie n'est autorisée pour la transposition.**

------------------------------------------------------------------------

# Chapitre VIII --- Exercice 05

## Pimp my image

**Dossier :** ex05/\
**Fichiers :** load_image.py, pimp_image.py\
**Fonctions autorisées :** toutes les librairies pour charger, manipuler, afficher des images et manipuler des tableaux

Vous devez développer 5 fonctions capables d'appliquer une variété de filtres couleur aux images, tout en gardant la même forme d'image.

**Voici comment elles doivent être prototypées :**
```python
def ft_invert(array) -> array:
    #your code here

def ft_red(array) -> array:
    #your code here

def ft_green(array) -> array:
    #your code here

def ft_blue(array) -> array:
    #your code here

def ft_grey(array) -> array:
    #your code here
```

**Vous avez des restrictions d'opérateurs pour chaque fonction :** (vous ne pouvez utiliser que ceux donnés, vous n'êtes pas obligé de tous les utiliser)

• **invert** : =, +, -, *
• **red** : =, *
• **green** : =, -
• **blue** : =
• **grey** : =, /

**Votre tester.py :**
```python
from load_image import ft_load
from pimp_image import ft_invert
...

array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
```

**Sortie attendue :** (les docstrings peuvent être différentes)
```
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
  [23 42 84]
  [28 43 84]
  ...
  [ 0  0  0]
  [ 1  1  1]
  [ 1  1  1]]]
...
Inverts the color of the image received.
$>
```

**Sortie attendue :** (vous devez afficher les images transformées)

Figure VIII.1: Original    Figure VIII.2: Invert
Figure VIII.3: Red         Figure VIII.4: Green  
Figure VIII.5: Blue        Figure VIII.6: Grey

------------------------------------------------------------------------

# Chapitre IX --- Rendu et peer-évaluation

Rendez votre travail dans votre dépôt Git comme d'habitude. Seul le travail à l'intérieur de votre dépôt sera évalué pendant la défense. N'hésitez pas à vérifier deux fois les noms de vos dossiers et fichiers pour vous assurer qu'ils sont corrects.

Le processus d'évaluation se déroulera sur l'ordinateur du groupe évalué.
