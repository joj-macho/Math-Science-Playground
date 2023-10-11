import math

def main():
    '''Main function to check if a number is composite or generate composite numbers.'''

    print('\nComposite Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is composite')
        print('2. Generate composite numbers within a range')
        print('3. Exit program')
        
        choice = get_valid_input('Enter your choice: ')
        
        if choice == 1:
            # Check if a single number is composite
            number = get_valid_input('Enter a positive integer to check if it is composite:\n> ')
            if is_composite(number):
                print(f'{number} is a composite number.\n')
            else:
                print(f'{number} is not a composite number.\n')

        elif choice == 2:
            # Generate composite numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            composite_numbers = generate_composite_numbers(start, end)
            print(f'Composite numbers between [{start}, {end}]: {composite_numbers}\n')

        elif choice == 3:
            # Exit the program
            print('Bye.')
            break
        else:
            # Invalid choice.
            print('Invalid choice. Please try again.\n')


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


def is_composite(n):
    '''Check if a number is composite.'''
    # Composite numbers start at 4
    if n < 4:
        return False

    # Check if the number has factors other than 1 and itself
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True

    return False


def generate_composite_numbers(start, end):
    '''Generate composite numbers within a specified range.'''
    # List to store composite numbers
    composite_numbers = []
    
    # Check each number in the given range
    for num in range(start, end + 1):
        if is_composite(num):
            composite_numbers.append(num)
    
    return composite_numbers


if __name__ == '__main__':
    main()
