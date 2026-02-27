from S1E9 import Character, Stark


def main():
    """Test function for S1E9 module."""
    # Vos tests ici
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

    # Test de la classe abstraite (doit lever une erreur)
    try:
        Character("hodor")
    except TypeError as e:
        print(f"Erreur attendue: {e}")


if __name__ == "__main__":
    main()
