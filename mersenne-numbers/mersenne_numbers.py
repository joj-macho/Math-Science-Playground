
def main():
    '''Main function to generate Mersenne numbers.'''

    print('\nMersenne Number Generator\n')

    while True:
        print('1. Generate Mersenne numbers')
        print('2. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            generate_mersenne_numbers()
        elif choice == '2' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def generate_mersenne_numbers():
    '''Function to generate Mersenne numbers.'''

    while True:
        try:
            n = int(input('Enter the number of Mersenne numbers to generate: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    mersenne_numbers = []
    count = 0
    exponent = 1

    while count < n:
        mersenne = 2 ** exponent - 1
        if is_prime(exponent) and is_prime(mersenne):
            mersenne_numbers.append(mersenne)
            count += 1
        exponent += 1

    print(f'Generated Mersenne numbers: {mersenne_numbers}.\n')

def is_prime(n):
    '''Checks if a number is prime.'''

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    main()
