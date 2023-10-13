# Euler's Totient function Numbers

## Description

This program calculates Euler's Totient function for a given positive integer. Euler's Totient function, also known as Euler's phi function ($\varphi(n)$), counts the number of positive integers less than or equal to a given number $n$ that are coprime (relatively prime) to it.

The formula for Euler's Totient function is as follows:
$$\varphi(n) = n \prod_{p|n} = n \left(1- \frac{1}{p_1} \right) \left(1- \frac{1}{p_2} \right) \cdots \left(1- \frac{1}{p_k} \right)$$
where $p_1, p_2, \dots, p_k$ are distinct prime factors of n.


The first few values of $\varphi(n)$ for $n=1, 2, \ldots$ are: $1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, \ldots$

You can read more about Euler's Totient function on [Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_totient_function) and [Wolfram MathWorld](https://mathworld.wolfram.com/TotientFunction.html)


## How it Works

- The `main` function begins the program by prompting the user for a positive integer and calculates its Euler's Totient function using the `calculate_totient` function.

- The `calculate_totient(n)` function calculates Euler's Totient function for a given number by iteratively finding the prime factors of the number and applying the totient formula. The function does the following
    - Initializes the result with the given number, $n$.
    - Starts with the smallest prime factor, 2.
    - Iterates through prime factors, reducing $n$ and applying the totient formula for each prime factor.
    - If $n$ is still greater than 1 after the loop, it is a prime factor, and the totient formula is applied again.
    - Finally, returns the calculated Euler's Totient function value for the given number.

## Program Input & Output

When you run the program, `euler_totient.py`, the output will look like this;

```
Euler's Totient Function Calculator

Enter a positive integer: 4
The Euler's Totient function value for 4 is: 2

.
.
.

Enter a positive integer: 5
The Euler's Totient function value for 5 is: 4

.
.
.

Enter a positive integer: 9
The Euler's Totient function value for 9 is: 6

.
.
.

Enter a positive integer: 11
The Euler's Totient function value for 11 is: 10
```