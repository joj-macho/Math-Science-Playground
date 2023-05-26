def main():
    '''This is the main function to demonstrate the generation of the Fibonacci sequence.'''

    print('\nFibonacci Sequence Generator\n')

    # Get the number of terms from the user
    while True:
        try:
            num_terms = int(input('Enter the number of terms to generate (1 or more):\n> '))
            if num_terms <= 0:
                raise ValueError()
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer greater than zero.')

    # Limit the number of terms
    max_terms = 100  # Adjust the maximum number of terms as desired
    if num_terms > max_terms:
        print(f'Warning: Generating more than {max_terms} terms may take a long time.')
        input('Press Enter to begin...')

    # Generate the Fibonacci sequence
    sequence = generate_fibonacci_sequence(num_terms)

    # Display the sequence
    print(f'\nThe Fibonacci sequence up to {num_terms} terms:')
    for term in sequence:
        print(term, end=' ')

    print('\n')


def generate_fibonacci_sequence(n):
    '''This function generates the Fibonacci sequence up to n terms and returns the sequence as a list.'''

    # Validate the input
    if n <= 0:
        return []

    # Initialize the sequence with the first two terms
    sequence = [0, 1]

    # Generate the Fibonacci sequence
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence



if __name__ == '__main__':
    main()
