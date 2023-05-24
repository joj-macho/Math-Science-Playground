def generate_square_sequence(n):
    """
    Generates the Square sequence up to the nth term.
    """
    square_sequence = []

    for i in range(1, n + 1):
        square_number = i ** 2
        square_sequence.append(square_number)

    return square_sequence


def main():
    """
    Main function to get user input and generate the Square sequence.
    """
    print("Square Sequence Generator\n")

    while True:
        try:
            n = int(input("Enter the number of terms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    square_sequence = generate_square_sequence(n)

    print("\nThe Square sequence is:")
    print(square_sequence)


if __name__ == "__main__":
    main()
