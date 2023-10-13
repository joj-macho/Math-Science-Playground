
def main():
    '''Main function to check Kaprekar and or Generate numbers.'''

    print('\nKaprekar Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is Kaprekar')
        print('2. List Kaprekar numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is Kaprekar
            number = get_valid_input('Enter a positive integer to check if it is a Kaprekar Number: ')

            if is_kaprekar(number):
                print(f'{number} is a Kaprekar number.\n')
            else:
                print(f'{number} is not a Kaprekar number.\n')

        elif choice == 2:
            # Generate Kaprekar numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            kaprekar_numbers = generate_kaprekar_numbers(start,end)

            if kaprekar_numbers:
                print(f'Kaprekar numbers within the range: {kaprekar_numbers}.\n')
            else:
                print(f'No Kaprekar numbers within the range ({start}, {end}).\n')

        elif choice == 3:
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


def is_kaprekar(n):
    '''Check if a number is Kaprekar.'''
    # Square the number
    square = n**2

    # Count the number of digits in the square
    digits = len(str(square))
    
    # Iterate through possible divisions of the square into two parts
    for i in range(1, digits):
        divisor = 10**i

        # Exclude division by n itself to avoid trivial cases
        if divisor == n:
            continue

        # Check if the sum of the two parts equals n
        sum_parts = square // divisor + square % divisor
        if sum_parts == n:
            return True

    # If no valid division found, the number is not a Kaprekar number
    return False


def generate_kaprekar_numbers(start, end):
    '''Generate Kaprekar numbers within a range.'''
    kaprekar_numbers = []
    for number in range(start, end + 1):
        if is_kaprekar(number):
            kaprekar_numbers.append(number)

    return kaprekar_numbers


if __name__ == '__main__':
    main()
