
def main():
    '''Main function to generate Fibonacci numbers.'''

    print('\nFibonacci Number Generator\n')

    while True:
        print('1. Generate Fibonacci sequence')
        print('2. Quit Program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            generate_fibonacci_sequence()
        elif choice == '2':
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def generate_fibonacci_sequence():
    '''Function to generate the Fibonacci sequence.'''

    while True:
        try:
            n = int(input('Enter the number of terms: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    fibonacci_sequence = [0, 1]

    if n <= 0:
        print('Invalid number of terms. Number of terms should be greater than 0.')
        return
    elif n == 1:
        print(f'Fibonacci sequence for n = {n}: {fibonacci_sequence[:1]}\n')
        return
    elif n == 2:
        print(f'Fibonacci sequence for n = {n}: {fibonacci_sequence}\n')
        return

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(f'Fibonacci sequence for n = {n}: {fibonacci_sequence}\n')

if __name__ == '__main__':
    main()
