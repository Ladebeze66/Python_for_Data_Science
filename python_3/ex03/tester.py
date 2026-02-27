from ft_calculator import calculator


def main():
    """Test function for ft_calculator module."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print("---")

    # Test division par zéro
    v4 = calculator([1.0, 2.0, 3.0])
    try:
        v4 / 0
    except ZeroDivisionError as e:
        print(f"Erreur attendue: {e}")


if __name__ == "__main__":
    main()
