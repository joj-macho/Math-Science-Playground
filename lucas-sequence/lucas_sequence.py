
def main():
    '''Main function to generate Lucas numbers.'''

    print('\nLucas Number Generator\n')

    while True:
        print('1. Generate nth Lucas number')
        print('2. Generate Lucas sequence up to nth term')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            generate_nth_lucas_number()
        elif choice == '2':
            generate_lucas_sequence()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def generate_nth_lucas_number():
    '''Function to generate the nth Lucas number.'''

    while True:
        try:
            n = int(input('Enter the value of n: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    lucas_number = get_nth_lucas_number(n)

    print(f'The {n}th Lucas number is: {lucas_number}\n')


def generate_lucas_sequence():
    '''Function to generate the Lucas sequence up to the nth term.'''

    while True:
        try:
            n = int(input('Enter the value of n: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    lucas_sequence = get_lucas_sequence(n)

    print(f'The Lucas sequence up to the {n}th term is:\n{lucas_sequence}.\n')

def get_nth_lucas_number(n):
    '''Returns the nth Lucas number.'''

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def get_lucas_sequence(n):
    '''Returns the Lucas sequence up to the nth term.'''

    sequence = []
    for i in range(n + 1):
        sequence.append(get_nth_lucas_number(i))
    return sequence

if __name__ == '__main__':
    main()
