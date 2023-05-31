# Factorial Calculator

## Description

The factorial of a non-negative integer `n`, denoted as `n!`, is the product of all positive integers from 1 to `n`. For example, the factorial of 5 ($5!$) is calculated as $5 × 4 × 3 × 2 × 1$, which equals 120.

The Factorial Calculator is a Python program that allows users to calculate the factorial of a given number.

## How it Works

- The program begins with a `main` function. Inside this function, a while loop is used to repeatedly prompt the user for input and calculate the factorial. The loop continues until the user enters 0 to quit.

- The `get_valid_input` function is called to obtain a valid input from the user. This function prompts the user to enter a non-negative integer or 0 to quit. It validates the input, ensuring that the entered value is a non-negative integer or 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The `calculate_factorial` function is called to calculate the factorial of the entered number. This function takes a non-negative integer `n` as input and iterates from 1 to `n`, multiplying each number to the running factorial product. The calculated factorial is then returned.

- Based on the calculated factorial, the `main` function displays the result to the user, indicating the factorial value for the entered number.


## Program Input & Output

When you run the program, `factorial_numbers.py`, the output will look like this;

```

Factorial Calculator

Enter a non-negative integer (or 0 to quit):
> 3
The factorial of 3 is 6.

Enter a non-negative integer (or 0 to quit):
> 6
The factorial of 6 is 720.

Enter a non-negative integer (or 0 to quit):
> 10
The factorial of 10 is 3628800.

Enter a non-negative integer (or 0 to quit):
> 0
Bye.
```