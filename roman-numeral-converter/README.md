# Roman Numeral Converter

## Description

The Roman Numeral Converter program is a Python program that converts a given number into its equivalent Roman numeral representation. Roman numerals are a numeral system that originated in ancient Rome and uses a combination of letters to represent numbers. 

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to prompt the user to enter a number. The input is validated to ensure it is a valid integer. The number is stored in the `number` variable.

- The program then calls the `convert_to_roman` function and passes the number as an argument.

- The `convert_to_roman` function is responsible for converting the number to a Roman numeral. It begins by defining a dictionary called `roman_numerals` that maps specific numbers to their corresponding Roman numeral symbols.

- The function initializes an empty string called `roman_numeral` to store the Roman numeral representation.

- It then iterates over the items in the `roman_numerals` dictionary using a for loop. For each item, it compares the current `value` with the given `number`. If the `number` is greater than or equal to the current `value`, it appends the corresponding `symbol` to the `roman_numeral` string and subtracts the `value` from the `number`. This process continues as long as the `number` is greater than or equal to the `value`.

- After iterating through all the items in the dictionary, the function returns the `roman_numeral` string, which represents the Roman numeral equivalent of the given number. After iterating through all the items in the dictionary, the function returns the `roman_numeral` string, which represents the Roman numeral equivalent of the given number.


## Program Input & Output

When you run the program, `roman_numeral.py`, the output will look like this;

```

Roman Numeral Converter

Enter a number:
> 42
Roman numeral: XLII


Roman Numeral Converter

Enter a number:
> 6596
Roman numeral: MMMMMMDXCVI
```