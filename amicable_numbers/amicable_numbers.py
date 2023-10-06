def main():
    '''Main function to get user input and find amicable pairs.'''

    print('\nAmicable Number Checker\n')

    while True:
        print('1. Check if a number is part of an amicable pair')
        print('2. List amicable pairs within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_amicable_pair()
        elif choice == '2':
            list_amicable_pairs()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_amicable_pair():
    '''Function to check if a number is part of an amicable pair.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    amicable_pair = find_amicable_pair(number)

    if amicable_pair:
        print(f'The amicable pair for {number} is: {amicable_pair}\n')
    else:
        print(f'{number} is not part of an amicable pair.\n')

def list_amicable_pairs():
    '''Function to list amicable pairs within a range.'''

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

    amicable_pairs = []
    for number in range(start, end + 1):
        pair = find_amicable_pair(number)
        if pair:
            amicable_pairs.append(pair)

    if amicable_pairs:
        print(f'Amicable pairs within the range ({start}, {end}):\n{amicable_pairs}\n')
    else:
        print(f'No amicable pairs within the range ({start}, {end}).\n')

def find_amicable_pair(n):
    '''Finds an amicable pair for a given number.'''

    sum_divisors_a = sum(get_divisors(n))
    sum_divisors_b = sum(get_divisors(sum_divisors_a))

    # Check if n is part of an amicable pair
    if n != sum_divisors_a and n == sum_divisors_b:
        return (n, sum_divisors_a)
    else:
        return None

def get_divisors(n):
    '''Returns a list of proper divisors of a given number.'''

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    main()