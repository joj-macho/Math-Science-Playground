import math

def main():
    '''This function represents the main logic of the Factor Finder program. It prompts the user to enter an integer and finds all the factors of that number.
    The factors are then displayed to the user.'''

    print('\nFactor Finder\n')

    # Get input from the user
    while True:
        try:
            number = int(input('Enter an integer to find its factors:\n> '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    # Find the factors
    factors = get_factors(number)

    # Display the result
    print(f"The factors of {number} are: {factors}")

def get_factors(number):
    '''This function finds the factors of a given number.'''

    if number < 0:
        return []

    factors = [i for i in range(1, int(math.sqrt(number)) + 1) if number % i == 0]
    factors.extend(number // i for i in factors[::-1] if i * i != number)

    return factors


if __name__ == '__main__':
    main()
