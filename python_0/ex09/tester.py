"""Test automatisé final pour ft_package"""


def test_ft_package():
    try:
        # Test d'import
        from ft_package import count_in_list
        print("Import réussi")

        # Tests obligatoires
        result1 = count_in_list(["toto", "tata", "toto"], "toto")
        result2 = count_in_list(["toto", "tata", "toto"], "tutu")

        # Messages de test (lignes raccourcies)
        test_list = ["toto", "tata", "toto"]
        print(f"Test 1: count_in_list({test_list}, 'toto') = {result1}")
        print(f"Test 2: count_in_list({test_list}, 'tutu') = {result2}")

        # Vérifications
        assert result1 == 2, f"Test 1 échoué: attendu 2, obtenu {result1}"
        assert result2 == 0, f"Test 2 échoué: attendu 0, obtenu {result2}"

        print("Tous les tests passent!")
        print("EXERCICE 09 VALIDÉ!")

    except Exception as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    test_ft_package()
