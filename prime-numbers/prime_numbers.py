
def main():
    '''Main function to generate prime numbers.'''

    print('\nPrime Number Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is prime')
        print('2. List prime numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is prime
            number = get_valid_input('Enter a positive integer to check if it is a Prime Number: ')
            if is_prime(number):
                print(f'{number} is a prime number.\n')
            else:
                print(f'{number} is not a prime number.\n')

        elif choice == 2:
            # Generate prime numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            prime_numbers = generate_prime_numbers(start, end)

            if prime_numbers:
                print(f'Prime numbers within the range ({start}, {end}):\n{prime_numbers}.\n')
            else:
                print(f'No prime numbers within the range ({start}, {end}).\n')

        elif choice == 3:
            # Exit program
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')


def get_valid_input(message):
    '''Get a valid input from the user.'''
    # Validate user input
    while True:
        try:
            user_input = int(input(message))
            if user_input >= 0:
                return user_input
            else:
                print('Invalid input. Please enter a non-negative integer.\n')
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')


def is_prime(n):
    '''Checks if a number is prime.'''

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def generate_prime_numbers(start, end):
    '''Generate prime numbers within a range.'''

    prime_numbers = []

    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers
    


if __name__ == '__main__':
    main()
