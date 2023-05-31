# Abundant Numbers

## Description

Abundant numbers are positive integers that have the intriguing property of being smaller than the sum of their proper divisors. This program, called the "Abundant Number Checker," is implemented in Python and allows users to perform various operations related to abundant numbers.

## How it Works

- The program starts by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is abundant, list abundant numbers within a range, display divisors of a number, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses a series of if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_abundant_number` function is called. If the user chooses option 2, the `list_abundant_numbers` function is called. If the user chooses option 3, the `display_divisors` function is called. If the user chooses option 4 or enters "q" to quit, the program terminates.

- To check if a number is abundant, the program calls the `check_abundant_number` function. This function prompts the user to enter a number and validates the input. The program then utilizes the `is_abundant` function to determine if the number is abundant and displays the result accordingly.

- When the user chooses to list abundant numbers within a range, the program calls the `list_abundant_numbers` function. This function prompts the user to enter a starting and ending number, validates the input, and iterates over each number in the range. For each number, the program checks if it is abundant using the `is_abundant` function. If it is, the number is added to a list of abundant numbers. Finally, the program displays the list of abundant numbers found within the specified range.

- To display the divisors of a number, the program utilizes the `display_divisors` function. This function prompts the user to enter a number, validates the input, and calls the `get_divisors` function to calculate the divisors of the number. The program then displays the list of divisors.

- The `get_divisors` function takes a number `n` as input and calculates its divisors. It iterates from 1 to the square root of `n` and checks if `n` is divisible by each number. If it is, the number and its quotient are added to the `divisors` list. The list of divisors is returned.

- The `is_abundant` function checks if a number `n` is abundant. It calls the `get_divisors` function to calculate the divisors of `n`, sums them, subtracts `n`, and checks if the sum is greater than `n`. The function returns `True` if the number is abundant and `False` otherwise.



## Program Input & Output

When you run the program, `abundant_numbers.py`, the output will look like this;

```

Abundant Number Checker

1. Check if a number is abundant
2. List abundant numbers within a range
3. Display divisors of a number
4. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 0
Enter the ending number: 100
Abundant numbers within the range (0, 100):
[12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100]

1. Check if a number is abundant
2. List abundant numbers within a range
3. Display divisors of a number
4. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number:
> 2
2 is not an abundant number.

1. Check if a number is abundant
2. List abundant numbers within a range
3. Display divisors of a number
4. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number:
> 42
42 is an abundant number.

1. Check if a number is abundant
2. List abundant numbers within a range
3. Display divisors of a number
4. Enter (q)uit to exit program
Enter your choice:
> 3
Enter a number:
> 42
Divisors of 42: [1, 2, 3, 6, 7, 14, 21, 42]

1. Check if a number is abundant
2. List abundant numbers within a range
3. Display divisors of a number
4. Enter (q)uit to exit program
Enter your choice:
> 4
Bye.
```