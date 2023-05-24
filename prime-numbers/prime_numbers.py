def is_prime(number):
    """
    Check if a given number is prime.

    Parameters:
    - number (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_primes(start, end):
    """
    Generate a list of prime numbers within a given range.

    Parameters:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range (exclusive).

    Returns:
    - list: A list of prime numbers within the specified range.
    """
    primes = []
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
    return primes


def main():
    """
    Main function to demonstrate the prime numbers program.
    """
    print("Prime Numbers Program\n")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    primes = generate_primes(start, end)
    print("Prime numbers in the given range:")
    print(primes)


if __name__ == "__main__":
    main()
