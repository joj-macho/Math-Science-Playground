
def main():
    '''Main function to get user input and check if a number is perfect.'''

    print('\nPerfect Number Checker\n')

    while True:
        print('1. Check if a number is perfect')
        print('2. List perfect numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_perfect_number()
        elif choice == '2':
            list_perfect_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_perfect_number():
    '''Function to check if a number is perfect.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_perfect(number):
        print(f'{number} is a perfect number.\n')
    else:
        print(f'{number} is not a perfect number.\n')

def list_perfect_numbers():
    '''Function to list perfect numbers within a range.'''

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

    perfect_numbers = []
    for number in range(start, end + 1):
        if is_perfect(number):
            perfect_numbers.append(number)

    if perfect_numbers:
        print(f'Perfect numbers within the range ({start}, {end}):\n{perfect_numbers}\n')
    else:
        print(f'No perfect numbers within the range.\n')

def is_perfect(n):
    '''Checks if a number is perfect.'''

    sum_divisors = sum(get_divisors(n))
    return sum_divisors == n

def get_divisors(n):
    '''Returns a list of proper divisors of a given number.'''

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    main()
