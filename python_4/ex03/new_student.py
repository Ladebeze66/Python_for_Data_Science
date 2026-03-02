import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Génère un identifiant aléatoire de 15 caractères.

    Returns:
        str: Chaîne de 15 caractères alphabétiques minuscules
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Classe représentant un étudiant avec génération automatique de login et ID.

    Attributes:
        name: Nom de l'étudiant
        surname: Prénom de l'étudiant
        active: Statut actif (True par défaut)
        login: Login généré automatiquement (non initialisable)
        id: Identifiant unique généré automatiquement (non initialisable)
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Initialise les champs calculés après la création de l'instance.

        Génère le login à partir du nom et prénom selon la logique :
        première lettre du nom + prénom, le tout capitalisé.
        """
        self.login = (self.name[0] + self.surname).capitalize()


def main():
    """Fonction principale - tests dans tester.py"""
    pass


if __name__ == "__main__":
    main()
