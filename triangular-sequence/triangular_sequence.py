def generate_triangular_sequence(n):
    """
    Generates the Triangular sequence up to the nth term.
    """
    triangular_sequence = []

    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        triangular_sequence.append(triangular_number)

    return triangular_sequence


def main():
    """
    Main function to get user input and generate the Triangular sequence.
    """
    print("Triangular Sequence Generator\n")

    while True:
        try:
            n = int(input("Enter the number of terms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    triangular_sequence = generate_triangular_sequence(n)

    print("\nThe Triangular sequence is:")
    print(triangular_sequence)


if __name__ == "__main__":
    main()
