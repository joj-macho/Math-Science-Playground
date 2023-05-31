
def main():
    '''Main function to get user input and check if a number is a perfect square.'''

    print('\nPerfect Squares Program\n')

    while True:
        print('1. Check if a number is a perfect square')
        print('2. List perfect squares within a limit')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_perfect_square()
        elif choice == '2':
            list_perfect_squares()
        elif choice == '3':
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_perfect_square():
    '''Function to check if a number is a perfect square.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_perfect_square(number):
        print(f'{number} is a perfect square.\n')
    else:
        print(f'{number} is not a perfect square.\n')

def list_perfect_squares():
    '''Function to list perfect squares within a limit.'''

    while True:
        try:
            limit = int(input('Enter the limit: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    squares = []
    for num in range(1, limit + 1):
        if is_perfect_square(num):
            squares.append(num)

    if squares:
        print(f'Perfect squares within the limit ({limit}):\n{squares}.\n')
    else:
        print(f'No perfect squares within the limit {limit}.\n')

def is_perfect_square(n):
    '''Checks if a number is a perfect square.'''

    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

if __name__ == '__main__':
    main()
