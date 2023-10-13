# Catalan Number Checker

## Description

Catalan numbers are a sequence of natural numbers that find applications in various counting problems, often involving nested parentheses. They have diverse applications in combinatorial mathematics, including in binary trees, expressions, and more. The nth Catalan number can be calculated using the following formula:
$$C_n = \frac{1}{n+1} \binom{2n}{n} = \frac{(2n)!}{(n+1)!n!}$$

where $\binom{n}{k}$ is a binomial coefficent, $n!$ is a factorial. The first few Catalan numbers for $n=1, 2, \dots$ are $1, 1, 2, 5, 14, 42, \ldots$

You can read more about Catalan numbers on [Wikipedia](https://en.wikipedia.org/wiki/Catalan_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/CatalanNumber.html)

This program, Catalan Number Checker, is a Python program that allows users to calculate the nth Catalan number and or generate Catalan numbers within a specified range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: compute the nth Catalan number, Generate Catalan numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `calculate_catalan_number` function is called. If the user chooses option 2, the `generate_catalan_numbers` function is called. If the user chooses option 3, the loop breaks and the program ends.

- To compute the nth Catalan number, the program calls the `calculate_catalan_number(n)` function. The `calculate_catalan_number(n)` function uses a recursive approach to calculate the nth Catalan number using the formula above, i.e. $C_n = \frac{1}{n+1} \binom{2n}{n}$.
    - If $n=0$, the function returns 1, as per the base case of the Catalan numbers: $C_0​=1$.
    - For $n \gt 0$, the function iterates from $0$ to $n-1$. For each $i$ in this range, it recursively calls itself twice: once for $i$ and once for $n-i-1$. This is because, according to the formula, the Catalan numbers involve a summation over values from $0$ to $n-1$.
    - The function sums up the recursive calls, each representing a subproblem in the Catalan number formula. The recursive calls correspond to the binomial coefficients in the formula, which are $\binom{2n}{n}$.
    - The calculated subproblem results are multiplied together and summed up to obtain the final Catalan number for nn using the formula $\frac{1}{n+1} \binom{2n}{n}$

- When the user chooses to generate Catalan numbers within a range, the program calls the `generate_catalan_numbers(start, end)` function. This function initialize a counter `i` to 0 to start calculating Catalan numbers from C_0. Then uses a loop to calculate Catalan numbers using `calculate_catalan_number(i)` and increment `i` in each iteration. For each `i`, the corresponding Catalan number is calculated using the recursive formula in `calculate_catalan_number(i)`, and if the calculated Catalan number is within the specified range, it is added to the `catalan_numbers` list.


## Program Input & Output

When you run the program, `catalan.py`, the output will look like this;

```

Catalan Numbers Calculator and Generator

Choose an option:
1. Compute the nth Catalan number
2. Generate Catalan numbers within a range
3. Exit program
Enter your choice: 1
Enter the nth (positive integer) Catalan number to compute: 5
The 5th Catalan number is: 42

Choose an option:
1. Compute the nth Catalan number
2. Generate Catalan numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 0
Enter an upper limit: 50
Catalan numbers within the range (0, 50): [1, 1, 2, 5, 14, 42]

Choose an option:
1. Compute the nth Catalan number
2. Generate Catalan numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 100
Enter an upper limit: 5000
Catalan numbers within the range (100, 5000): [132, 429, 1430, 4862]

Choose an option:
1. Compute the nth Catalan number
2. Generate Catalan numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```