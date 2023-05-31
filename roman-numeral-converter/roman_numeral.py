def main():
    '''Main function to get a number and convert it to a Roman numeral.'''

    print('\nRoman Numeral Converter\n')

    while True:
        try:
            number = int(input('Enter a number:\n> '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    roman_numeral = convert_to_roman(number)
    print('Roman numeral:', roman_numeral)

def convert_to_roman(number):
    '''Function to convert a number to a Roman numeral.'''

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral

if __name__ == '__main__':
    main()
