
def main():
    '''Main function to generate prime numbers.'''

    print('\nPrime Number Generator\n')

    while True:
        print('1. Check if a number is prime')
        print('2. List prime numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_prime_number()
        elif choice == '2':
            list_prime_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_prime_number():
    '''Function to check if a number is prime.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_prime(number):
        print(f'{number} is a prime number.\n')
    else:
        print(f'{number} is not a prime number.\n')

def list_prime_numbers():
    '''Function to list prime numbers within a range.'''

    while True:
        try:
            start = int(input('Enter the starting number: '))
            end = int(input('Enter the ending number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if start > end:
        print('Invalid range. Starting number should be less than or equal to the ending number.\n')
        return

    prime_numbers = []

    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)

    if prime_numbers:
        print(f'Prime numbers within the range ({start}, {end}):\n{prime_numbers}.\n')
    else:
        print(f'No prime numbers within the range ({start}, {end}).\n')

def is_prime(n):
    '''Checks if a number is prime.'''

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    main()
