# Composite Number Checker

## Description

Composite numbers are positive integers that have more than two distinct positive divisors. In other words, they are non-prime numbers. For example, the number 12 is composite because it has divisors 1, 2, 3, 4, 6, and 12.

This program, Composite Number Checker, is a Python program that allows users to check if a number is composite or not.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly prompt the user for input and check if the entered number is composite. The loop continues until the user enters 0 to quit.

- The `get_valid_input` function is called to obtain a valid input from the user. This function prompts the user to enter a positive integer or 0 to exit. It validates the input, ensuring that the entered value is a positive integer or 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The `is_composite` function is called to check if the entered number is composite. This function takes a number `n` as input and performs the composite check. If `n` is less than 4, it is considered a prime number and therefore not composite. Otherwise, the function iterates from 2 to the square root of `n` and checks if `n` is divisible by any number within that range. If a divisor is found, the function returns `True`, indicating that the number is composite. If no divisors are found, the function returns `False`, indicating that the number is not composite.

- Based on the result returned by the `is_composite` function, the `main` function displays an appropriate message to inform the user whether the entered number is composite or not.

## Program Input & Output

When you run the program, `composite_numbers.py`, the output will look like this;

```

Composite Number Checker

Enter a positive integer (or 0 to exit):
> 15
15 is a composite number.

Enter a positive integer (or 0 to exit):
> 24
24 is a composite number.

Enter a positive integer (or 0 to exit):
> 42
42 is a composite number.

Enter a positive integer (or 0 to exit):
> 2
2 is not a composite number.

Enter a positive integer (or 0 to exit):
> 0
Bye.
```