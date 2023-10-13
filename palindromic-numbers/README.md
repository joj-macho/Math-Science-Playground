# Palindrome Number Checker

## Description

Palindrome numbers are positive integers that remain the same when their digits are reversed. In other words, they read the same forwards and backwards. For example, the numbers 121, 3443, or 12321 are palindrome numbers because they remain unchanged when the digits are reversed.

You can read more about Palindromic numbers on [Wikipedia](https://en.wikipedia.org/wiki/Palindromic_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/PalindromicNumber.html)

This program, Palindrome Number Checker, is a Python program that allows users to check if a number is a palindrome number and generate palindrome numbers within a specified range.


## How it Works

- The program starts with a `main` function. Within this function, a while loop is used to continuously display a menu of options and handle user input. The user is presented with three options: check if a number is palindromic, list palindromic numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- If the user selects option 1, the program calls the `is_palindromic` function. This function takes an integer as input and converts it to a string for easy comparison. The function then checks if the string representation of the number is equal to its reverse, achieved by using string slicing with a step of -1. If the number is palindromic, the function returns `True`; otherwise, it returns `False`.

- If the user selects option 2, the program calls the `generate_palindromic_numbers` function. This function iterates through each number in the range and checks if it is palindromic using the `is_palindromic` function. Palindromic numbers are added to a list, which is displayed to the user at the end.


## Program Input & Output

When you run the program, `palindrome_numbers.py`, the output will look like this;

```

Palindromic Numbers Checker and Generator

Choose an option:
1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is Palindromic: 16
16 is not a palindromic number.

Choose an option:
1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is Palindromic: 88288
88288 is a palindromic number.

Choose an option:
1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 10
Enter an upper limit: 1000
Palindromic numbers within the range (10, 1000): [11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]

Choose an option:
1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```