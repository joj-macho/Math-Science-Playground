def main():
    '''Main function to check if a number is palindromic and generate palindromic numbers.'''

    print('\nPalindromic Numbers Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is palindromic')
        print('2. List palindromic numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is palindromic
            number = get_valid_input('Enter a positive integer to check if it is Palindromic: ')

            if is_palindromic(number):
                print(f'{number} is a palindromic number.\n')
            else:
                print(f'{number} is not a palindromic number.\n')

        elif choice == 2:
            # Generate palindromic numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            palindromic_numbers = generate_palindromic_numbers(start,end)

            if palindromic_numbers:
                print(f'Palindromic numbers within the range ({start}, {end}): {palindromic_numbers}\n')
            else:
                print(f'No palindromic numbers within the range ({start}, {end}).\n')

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


def is_palindromic(n):
    '''Checks if a number is palindromic.'''
    # Convert the number to a string for easy comparison
    number_str = str(n)
    return number_str == number_str[::-1]


def generate_palindromic_numbers(start, end):
    '''Generate palindromic numbers within a range.'''
    palindromic_numbers = []
    for number in range(start, end + 1):
        if is_palindromic(number):
            palindromic_numbers.append(number)

    return palindromic_numbers


if __name__ == '__main__':
    main()
