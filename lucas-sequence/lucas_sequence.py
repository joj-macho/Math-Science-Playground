def generate_lucas_sequence(n):
    """
    Generates the Lucas sequence up to the nth term.
    """
    lucas_sequence = [2, 1]  # Initialize the sequence with the first two terms

    for i in range(2, n):
        lucas_number = lucas_sequence[i - 1] + lucas_sequence[i - 2]
        lucas_sequence.append(lucas_number)

    return lucas_sequence


def main():
    """
    Main function to get user input and generate the Lucas sequence.
    """
    print("Lucas Sequence Generator\n")

    while True:
        try:
            n = int(input("Enter the number of terms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    lucas_sequence = generate_lucas_sequence(n)

    print("\nThe Lucas sequence is:")
    print(lucas_sequence)


if __name__ == "__main__":
    main()
