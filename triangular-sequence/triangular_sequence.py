def main():
    '''Main function to check if a number is a triangular number or generate a sequence of triangular numbers.'''

    print('\nTriangular Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is a triangular number')
        print('2. Generate a sequence of triangular numbers')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is triangular
            number = get_valid_input('Enter a positive integer to check if it is a Triangular Number: ')

            if is_triangular_number(number):
                print(f'{number} is a triangular number.\n')
            else:
                print(f'{number} is not a triangular number.\n')

        elif choice == 2:
            limit = get_valid_input('Enter the number of triangular numbers to generate: ')
            triangular_sequence = generate_triangular_sequence(limit)
            print(f'Triangular Sequence: {triangular_sequence}\n')

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


def is_triangular_number(n):
    '''Checks if a number is a triangular number.'''

    if n < 0:
        return False

    i = 1
    total = 0

    while total < n:
        total += i
        i += 1

    return total == n


def generate_triangular_sequence(n):
    '''Generate a sequence of triangular numbers.'''

    sequence = []

    for i in range(1, n + 1):
        sequence.append(calculate_triangular_number(i))

    return sequence


def calculate_triangular_number(n):
    '''Calculates the n-th triangular number.'''

    return (n * (n + 1)) // 2


if __name__ == '__main__':
    main()
