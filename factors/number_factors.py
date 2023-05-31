
def main():
    '''Main function to find the factors of a number.'''

    print('\nNumber Factors Calculator\n')

    while True:
        number = get_valid_input()
        if number == 0:
            print('Bye.')
            break

        factors = find_factors(number)
        print(f'The factors of {number} are {factors}.\n')

def get_valid_input():
    '''Function to get a valid input from the user (a positive integer) or 0 to quit.'''

    while True:
        try:
            number = int(input('Enter a positive integer (or 0 to quit):\n> '))
            if number >= 0:
                break
            else:
                print('Invalid input. Please enter a positive integer or 0.\n')
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    return number

def find_factors(n):
    '''Function to find the factors of a number.'''

    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

if __name__ == '__main__':
    main()
