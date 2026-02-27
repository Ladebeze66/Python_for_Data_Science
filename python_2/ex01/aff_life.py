import matplotlib.pyplot as plt
from load_csv import load


def display_life_expectancy(country_name: str):
    """
    Affiche l'évolution de l'espérance de vie pour un pays donné.

    Args:
        country_name (str): Nom du pays à afficher
    """
    # Charger les données
    dataset = load("life_expectancy_years.csv")

    if dataset is None:
        print("Erreur : Impossible de charger les données")
        return

    # Filtrer pour le pays demandé
    country_data = dataset[dataset['country'] == country_name]

    if country_data.empty:
        print(f"Erreur : Pays '{country_name}' non trouvé dans les données")
        print("Pays disponibles :", dataset['country'].tolist()[:10], "...")
        return

    # Extraire les années (colonnes sauf 'country')
    years = [col for col in dataset.columns if col != 'country']

    # Extraire les valeurs d'espérance de vie
    life_expectancy_values = country_data.iloc[0, 1:].values
    # Toutes les colonnes sauf 'country'

    # Convertir les années en entiers pour l'affichage
    years_int = [int(year) for year in years]

    # Créer le graphique
    plt.figure(figsize=(8, 6))
    plt.plot(years_int, life_expectancy_values, linewidth=2, color='blue')

    plt.xticks(range(1800, 2101, 40))  # Intervalles de 40 ans sur l'axe X

    # Ajouter titre et légendes
    plt.title(f"Évolution de l'espérance de vie - {country_name}",
              fontsize=14, fontweight='bold')
    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Espérance de vie (années)", fontsize=12)

    # Améliorer l'affichage
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Afficher le graphique
    plt.show()


def main():
    """
    Fonction principale pour afficher l'espérance de vie du pays du campus.
    """
    # Pays du campus (à adapter selon votre campus)
    campus_country = "France"  # Pour les campus 42 en France

    # Afficher l'évolution
    display_life_expectancy(campus_country)


if __name__ == "__main__":
    main()
