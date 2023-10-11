import math

def main():
    '''Main function to check if a number is abundant or generate abundant numbers.'''

    print('\nAbundant Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is abundant')
        print('2. Generate abundant numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a single number is abundant
            number = get_valid_input('Enter a positive integer to check if it is abundant:\n> ')

            divisors = get_divisors(number)
            divisors_str = ' + '.join(map(str, divisors[:-1]))

            if is_abundant(number):
                print(f'{number} is an abundant number...')
                print(f'Sum of divisors of {number}: {divisors_str} = {sum(divisors[:-1])} > {number}\n')
            else:
                print(f'{number} is not an abundant number...')
                print(f'Sum of divisors of {number}: {divisors_str} = {sum(divisors[:-1])} < {number}\n')

        elif choice == 2:
            # Generate abundant numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            abundant_numbers = generate_abundant_numbers(start, end)
            if abundant_numbers:
                print(f'Abundant numbers between [{start}, {end}]: {abundant_numbers}\n')
            else:
                print(f'No abundant numbers between [{start}, {end}].\n')

        elif choice == 3:
            # Exit the program
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.\n')


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


def get_divisors(n):
    '''Returns a list of divisors of a given number.'''
    # Calculate divisors for a given number
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)


def is_abundant(n):
    '''Checks if a number is abundant.'''
    # Check if a number is abundant by comparing the sum of divisors with the number
    sum_divisors = sum(get_divisors(n)) - n
    return sum_divisors > n


def generate_abundant_numbers(start, end):
    '''Generate abundant numbers within a specified range.'''
    # List to store abundant numbers
    abundant_numbers = []

    # Check each number in the given range
    for number in range(start, end + 1):
        if is_abundant(number):
            abundant_numbers.append(number)

    return abundant_numbers


if __name__ == '__main__':
    main()