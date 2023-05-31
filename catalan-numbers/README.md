# Catalan Number Checker
## Description

Catalan numbers are a sequence of natural numbers that occur in various counting problems, often involving nested parentheses. They can be calculated using a recursive formula. For example, the first few Catalan numbers are 1, 1, 2, 5, 14, 42, ...

This program, Catalan Number Checker, is a Python program that allows users to calculate and check if a given number is a Catalan number.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: compute the nth Catalan number, list Catalan numbers up to a certain limit, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `compute_nth_catalan_number` function is called. If the user chooses option 2, the `list_catalan_numbers` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To compute the nth Catalan number, the program calls the `compute_nth_catalan_number` function. This function prompts the user to enter a value for `n` and validates the input. The program then calls the `calculate_catalan_number` function to calculate the nth Catalan number and displays the result.

- When the user chooses to list Catalan numbers up to a certain limit, the program calls the `list_catalan_numbers` function. This function prompts the user to enter a limit and validates the input. The program then iterates over each number from 0 to the specified limit and calls the `calculate_catalan_number` function to calculate the Catalan number for each value of `n`. The calculated Catalan numbers are stored in a list and displayed.

- The `calculate_catalan_number` function is a recursive function that calculates the nth Catalan number using the recursive formula. If the value of `n` is 0, the function returns 1. Otherwise, it iterates over each value from 0 to `n - 1` and recursively calls itself to calculate the Catalan number for each subproblem. The calculated subproblem results are multiplied together and summed up to obtain the final Catalan number for `n`, which is then returned.

## Program Input & Output

When you run the program, `catalan.py`, the output will look like this;

```

Catalan Numbers

1. Compute the nth Catalan number
2. List Catalan numbers up to a certain limit
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the limit: 10
Catalan numbers up to the limit: [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]

1. Compute the nth Catalan number
2. List Catalan numbers up to a certain limit
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter the value of n:
> 8
The 8th Catalan number is: 1430

1. Compute the nth Catalan number
2. List Catalan numbers up to a certain limit
3. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```