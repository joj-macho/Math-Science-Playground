def main():
    '''Main function to check Harshad numbers.'''

    print('\nHarshad Number Checker\n')

    while True:
        print('1. Check if a number is Harshad')
        print('2. List Harshad numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_harshad_number()
        elif choice == '2':
            list_harshad_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_harshad_number():
    '''Function to check if a number is Harshad.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_harshad(number):
        print(f'{number} is a Harshad number.\n')
    else:
        print(f'{number} is not a Harshad number.\n')

def list_harshad_numbers():
    '''Function to list Harshad numbers within a range.'''

    while True:
        try:
            start = int(input('Enter the starting number > 0: '))
            end = int(input('Enter the ending number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if start > end:
        print('Invalid range. Starting number should be less than or equal to the ending number.\n')
        return

    harshad_numbers = []
    for number in range(start, end + 1):
        if is_harshad(number):
            harshad_numbers.append(number)

    if harshad_numbers:
        print(f'Harshad numbers within the range ({start}, {end}):\n{harshad_numbers}.\n')
    else:
        print(f'No Harshad numbers within the range ({start}, {end}).\n')

def is_harshad(n):
    '''Checks if a number is Harshad.'''

    sum_of_digits = sum(int(digit) for digit in str(n))
    return n % sum_of_digits == 0

if __name__ == '__main__':
    main()
