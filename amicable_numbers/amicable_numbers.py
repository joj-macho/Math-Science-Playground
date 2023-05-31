
def main():
    '''Main function to get user input and check if a number is amicable.'''

    print('\nAmicable Number Checker\n')

    while True:
        print('1. Check if a number is amicable')
        print('2. List amicable numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_amicable_number()
        elif choice == '2':
            list_amicable_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_amicable_number():
    '''Function to check if a number is amicable.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_amicable(number):
        print(f'{number} is an amicable number.\n')
    else:
        print(f'{number} is not an amicable number.\n')

def list_amicable_numbers():
    '''Function to list amicable numbers within a range.'''

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

    amicable_numbers = []
    for number in range(start, end + 1):
        if is_amicable(number):
            amicable_numbers.append(number)

    if amicable_numbers:
        print(f'Amicable numbers within the range ({start}, {end}):\n{amicable_numbers}\n')
    else:
        print(f'No amicable numbers within the range ({start}, {end}).\n')

def is_amicable(n):
    '''Checks if a number is amicable.'''

    sum_divisors_a = sum(get_divisors(n))
    sum_divisors_b = sum(get_divisors(sum_divisors_a))

    return n != sum_divisors_a and n == sum_divisors_b

def get_divisors(n):
    '''Returns a list of proper divisors of a given number.'''

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    main()
