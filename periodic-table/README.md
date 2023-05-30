# The Periodic Table of Elements

## Description

This program is a simple implementation of a periodic table information lookup tool. It allows users to enter either an element symbol or atomic number to retrieve information about the corresponding element.

This program reads data from a CSV file containing information about the elements in the periodic table and stores it in a dictionary. The Data is from Wikipedia and stored in a file `periodictable.csv`

## How it Works

- The program first imports the `csv`, `sys`, and `re` modules.
    - `csv` module: Used to read data from a CSV file.
    - `sys` module: Used to exit the program when errors occur or when the user chooses to quit.
    - `re` module: Used to remove the [roman numeral] text from certain elements' values.

- The `main` function is defined. It first prints a welcome message to the user.

- The program reads the periodic table data from a CSV file using the `read_periodic_table()` function. The file path is provided as an argument to the function. The data is stored in a dictionary where the atomic number and symbol are mapped to the corresponding element information.

- The program enters a loop where it repeatedly prompts the user for input. The user can enter an element symbol, atomic number, or choose to quit the program. If the user chooses to quit, the program exits.

- If the user enters a valid element symbol or atomic number, the program calls the `print_element_info()` function to display the information of the corresponding element. The `print_element_info()` function takes an element dictionary as input and prints each piece of information in a formatted manner. The information to be printed is stored in the `ALL_COLUMNS` list, and the longest column length is calculated to ensure proper alignment of the output.

- After displaying the element information, the program waits for the user to press Enter before prompting for the next input.

## Program Input & Output

When you run the program `periodic_table.py`, the output will look like this;

```

Welcome to the Periodic Table.

Enter symbol or atomic number to examine. Enter (q)uit to exit.
> 1
             Atomic Number: 1
                    Symbol: H
                   Element: Hydrogen
            Origin of name: Greek elements hydro- and -gen, meaning 'water-forming'
                     Group: 1
                    Period: 1
             Atomic weight: 1.008 u
                   Density: 0.00008988 g/cm^3
             Melting point: 14.01 K
             Boiling point: 20.28 K
    Specific heat capacity: 14.304 J/(g*K)
         Electronegativity: 2.2
Abundance in earth's crust: 1400 mg/kg
Press Enter to Continue ...

Enter symbol or atomic number to examine. Enter (q)uit to exit.
> au
             Atomic Number: 79
                    Symbol: Au
                   Element: Gold
            Origin of name: English word (The symbol derives from Latin aurum)
                     Group: 11
                    Period: 6
             Atomic weight: 196.966570(4) u
                   Density: 19.282 g/cm^3
             Melting point: 1337.33 K
             Boiling point: 3129 K
    Specific heat capacity: 0.129 J/(g*K)
         Electronegativity: 2.54
Abundance in earth's crust: 0.004 mg/kg
Press Enter to Continue ...

Enter symbol or atomic number to examine. Enter (q)uit to exit.
> helium
Error: Invalid symbol or atomic number.
Enter symbol or atomic number to examine. Enter (q)uit to exit.
> hel
Error: Invalid symbol or atomic number.
Enter symbol or atomic number to examine. Enter (q)uit to exit.
> 42
             Atomic Number: 42
                    Symbol: Mo
                   Element: Molybdenum
            Origin of name: Greek molýbdaina, 'piece of lead', from mólybdos, 'lead'
                     Group: 6
                    Period: 5
             Atomic weight: 95.95(1) u
                   Density: 10.22 g/cm^3
             Melting point: 2896 K
             Boiling point: 4912 K
    Specific heat capacity: 0.251 J/(g*K)
         Electronegativity: 2.16
Abundance in earth's crust: 1.2 mg/kg
Press Enter to Continue ...

Enter symbol or atomic number to examine. Enter (q)uit to exit.
> q
Bye.
```
