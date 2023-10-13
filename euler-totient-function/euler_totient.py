def main():
    '''Main function to calculate Euler's Totient function.'''

    print('Euler\'s Totient Function Calculator\n')

    while True:
        try:
            number = int(input('Enter a positive integer: '))
            if number <= 0:
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please enter a positive integer.')

    # Calculate the Euler Totient
    totient = calculate_totient(number)
    if totient is not None:
        print(f'The Euler\'s Totient function value for {number} is: {totient}')


def calculate_totient(n):
    '''Calculates Euler's Totient function for a given number.'''

    if n <= 0:
        return None

    # Initialize the result with n
    result = n
    # Start with the smallest prime factor, 2
    p = 2

    # Iterate through prime factors
    while p * p <= n:
        if n % p == 0:
            # Reduce n by dividing with the prime factor
            while n % p == 0:
                n //= p
            # Apply the totient formula
            result -= result // p

        # Move to the next potential prime factor
        p += 1

    # If n is still greater than 1, it is a prime factor
    if n > 1:
        result -= result // n

    return result


if __name__ == '__main__':
    main()
