def main():
    '''Main function to get user input, generate a geometric series, and calculate its sum.'''

    print('\nWelcome to the Geometric Series Generator\n')

    while True:
        try:
            first_term = float(input('Enter the first term: '))
            common_ratio = float(input('Enter the common ratio: '))
            num_terms = int(input('Enter the number of terms: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid numbers.')

    geometric_series = generate_geometric_series(first_term, common_ratio, num_terms)
    series_sum = geometric_series_sum(first_term, common_ratio, num_terms)

    print('\nThe generated geometric series is:')
    print(geometric_series)

    print(f'\nThe sum of the geometric series is: {series_sum}')


def generate_geometric_series(first_term, common_ratio, num_terms):
    '''Generates a geometric series.'''
    series = [first_term * common_ratio ** n for n in range(num_terms)]
    return series


def geometric_series_sum(first_term, common_ratio, num_terms):
    '''Calculates the sum of a geometric series.'''
    if common_ratio == 1:
        series_sum = first_term * num_terms
    else:
        series_sum = (first_term * (1 - common_ratio ** num_terms)) / (1 - common_ratio)
    return series_sum


if __name__ == '__main__':
    main()
