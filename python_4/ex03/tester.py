from new_student import Student


def main():
    """Fonction principale"""
    student = Student(name="Edward", surname="agle")
    print(student)

    student = Student(name = "Edward", surname = "agle", id = "toto")
    print(student)


if __name__ == "__main__":
    main()
