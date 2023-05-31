# Triangular Number Checker

## Description

Triangular numbers are positive integers that can form an equilateral triangle. The n-th triangular number represents the number of dots in an equilateral triangle with n dots on each side. For example, the number 6 is a triangular number because it can form an equilateral triangle with 6 dots on each side.

This program, Triangular Number Checker, is a Python program that allows users to check if a number is a triangular number or generate a sequence of triangular numbers.

## How it Works

- The program starts by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is a triangular number, generate a sequence of triangular numbers, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses an if-elif-else statement to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_triangular_number` function is called. If the user chooses option 2, the `generate_triangular_sequence` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To check if a number is a triangular number, the program calls the `check_triangular_number` function. This function prompts the user to enter a number and validates the input. The program then uses the `is_triangular_number` function to determine if the number is a triangular number and displays the result accordingly.

- The `is_triangular_number` function checks if a number `n` is a triangular number. It initializes a variable `total` to 0 and a counter `i` to 1. It iteratively adds the values of `i` to `total` until `total` is equal to or greater than `n`. If `total` is equal to `n`, it means that `n` is a triangular number and the function returns `True`. Otherwise, it returns `False`.

- To generate a sequence of triangular numbers, the program calls the `generate_triangular_sequence` function. This function prompts the user to enter the number of triangular numbers to generate and validates the input. The program then uses the `calculate_triangular_number` function to calculate each triangular number in the sequence and appends it to a list. Finally, the program displays the generated triangular sequence.

- The `calculate_triangular_number` function takes a number `n` as input and calculates the n-th triangular number using the formula `(n * (n + 1)) // 2`.


## Program Input & Output

When you run the program, `triangular_sequence.py`, the output will look like this;

```

Triangular Number Checker

1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the number of triangular numbers to generate: 10
Triangular sequence: 
[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 5
5 is not a triangular number.

1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```