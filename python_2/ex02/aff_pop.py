import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def convert_population_value(value):
    """
    Convertit une valeur de population du format texte en nombre.

    Args:
        value: Valeur à convertir ('28.1M', '400k', etc.)

    Returns:
        float: Valeur numérique (28100000, 400000, etc.)
    """
    # Gérer les valeurs vides ou NaN
    if pd.isna(value) or value == '':
        return 0

    # Convertir en chaîne et nettoyer
    value_str = str(value).strip()

    try:
        # Cas 1: Millions (ex: "28.1M" -> 28100000)
        if value_str.endswith('M'):
            return float(value_str[:-1]) * 1_000_000
        # Cas 2: Milliers (ex: "400k" -> 400000)
        elif value_str.endswith('k'):
            return float(value_str[:-1]) * 1_000
        # Cas 3: Nombre simple (ex: "2650" -> 2650)
        else:
            return float(value_str)
    except ValueError:
        # En cas d'erreur de conversion, retourner 0
        return 0


def main():
    """
    Compare l'évolution de la population entre France et Belgium (1800-2050).
    Respecte les exigences de l'exercice 02 : deux pays, période 1800-2050,
    titre, légendes des axes et des courbes.
    """
    # Étape 1: Charger les données avec la fonction load() de l'ex00
    dataset = load("population_total.csv")

    if dataset is None:
        print("Erreur : Impossible de charger les données")
        return

    # Étape 2: Filtrer les données pour les deux pays choisis
    france_data = dataset[dataset['country'] == 'France']
    belgium_data = dataset[dataset['country'] == 'Belgium']

    # Vérifier que les pays existent dans les données
    if france_data.empty:
        print("Erreur : France non trouvée dans les données")
        return
    if belgium_data.empty:
        print("Erreur : Belgium non trouvé dans les données")
        return

    # Étape 3: Filtrer les années de 1800 à 2050 (exigence de l'exercice)
    year_columns = [col for col in dataset.columns
                    if col != 'country' and 1800 <= int(col) <= 2050]
    years = [int(col) for col in year_columns]

    # Étape 4: Convertir les valeurs de population (format texte -> nombres)
    france_values = [convert_population_value(france_data.iloc[0][col])
                     for col in year_columns]
    belgium_values = [convert_population_value(belgium_data.iloc[0][col])
                      for col in year_columns]

    # Étape 5: Créer le graphique
    plt.figure(figsize=(8, 6))  # Taille optimale pour la lisibilité

    # Tracer les deux courbes avec couleurs distinctes
    plt.plot(years, france_values, label='France', linewidth=2, color='green')
    plt.plot(years, belgium_values, label='Belgium', linewidth=2, color='blue')

    # Étape 6: Configurer l'axe Y (Population)
    plt.ylim(0, 70_000_000)  # Limite de 0 à 80 millions
    plt.yticks([0, 20_000_000, 40_000_000, 60_000_000],
               ['0', '20M', '40M', '60M'])  # Affichage propre

    # Étape 7: Configurer l'axe X (Années) - S'arrêter à 2050
    plt.xlim(1800, 2060)  # Limite stricte selon l'exercice
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])  # Marques propres

    # Étape 8: Ajouter titre et légendes (OBLIGATOIRES selon l'exercice)
    plt.title("Population Projections")  # Titre du graphique
    plt.xlabel("Year")  # Légende axe X
    plt.ylabel("Population")  # Légende axe Y
    plt.legend(loc='lower right')  # Légende des courbes en bas à droite

    # Étape 9: Améliorer la lisibilité
    plt.grid(True)  # Grille pour faciliter la lecture

    # Étape 10: Afficher le graphique
    plt.show()


if __name__ == "__main__":
    main()
