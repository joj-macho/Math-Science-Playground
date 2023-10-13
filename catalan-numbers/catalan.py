def main():
    '''Main function to compute the nth Catalan numbers and generate Catalan numbers'''

    print('\nCatalan Numbers Calculator and Generator\n')

    while True:
        # Display menu options
        print('Choose an option:')
        print('1. Compute the nth Catalan number')
        print('2. Generate Catalan numbers within a range')
        print('3. Exit program')

        choice = get_valid_input('Enter your choice: ')

        if choice == 1:
            # Compute the nth Catalan Number
            number = get_valid_input('Enter the nth (positive integer) Catalan number to compute: ')

            nth_catalan = calculate_catalan_number(number)
            print(f'The {number}th Catalan number is: {nth_catalan}\n')

        elif choice == 2:
            # Generate Catalan numbers within a given range
            start = get_valid_input('Enter the lower limit: ')
            end = get_valid_input('Enter an upper limit: ')

            if start > end:
                print('\nInvalid range. Lower limit should be less than or equal to the upper limit.\n')
                continue

            catalan_numbers = generate_catalan_numbers(start, end)
            if catalan_numbers:
                print(f'Catalan numbers within the range ({start}, {end}): {catalan_numbers}\n')
            else:
                print(f'No Catalan numbers within the range ({start}, {end}).\n')
    
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


def calculate_catalan_number(n):
    '''Calculate the nth Catalan number using the recursive formula.'''
    # Base case: C_0 = 1
    if n == 0:
        return 1

    catalan = 0
    # Calculate the nth Catalan number using the recursive formula
    for i in range(n):
        catalan += calculate_catalan_number(i) * calculate_catalan_number(n - i - 1)

    return catalan


def generate_catalan_numbers(start, end):
    '''Generate Catalan numbers within a range.'''
    # List to store Catalan Numbers
    catalan_numbers = []
    # Initialize the counter for calculating Catalan numbers
    i = 0

    # Iterate to calculate Catalan numbers until they exceed the 'end' value
    while True:
        # Calculate the nth Catalan number using the recursive formula
        catalan = calculate_catalan_number(i)
        # Check if the calculated Catalan number exceeds the 'end' value
        if catalan > end:
            break
        # Check if the Catalan number is within the specified range [start, end]
        if catalan >= start:
            catalan_numbers.append(catalan)
        
        i += 1

    return catalan_numbers


if __name__ == '__main__':
    main()
