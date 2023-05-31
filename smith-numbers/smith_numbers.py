def main():
    '''Main function to check if a number is a Smith number.'''

    print('\nSmith Number Checker\n')

    while True:
        print('1. Check if a number is a Smith number')
        print('2. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_smith_number()
        elif choice == '2' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_smith_number():
    '''Function to check if a number is a Smith number.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_smith_number(number):
        print(f'{number} is a Smith number.\n')
    else:
        print(f'{number} is not a Smith number.\n')

def is_smith_number(n):
    '''Checks if a number is a Smith number.'''

    prime_factors = get_prime_factors(n)
    digit_sum = get_digit_sum(n)

    return sum(prime_factors) == digit_sum

def get_prime_factors(n):
    '''Returns the prime factors of a given number.'''

    factors = []
    i = 2

    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    return factors

def get_digit_sum(n):
    '''Returns the sum of digits of a given number.'''

    digit_sum = 0

    while n > 0:
        digit_sum += n % 10
        n //= 10

    return digit_sum

if __name__ == '__main__':
    main()
