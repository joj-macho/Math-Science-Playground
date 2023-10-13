# Perfect Number Checker

## Description

Perfect numbers are positive integers that are equal to the sum of their proper divisors. In other words, the sum of the divisors of a perfect number, excluding the number itself, is equal to the number. For example, the number 6 is a perfect number because the sum of its divisors ($1 + 2 + 3 = 6$) is equal to 6. The number 28 is a perfect number because the sum of its divisors ($1+2+4+7+14 = 28)$ is equal to 28.

You can read more about Perfect numbers on [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/PerfectNumber.html)

This program, Perfect Number Checker, is a Python program that allows users to check if a number is perfect and generate perfect numbers within a range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is perfect, list perfect numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_perfect` function is called. If the user chooses option 2, the `generate_perfect_numbers` function is called. If the user chooses option 3 the program terminates.

- To check if a number is perfect, the program calls the `is_perfect` function. This function takes a number `n` and calculates the sum of its proper divisors using the `get_divisors` function. It then compares the sum of divisors with the original number `n` and returns `True` if they are equal, indicating that the number is perfect. Otherwise, it returns `False`.

- The `get_divisors` function takes a number `n` and returns a list of its proper divisors. It iterates from 1 to `n - 1` and checks if `n` is divisible by each number. If it is, the number is added to the `divisors` list.

- To generate perfect numbers within a range, the program calls the `generate_perfect_numbers(start, end)` function. This function iterates over each number in the range and checks if it is perfect using the `is_perfect` function. If a number is perfect, it is added to the `perfect_numbers` list.


## Program Input & Output

When you run the program, `perfect_numbers.py`, the output will look like this;

```
Perfect Number Checker and Generator

Choose an option:
1. Check if a number is perfect
2. List perfect numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Perfect Number: 42
42 is not a perfect number.

Choose an option:
1. Check if a number is perfect
2. List perfect numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Perfect Number: 496
496 is a perfect number.

Choose an option:
1. Check if a number is perfect
2. List perfect numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 1
Enter an upper limit: 10000
Perfect numbers within the range [1, 10000]: [6, 28, 496, 8128]

Choose an option:
1. Check if a number is perfect
2. List perfect numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```