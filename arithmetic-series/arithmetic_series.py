def main():
    '''Main function to get user input, generate the arithmetic series, and calculate the sum.'''

    print('Arithmetic Series Sum\n')

    while True:
        try:
            first_term = float(input('Enter the first term: '))
            common_difference = float(input('Enter the common difference: '))
            num_terms = int(input('Enter the number of terms: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid numbers.')

    series = generate_arithmetic_series(first_term, common_difference, num_terms)
    series_sum = arithmetic_series_sum(first_term, common_difference, num_terms)

    print(f'Arithmetic Series for {num_terms} terms: a_1 = {first_term}, d = {common_difference}')
    print(series)
    print(f'\nThe sum of the arithmetic series is: {series_sum}')


def generate_arithmetic_series(first_term, common_difference, num_terms):
    '''Generates the arithmetic series.'''
    # Create a list comprehension to generate the arithmetic series
    # Each term is generated by adding the common difference to the previous term
    series = [first_term + i * common_difference for i in range(num_terms)]

    return series


def arithmetic_series_sum(first_term, common_difference, num_terms):
    '''Calculates the sum of an arithmetic series.'''
    # Calculate the last term of the series
    last_term = first_term + (num_terms - 1) * common_difference
    # Use the arithmetic series sum formula to calculate the sum
    series_sum = (num_terms / 2) * (first_term + last_term)
    
    return series_sum


if __name__ == '__main__':
    main()
