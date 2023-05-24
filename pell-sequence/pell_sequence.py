def generate_pell_sequence(n):
    """
    Generates the Pell sequence up to the nth term.
    """
    pell_sequence = [0, 1]  # Initialize the sequence with the first two terms

    for i in range(2, n):
        pell_number = 2 * pell_sequence[i - 1] + pell_sequence[i - 2]
        pell_sequence.append(pell_number)

    return pell_sequence


def main():
    """
    Main function to get user input and generate the Pell sequence.
    """
    print("Pell Sequence Generator\n")

    while True:
        try:
            n = int(input("Enter the number of terms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    pell_sequence = generate_pell_sequence(n)

    print("\nThe Pell sequence is:")
    print(pell_sequence)


if __name__ == "__main__":
    main()
