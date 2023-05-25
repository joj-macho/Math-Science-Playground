# The Collatz Sequence Generator

## Description

The Collatz Sequence is a sequence of numbers that starts with any positive integer n, and each subsequent number in the sequence is obtained by applying the following rules:
- If the current number is even, divide it by 2 (i.e. $n = \frac{n}{2}$)
- If the current number is odd, multiply it by 3 and add 1 (i.e. $n =3n + 1$).
- The sequence ends when the current number is 1.

This program implements the Collatz Sequence for a user-specified integer.


## How it Works

- The program begins by importing the `sys` (used to exit the program using `sys.exit()` when the user chooses to quit.) and the `time` (used for introducing a small delay between each number in the Collatz sequence using `time.sleep()`) module.

- The program calls the `main()` function, which begins by prompting the user to enter a number greater than 0 or 'q' to quit. If the user enters 'q', the program terminates with a goodbye message. If the user enters an invalid input, the program prints an error message and prompts the user to enter a valid integer greater than 0.

- Once a valid input is received, the program converts the input to an integer and starts the Collatz sequence. The sequence starts with the input value and iteratively applies the rules listed in the program description (i.e. #1 - If the current number is even, divide it by 2. #2 - If the current number is odd, multiply it by 3 and add 1.) 

- The program continues the sequence until the current number is 1. During each iteration, the program prints the current number separated by commas. A sleep of 0.1 seconds is added between each number to allow the user to follow the sequence.


## Program Input & Output

When you run `collatz.py`, the output will look like this;

```
The Collatz Sequence.

Enter a number greater than 0 or (q)uit to exit.
> 25

Collatz Sequence starting from 25:
25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
```
