import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    """
    Affiche la corrélation PIB vs Espérance de vie pour l'année 1900.
    """
    # Étape 1: Charger les deux datasets
    gdp_dataset = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_dataset = load("life_expectancy_years.csv")

    if gdp_dataset is None or life_dataset is None:
        print("Erreur : Impossible de charger les données")
        return

    # Étape 2: Extraire les données pour l'année 1900
    gdp_1900 = gdp_dataset[['country', '1900']].copy()
    life_1900 = life_dataset[['country', '1900']].copy()

    # Étape 3: Fusionner les datasets sur le pays
    merged_data = pd.merge(gdp_1900, life_1900, on='country',
                           suffixes=('_gdp', '_life'))

    # Étape 4: Nettoyer les données (supprimer les valeurs manquantes)
    merged_data = merged_data.dropna()

    # Étape 5: Convertir les valeurs (si nécessaire, selon le format)
    gdp_values = pd.to_numeric(merged_data['1900_gdp'], errors='coerce')
    life_values = pd.to_numeric(merged_data['1900_life'], errors='coerce')

    # Supprimer les lignes avec des valeurs non convertibles
    valid_mask = gdp_values.notna() & life_values.notna()
    gdp_values = gdp_values[valid_mask]
    life_values = life_values[valid_mask]

    # Étape 6: Créer le scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(gdp_values, life_values, alpha=0.6, color='blue', s=30)

    # Étape 7: Configuration des axes (pour correspondre au visuel voulu)
    plt.xscale('log')  # Échelle logarithmique pour le PIB
    plt.xlim(300, 10000)
    plt.ylim(18, 55)  # Commence en dessous de 20 pour laisser de l'espace

    # Configurer les marques des axes pour correspondre au visuel
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.yticks([20, 25, 30, 35, 40, 45, 50, 55])  # Marques exactes du visuel

    # Étape 8: Titre et légendes (OBLIGATOIRES)
    plt.title("1900", fontsize=14)
    plt.xlabel("Gross domestic product", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)

    # Étape 9: Grille discrète et affichage
    plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    plt.show()


if __name__ == "__main__":
    main()
