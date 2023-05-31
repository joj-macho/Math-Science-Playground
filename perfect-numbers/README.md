# Perfect Number Checker

## Description

Perfect numbers are positive integers that are equal to the sum of their proper divisors. In other words, the sum of the divisors of a perfect number, excluding the number itself, is equal to the number. For example, the number 6 is a perfect number because the sum of its divisors (1 + 2 + 3 = 6) is equal to 6.

This program, Perfect Number Checker, is a Python program that allows users to check if a number is perfect and list perfect numbers within a range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is perfect, list perfect numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_perfect_number` function is called. If the user chooses option 2, the `list_perfect_numbers` function is called. If the user chooses option 3 or enters 'q', the program terminates.

- To check if a number is perfect, the program calls the `check_perfect_number` function. This function prompts the user to enter a number and validates the input. The program then checks if the number is perfect using the `is_perfect` function.

- The `is_perfect` function takes a number `n` and calculates the sum of its proper divisors using the `get_divisors` function. It then compares the sum of divisors with the original number `n` and returns `True` if they are equal, indicating that the number is perfect. Otherwise, it returns `False`.

- The `get_divisors` function takes a number `n` and returns a list of its proper divisors. It iterates from 1 to `n - 1` and checks if `n` is divisible by each number. If it is, the number is added to the `divisors` list.

- To list perfect numbers within a range, the program calls the `list_perfect_numbers` function. This function prompts the user to enter the starting and ending numbers of the range and validates the input. The program then iterates over each number in the range and checks if it is perfect using the `is_perfect` function. If a number is perfect, it is added to the `perfect_numbers` list.

- After checking or listing perfect numbers, the program displays the result to the user. If the number is perfect, it indicates that the number is perfect. If listing perfect numbers, it displays the list of perfect numbers within the specified range.

## Program Input & Output

When you run the program, `perfect_numbers.py`, the output will look like this;

```

Perfect Number Checker

1. Check if a number is perfect
2. List perfect numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 1
Enter the ending number: 500
Perfect numbers within the range (1, 500):
[6, 28, 496]

1. Check if a number is perfect
2. List perfect numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 1
Enter the ending number: 20
Perfect numbers within the range (1, 20):
[6]

1. Check if a number is perfect
2. List perfect numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 5
5 is not a perfect number.

1. Check if a number is perfect
2. List perfect numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```