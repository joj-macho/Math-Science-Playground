def euler_totient(n):
    """
    Calculates Euler's Totient function for a given number.
    """
    if n <= 0:
        return None

    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result


def main():
    """
    Main function to get user input and calculate Euler's Totient function.
    """
    print("Euler's Totient Function Calculator\n")

    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    totient = euler_totient(number)
    if totient is not None:
        print(f"The Euler's Totient function value for {number} is: {totient}")


if __name__ == "__main__":
    main()
