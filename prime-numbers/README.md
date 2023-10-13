# Prime Number Checker

## Description

A prime number is a positive integer greater than 1 that has exactly two positive divisors: 1 and the number itself. That is, a number $p$ is considered prime if and only if it satisfies the following conditions:
1. $p \gt 1$
2. $p$ has exactly two positive divisors: 1 and $p$ itself.

For example, the number 7 is a prime number because its only divisors are 1 and 7. Some examples of prime numbers include $2, 3, 5, 7, 11, 13, 17, \ldots$

You can read more about Prime numbers on [Wikipedia](https://en.wikipedia.org/wiki/Prime_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/PrimeNumber.html)

This program, Prime Number Checker, is a Python program that allows users to check if a number is prime and list prime numbers within a range.

## How it Works

- The program begins by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is prime, list prime numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses a series of if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_prime` function is called. If the user chooses option 2, the `generate_prime_numbers` function is called. If the user chooses option 3 the program terminates.

- To check if a number is prime, the program calls the `is_prime(n)` function. This function takes a number `n` as input and checks if it is prime. The function first checks if the number is less than 2, in which case it returns `False` since prime numbers must be greater than 1. Then, it iterates from 2 to the square root of `n` and checks if `n` is divisible by any of these numbers. If a divisor is found, the function immediately returns `False`. If no divisors are found, the function returns `True`, indicating that the number is prime.

- When the user chooses to list prime numbers within a range, the program calls the `generate_prime_numbers` function. This function iterates over each number in the range. For each number, the program checks if it is prime using the `is_prime` function. If it is, the number is added to a list of prime numbers.


## Program Input & Output

When you run the program, `prime_numbers.py`, the output will look like this;

```

Prime Number Generator

Choose an option:
1. Check if a number is prime
2. List prime numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Prime Number: 11
11 is a prime number.

Choose an option:
1. Check if a number is prime
2. List prime numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Prime Number: 42
42 is not a prime number.

Choose an option:
1. Check if a number is prime
2. List prime numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 1
Enter an upper limit: 100
Prime numbers within the range (1, 100):
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].

Choose an option:
1. Check if a number is prime
2. List prime numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```