def main():
    '''Main function to check Harshad numbers and generate Harshad numbers.'''

    print('\nHarshad Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is Harshad')
        print('2. Generate Harshad numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is Harshad
            number = get_valid_input('Enter a positive integer to check if it is a Harshad Number: ')

            if is_harshad(number):
                print(f'{number} is a Harshad number.\n')
            else:
                print(f'{number} is not a Harshad number.\n')

        elif choice == 2:
            # Generate Harshad numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue
            
            harshad_numbers = generate_harshad_numbers(start, end)
            if harshad_numbers:
                print(f'Harshad numbers within the range ({start}, {end}): {harshad_numbers}.\n')
            else:
                print(f'No Harshad numbers within the range ({start}, {end}).\n')

        elif choice == 3:
            # Exit the program
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


def is_harshad(n):
    '''Checks if a number is Harshad.'''
    # Calculate sum of digits for n
    sum_of_digits = sum(int(digit) for digit in str(n))
    return n % sum_of_digits == 0


def generate_harshad_numbers(start, end):
    '''Generate Harshad numbers within a range.'''
    harshad_numbers = []
    for number in range(start, end + 1):
        if is_harshad(number):
            harshad_numbers.append(number)

    return harshad_numbers


if __name__ == '__main__':
    main()
