def prime_factorization(number):
    """
    Perform prime factorization of a given number.

    Parameters:
    - number (int): The number to be factorized.

    Returns:
    - list: A list of prime factors of the number.
    """
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors


def main():
    """
    This program performs prime factorization of a given number.
    """
    print("Prime Factorization\n")

    # Get input from the user
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Perform prime factorization
    factors = prime_factorization(number)

    # Display the prime factors
    print(f"The prime factors of {number} are: {factors}")


# Execute the main function
if __name__ == "__main__":
    main()
