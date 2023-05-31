
def main():
    '''Main function to calculate the factorial of a number.'''

    print('\nFactorial Calculator\n')

    while True:
        number = get_valid_input()
        if number == 0:
            print('Bye.')
            break

        factorial = calculate_factorial(number)
        print(f'The factorial of {number} is {factorial}.\n')

def get_valid_input():
    '''Function to get a valid input from the user (a non-negative integer) or 0 to quit.'''

    while True:
        try:
            number = int(input('Enter a non-negative integer (or 0 to quit):\n> '))
            if number >= 0:
                break
            else:
                print('Invalid input. Please enter a non-negative integer or 0.\n')
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    return number

def calculate_factorial(n):
    '''Function to calculate the factorial of a number.'''

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial

if __name__ == '__main__':
    main()
