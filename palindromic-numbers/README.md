# Palindrome Number Checker

## Description

Palindrome numbers are positive integers that remain the same when their digits are reversed. In other words, they read the same forwards and backwards. For example, the numbers 121, 3443, or 12321 are palindrome numbers because they remain unchanged when the digits are reversed.

This program, Palindrome Number Checker, is a Python program that allows users to check if a number is a palindrome number.


## How it Works

- The program starts with a `main` function. Within this function, a while loop is used to continuously display a menu of options and handle user input. The user is presented with three options: check if a number is palindromic, list palindromic numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- If the user selects option 1, the program calls the `check_palindromic_number` function. This function prompts the user to enter a number and validates the input. It then uses the `is_palindromic` function to check if the number is palindromic. The result is displayed to the user.

- If the user selects option 2, the program calls the `list_palindromic_numbers` function. This function prompts the user to enter a starting and ending number for the range. The input is validated, ensuring that the starting number is less than or equal to the ending number. The program then iterates through each number in the range and checks if it is palindromic using the `is_palindromic` function. Palindromic numbers are added to a list, which is displayed to the user at the end.

- The `is_palindromic` function is used to check if a number is palindromic. It takes an integer as input and converts it to a string for easy comparison. The function then checks if the string representation of the number is equal to its reverse, achieved by using string slicing with a step of -1. If the number is palindromic, the function returns `True`; otherwise, it returns `False`.

- The program continues to run until the user chooses to quit by selecting option 3 or entering 'q'.


## Program Input & Output

When you run the program, `palindrome_numbers.py`, the output will look like this;

```

Palindromic Numbers Program

1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 88588
88588 is a palindromic number.

1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 1000
Enter the ending number: 5000
Palindromic numbers within the range (1000, 5000):
[1001, 1111, 1221, 1331, 1441, 1551, 1661, 1771, 1881, 1991, 2002, 2112, 2222, 2332, 2442, 2552, 2662, 2772, 2882, 2992, 3003, 3113, 3223, 3333, 3443, 3553, 3663, 3773, 3883, 3993, 4004, 4114, 4224, 4334, 4444, 4554, 4664, 4774, 4884, 4994]

1. Check if a number is palindromic
2. List palindromic numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```