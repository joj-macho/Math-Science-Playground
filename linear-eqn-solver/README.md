# Linear Equation Solver

## Description

The Linear Equation Solver is a simple Python program that calculates the root of a linear equation in the form $ax + b = 0$ and provides the solution to the user.


## How it Works

- The main function begins by prompting the user to enter the coefficients `a` and `b` of the linear equation. The function then calls the `linear_equation_solver` function with the provided coefficients 'a' and 'b' as arguments, to solve the linear equation with the coefficients provided.

- The `linear_equation_solver` function calculates the root of the linear equation. Where the following outcomes are possible:
    - If 'a' is 0 and 'b' is 0, the equation has infinite solutions (an identity equation).
    - If 'a' is 0 and 'b' is not 0, the equation is contradictory, and it has no solution. 
    - If 'a' is not 0, the program calculates the root 'x' using the formula $x = - \frac{b}{a}$ and provides the solution to the user.


## Program Input & Output

When you run the program, `linear_solver.py`, the output will look like this;

```

Linear Equation Solver

Enter a: 6
Enter b: -9
Solution: x = 1.5

.
.
.

Enter a: 0
Enter b: 5

No solution (contradictory equation)

.
.
.

Enter a: 0
Enter b: 0

Infinite solutions (identity equation)
```