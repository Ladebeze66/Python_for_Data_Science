# Training Piscine Python for Data Science - 4

## Data Oriented Design --- Traduction française

**Résumé :** Aujourd'hui, vous allez voir quelques concepts de Structure Design.  
**Version :** 1.00

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

- Vous devez rendre vos modules depuis un ordinateur du cluster en utilisant soit une machine virtuelle :
  - Vous pouvez choisir le système d'exploitation à utiliser pour votre machine virtuelle
  - Votre machine virtuelle doit avoir tous les logiciels nécessaires pour réaliser votre projet. Ces logiciels doivent être configurés et installés.
- Ou vous pouvez utiliser l'ordinateur directement si les outils sont disponibles.
  - Assurez-vous d'avoir l'espace sur votre session pour installer ce dont vous avez besoin pour tous les modules (utilisez le goinfre si votre campus en a un)
  - Vous devez avoir tout installé avant les évaluations
- Vos fonctions ne doivent pas quitter de manière inattendue (segmentation fault, bus error, double free, etc.) en dehors des comportements non définis. Si cela arrive, votre projet sera considéré comme non fonctionnel et recevra un 0 pendant l'évaluation.
- Nous vous encourageons à créer des programmes de test pour votre projet même si ce travail n'aura pas à être rendu et ne sera pas noté. Cela vous donnera une chance de tester facilement votre travail et celui de vos pairs. Vous trouverez ces tests particulièrement utiles pendant votre soutenance. En effet, pendant la soutenance, vous êtes libre d'utiliser vos tests et/ou les tests du pair que vous évaluez.
- Rendez votre travail dans votre dépôt git assigné. Seul le travail dans le dépôt git sera noté. Si Deepthought est assigné pour noter votre travail, cela sera fait après vos peer-évaluations. Si une erreur arrive dans n'importe quelle section de votre travail pendant la notation de Deepthought, l'évaluation s'arrêtera.
- Vous devez utiliser la version Python 3.10
- Vos imports de lib doivent être explicites, par exemple vous devez "import numpy as np". Importer "from pandas import *" n'est pas autorisé, et vous aurez 0 sur l'exercice.
- Il n'y a pas de variable globale.
- Par Odin, par Thor ! Utilisez votre cerveau !!!

------------------------------------------------------------------------

# Chapitre II --- Instructions spécifiques du jour

Une plainte commune aux data scientists est qu'ils écrivent du shitcode (soit dit en passant, seulement à des fins éducatives vous pouvez trouver beaucoup d'exemples de Python shitcode ici, fournis strictement à des fins éducatives). Pourquoi ? Parce que le data scientist moyen utilise beaucoup de techniques inefficaces et de variables codées en dur et néglige la programmation orientée objet.
Ne soyez pas comme eux.

- Pas de code dans le scope global. Utilisez des fonctions !
- Chaque programme doit avoir son main et ne pas être un simple script :

```python
def main():
    # vos tests et votre gestion d'erreur

if __name__ == "__main__":
    main()
```

- Toute exception non attrapée invalidera les exercices, même en cas d'erreur que vous étiez censé tester.
- Vous pouvez utiliser n'importe quelle fonction built-in si elle n'est pas interdite dans l'exercice.
- Toutes vos fonctions, classes et méthodes doivent avoir une documentation (__doc__)
- Votre code doit être à la norme
  - pip install flake8
  - alias norminette=flake8

------------------------------------------------------------------------

# Chapitre III --- Exercice 00

## Exercice 00: Calculate my statistics

**Dossier de rendu :** ex00/  
**Fichiers à rendre :** statistics.py  
**Fonctions autorisées :** Aucune

Vous devez prendre en *args une quantité de nombre inconnue et faire la Moyenne, Médiane, Quartile (25% et 75%), Écart-type et Variance selon ce que demandent les **kwargs.

Vous devez gérer les erreurs.

Le prototype de la fonction est :
```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
    #your code here
```

Votre tester.py :
```python
from statistics import ft_statistics

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

Sortie attendue :
```
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
$>
```

------------------------------------------------------------------------

# Chapitre IV --- Exercice 01

## Exercice 01: Outer_inner

**Dossier de rendu :** ex01/  
**Fichiers à rendre :** in_out.py  
**Fonctions autorisées :** Aucune

Écrivez une fonction qui retourne le carré de l'argument, une fonction qui retourne l'exponentiation de l'argument par lui-même et une fonction qui prend comme argument un nombre et une fonction, elle retourne un objet qui quand appelé retourne le résultat du calcul des arguments.

Le prototype des fonctions est :
```python
def square(x: int | float) -> int | float:
    #your code here

def pow(x: int | float) -> int | float:
    #your code here

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        #your code here
```

Votre tester.py :
```python
from in_out import outer
from in_out import square
from in_out import pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
```

Sortie attendue :
```
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
$>
```

Nous vous rappelons que l'utilisation de global est interdite

------------------------------------------------------------------------

# Chapitre V --- Exercice 02

## Exercice 02: my first decorating

**Dossier de rendu :** ex02/  
**Fichiers à rendre :** callLimit.py  
**Fonctions autorisées :** Aucune

Écrivez une fonction qui prend comme argument une limite d'appel d'une autre fonction et bloque son exécution au-dessus d'une limite.

Le prototype des fonctions est :
```python
def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            #your code here
```

Votre tester.py :
```python
from callLimit import callLimit

@callLimit(3)
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
    f()
    g()
```

Sortie attendue :
```
$> python tester.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>
```

Wrappers

------------------------------------------------------------------------

# Chapitre VI --- Exercice 03

## Exercice 03: data class

**Dossier de rendu :** ex03/  
**Fichiers à rendre :** new_student.py  
**Fonctions autorisées :** dataclasses, random, string

Écrivez une dataclass qui prend comme arguments un name et nickname, met active à True, crée le login étudiant, et génère un ID aléatoire avec la fonction generate_id.

Vous ne devez pas utiliser __str__ , __repr__ dans votre classe.

Le prototype de la fonction et classe est :
```python
import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    #your code here
```

Votre tester.py :
```python
from new_student import Student

student = Student(name = "Edward", surname = "agle")
print(student)
```

Sortie attendue : (id est aléatoire)
```
$> python tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
$>
```

Le login et id ne doivent pas être initialisables et doivent retourner une erreur.

Votre tester.py :
```python
from new_student import Student

student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
```

Sortie attendue :
```
$> python tester.py
...
TypeError: Student.__init__() got an unexpected keyword argument 'id'
$>
```

------------------------------------------------------------------------

# Chapitre VII --- Rendu et peer-évaluation

Rendez votre assignment dans votre dépôt Git comme d'habitude. Seul le travail à l'intérieur de votre dépôt sera évalué pendant la soutenance. N'hésitez pas à vérifier deux fois les noms de vos dossiers et fichiers pour vous assurer qu'ils sont corrects.

Le processus d'évaluation se déroulera sur l'ordinateur du groupe évalué.
