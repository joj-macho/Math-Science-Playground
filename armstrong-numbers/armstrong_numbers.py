def main():
    '''Main function to check if a number is an Armstrong number and generate Armstrong numbers'''

    print('\nArmstrong Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is an Armstrong number')
        print('2. Generate Armstrong numbers within a range')
        print('3. Enter (q)uit to exit program')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is amicable
            number = get_valid_input('Enter a positive integer to check if it is an Armstrong number: ')

            if is_armstrong(number):
                print(f'{number} is an Armstrong number.\n')
            else:
                print(f'{number} is not an Armstrong number.\n')

        elif choice == 2:
            # Generate Armstrong numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            armstrong_numbers = generate_armstrong_numbers(start, end)

            if armstrong_numbers:
                print(f'Armstrong numbers within the range ({start}, {end}): {armstrong_numbers}\n')
            else:
                print(f'No Armstrong numbers within the range ({start}, {end}).\n')

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


def is_armstrong(n):
    '''Checks if a number is an Armstrong number.'''
    # Convert the number to a string to get its digit
    num_str = str(n)
    # Calculate the number of digits in the number
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the number is equal to the sum of the nth powers of its digits
    return n == sum_of_digits


def generate_armstrong_numbers(start, end):
    '''Generate Armstrong numbers within a range.'''
    # List to store Armstrong numbers
    armstrong_numbers = []
    for number in range(start, end + 1):
        if is_armstrong(number):
            armstrong_numbers.append(number)

    return armstrong_numbers


if __name__ == '__main__':
    main()
