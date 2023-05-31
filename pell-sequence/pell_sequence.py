def main():
    '''Main function to generate Pell numbers.'''

    print('\nPell Number Generator\n')

    while True:
        print('1. Generate Pell numbers')
        print('2. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            generate_pell_numbers()
        elif choice == '2' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def generate_pell_numbers():
    '''Function to generate Pell numbers.'''

    while True:
        try:
            n = int(input('Enter the number of Pell numbers to generate: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    pell_numbers = [0, 1]

    if n <= 2:
        print(f'Generated Pell numbers: {pell_numbers[:n]}\n.')
        return

    for i in range(2, n):
        pell = 2 * pell_numbers[i - 1] + pell_numbers[i - 2]
        pell_numbers.append(pell)

    print(f'Generated Pell numbers:\n{pell_numbers}.\n')

if __name__ == '__main__':
    main()
