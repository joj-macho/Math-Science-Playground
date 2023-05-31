def main():
    '''Main function to get user input and generate Pythagorean triplets.'''

    print('\nPythagorean Triplets\n')

    while True:
        print('1. Generate Pythagorean triplets within a range')
        print('2. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            generate_triplets()
        elif choice == '2' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def generate_triplets():
    '''Function to generate Pythagorean triplets within a given range.'''

    while True:
        try:
            start = int(input('Enter the starting number: '))
            end = int(input('Enter the ending number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    triplets = find_triplets(start, end)

    if triplets:
        print(f'Pythagorean triplets within the range ({start}, {end}):')
        for triplet in triplets:
            print(triplet[0], triplet[1], triplet[2])
        print()
    else:
        print(f'No Pythagorean triplets found within the range ({start}, {end}).\n')

def find_triplets(start, end):
    '''Returns a list of Pythagorean triplets within a given range.'''

    triplets = []
    for a in range(start, end + 1):
        for b in range(a, end + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer() and c <= end:
                triplets.append((a, b, int(c)))
    return triplets

if __name__ == '__main__':
    main()
