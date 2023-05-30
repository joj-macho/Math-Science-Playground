def main():
    '''The main function of the program.'''

    try:
        size = get_table_size()
        print_multiplication_table(size)
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def get_table_size():
    '''Gets the size of the multiplication table from the user.'''

    while True:
        try:
            size = int(input('\nEnter the size of the multiplication table:\n> '))
            if size >= 1:
                return size
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def print_multiplication_table(size):
    '''Prints a multiplication table of the given size.'''

    print(f'\n {size}x{size} Multiplication Table.\n')

    # Horizontal number labels
    print('  |', end='')
    for i in range(size + 1):
        print(f' {i:3}', end='')
    print('\n--+---' + '---' * size)

    # Each row
    for n in range(size + 1):
        print(f'{n:2}|', end='')
        for m in range(size + 1):
            print(f' {n * m:3}', end='')
        print()



if __name__ == '__main__':
    main()
