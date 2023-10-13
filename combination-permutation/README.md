# Combination and Permutation Calculator

## Description

The Combination and Permutation Calculator is a Python program that performs calculations related to combinations and permutations. Combinations and permutations are mathematical concepts used to count the number of possible arrangements or selections from a given set of items. The program provides options to calculate combinations (nCr) and permutations (nPr) based on user input values for n and r. It utilizes the factorial function to compute the necessary factorials and applies the formulas for combinations and permutations to produce the desired results.

<strong>Combination (nCr)</strong>: The combination of $n$ objects taken $r$ at a time is denoted as $nCr$, or $C(n,r)$. It represents the number of ways to choose $r$ items from a set of $n$ items, disregarding the order of selection. The formula to calculate $nCr$ is:
$$C(n,r) = \frac{n!}{r!(n-r)!}$$
You can read more about combinations on [Wikipedia](https://en.wikipedia.org/wiki/Combination) and [Wolfram MathWorld](https://mathworld.wolfram.com/Combination.html)

<strong>Permutation (nPr)</strong>: The permutation of $n$ objects taken $r$ at a time is denoted as $nPr$, or $P(n,r)$. It signifies the number of ways to arrange $r$ items from a set of $n$ items, considering the order of selection. The formula to calculate $nPr$ is:
$$P(n,r) = \frac{n!}{(n-r)!}$$
You can read more about permutation on [Wikipedia](https://en.wikipedia.org/wiki/Permutation) and [Wolfram MathWorld](https://mathworld.wolfram.com/Permutation.html)


## How it Works

- The program starts by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: calculate combination (nCr), calculate permutation (nPr), or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses an if-elif-else statement to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `calculate_combination` function is called. If the user chooses option 2, the `calculate_permutation` function is called. If the user chooses option 3, the loop breaks and the program ends.

- To calculate the combination, the program calls the `calculate_combination(n, r)` function. Where n is the total number of objects and r is the number of objects to choose. The function calculates the combination using the formula `factorial(n) // (factorial(r) * factorial(n - r))`.

- To calculate the permutation, the program calls the `calculate_permutation(n, r)` function. Where n is the total number of objects and r is the number of objects to arrange. The function calculates the permutation using the formula `factorial(n) // factorial(n - r)`. 

- The `factorial` function is used to calculate the factorial of a given number. It is a recursive function that returns the factorial of `n`. If `n` is 0, the function returns 1. Otherwise, it multiplies `n` by the factorial of `n - 1` to compute the factorial.


## Program Input & Output

When you run the program, `combination_permutation.py`, the output will look like this;

```

Combination and Permutation Calculator

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 1
Enter the value of n: 2
Enter the value of r: 5
Invalid values. Make sure n >= r >= 0.

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 1
Enter the value of n: 5
Enter the value of r: 2
The combination of 5 choose 2 is 10.

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 2
Enter the value of n: 5
Enter the value of r: 2
The permutation of 5P2 is 20.

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 3
Bye.
```