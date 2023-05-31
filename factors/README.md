# Number Factors Calculator 

## Description

The Number Factors Calculator is a Python program that determines the factors of a given number. Factors are the positive integers that evenly divide a given number without leaving a remainder. For instance, the factors of 12 are 1, 2, 3, 4, 6, and 12. 

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly prompt the user for input and find the factors. The loop continues until the user enters 0 to quit.

- The `get_valid_input` function is called to obtain a valid input from the user. This function prompts the user to enter a positive integer or 0 to quit. It validates the input, ensuring that the entered value is a positive integer or 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The `find_factors` function is called to calculate the factors of the entered number. This function takes a positive integer `n` as input and iterates from 1 to `n`. For each iteration, it checks if `n` is divisible by the current number (`i`) without leaving a remainder. If it is, the current number is considered a factor of `n` and is added to the list of factors.

- Based on the calculated factors, the `main` function displays the result to the user, indicating the factors of the entered number.


## Program Input & Output

When you run the program, `number_factors.py`, the output will look like this;

```

Number Factors Calculator

Enter a positive integer (or 0 to quit):
> 1
The factors of 1 are [1].

Enter a positive integer (or 0 to quit):
> 5
The factors of 5 are [1, 5].

Enter a positive integer (or 0 to quit):
> 15
The factors of 15 are [1, 3, 5, 15].

Enter a positive integer (or 0 to quit):
> 2569896
The factors of 2569896 are [1, 2, 3, 4, 6, 7, 8, 9, 12, 14, 18, 21, 24, 28, 36, 42, 56, 63, 72, 84, 126, 168, 252, 504, 5099, 10198, 15297, 20396, 30594, 35693, 40792, 45891, 61188, 71386, 91782, 107079, 122376, 142772, 183564, 214158, 285544, 321237, 367128, 428316, 642474, 856632, 1284948, 2569896].

Enter a positive integer (or 0 to quit):
> 0
Bye.
```
