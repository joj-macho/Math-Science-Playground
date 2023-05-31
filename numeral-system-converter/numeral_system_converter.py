def main():
    '''Main function to convert numbers between numeral systems.'''

    print('\nNumeral System Converter\n')

    while True:
        print('1. Convert from Decimal')
        print('2. Convert from Hexadecimal')
        print('3. Convert from Octal')
        print('4. Convert from Binary')
        print('5. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            convert_from_decimal()
        elif choice == '2':
            convert_from_hexadecimal()
        elif choice == '3':
            convert_from_octal()
        elif choice == '4':
            convert_from_binary()
        elif choice == '5' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def convert_from_decimal():
    '''Function to convert a decimal number to other numeral systems.'''

    while True:
        try:
            number = int(input('Enter a decimal number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    hex_number = hex(number)
    octal_number = oct(number)
    binary_number = bin(number)

    print('DEC:', number, '   HEX:', hex_number, '   OCT:', octal_number, '   BIN:', binary_number)
    print()

def convert_from_hexadecimal():
    '''Function to convert a hexadecimal number to other numeral systems.'''

    number = input('Enter a hexadecimal number: ')

    decimal_number = int(number, 16)
    octal_number = oct(decimal_number)
    binary_number = bin(decimal_number)

    print('HEX:', number, '   DEC:', decimal_number, '   OCT:', octal_number, '   BIN:', binary_number)
    print()

def convert_from_octal():
    '''Function to convert an octal number to other numeral systems.'''

    number = input('Enter an octal number: ')

    decimal_number = int(number, 8)
    hex_number = hex(decimal_number)
    binary_number = bin(decimal_number)

    print('OCT:', number, '   DEC:', decimal_number, '   HEX:', hex_number, '   BIN:', binary_number)
    print()

def convert_from_binary():
    '''Function to convert a binary number to other numeral systems.'''

    number = input('Enter a binary number: ')

    decimal_number = int(number, 2)
    hex_number = hex(decimal_number)
    octal_number = oct(decimal_number)

    print('BIN:', number, '   DEC:', decimal_number, '   HEX:', hex_number, '   OCT:', octal_number)
    print()

if __name__ == '__main__':
    main()

