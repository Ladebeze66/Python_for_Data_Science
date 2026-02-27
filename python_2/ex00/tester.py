from load_csv import load


def main():
    """
    Tests essentiels de la fonction load.
    """

    # Test principal (comme demandé dans le sujet)
    print("Test du fichier principal:")
    dataset = load("life_expectancy_years.csv")

    if dataset is not None:
        print("Dataset chargé avec succès!")
        print(f"Nombre de pays: {len(dataset)}")
        print("\nPremières lignes:")
        print(dataset.head(3))  # Affiche les 3 premières lignes

    # Test d'erreur simple
    print("\n" + "="*50)
    print("Test fichier inexistant:")
    result = load("fichier_qui_nexiste_pas.csv")
    print(f"Résultat: {result}")


if __name__ == "__main__":
    main()
