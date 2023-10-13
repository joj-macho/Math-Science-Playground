# Abundant Number Checker

## Description

Abundant numbers are positive integers that are smaller than the sum of their proper divisors. In other words, the sum of all the divisors of an abundant number, excluding the number itself, is greater than the number itself. In mathematical terms, an abundant number $n$ satisfies $\sigma(n) \gt 2n$, where $\sigma(n)$ represents the sum of all divisors of $n$. For example, the number $12$ is an abundant number because the sum of its proper divisors ($1 + 2 + 3 + 4 + 6 = 16 \gt 12$. You can read more about abundant numbers on [Wikipedia](https://en.wikipedia.org/wiki/Abundant_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/AbundantNumber.html)

This program, Abundant Number Checker, is a Python program that allows users to check if a given number is an abundant number or generates abundant numbers within a specified range.

## How it Works

- The program starts by defining a `main` function, which uses a while loop to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is abundant, generate abundant numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses a series of if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_abundant` function is called. If the user chooses option 2, the `generate_abundant_numbers` function is called. If the user chooses option 3, the loop breaks and the program ends.

- To check if a number is abundant (Option 1), the program calls the `is_abundant(n)` function. This function checks if a number `n` is abundant. It calls the `get_divisors` function to calculate the divisors of `n`, sums them, subtracts `n`, and checks if the sum is greater than `n`. The function returns `True` if the number is abundant and `False` otherwise.

- The `get_divisors` function takes a number `n` as input and calculates its divisors. It iterates from 1 to the square root of `n` and checks if `n` is divisible by each number. If it is, the number and its quotient are added to the `divisors` list. The list of divisors is returned.

- When the user chooses to generate abundant numbers within a range, the program calls the `generate_abundant_numbers(start, end)` function. This function iterates over each number in the range `start` to `end + 1`. For each number, the program checks if it is abundant using the `is_abundant` function. If it is, the number is added to a list of abundant numbers. 


## Program Input & Output

When you run the program, `abundant_numbers.py`, the output will look like this;

```

Abundant Number Checker and Generator

Choose an option:
1. Check if a number is abundant
2. List abundant numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is abundant:
> 9
9 is not an abundant number...
Sum of divisors of 9: 1 + 3 = 4 < 9

Choose an option:
1. Check if a number is abundant
2. List abundant numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is abundant:
> 50
50 is not an abundant number...
Sum of divisors of 50: 1 + 2 + 5 + 10 + 25 = 43 < 50

Choose an option:
1. Check if a number is abundant
2. List abundant numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is abundant:
> 36
36 is an abundant number...
Sum of divisors of 36: 1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 = 55 > 36

Choose an option:
1. Check if a number is abundant
2. List abundant numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 10
Enter an upper limit: 100
Abundant numbers between [10, 100]: [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100]

Choose an option:
1. Check if a number is abundant
2. List abundant numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```