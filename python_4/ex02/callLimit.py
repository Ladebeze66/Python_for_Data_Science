from typing import Any  # Importation de Any pour les arguments variables


def callLimit(limit: int):
    """Factory de décorateurs avec limitation d'appels"""
    count = 0

    def callLimiter(function):
        """Décorateur qui limite les appels d'une fonction"""

        def limit_function(*args: Any, **kwargs: Any):
            """Wrapper qui contrôle les appels"""
            nonlocal count
            count += 1

            if count <= limit:
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function
    return callLimiter


def main():
    """Fonction principale"""
    pass


if __name__ == "__main__":
    main()
