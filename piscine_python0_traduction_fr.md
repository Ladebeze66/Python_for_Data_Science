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

Vous devez modifier les chaînes de caractères de chaque objet de données pour afficher les salutations suivantes :
"Hello World", "Hello «pays de votre campus»", "Hello «ville de votre campus»", "Hello «nom de votre campus»"

**Code de départ :**
```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

**Sortie attendue :**
```
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

------------------------------------------------------------------------

# Chapitre III --- Exercice 01

## First use of package

**Dossier :** ex01/\
**Fichier :** format_ft_time.py\
**Fonctions autorisées :** time, datetime ou toute autre librairie permettant de recevoir la date

Écrivez un script qui formate les dates de cette manière. Bien sûr, votre date ne sera pas la même que la mienne, comme dans l'exemple, mais elle doit être formatée de la même manière.

**Sortie attendue :**
```
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

------------------------------------------------------------------------

# Chapitre IV --- Exercice 02

## First function python

**Dossier :** ex02/\
**Fichier :** find_ft_type.py\
**Fonctions autorisées :** aucune

Écrivez une fonction qui affiche les types d'objets et retourne 42.

Voici comment elle doit être prototypée :
```python
def all_thing_is_obj(object: any) -> int:
    #your code here
```

**Votre tester.py :**
```python
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

**Sortie attendue :**
```
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

Exécuter votre fonction seule ne fait rien.
**Sortie attendue :**
```
$>python find_ft_type.py | cat -e
$>
```

------------------------------------------------------------------------

# Chapitre V --- Exercice 03

## NULL not found

**Dossier :** ex03/\
**Fichier :** NULL_not_found.py\
**Fonctions autorisées :** aucune

Écrivez une fonction qui affiche le type d'objet de tous les types de "Null".
Retourne 0 si tout va bien et 1 en cas d'erreur.
Votre fonction doit afficher tous les types de "Null".

Voici comment elle doit être prototypée :
```python
def NULL_not_found(object: any) -> int:
    #your code here
```

**Votre tester.py :**
```python
from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
```

**Sortie attendue :**
```
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

Exécuter votre fonction seule ne fait rien.
**Sortie attendue :**
```
$>python NULL_not_found.py | cat -e
$>
```

------------------------------------------------------------------------

# Chapitre VI --- Exercice 04

## The Even and the Odd

**Dossier :** ex04/\
**Fichier :** whatis.py\
**Fonctions autorisées :** sys ou toute autre librairie permettant de recevoir les arguments

Créez un script qui prend un nombre en argument, vérifie s'il est pair ou impair, et affiche le résultat.

Si plus d'un argument est fourni ou si l'argument n'est pas un entier, affichez une AssertionError.

**Sortie attendue :**
```
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

------------------------------------------------------------------------

# Chapitre VII --- À partir de maintenant, vous devez suivre ces règles supplémentaires

• Pas de code dans la portée globale. Utilisez des fonctions !
• Chaque programme doit avoir son main et ne pas être un simple script :

```python
def main():
    # vos tests et votre gestion d'erreurs

if __name__ == "__main__":
    main()
```

• Toute exception non capturée invalidera les exercices, même en cas d'erreur que vous étiez censé tester.
• Toutes vos fonctions doivent avoir une documentation (__doc__)
• Votre code doit suivre la norme
  ◦ pip install flake8
  ◦ alias norminette=flake8

------------------------------------------------------------------------

# Chapitre VIII --- Exercice 05

## First standalone program python

**Dossier :** ex05/\
**Fichier :** building.py\
**Fonctions autorisées :** sys ou toute autre librairie permettant de recevoir les arguments

Cette fois, vous devez créer un vrai programme autonome, avec un main, qui prend un seul argument de chaîne et affiche les sommes de ses caractères majuscules, minuscules, de ponctuation, chiffres et espaces.

• Si aucun argument ou rien n'est fourni, l'utilisateur est invité à fournir une chaîne.
• Si plus d'un argument est fourni au programme, affichez une AssertionError.

**Sorties attendues :**
```
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$>
```

**Sorties attendues :** (le retour chariot compte comme un espace, si vous ne voulez pas en retourner un, utilisez ctrl + D)
```
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

Par Odin, par Thor ! Utilisez votre cerveau !!! Ne réinventez pas la roue, utilisez les fonctionnalités du langage.

------------------------------------------------------------------------

# Chapitre IX --- Exercice 06

