
def main():
    '''Main function to check if a number is composite.'''

    print('\nComposite Number Checker\n')

    while True:
        number = get_valid_input()
        if number == 0:
            print('Bye.')
            break

        if is_composite(number):
            print(f'{number} is a composite number.\n')
        else:
            print(f'{number} is not a composite number.\n')

def get_valid_input():
    '''Function to get a valid input from the user (a positive integer) or 0 to quit.'''

    while True:
        try:
            number = int(input('Enter a positive integer (or 0 to exit):\n> '))
            if number >= 0:
                break
            else:
                print('Invalid input. Please enter a positive integer or 0.\n')
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    return number

def is_composite(n):
    '''Function to check if a number is composite.'''

    if n < 4:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True

    return False

if __name__ == '__main__':
    main()
