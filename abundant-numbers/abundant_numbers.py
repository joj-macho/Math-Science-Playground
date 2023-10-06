def main():
    '''Main function to get user input and check if a number is abundant.'''

    print('\nAbundant Number Checker\n')

    # Display menu options and handle user input accordingly
    while True:
        print('1. Check if a number is abundant')
        print('2. List abundant numbers within a range')
        print('3. Display divisors of a number')
        print('4. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_abundant_number()
        elif choice == '2':
            list_abundant_numbers()
        elif choice == '3':
            display_divisors()
        elif choice == '4' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_abundant_number():
    '''Function to check if a number is abundant.'''
    # Get user input for a number and check if it is abundant
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    if is_abundant(number):
        print(f'{number} is an abundant number.\n')
    else:
        print(f'{number} is not an abundant number.\n')

def list_abundant_numbers():
    '''Function to list abundant numbers within a range.'''
    # Get user input for a range and list abundant numbers within that range
    while True:
        try:
            start = int(input('Enter the starting number: '))
            end = int(input('Enter the ending number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if start > end:
        print('Invalid range. Starting number should be less than or equal to the ending number.')
        return

    abundant_numbers = []
    for number in range(start, end + 1):
        if is_abundant(number):
            abundant_numbers.append(number)

    if abundant_numbers:
        print(f'Abundant numbers within the range ({start}, {end}):\n{abundant_numbers}\n')
    else:
        print(f'No abundant numbers within the range ({start}, {end}).\n')

def display_divisors():
    '''Function to display the divisors of a number.'''
    # Get user input for a number and display its divisors
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    divisors = get_divisors(number)

    if divisors:
        print(f'Divisors of {number}: {sorted(divisors)}\n')
    else:
        print(f'No divisors found for the number {number}.\n')

def get_divisors(n):
    '''Returns a list of divisors of a given number.'''
    # Calculate divisors for a given number
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    '''Checks if a number is abundant.'''
    # Check if a number is abundant by comparing the sum of divisors with the number
    sum_divisors = sum(get_divisors(n)) - n
    return sum_divisors > n

if __name__ == '__main__':
    main()