## Recode filter

**Dossier :** ex06/\
**Fichiers :** ft_filter.py, filterstring.py\
**Fonctions autorisées :** sys ou toute autre librairie permettant de recevoir les arguments

### Partie 1: Recoder la fonction filter

Recodez votre propre ft_filter, elle doit se comporter comme la fonction built-in originale (elle doit retourner la même chose que "print(filter.__doc__)"), vous devez utiliser les list comprehensions pour recoder votre ft_filter.

Bien sûr, utiliser le filter built-in original est interdit.

Vous pouvez valider le module à partir d'ici, mais nous vous encourageons à continuer car il y a des choses que vous devrez savoir pour les projets suivants.

### Partie 2: Le programme

Créez un programme qui accepte deux arguments : une chaîne (S) et un entier (N). Le programme doit afficher une liste de mots de S qui ont une longueur supérieure à N.

• Les mots sont séparés les uns des autres par des caractères d'espace.
• Les chaînes ne contiennent aucun caractère spécial (ponctuation ou invisible).
• Le programme doit contenir au moins une expression de list comprehension et une lambda.
• Si le nombre d'arguments est différent de 2, ou si le type de n'importe quel argument est mauvais, le programme affiche une AssertionError.

**Sorties attendues :**
```
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
$> python filterstring.py 'Hello the World' 99
[]
$>
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

------------------------------------------------------------------------

# Chapitre X --- Exercice 07

## Dictionaries SoS

**Dossier :** ex07/\
**Fichier :** sos.py\
**Fonctions autorisées :** sys ou toute autre librairie permettant de recevoir les arguments

Créez un programme qui prend une chaîne en argument et l'encode en code Morse.

• Le programme supporte les espaces et les caractères alphanumériques.
• Un caractère alphanumérique est représenté par des points . et des tirets -.
• Les caractères Morse complets sont séparés par un seul espace.
• Un caractère d'espace est représenté par une barre oblique /.

Vous devez utiliser un dictionnaire pour stocker votre code morse.

```python
NESTED_MORSE = { " ": "/ ",
"A": ".- ",
...
```

Si le nombre d'arguments est différent de 1, ou si le type de n'importe quel argument est mauvais, le programme affiche une AssertionError.

**Sorties attendues :**
```
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

------------------------------------------------------------------------

# Chapitre XI --- Exercice 08

## Loading ...

**Dossier :** ex08/\
**Fichier :** Loading.py\
**Fonctions autorisées :** os

Alors créons une fonction appelée ft_tqdm.
La fonction doit copier la fonction tqdm avec l'opérateur yield.

Voici comment elle doit être prototypée :
```python
def ft_tqdm(lst: range) -> None:
    #your code here
```

**Votre tester.py :** (vous comparez votre version avec l'originale)
```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
```

**Sortie attendue :** (vous devez avoir une fonction aussi proche que possible de la version originale)
```
$> python tester.py
100%|[===============================================================>]| 333/333
100%| | 333/333 [00:01<00:00, 191.61it/s]
```

Vous pouvez utiliser get_terminal_size pour vous adapter à la taille de votre terminal.

------------------------------------------------------------------------

# Chapitre XII --- Exercice 09

## My first package creation

**Dossier :** ex09/\
**Fichiers :** *.py, *.txt, *.toml, README.md, LICENSE
**Fonctions autorisées :** PyPI ou toute librairie pour la création de package

Créez votre premier package en python comme vous le souhaitez, il apparaîtra dans la liste des packages installés quand vous tapez la commande "pip list" et affichera ses caractéristiques quand vous tapez "pip show -v ft_package"

```
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

Le package sera installé via pip en utilisant une des commandes suivantes (les deux doivent fonctionner) :
• pip install ./dist/ft_package-0.0.1.tar.gz
• pip install ./dist/ft_package-0.0.1-py3-none-any.whl

Votre package doit pouvoir être appelé depuis un script comme celui-ci :
```python
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

------------------------------------------------------------------------

# Chapitre XIII --- Rendu et peer-évaluation

Rendez votre travail dans votre dépôt Git comme d'habitude. Seul le travail à l'intérieur de votre dépôt sera évalué pendant la défense. N'hésitez pas à vérifier deux fois les noms de vos dossiers et fichiers pour vous assurer qu'ils sont corrects.

Le processus d'évaluation se déroulera sur l'ordinateur du groupe évalué.
