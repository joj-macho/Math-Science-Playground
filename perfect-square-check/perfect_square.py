
def main():
    '''Main function to check if a number is a perfect square and generate perfect square numbers.'''

    print('\nPerfect Squares Program\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is a perfect square')
        print('2. List perfect squares within a limit')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is perfect square
            number = get_valid_input('Enter a positive integer to check if it is a Perfect Square: ')

            if is_perfect_square(number):
                print(f'{number} is a perfect square.\n')
            else:
                print(f'{number} is not a perfect square.\n')

        elif choice == 2:
            # Generate perfect squares within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            perfect_squares = generate_perfect_squares(start,end)

            if perfect_squares:
                print(f'Perfect squares within the range [{start}, {end}]: {perfect_squares}.\n')
            else:
                print(f'No perfect squares within the range [{start}, {end}].\n')

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


def is_perfect_square(n):
    '''Checks if a number is a perfect square.'''

    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n


def generate_perfect_squares(start, end):
    '''Generate perfect squares within a limit.'''

    squares = []
    for num in range(start, end + 1):
        if is_perfect_square(num):
            squares.append(num)

    return squares


if __name__ == '__main__':
    main()
