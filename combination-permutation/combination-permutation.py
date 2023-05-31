def main():
    '''Main function to get user input and perform combination or permutation calculations.'''

    print('\nCombination and Permutation Calculator\n')

    while True:
        print('1. Calculate Combination (nCr)')
        print('2. Calculate Permutation (nPr)')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice: ')

        if choice == '1':
            calculate_combination()
        elif choice == '2':
            calculate_permutation()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def calculate_combination():
    '''Function to calculate combination.'''

    while True:
        try:
            n = int(input('Enter the value of n: '))
            r = int(input('Enter the value of r: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if n >= r >= 0:
        result = factorial(n) // (factorial(r) * factorial(n - r))
        print(f'The combination of {n} choose {r} is {result}.\n')
    else:
        print('Invalid values. Make sure n >= r >= 0.\n')

def calculate_permutation():
    '''Function to calculate permutation.'''

    while True:
        try:
            n = int(input('Enter the value of n: '))
            r = int(input('Enter the value of r: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if n >= r >= 0:
        result = factorial(n) // factorial(n - r)
        print(f'The permutation of {n}P{r} is {result}.\n')
    else:
        print('Invalid values. Make sure n >= r >= 0.\n')

def factorial(n):
    '''Function to calculate factorial.'''

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    main()
