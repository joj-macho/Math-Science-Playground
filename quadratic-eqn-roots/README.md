# Quadratic Equation Solver

## Description

The Quadratic Equation Solver is a Python program that calculates the roots of a quadratic equation. It's designed to find the real or complex solutions to equations in the form of $ax^2 + bx + c = 0$ where $a$, $b$, and $c$ are coefficients provided by the user.

The program uses the quadratic formula to solve for the roots of a quadratic equation. The quadratic formula is expressed as follows:
$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
Where
- $x_{1,2}$ represents the roots
- $a$, $b$, and $c$ are coefficients
- $b^2 - 4ac$ is the discriminant. 

If the discriminant ($b^2 - 4ac$) is greater than 0, it implies that there are two real roots. If it's equal to 0, it means there is one real root (repeated), and if it's less than 0, there are two complex roots.

## How it Works

- The main function begins by prompting the user to enter the coefficients `a`, `b`, and `c`. It ensures that 'a' is a non-zero value, as it's a requirement for a quadratic equation. Then calculates and displays the roots.

- The `calculate_roots` function calculates the roots using the quadratic formula. If the discriminant is greater than 0, it finds two real roots. If it's equal to 0, it calculates one real root (repeated). If the discriminant is less than 0, it uses complex numbers to find two complex roots.


## Program Input & Output

When you run the program, `quadratic_roots.py`, the output will look like this;

```

Quadratic Equation Solver

Enter a: 1
Enter b: 0
Enter c: -9

Two roots (real or complex):
Root 1: 3.0
Root 2: -3.0

.
.
.

Enter a: 5
Enter b: 2
Enter c: 9

Two roots (real or complex):
Root 1: (-0.2+1.3266499161421599j)
Root 2: (-0.2-1.3266499161421599j)

.
.
.

Enter a: 0
a must be a non-zero value.
Enter a: 1
Enter b: -9
Enter c: 0

Two roots (real or complex):
Root 1: 9.0
Root 2: 0.0
```