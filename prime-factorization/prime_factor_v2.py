def prime_factorization(number):
    """
    Perform prime factorization of a given number.

    Parameters:
    - number (int): The number to be factorized.

    Returns:
    - dict: A dictionary with prime factors as keys and their counts as values.
    """
    if number <= 1:
        return {}

    factors = {}
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            number //= divisor
        else:
            divisor += 2 if divisor > 2 else 1

    if number > 1:
        factors[number] = factors.get(number, 0) + 1

    return factors


def main():
    """
    This program performs prime factorization of a given number.
    """
    print("Prime Factorization\n")

    # Get input from the user
    while True:
        try:
            number = int(input("Enter a positive integer greater than 1: "))
            if number > 1:
                break
            else:
                print("Invalid input. Please enter a positive integer greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Perform prime factorization
    factors = prime_factorization(number)

    # Display the prime factors and their counts
    print(f"The prime factorization of {number} is:")
    for factor, count in factors.items():
        print(f"{factor}^{count}")

# Execute the main function
if __name__ == "__main__":
    main()
