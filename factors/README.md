# Factors of a Number

## Description

This folder contains two Python programs, `is_factor` and `number_factors`, that handle factor-related computations for integers.

<ol>
  <li><p><strong>is_factor Program:</strong> The <code>is_factor</code> program provides a function <code>is_factor(factor, number)</code> to check if a given number is a factor of another number.</p></li>
  <li><p><strong>number_factors Program:</strong> The <code>number_factors</code> program offers a function <code>find_factors(number)</code> to determine all the factors of a given number.</p></li>
</ol>

## How it Works

- In both programs, there is a main function that is defined. It prompts the user for input, calls the respective function (`is_factor` or `find_factors`), and displays the result to the user.

1. The `is_factor.py` Program:
- The `is_factor` program defines a function `is_factor(factor, number)` that checks if factor is a factor of number. Here's how it works:
    - The `is_factor` function takes two integer parameters: `factor` (the potential factor) and `number` (the number to be checked for divisibility) and returns a boolean value (`True` if `factor` is a factor of `number`, and `False` otherwise).
    - The function checks if `number` is divisible by `factor` using the modulo operator (`%`). If the remainder of `number` divided by `factor` is zero, it means `factor` is a factor of `number`.

2. The `number_factors.py` Program:
- The `number_factors` program defines a function `find_factors(number)` that finds the factors of a given number. Here's how it works:
    - The function takes an integer parameter `number` for which to find the factors.
    - The function initializes an empty list `factors` to store the factors. Then uses a `for` loop to iterate from 1 to `number + 1`. For each iteration, it checks if `number` is divisible by the current iteration value. If it is, the current iteration value is a factor of `number`, so it is appended to the `factors` list.
    - The function returns the `factors` list containing all the factors of the given number.

## Program Input & Output

When you run the program, `is_factor.py`, the output will look like this;

```
Factor Checker

Enter the potential factor: 4
Enter the number to be checked: 48
4 is a factor of 48: True
sh-5.1$ /usr/bin/python3 ".../factors/is_factor.py"

Factor Checker

Enter the potential factor: 3
Enter the number to be checked: 198
3 is a factor of 198: True
sh-5.1$ /usr/bin/python3 ".../factors/is_factor.py"

Factor Checker

Enter the potential factor: 7
Enter the number to be checked: 15
7 is a factor of 15: False
```

When you run the program, `number_factors.py`, the output will look like this;

```
Factor Finder

Enter an integer to find its factors: 158
The factors of 158 are: [1, 2, 79, 158]
sh-5.1$ /usr/bin/python3 ".../factors/number_factors.py"

Factor Finder

Enter an integer to find its factors: 42
The factors of 42 are: [1, 2, 3, 6, 7, 14, 21, 42]
sh-5.1$ /usr/bin/python3 ".../factors/number_factors.py"

Factor Finder

Enter an integer to find its factors: 12345
The factors of 12345 are: [1, 3, 5, 15, 823, 2469, 4115, 12345]
```
