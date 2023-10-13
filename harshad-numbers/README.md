# Harshad Number Checker

## Description

Harshad numbers, also known as Niven numbers, are positive integers that are divisible by the sum of their digits. In other words, a number is considered Harshad if it can be evenly divided by the sum of its individual digits.

Let $n$ be a positive integer, and let $d_1,d_2, \ldots, d_k$​ be the individual digits of $n$. Then, $n$ is a Harshad number if and only if:
$$n \, \text{mod} \,(d_1 + d_2 + \dots + d_k) = 0$$


For example, consider $n=18$. The sum of its digits is $1 + 8 = 9$. We can check if $n=18$ is a Harshad number as follows:
$$18 \, \text{mod} \,9 = 0$$
That is, $n=1$ is a Harshad number since the sum of its digits, $9$, divides $n=18$ evenly. Similarly, 21 is a Harshad number because it is divisible by the sum of its digits, i.e. $21 \, mod \, (2+1) = 0$

You can read more about Harshad numbers on [Wikipedia](https://en.wikipedia.org/wiki/Harshad_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/HarshadNumber.html)

This program, Harshad Number Checker, is a Python program that allows users to check if a number is a Harshad number or generate Harshad numbers within a specified range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is Harshad, generate Harshad numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_harshad` function is called. If the user chooses option 2, the `generate_harshad_numbers` function is called. If the user chooses option 3 the program terminates.

- To check if a number is Harshad, the program calls the `is_harshad(n)` function. This function checks if a number is Harshad by calculating the sum of its digits. It converts the number to a string, iterates over each digit, converts it back to an integer, and calculates the sum of the digits. If the number is divisible by the sum of its digits without a remainder, it is a Harshad number.

- To generate Harshad numbers within a range, the program calls the `generate_harshad_numbers(start, end)` function. This function iterates over the range from the starting number to the ending number (inclusive) and checks if each number is a Harshad number using the `is_harshad` function. If a number is a Harshad number, it is added to a list.


## Program Input & Output

When you run the program, `harshad_numbers.py`, the output will look like this;

```

Harshad Number Checker and Generator

Choose an option:
1. Check if a number is Harshad
2. Generate Harshad numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Harshad Number: 15
15 is not a Harshad number.

Choose an option:
1. Check if a number is Harshad
2. Generate Harshad numbers within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Harshad Number: 18
18 is a Harshad number.

Choose an option:
1. Check if a number is Harshad
2. Generate Harshad numbers within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 1
Enter an upper limit: 25
Harshad numbers within the range (1, 25): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24].

Choose an option:
1. Check if a number is Harshad
2. Generate Harshad numbers within a range
3. Exit program
Enter your choice: 3
Bye.
```