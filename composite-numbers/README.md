# Composite Number Checker

## Description

A composite number, $n$, is a positive integers $n \gt 1$ that has more than two distinct positive divisors, i.e. is non-prime number. For example, the number 12 is composite because it has divisors 1, 2, 3, 4, 6, and 12. The first few composite numbers are $4, 6, 8, 9, 10, 12, 14, 15, \dots$. You can read more about composite numbers on [Wikipedia](https://en.wikipedia.org/wiki/Composite_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/CompositeNumber.html)


This program, Composite Number Checker, is a Python program that allows users to check if a number is a composite number and generate composite numbers within a specified range.

## How it Works

- The program starts by defining the `main` function. Inside this function, a while loop is used to display a menu of options for the user and repeatedly prompt the user for input and checks if a number is composite or generate composite numbers within a range.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The `is_composite(n)` function is called to check if the entered number is composite. This function checks if a number `n` is a composite by verifying if it has factors other than 1 and itself. If `n` is less than 4, it is considered a prime number and therefore not composite. Otherwise, this function uses the fact that composite numbers have at least one divisor between 2 and the square root of the number, i.e. the function iterates from 2 to the square root of `n` and checks if `n` is divisible by any number within that range. If a divisor is found, the function returns `True`, indicating that the number is composite. If no divisors are found, the function returns `False`, indicating that the number is not composite.

- The `generate_composite_numbers(start, end)` function is called to generate composite numbers within the specified range `[start, end]` by checking each number in the range. That is, this function calls the `is_composite` function to identify composite numbers within a range, then appends them to a list of composite numbers to be displayed as a result.

## Program Input & Output

When you run the program, `composite_numbers.py`, the output will look like this;

```

Composite Number Checker and Generator

Choose an option:
1. Check if a number is composite
2. Generate composite numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is composite:
> 42
42 is a composite number.

Choose an option:
1. Check if a number is composite
2. Generate composite numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is composite:
> 13
13 is not a composite number.

Choose an option:
1. Check if a number is composite
2. Generate composite numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 10
Enter an upper limit: 100
Composite numbers between [10, 100]: [10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]

Choose an option:
1. Check if a number is composite
2. Generate composite numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```