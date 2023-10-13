# Triangular Number Checker

## Description

Triangular numbers are positive integers that can form an equilateral triangle. The n-th triangular number represents the number of dots in an equilateral triangle with $n$ dots on each side.

The n-th triangular number, is given by the formula:
$$T_n = \frac{n(n + 1)}{2}$$
where $T_n$ is the n-th triangular number, $n$ is a non-negative integer representing the n-th term or position in the sequence.


For example, the number 6 is a triangular number because it can form an equilateral triangle with 6 dots on each side.

You can read more about Triangular numbers on [Wikipedia](https://en.wikipedia.org/wiki/Triangular_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/TriangularNumber.html)

This program, Triangular Number Checker, is a Python program that allows users to check if a number is a triangular number or generate a sequence of triangular numbers.

## How it Works

- The program starts by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is a triangular number, generate a sequence of triangular numbers, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses an if-elif-else statement to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_triangular_number` function is called. If the user chooses option 2, the `generate_triangular_sequence` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To check if a number is a triangular number, the program calls the `is_triangular_number` function. This function checks if a number `n` is a triangular number. It initializes a variable `total` to 0 and a counter `i` to 1. It iteratively adds the values of `i` to `total` until `total` is equal to or greater than `n`. If `total` is equal to `n`, it means that `n` is a triangular number and the function returns `True`. Otherwise, it returns `False`.

- To generate a sequence of triangular numbers, the program calls the `generate_triangular_sequence` function. This function uses the `calculate_triangular_number` function to calculate each triangular number in the sequence and appends it to a list.

- The `calculate_triangular_number` function takes a number `n` as input and calculates the n-th triangular number using the formula `(n * (n + 1)) // 2`.


## Program Input & Output

When you run the program, `triangular_sequence.py`, the output will look like this;

```

Triangular Number Checker and Generator

Choose an option:
1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Triangular Number: 42
42 is not a triangular number.

Choose an option:
1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Triangular Number: 45
45 is a triangular number.

Choose an option:
1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Exit program
Enter your choice: 2
Enter the number of triangular numbers to generate: 25
Triangular Sequence: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325]

Choose an option:
1. Check if a number is a triangular number
2. Generate a sequence of triangular numbers
3. Exit program
Enter your choice: 3
Bye.
```