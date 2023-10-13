# Armstrong Number Checker

## Description

An Armstrong number (also known as a narcissistic number, pluperfect number, or pluperfect digital invariant) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. In other words, it's a number for which the sum of the nth power of its digits is equal to the number itself. 
Consider a number $n$ with $d$ digits $d_1,d_2, \ldots,d_d​$​. The sum of the $d$-th power of its digits can be written as:
$$d_{1}^d + d_{2}^d + \dots + d_{d}^d$$

The number $n$ is an Armstrong number if this sum equals $n$:
$$d_{1}^d + d_{2}^d + \dots + d_{d}^d = n$$

where $d_1,d_2, \ldots,d_d​$ are the digits of $n$, and $d$ is the number of digits in $n$

For example, the number $n=153$ has three digits, 1, 5, and 3. The sum of the the ($d=3$)-power of its digits is:
$$1^3 + 5^3 + 3^3 = 153$$

Hence the number $n=153$ is an Armstrong number. The first few Armstrong numbers are given by: $1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, \dots$

You can read more about Armstrong numbers on [Wikipedia](https://en.wikipedia.org/wiki/Narcissistic_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/NarcissisticNumber.html)


This program, Armstrong Number Checker, allows users to check if a given number is an Armstrong number or generate Armstrong numbers within a specified range.

## How it Works

- The program starts by defining a `main` function, which uses a while loop to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is an Armstrong number, generate Armstrong numbers within a range, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `is_armstrong` function is called. If the user chooses option 2, the `generate_armstrong_numbers` function is called. If the user chooses option 3, the loop breaks and the program ends.

- To check if a number is an Armstrong number, the program calls the `is_armstrong(n)` function. This function checks if a number `n` is an Armstrong number. It first converts the number to a string to facilitate digit extraction. It then determines the number of digits by getting the length of the string. Next, it calculates the sum of each digit raised to the power of the number of digits and stores it in the variable `sum_of_digits`. Finally, it compares `n` with `sum_of_digits` and returns `True` if they are equal, indicating that `n` is an Armstrong number.

- When the user chooses to generate Armstrong numbers within a range, the program calls the `generate_armstrong_numbers(start, end)` function. This function iterates over each number in the range. For each number, the program checks if it is an Armstrong number using the `is_armstrong` function. If it is, the number is added to a list of Armstrong numbers. Finally, the program displays the list of Armstrong numbers found within the specified range.



## Program Input & Output

When you run the program, `armstrong_numbers.py`, the output will look like this;

```

Armstrong Number Checker

Choose an option:
1. Check if a number is an Armstrong number
2. Generate Armstrong numbers within a range
3. Enter (q)uit to exit program
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is an Armstrong number: 25
25 is not an Armstrong number.

Choose an option:
1. Check if a number is an Armstrong number
2. Generate Armstrong numbers within a range
3. Enter (q)uit to exit program
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is an Armstrong number: 153
153 is an Armstrong number.

Choose an option:
1. Check if a number is an Armstrong number
2. Generate Armstrong numbers within a range
3. Enter (q)uit to exit program
3. Exit program
Enter your choice: 2
Enter the lower limit: 0
Enter an upper limit: 500
Armstrong numbers within the range (0, 500): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

Choose an option:
1. Check if a number is an Armstrong number
2. Generate Armstrong numbers within a range
3. Enter (q)uit to exit program
3. Exit program
Enter your choice: 2
Enter the lower limit: 1000
Enter an upper limit: 10000
Armstrong numbers within the range (1000, 10000): [1634, 8208, 9474]

Choose an option:
1. Check if a number is an Armstrong number
2. Generate Armstrong numbers within a range
3. Enter (q)uit to exit program
3. Exit program
Enter your choice: 3
Bye.
```