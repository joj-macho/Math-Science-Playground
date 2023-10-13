def main():
    '''Main function to get user input and perform combination or permutation calculations.'''

    print('\nCombination and Permutation Calculator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Calculate Combination (nCr)')
        print('2. Calculate Permutation (nPr)')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Calculate Combination
            n = get_valid_input('Enter the value of n: ')
            r = get_valid_input('Enter the value of r: ')
            calculate_combination(n, r)

        elif choice == 2:
            # Calculate Permutation
            n = get_valid_input('Enter the value of n: ')
            r = get_valid_input('Enter the value of r: ')
            calculate_permutation(n, r)

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


def calculate_combination(n, r):
    '''Calculate combination.'''

    if n >= r >= 0:
        result = factorial(n) // (factorial(r) * factorial(n - r))
        print(f'The combination of {n} choose {r} is {result}.\n')
    else:
        print('Invalid values. Make sure n >= r >= 0.\n')

def calculate_permutation(n, r):
    '''Calculate permutation.'''

    if n >= r >= 0:
        result = factorial(n) // factorial(n - r)
        print(f'The permutation of {n}P{r} is {result}.\n')
    else:
        print('Invalid values. Make sure n >= r >= 0.\n')

def factorial(n):
    '''Calculate factorial.'''

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    main()
