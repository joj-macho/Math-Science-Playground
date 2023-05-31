def main():
    '''Main function to check if a number is a triangular number or generate a sequence of triangular numbers.'''

    print('\nTriangular Number Checker\n')

    while True:
        print('1. Check if a number is a triangular number')
        print('2. Generate a sequence of triangular numbers')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_triangular_number()
        elif choice == '2':
            generate_triangular_sequence()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_triangular_number():
    '''Function to check if a number is a triangular number.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    if is_triangular_number(number):
        print(f'{number} is a triangular number.\n')
    else:
        print(f'{number} is not a triangular number.\n')

def generate_triangular_sequence():
    '''Function to generate a sequence of triangular numbers.'''

    while True:
        try:
            count = int(input('Enter the number of triangular numbers to generate: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    sequence = []

    for i in range(1, count + 1):
        sequence.append(calculate_triangular_number(i))

    print(f'Triangular sequence: \n{sequence}.\n')

def calculate_triangular_number(n):
    '''Calculates the n-th triangular number.'''

    return (n * (n + 1)) // 2

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

if __name__ == '__main__':
    main()
