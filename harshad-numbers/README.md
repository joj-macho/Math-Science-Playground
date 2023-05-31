# Harshad Number Checker

## Description

Harshad numbers, also known as Niven numbers, are positive integers that are divisible by the sum of their digits. In other words, a number is considered Harshad if it can be evenly divided by the sum of its individual digits. For example, the number 18 is a Harshad number because the sum of its digits (1 + 8 = 9) divides 18 evenly. Similarly, 21 is a Harshad number because it is divisible by the sum of its digits (2 + 1 = 3).

This program, Harshad Number Checker, is a Python program that allows users to check if a number is a Harshad number or list Harshad numbers within a specified range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is Harshad, list Harshad numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_harshad_number` function is called. If the user chooses option 2, the `list_harshad_numbers` function is called. If the user chooses option 3 or enters 'q', the program terminates.

- To check if a number is Harshad, the program calls the `check_harshad_number` function. This function prompts the user to enter a number and validates the input. The program then checks if the number is a Harshad number using the `is_harshad` function.

- The `is_harshad` function checks if a number is Harshad by calculating the sum of its digits. It converts the number to a string, iterates over each digit, converts it back to an integer, and calculates the sum of the digits. If the number is divisible by the sum of its digits without a remainder, it is a Harshad number.

- If the number is a Harshad number, the program displays a message indicating that the number is Harshad. Otherwise, it displays a message indicating that the number is not a Harshad number.

- To list Harshad numbers within a range, the program calls the `list_harshad_numbers` function. This function prompts the user to enter a starting number and an ending number, and validates the input. The program then iterates over the range from the starting number to the ending number (inclusive) and checks if each number is a Harshad number using the `is_harshad` function. If a number is a Harshad number, it is added to a list.

- After iterating over the range, the program checks if any Harshad numbers were found within the range. If there are Harshad numbers, it displays them. Otherwise, it displays a message indicating that no Harshad numbers were found within the range.

## Program Input & Output

When you run the program, `harshad_numbers.py`, the output will look like this;

```

Harshad Number Checker

1. Check if a number is Harshad
2. List Harshad numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number > 0: 1
Enter the ending number: 100
Harshad numbers within the range (1, 100):
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90, 100].

1. Check if a number is Harshad
2. List Harshad numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 42
42 is a Harshad number.

1. Check if a number is Harshad
2. List Harshad numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```