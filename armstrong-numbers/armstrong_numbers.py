
def main():
    '''Main function to get user input and check if a number is an Armstrong number.'''

    print('\nArmstrong Number Checker\n')

    while True:
        print('1. Check if a number is an Armstrong number')
        print('2. List Armstrong numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_armstrong_number()
        elif choice == '2':
            list_armstrong_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_armstrong_number():
    '''Function to check if a number is an Armstrong number.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_armstrong(number):
        print(f'{number} is an Armstrong number.\n')
    else:
        print(f'{number} is not an Armstrong number.\n')

def list_armstrong_numbers():
    '''Function to list Armstrong numbers within a range.'''

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

    armstrong_numbers = []
    for number in range(start, end + 1):
        if is_armstrong(number):
            armstrong_numbers.append(number)

    if armstrong_numbers:
        print(f'Armstrong numbers within the range ({start}, {end}):\n{armstrong_numbers}\n')
    else:
        print(f'No Armstrong numbers within the range ({start}, {end}).\n')

def is_armstrong(n):
    '''Checks if a number is an Armstrong number.'''

    num_str = str(n)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    return n == sum_of_digits

if __name__ == '__main__':
    main()
