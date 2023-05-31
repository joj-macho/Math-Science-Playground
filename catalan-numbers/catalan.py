
def main():
    '''Main function to compute Catalan numbers.'''

    print('\nCatalan Numbers\n')

    while True:
        print('1. Compute the nth Catalan number')
        print('2. List Catalan numbers up to a certain limit')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            compute_nth_catalan_number()
        elif choice == '2':
            list_catalan_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def compute_nth_catalan_number():
    '''Function to compute the nth Catalan number.'''

    while True:
        try:
            n = int(input('Enter the value of n:\n> '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if n < 0:
        print('Invalid input. n must be a non-negative integer.\n')
        return

    catalan = calculate_catalan_number(n)
    print(f'The {n}th Catalan number is: {catalan}\n')

def list_catalan_numbers():
    '''Function to list Catalan numbers up to a certain limit.'''

    while True:
        try:
            limit = int(input('Enter the limit: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if limit < 0:
        print('Invalid input. Limit must be a non-negative integer.\n')
        return

    catalan_numbers = []
    for n in range(limit + 1):
        catalan = calculate_catalan_number(n)
        catalan_numbers.append(catalan)

    print(f'Catalan numbers up to the limit ({limit}): {catalan_numbers}\n')

def calculate_catalan_number(n):
    '''Function to calculate the nth Catalan number using the recursive formula.'''

    if n == 0:
        return 1

    catalan = 0
    for i in range(n):
        catalan += calculate_catalan_number(i) * calculate_catalan_number(n - i - 1)

    return catalan

if __name__ == '__main__':
    main()
