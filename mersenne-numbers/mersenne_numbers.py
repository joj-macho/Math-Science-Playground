def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def generate_mersenne_sequence(n):
    """
    Generates the Mersenne sequence up to the nth term.
    """
    mersenne_sequence = []

    for i in range(n):
        number = 2 ** i - 1
        if is_prime(number):
            mersenne_sequence.append(number)

    return mersenne_sequence


def main():
    """
    Main function to get user input and generate the Mersenne sequence.
    """
    print("Mersenne Sequence Generator\n")

    while True:
        try:
            n = int(input("Enter the number of terms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    mersenne_sequence = generate_mersenne_sequence(n)

    print("\nThe Mersenne sequence is:")
    print(mersenne_sequence)


if __name__ == "__main__":
    main()
