def main():
    '''Main function to generate Lucas numbers.'''

    print('\nLucas Number Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Generate nth Lucas number')
        print('2. Generate Lucas sequence up to nth term')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Generate the nth Lucas Number
            number = get_valid_input('Enter a positive integer: ')
            print(f'The {number}th Lucas number is: {get_nth_lucas_number(number)}\n')

        elif choice == 2:
            # Generate Lucas sequence up to the nth term.
            number = get_valid_input('Enter a positive integer: ')
            lucas_sequence = generate_lucas_sequence(number)
            print(f'The Lucas sequence up to the {number}th term is:\n{lucas_sequence}.\n')

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


def get_nth_lucas_number(n):
    '''Returns the nth Lucas number.'''
    # Base cases for 0th and 1st Lucas numbers
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        # Initialize the first two Lucas numbers
        a, b = 2, 1
        # Calculate subsequent Lucas numbers using the Lucas sequence formula
        for _ in range(2, n + 1):
            a, b = b, a + b  # Update values using the formula L(n) = L(n-1) + L(n-2)
        return b


def generate_lucas_sequence(n):
    '''Generates the Lucas sequence up to the nth term.'''
    lucas_sequence = []
    for i in range(n + 1):
        lucas_sequence.append(get_nth_lucas_number(i))

    return lucas_sequence


if __name__ == '__main__':
    main()
