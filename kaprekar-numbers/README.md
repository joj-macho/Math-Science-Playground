# Kaprekar Number Checker

## Description

Kaprekar numbers are positive integers that, when squared and divided into two parts (left and right), produce a sum equal to the original number.

Let $n$ be a positive integer. $n$ is a Kaprekar number if, when $n^2$ is divided into two parts, the sum of these parts equals the original number $n$:
$$n= \text{left part} + \text{right part}$$
where $\text{left part} + \text{right part} = n^2$


For example, consider the number $n=9$. The square of $9$ is $n^2 = 81$. Now the two parts of $n^2$ are $\text{left part}=8$ and $\text{right part}=1$, and the sum of these two parts is $8 + 1 = 9$ which is the original number $n$. Therefore, $n=9$ is a Kaprekar number.

Here's another example; consider the number $n=703$. The square of $703$ is $n^2 = 494209$. Now the two parts of $n^2$ are $\text{left part}=494$ and $\text{right part}=209$, and the sum of these two parts is $494 + 209 = 703$ which is the original number $n$. Therefore, $n=703$ is a Kaprekar number.


You can read more about Kaprekar numbers on [Wikipedia](https://en.wikipedia.org/wiki/Kaprekar_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/KaprekarNumber.html)

This program, Kaprekar Number Checker, is a Python program that allows users to check if a number is a Kaprekar number or generate Kaprekar numbers within a specified range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is a Kaprekar number, generate Kaprekar numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_kaprekar` function is called. If the user chooses option 2, the `generate_kaprekar_numbers` function is called. If the user chooses option 3, the program terminates.

- To check if a number is a Kaprekar number, the program calls the `is_kaprekar` function. This function checks if a number is a Kaprekar number by squaring it and comparing the sum of its parts to the original number. It calculates the square of the number and determines the number of digits in the square. It then iterates over the range of digits to check if each digit is a divisor of the square. If a digit is a divisor, it calculates the sum of the parts of the square divided by the divisor. If the sum of the parts is equal to the original number, it returns `True`, indicating that the number is a Kaprekar number. Otherwise, it returns `False`.

- To generate Kaprekar numbers within a range, the program calls the `generate_kaprekar_numbers` function. This function iterates over the range from the starting number to the ending number (inclusive) and checks if each number is a Kaprekar number using the `is_kaprekar` function. If a number is a Kaprekar number, it is added to a list.


## Program Input & Output

When you run the program, `kaprekar_numbers.py`, the output will look like this;

```

Kaprekar Number Checker and Generator

Choose an option:
1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Kaprekar Number: 8
8 is not a Kaprekar number.

Choose an option:
1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Kaprekar Number: 9
9 is a Kaprekar number.

Choose an option:
1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 1
Enter an upper limit: 500
Kaprekar numbers within the range: [9, 45, 55, 99, 297].

Choose an option:
1. Check if a number is Kaprekar
2. List Kaprekar numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```