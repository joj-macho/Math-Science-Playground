# Numeral System Converter

## Description

The Numeral System Converter program is a Python program that allows users to convert numbers between different numeral systems. It supports conversions from decimal, hexadecimal, octal, and binary numeral systems.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to continuously display a menu of options and handle user input. The user is presented with five options: convert from decimal, convert from hexadecimal, convert from octal, convert from binary, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `convert_from_decimal` function is called. If the user chooses option 2, the `convert_from_hexadecimal` function is called. If the user chooses option 3, the `convert_from_octal` function is called. If the user chooses option 4, the `convert_from_binary` function is called. If the user chooses option 5 or enters 'q', the program terminates.

- Each conversion function prompts the user to enter a number in the respective numeral system. The input is validated to ensure it is a valid number in the specified numeral system.

- The conversion functions utilize built-in Python functions to perform the conversions. For example, the `convert_from_decimal` function converts a decimal number to hexadecimal, octal, and binary by using the `hex()`, `oct()`, and `bin()` functions, respectively. Similarly, the other conversion functions convert numbers from their respective numeral systems using appropriate Python functions.

- After performing the conversions, the program displays the original number along with its converted representations in the different numeral systems.

- The program continues to run until the user chooses to quit by selecting option 5 or entering 'q'.


## Program Input & Output

When you run the program, `numeral_system_converter.py`, the output will look like this;

```

Numeral System Converter

1. Convert from Decimal
2. Convert from Hexadecimal
3. Convert from Octal
4. Convert from Binary
5. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a decimal number: 42
DEC: 42    HEX: 0x2a    OCT: 0o52    BIN: 0b101010

1. Convert from Decimal
2. Convert from Hexadecimal
3. Convert from Octal
4. Convert from Binary
5. Enter (q)uit to exit program
Enter your choice:
> 2
Enter a hexadecimal number: 0x3e
HEX: 0x3e    DEC: 62    OCT: 0o76    BIN: 0b111110

1. Convert from Decimal
2. Convert from Hexadecimal
3. Convert from Octal
4. Convert from Binary
5. Enter (q)uit to exit program
Enter your choice:
> 3
Enter an octal number: 0o53
OCT: 0o53    DEC: 43    HEX: 0x2b    BIN: 0b101011

1. Convert from Decimal
2. Convert from Hexadecimal
3. Convert from Octal
4. Convert from Binary
5. Enter (q)uit to exit program
Enter your choice:
> 4
Enter a binary number: 11001
BIN: 11001    DEC: 25    HEX: 0x19    OCT: 0o31

1. Convert from Decimal
2. Convert from Hexadecimal
3. Convert from Octal
4. Convert from Binary
5. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```