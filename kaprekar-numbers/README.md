# Kaprekar Number Checker

## Description

Kaprekar numbers are positive integers that, when squared and divided into two parts (left and right), produce a sum equal to the original number. For example, the number 9 is a Kaprekar number because 9^2 = 81 and 8 + 1 = 9.

This program, Kaprekar Number Checker, is a Python program that allows users to check if a number is a Kaprekar number or list Kaprekar numbers within a specified range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is a Kaprekar number, list Kaprekar numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_kaprekar_number` function is called. If the user chooses option 2, the `list_kaprekar_numbers` function is called. If the user chooses option 3 or enters 'q', the program terminates.

- To check if a number is a Kaprekar number, the program calls the `check_kaprekar_number` function. This function prompts the user to enter a number and validates the input. The program then checks if the number is a Kaprekar number using the `is_kaprekar` function.

- The `is_kaprekar` function checks if a number is a Kaprekar number by squaring it and comparing the sum of its parts to the original number. It calculates the square of the number and determines the number of digits in the square. It then iterates over the range of digits to check if each digit is a divisor of the square. If a digit is a divisor, it calculates the sum of the parts of the square divided by the divisor. If the sum of the parts is equal to the original number, it returns True, indicating that the number is a Kaprekar number. Otherwise, it returns False.

- If the number is a Kaprekar number, the program displays a message indicating that the number is a Kaprekar number. Otherwise, it displays a message indicating that the number is not a Kaprekar number.

- To list Kaprekar numbers within a range, the program calls the `list_kaprekar_numbers` function. This function prompts the user to enter a starting number and an ending number, and validates the input. The program then iterates over the range from the starting number to the ending number (inclusive) and checks if each number is a Kaprekar number using the `is_kaprekar` function. If a number is a Kaprekar number, it is added to a list.

- After iterating over the range, the program checks if any Kaprekar numbers were found within the range. If there are Kaprekar numbers, it displays them. Otherwise, it displays a message indicating that no Kaprekar numbers were found within the range.


## Program Input & Output

When you run the program, `kaprekar_numbers.py`, the output will look like this;

```

Kaprekar Number Checker

1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 1
Enter the ending number: 100
Kaprekar numbers within the range: [9, 45, 55, 99]
1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 45
45 is a Kaprekar number.

1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 25
Invalid choice. Please enter a valid option.
1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 25
25 is not a Kaprekar number.

1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```