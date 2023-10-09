# Catalan Number Checker

## Description

Catalan numbers are a sequence of natural numbers that find applications in various counting problems, often involving nested parentheses. They have diverse applications in combinatorial mathematics, including in binary trees, expressions, and more. The nth Catalan number can be calculated using the following formula:
$$C_n = \frac{1}{n+1} \binom{2n}{n} = \frac{(2n)!}{(n+1)!n!}$$

where $\binom{n}{k}$ is a binomial coefficent, $n!$ is a factorial. The first few Catalan numbers for $n=1, 2, \dots$ are $1, 1, 2, 5, 14, 42, \ldots$

This program, Catalan Number Checker, is a Python program that allows users to calculate and check if a given number is a Catalan number.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: compute the nth Catalan number, list Catalan numbers up to a certain limit, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `compute_nth_catalan_number` function is called. If the user chooses option 2, the `list_catalan_numbers` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To compute the nth Catalan number, the program calls the `compute_nth_catalan_number` function. This function prompts the user to enter a value for `n` and validates the input. The program then calls the `calculate_catalan_number` function to calculate the nth Catalan number using the given formula. The result is displayed to the user.

- When the user chooses to list Catalan numbers up to a certain limit, the program calls the `list_catalan_numbers` function. This function prompts the user to enter a limit and validates the input. The program then iterates over each number from 0 to the specified limit and calls the `calculate_catalan_number` function to calculate the Catalan number for each value of `n`. The calculated Catalan numbers are stored in a list and displayed.

- The `calculate_catalan_number` function uses a recursive approach to calculate the nth Catalan number using the formula above, i.e. $C_n = \frac{1}{n+1} \binom{2n}{n}$.
    - If $n=0$, the function returns 1, as per the base case of the Catalan numbers: $C_0​=1$.
    - For $n \gt 0$, the function iterates from $0$ to $n-1$. For each $i$ in this range, it recursively calls itself twice: once for $i$ and once for $n-i-1$. This is because, according to the formula, the Catalan numbers involve a summation over values from $0$ to $n-1$.
    - The function sums up the recursive calls, each representing a subproblem in the Catalan number formula. The recursive calls correspond to the binomial coefficients in the formula, which are $\binom{2n}{n}$.
    - The calculated subproblem results are multiplied together and summed up to obtain the final Catalan number for nn using the formula $\frac{1}{n+1} \binom{2n}{n}$

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