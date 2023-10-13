def main():
    '''Main function to get user input and find amicable pairs.'''

    print('\nAmicable Number Checker and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Check if a number is part of an amicable pair')
        print('2. Generate amicable pairs within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Check if a number is amicable
            number = get_valid_input('Enter a positive integer to check if it is an amicable number: ')
            amicable_pair = find_amicable_pair(number)

            if amicable_pair:
                print(f'The amicable pair for {number} is: {amicable_pair}\n')
            else:
                print(f'{number} is not part of an amicable pair.\n')

        elif choice == 2:
            # Generate amicable pairs within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            amicable_pairs = generate_amicable_pairs(start, end)

            if amicable_pairs:
                print(f'Amicable pairs within the range ({start}, {end}):\n{amicable_pairs}\n')
            else:
                print(f'No amicable pairs within the range ({start}, {end}).\n')

        elif choice == 3:
            # Exit the program
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')


def get_valid_input(message):
    '''Get a valid input from the user.'''
    # Validate user input
    while True:
        try:
            user_input = int(input(message))
            if user_input >= 0:
                return user_input
            else:
                print('Invalid input. Please enter a non-negative integer.\n')
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')


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


def generate_amicable_pairs(start, end):
    '''Generate amicable pairs within a range.'''
    # List to store amicable pairs
    amicable_pairs = []
    found_pairs = set()  # Store pairs to avoid duplicates
    for number in range(start, end + 1):
        pair = find_amicable_pair(number)
        if pair and pair not in found_pairs:
            amicable_pairs.append(pair)
            # Add both pairs to the set to avoid duplicates
            found_pairs.add(pair)
            found_pairs.add((pair[1], pair[0]))

    return amicable_pairs


if __name__ == '__main__':
    main()
