def generate_catalan_sequence(n):
    """
    Generates the Catalan sequence up to the nth term.
    """
    catalan_sequence = [1]

    for i in range(1, n):
        term = 0
        for j in range(i):
            term += catalan_sequence[j] * catalan_sequence[i - j - 1]
        catalan_sequence.append(term)

    return catalan_sequence


def main():
    """
    Main function to get user input and generate the Catalan sequence.
    """
    print("Catalan Sequence Generator\n")

    while True:
        try:
            n = int(input("Enter the number of terms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    catalan_sequence = generate_catalan_sequence(n)

    print("\nThe Catalan sequence is:")
    print(catalan_sequence)


if __name__ == "__main__":
    main()
