import csv
import sys
import re


def main():
    '''Main function to run the program.'''

    print('\nWelcome to the Periodic Table.\n')

    elements = read_periodic_table('periodictable.csv')

    while True:
        response = input(
            'Enter symbol or atomic number to examine. Enter (q)uit to exit.\n> '
        ).title()

        if response == 'Q' or response == 'Quit':
            print('Bye.')
            sys.exit()

        if response in elements:
            print_element_info(elements[response])
        else:
            print('Error: Invalid symbol or atomic number.')


def read_periodic_table(file_path):
    '''Read data from the CSV file and return a dictionary of elements.'''

    elements = {}

    try:
        with open(file_path, encoding='utf-8') as periodic_file:
            reader = csv.reader(periodic_file)
            for line in reader:
                element = {
                    'Atomic Number': line[0],
                    'Symbol': line[1],
                    'Element': line[2],
                    'Origin of name': line[3],
                    'Group': line[4],
                    'Period': line[5],
                    'Atomic weight': line[6] + ' u',
                    'Density': line[7] + ' g/cm^3',
                    'Melting point': line[8] + ' K',
                    'Boiling point': line[9] + ' K',
                    'Specific heat capacity': line[10] + ' J/(g*K)',
                    'Electronegativity': line[11],
                    'Abundance in earth\'s crust': line[12] + ' mg/kg'
                }

                for key, value in element.items():
                    # Remove the [roman numeral] text
                    element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

                atomic_number = line[0]
                symbol = line[1]
                elements[atomic_number] = element
                elements[symbol] = element
    except FileNotFoundError:
        print('Error: Periodic table file not found.')
        sys.exit()
    except csv.Error:
        print('Error: Invalid CSV file format.')
        sys.exit()

    return elements


def print_element_info(element):
    '''Print the information of a given element.'''

    ALL_COLUMNS = [
        'Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group',
        'Period', 'Atomic weight', 'Density', 'Melting point', 'Boiling point',
        'Specific heat capacity', 'Electronegativity',
        'Abundance in earth\'s crust'
    ]

    longest_column = max(len(key) for key in ALL_COLUMNS)

    for key in ALL_COLUMNS:
        key_justified = key.rjust(longest_column)
        print(key_justified + ':', element[key])

    input('Press Enter to Continue ...')
    print()



if __name__ == '__main__':
    main()
