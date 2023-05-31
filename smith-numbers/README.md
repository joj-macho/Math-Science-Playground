# Smith Number Checker

## Description

Smith numbers are composite numbers that have a unique property. The sum of their digits is equal to the sum of the digits of their prime factors. For example, the number 22 is a Smith number because its prime factors are 2 and 11, and the sum of its digits (2 + 2 = 4) is equal to the sum of the digits of its prime factors (2 + 1 + 1 = 4).

This program, Smith Number Checker, is a Python program that allows users to check if a number is a Smith number.

## How it Works

- The program starts by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is a Smith number or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses an if-elif-else statement to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_smith_number` function is called. If the user chooses option 2 or enters "q" to quit, the program terminates.

- To check if a number is a Smith number, the program calls the `check_smith_number` function. This function prompts the user to enter a number and validates the input. The program then uses the `is_smith_number` function to determine if the number is a Smith number and displays the result accordingly.

- The `is_smith_number` function checks if a number `n` is a Smith number. It calls the `get_prime_factors` function to obtain the prime factors of `n` and the `get_digit_sum` function to calculate the sum of the digits of `n`. It then compares the sum of the prime factors with the digit sum and returns `True` if they are equal, indicating that the number is a Smith number.

- The `get_prime_factors` function takes a number `n` as input and returns a list of its prime factors. It iteratively divides `n` by prime numbers starting from 2 until `n` is no longer divisible by the current prime number. The prime factors are appended to the `factors` list.

- The `get_digit_sum` function takes a number `n` as input and calculates the sum of its digits. It iteratively extracts the last digit of `n`, adds it to the `digit_sum`, and updates `n` by removing the last digit. This process continues until `n` becomes 0.


## Program Input & Output

When you run the program, `smith_numbers.py`, the output will look like this;

```

Smith Number Checker

1. Check if a number is a Smith number
2. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 25
25 is not a Smith number.

1. Check if a number is a Smith number
2. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 5
5 is a Smith number.

1. Check if a number is a Smith number
2. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```