
def main():
    '''Main function to get user input and check if a number is palindromic.'''

    print('\nPalindromic Numbers Program\n')

    while True:
        print('1. Check if a number is palindromic')
        print('2. List palindromic numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_palindromic_number()
        elif choice == '2':
            list_palindromic_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_palindromic_number():
    '''Function to check if a number is palindromic.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_palindromic(number):
        print(f'{number} is a palindromic number.\n')
    else:
        print(f'{number} is not a palindromic number.\n')

def list_palindromic_numbers():
    '''Function to list palindromic numbers within a range.'''

    while True:
        try:
            start = int(input('Enter the starting number: '))
            end = int(input('Enter the ending number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if start > end:
        print('Invalid range. Starting number should be less than or equal to the ending number.\n')
        return

    palindromic_numbers = []
    for number in range(start, end + 1):
        if is_palindromic(number):
            palindromic_numbers.append(number)

    if palindromic_numbers:
        print(f'Palindromic numbers within the range ({start}, {end}):\n{palindromic_numbers}\n')
    else:
        print(f'No palindromic numbers within the range ({start}, {end}).\n')

def is_palindromic(n):
    '''Checks if a number is palindromic.'''

    # Convert the number to a string for easy comparison
    number_str = str(n)
    return number_str == number_str[::-1]

if __name__ == '__main__':
    main()
