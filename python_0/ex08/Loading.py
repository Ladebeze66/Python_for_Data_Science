import os


def ft_tqdm(lst: range) -> None:
    """
    Générateur qui imite tqdm pour afficher une barre de progression.

    Affiche une barre de progression en temps réel pendant l'itération
    sur une séquence range. Utilise yield pour retourner chaque élément
    tout en mettant à jour l'affichage. La barre s'adapte automatiquement
    à la largeur du terminal.

    Args:
        lst (range): La séquence range à itérer

    Yields:
        int: Chaque élément de la séquence range

    Raises:
        OSError: Si la taille du terminal ne peut pas être déterminée,
                 utilise une largeur par défaut
    """
    total = len(lst)

    # Calcul de la largeur de barre optimal
    try:
        terminal_width = os.get_terminal_size().columns
        total_digits = len(str(total))
        # Format: "100%|[{bar}]| xxx/xxx"
        # "100%|[" (6) + "]| " (3) + "xxx/xxx" (total_digits*2+1)
        metadata_chars = 6 + 3 + (total_digits * 2 + 1)
        # Ajustement visuel pour correspondre au rendu de tqdm
        bar_width = min(90, max(10, terminal_width - metadata_chars))
    except OSError:
        # Largeur par défaut si le terminal n'est pas accessible
        bar_width = 76

    for i, item in enumerate(lst):
        current = i + 1
        percentage = int((current / total) * 100)

        # Construction de la barre de progression
        filled_length = int(bar_width * current / total)
        arrow = '>' * (1 if filled_length < bar_width else 0)
        bar = '=' * filled_length + arrow
        bar = bar.ljust(bar_width)

        # Affichage de la progression (format du sujet)
        progress_display = f"\r{percentage:3d}%|[{bar}]| {current}/{total}"

        print(progress_display, end="", flush=True)
        yield item

    # Nouvelle ligne à la fin pour ne pas écraser l'affichage final
    print()


def main():
    """
    Fonction principale pour tester ft_tqdm.

    Teste la barre de progression avec une séquence de 100 éléments
    et une pause de 0.01 seconde entre chaque itération.
    """
    try:
        print("Test de ft_tqdm:")
        for elem in ft_tqdm(range(100)):
            # Simulation d'un traitement avec une pause
            import time
            time.sleep(0.01)
        print("Test terminé avec succès !")
    except KeyboardInterrupt:
        print("\nTest interrompu par l'utilisateur.")
    except Exception as e:
        print(f"Erreur lors du test: {e}")


if __name__ == "__main__":
    main()
