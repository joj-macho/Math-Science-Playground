def get_divisors(n):
    """
    Returns a list of divisors of a given number.
    """
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def is_abundant(n):
    """
    Checks if a number is abundant.
    """
    sum_divisors = sum(get_divisors(n)) - n
    return sum_divisors > n


def main():
    """
    Main function to get user input and check if a number is abundant.
    """
    print("Abundant Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_abundant(number):
        print(number, "is an abundant number.")
    else:
        print(number, "is not an abundant number.")


if __name__ == "__main__":
    main()
