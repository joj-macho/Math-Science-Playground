# Mersenne Numbers

## Description

Mersenne numbers are positive integers that are one less than a power of two. In other words, they can be represented as $2^n - 1$, where $n$ is a positive integer. For example, the number 7 is a Mersenne number because it can be expressed as $2^3 - 1$.

This program, Mersenne Number Generator, is a Python program that allows users to generate Mersenne numbers.


## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: generate Mersenne numbers or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `generate_mersenne_numbers` function is called. If the user chooses option 2 or enters 'q', the program terminates.

- To generate Mersenne numbers, the program calls the `generate_mersenne_numbers` function. This function prompts the user to enter the number of Mersenne numbers to generate and validates the input. The program then generates the Mersenne numbers using a loop.

- The loop starts with a count of 0 and an exponent of 1. It continues until the count reaches the specified number of Mersenne numbers to generate. In each iteration, it calculates a Mersenne number using the formula 2^exponent - 1.

- To determine if a Mersenne number is valid, the program uses the `is_prime` function. It checks if both the exponent and the Mersenne number itself are prime numbers. If they are, the Mersenne number is considered valid and added to the list of generated Mersenne numbers. After generating the Mersenne numbers, the program displays them to the user.

- The `is_prime` function is used to check if a number is prime. It takes a number as input and iterates from 2 to the square root of the number (inclusive). If any number in that range divides the input number without a remainder, the function returns False. Otherwise, it returns True.


## Program Input & Output

When you run the program, `mersenne_numbers.py`, the output will look like this;

```

Mersenne Number Generator

1. Generate Mersenne numbers
2. Enter (q)uit to exit program
Enter your choice:
> 1
Enter the number of Mersenne numbers to generate: 7
Generated Mersenne numbers: [3, 7, 31, 127, 8191, 131071, 524287]

1. Generate Mersenne numbers
2. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```