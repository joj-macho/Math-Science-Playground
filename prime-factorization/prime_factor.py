def main():
    '''Main function to get user input and perform prime factorization.'''

    print('\nPrime Factorization Program\n')

    while True:
        print('1. Perform prime factorization of a number')
        print('2. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            perform_prime_factorization()
        elif choice == '2' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def perform_prime_factorization():
    '''Function to perform prime factorization of a number.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    factors = prime_factorization(number)

    if factors:
        print(f'Prime factors of {number}:')
        for factor, count in factors.items():
            print(f'{factor}^{count}')
        print()
    else:
        print('No prime factors found for the number.\n')

def prime_factorization(n):
    '''Returns a dictionary with prime factors as keys and their counts as values of a given number.'''

    if n <= 1:
        return {}

    factors = {}
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        else:
            divisor += 2 if divisor > 2 else 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors

if __name__ == '__main__':
    main()
