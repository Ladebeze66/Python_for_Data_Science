from aff_life import display_life_expectancy


# Dans votre main() ou un fichier de test
def main():
    """Test avec différents pays."""
    countries_to_test = ["France", "Germany", "United States"]

    for country in countries_to_test:
        print(f"Test pour {country}:")
        display_life_expectancy(country)


if __name__ == "__main__":
    main()
