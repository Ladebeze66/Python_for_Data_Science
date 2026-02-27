# Training Piscine Python for Data Science - 3

## Programmation Orientée Objet --- Traduction française

**Résumé :** Aujourd'hui, vous allez découvrir les classes et l'héritage.  
**Version :** 1.00

------------------------------------------------------------------------

# Sommaire

- I Règles générales
- II Instructions spécifiques du jour  
- III Exercice 00
- IV Exercice 01
- V Exercice 02
- VI Exercice 03
- VII Exercice 04
- VIII Rendu et peer-évaluation

------------------------------------------------------------------------

# Chapitre I --- Règles générales

• Vous devez rendre vos modules depuis un ordinateur du cluster en utilisant soit une machine virtuelle :
  ◦ Vous pouvez choisir le système d'exploitation à utiliser pour votre machine virtuelle
  ◦ Votre machine virtuelle doit avoir tous les logiciels nécessaires pour réaliser votre projet. Ces logiciels doivent être configurés et installés.

• Ou vous pouvez utiliser l'ordinateur directement si les outils sont disponibles.
  ◦ Assurez-vous d'avoir l'espace sur votre session pour installer ce dont vous avez besoin pour tous les modules (utilisez le goinfre si votre campus en a un)
  ◦ Vous devez avoir tout installé avant les évaluations

• Vos fonctions ne doivent pas quitter de manière inattendue (segmentation fault, bus error, double free, etc.) à part les comportements indéfinis. Si cela arrive, votre projet sera considéré comme non fonctionnel et recevra un 0 pendant l'évaluation.

• Nous vous encourageons à créer des programmes de test pour votre projet même si ce travail ne devra pas être rendu et ne sera pas noté. Cela vous donnera une chance de tester facilement votre travail et celui de vos pairs. Vous trouverez ces tests particulièrement utiles pendant votre soutenance. En effet, pendant la soutenance, vous êtes libre d'utiliser vos tests et/ou les tests du pair que vous évaluez.

• Rendez votre travail dans votre dépôt git assigné. Seul le travail dans le dépôt git sera noté. Si Deepthought est assigné pour noter votre travail, cela sera fait après vos peer-évaluations. Si une erreur arrive dans n'importe quelle section de votre travail pendant la notation de Deepthought, l'évaluation s'arrêtera.

• Vous devez utiliser la version Python 3.10

• Vos imports de librairies doivent être explicites, par exemple vous devez "import numpy as np". Importer "from pandas import *" n'est pas autorisé, et vous aurez 0 à l'exercice.

• Il n'y a pas de variable globale.

• Par Odin, par Thor ! Utilisez votre cerveau !!!

------------------------------------------------------------------------

# Chapitre II --- Instructions spécifiques du jour

Une plainte commune envers les data scientists est qu'ils écrivent du code de merde (soit dit en passant, uniquement à des fins éducatives, vous pouvez trouver beaucoup d'exemples de code Python de merde ici, fourni strictement à des fins éducatives). Pourquoi ? Parce que le data scientist moyen utilise beaucoup de techniques inefficaces et de variables codées en dur et néglige la programmation orientée objet.
Ne soyez pas comme eux.

• Pas de code dans le scope global. Utilisez des fonctions !

• Chaque programme doit avoir son main et ne pas être un simple script :

```python
def main():
    # vos tests et votre gestion d'erreurs
    
if __name__ == "__main__":
    main()
```

• Toute exception non attrapée invalidera les exercices, même dans le cas d'une erreur que vous étiez censé tester.

• Vous pouvez utiliser n'importe quelle fonction built-in si elle n'est pas interdite dans l'exercice.

• Toutes vos fonctions, classes et méthodes doivent avoir une documentation (__doc__)

• Votre code doit être à la norme
  ◦ pip install flake8
  ◦ alias norminette=flake8

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Exercice 00: GOT S1E9

**Répertoire de rendu :** ex00/  
**Fichiers à rendre :** S1E9.py  
**Fonctions autorisées :** Aucune

Créez une classe abstraite "character" qui peut prendre un first_name comme premier paramètre, is_alive comme second paramètre non obligatoire défini à True par défaut et peut changer l'état de santé du personnage avec une méthode qui fait passer is_alive de True à False.
Et une classe "stark" qui hérite de Character

Le prototype de la classe est :

```python
from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    #your code here

class Stark(Character):
    """Your docstring for Class"""
    #your code here
```

Votre tester.py :

```python
from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
```

**Sortie attendue :** (les docstrings peuvent être différentes)

