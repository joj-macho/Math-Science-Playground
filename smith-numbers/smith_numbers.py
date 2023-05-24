def sum_of_digits(n):
    """
    Calculates the sum of the digits of a number.
    """
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum


def prime_factors(n):
    """
    Generates a list of prime factors of a number.
    """
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors


def is_smith_number(n):
    """
    Checks if a number is a Smith number.
    """
    digit_sum = sum_of_digits(n)
    prime_factors_sum = sum(sum_of_digits(factor) for factor in prime_factors(n))
    return digit_sum == prime_factors_sum


def main():
    """
    Main function to get user input and check if a number is a Smith number.
    """
    print("Smith Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_smith_number(number):
        print(f"{number} is a Smith number.")
    else:
        print(f"{number} is not a Smith number.")


if __name__ == "__main__":
    main()
