# Greatest Common Divisor (GCD) and Least Common Multiple (LCM) Calculator

## Description

The GCD (Greatest Common Divisor) and LCM (Least Common Multiple) are fundamental concepts in number theory and play a crucial role in various mathematical calculations. The GCD is the largest positive integer that divides two or more numbers without leaving a remainder, while the LCM is the smallest positive integer that is divisible by two or more numbers. Example; GCD of 12 and 18: The common divisors of 12 and 18 are 1, 2, 3, and 6. The largest among them is 6, so the GCD of 12 and 18 is 6. LCM of 12 and 18: The multiples of 12 are 12, 24, 36, 48, 60, ... and the multiples of 18 are 18, 36, 54, 72, 90, .... The smallest common multiple among them is 36, so the LCM of 12 and 18 is 36.

This program, the GCD and LCM Calculator, is a Python program that allows users to calculate the GCD and LCM of two or more numbers.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: compute GCD and LCM of two numbers or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `compute_gcd_lcm` function is called. If the user chooses option 2, the program terminates.

- To compute the GCD and LCM, the program calls the `compute_gcd_lcm` function. This function prompts the user to enter two numbers and validates the input. The program then calculates the GCD and LCM using the `find_gcd` and `find_lcm` functions.

- The `find_gcd` function implements the Euclidean algorithm to find the GCD of two numbers. It repeatedly divides the larger number by the smaller number and updates the values until the remainder becomes zero. The final non-zero remainder is the GCD.

- The `find_lcm` function calculates the LCM of two numbers by dividing their product by the GCD. It uses the `find_gcd` function to obtain the GCD of the two numbers.

- Once the GCD and LCM are computed, the program displays them to the user.


## Program Input & Output

When you run the program, `gcd_lcm.py`, the output will look like this;

```

GCD and LCM Calculator

1. Compute GCD and LCM of two numbers
2. Quit Program
Enter your choice:
> 1
Enter the first number: 2
Enter the second number: 42
GCD of 2 and 42: 2

LCM of 2 and 42: 42

1. Compute GCD and LCM of two numbers
2. Quit Program
Enter your choice:
> 9
Invalid choice. Please enter a valid option.
1. Compute GCD and LCM of two numbers
2. Quit Program
Enter your choice:
> 1
Enter the first number: 9
Enter the second number: 45
GCD of 9 and 45: 9

LCM of 9 and 45: 45

1. Compute GCD and LCM of two numbers
2. Quit Program
Enter your choice:
> 2
Bye.
```