```
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>
```

Assurez-vous d'avoir utilisé une classe abstraite, le code ci-dessous devrait faire une erreur.

```python
from S1E9 import Character
hodor = Character("hodor")
```

```
TypeError: Can't instantiate abstract class Character with abstract method
$>
```

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## Exercice 01: GOT S1E7

**Répertoire de rendu :** ex01/  
**Fichiers à rendre :** Fichiers des exercices précédents + S1E7.py  
**Fonctions autorisées :** Aucune

Créez deux familles qui héritent de la classe Character, que nous pouvons instancier sans passer par la classe Character. Trouvez une solution pour que "__str__" et "__repr__" retournent des chaînes et non des objets. Écrivez une méthode de classe pour créer des personnages en chaîne.

Le prototype de la classe est :

```python
from S1E9 import Character

class Baratheon(Character):
    #your code here

class Lannister(Character):
    #your code here

# decorator
def create_lannister(your code here):
    #your code here
```

Votre tester.py :

```python
from S1E7 import Baratheon, Lannister

Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
```

**Sortie attendue :** (les docstrings peuvent être différentes)

```
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>
```

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## Exercice 02: Now it's weird!

**Répertoire de rendu :** ex02/  
**Fichiers à rendre :** Fichiers des exercices précédents + DiamondTrap.py  
**Fonctions autorisées :** Aucune

Dans cet exercice, vous allez créer un monstre : Joffrey Baratheon.
C'est si risqué !
Il y a quelque chose d'incohérent avec ce nouveau "faux" roi.
Vous devez utiliser les Properties pour changer les caractéristiques physiques de notre nouveau roi.

Le prototype de la classe est :

```python
from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    #your code here
```

Votre tester.py :

```python
from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
```

**Sortie attendue :** (les docstrings peuvent être différentes)

```
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>
```

Depuis Python 2.3, le langage utilise la linéarisation C3 pour contrer le problème d'héritage en diamant.

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## Exercice 03: Calculate my vector

**Répertoire de rendu :** ex03/  
**Fichiers à rendre :** ft_calculator.py  
**Fonctions autorisées :** Aucune

Écrivez une classe calculatrice qui est capable de faire des calculs (addition, multiplication, soustraction, division) de vecteur avec un scalaire.

Le prototype de la classe est :

```python
class calculator:
    #your code here
    
def __add__(self, object) -> None:
    #your code here

def __mul__(self, object) -> None:
    #your code here

def __sub__(self, object) -> None:
    #your code here

def __truediv__(self, object) -> None:
    #your code here
```

Votre tester.py :

```python
from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
```

**Sortie attendue :** (les docstrings peuvent être différentes)

```
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
```

Vous n'avez pas à faire de gestion d'erreurs, sauf pour la division par 0

------------------------------------------------------------------------

# Chapitre VII --- Exercice 04

## Exercice 04: Calculate my dot product

**Répertoire de rendu :** ex04/  
**Fichiers à rendre :** ft_calculator.py  
**Fonctions autorisées :** Aucune

Écrivez une classe calculatrice qui est capable de faire des calculs (produit scalaire, addition, soustraction) de 2 vecteurs.
Les vecteurs auront toujours des tailles identiques, pas de gestion d'erreurs.
C'est à vous de trouver un décorateur qui peut vous aider à utiliser les méthodes de la classe calculator sans instancier cette classe.

Le prototype de la classe est :

```python
class calculator:
    #your code here

# decorator
def dotproduct(V1: list[float], V2: list[float]) -> None:
    #your code here

# decorator
def add_vec(V1: list[float], V2: list[float]) -> None:
    #your code here

# decorator
def sous_vec(V1: list[float], V2: list[float]) -> None:
    #your code here
```

Votre tester.py :

```python
from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
```

**Sortie attendue :** (les docstrings peuvent être différentes)

```
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
```

Vous n'avez pas à faire de gestion d'erreurs.
Si vous voulez aller plus loin dans les calculs de vecteurs ou de matrices, allez au projet matrix après cette "piscine".

------------------------------------------------------------------------

# Chapitre VIII --- Rendu et peer-évaluation

Rendez votre travail dans votre dépôt Git comme d'habitude. Seul le travail à l'intérieur de votre dépôt sera évalué pendant la soutenance. N'hésitez pas à vérifier deux fois les noms de vos dossiers et fichiers pour vous assurer qu'ils sont corrects.

Le processus d'évaluation se déroulera sur l'ordinateur du groupe évalué.
