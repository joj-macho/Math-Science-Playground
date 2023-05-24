def main():
    '''This is the main function.'''
    print('\nFactor Finder\n')

    # Get input from the user
    while True:
        try:
            number = int(input('Enter an integer to find its factors: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    # Find the factors
    factors = find_factors(number)

    # Display the result
    print(f"The factors of {number} are: {factors}")

def find_factors(number):
    '''This function finds the factors of a given number.'''

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
            
    return factors


if __name__ == '__main__':
    main()
