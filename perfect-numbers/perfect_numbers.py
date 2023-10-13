
def main():
    '''Main function to check if a number is perfect and generates perfect numbers'''

    print('\nPerfect Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is perfect')
        print('2. List perfect numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is perfect
            number = get_valid_input('Enter a positive integer to check if it is a Perfect Number: ')

            if is_perfect(number):
                print(f'{number} is a perfect number.\n')
            else:
                print(f'{number} is not a perfect number.\n')

        elif choice == 2:
            # Generate perfect numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            perfect_numbers = generate_perfect_numbers(start,end)

            if perfect_numbers:
                print(f'Perfect numbers within the range [{start}, {end}]: {perfect_numbers}\n')
            else:
                print(f'No perfect numbers within the range [{start}, {end}].\n')

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


def is_perfect(n):
    '''Checks if a number is perfect.'''

    sum_divisors = sum(get_divisors(n))
    return sum_divisors == n


def get_divisors(n):
    '''Returns a list of proper divisors of a given number.'''

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def generate_perfect_numbers(start, end):
    '''Generate perfect numbers within a range.'''
    perfect_numbers = []
    for number in range(start, end + 1):
        if is_perfect(number):
            perfect_numbers.append(number)

    return perfect_numbers


if __name__ == '__main__':
    main()
