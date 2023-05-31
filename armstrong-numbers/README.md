# Armstrong Number Checker

## Description

Armstrong numbers, also known as narcissistic numbers, are positive integers that are equal to the sum of their own digits raised to the power of the number of digits. For example, the number 153 is an Armstrong number because $1^3 + 5^3 + 3^3 = 153$.

This program, Armstrong Number Checker, is a Python program that provides functionality to check if a number is an Armstrong number and to list all Armstrong numbers within a given range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is an Armstrong number, list Armstrong numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_armstrong_number` function is called. If the user chooses option 2, the `list_armstrong_numbers` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To check if a number is an Armstrong number, the program calls the `check_armstrong_number` function. This function prompts the user to enter a number and validates the input. The program then utilizes the `is_armstrong` function to determine if the number is an Armstrong number and displays the result accordingly.

- When the user chooses to list Armstrong numbers within a range, the program calls the `list_armstrong_numbers` function. This function prompts the user to enter a starting and ending number, validates the input, and iterates over each number in the range. For each number, the program checks if it is an Armstrong number using the `is_armstrong` function. If it is, the number is added to a list of Armstrong numbers. Finally, the program displays the list of Armstrong numbers found within the specified range.

- The `is_armstrong` function checks if a number `n` is an Armstrong number. It first converts the number to a string to facilitate digit extraction. It then determines the number of digits by getting the length of the string. Next, it calculates the sum of each digit raised to the power of the number of digits and stores it in the variable `sum_of_digits`. Finally, it compares `n` with `sum_of_digits` and returns `True` if they are equal, indicating that `n` is an Armstrong number.


## Program Input & Output

When you run the program, `armstrong_numbers.py`, the output will look like this;

```

Armstrong Number Checker

1. Check if a number is an Armstrong number
2. List Armstrong numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 9
9 is an Armstrong number.

1. Check if a number is an Armstrong number
2. List Armstrong numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 10
Enter the ending number: 25
No Armstrong numbers within the range (10, 25).

1. Check if a number is an Armstrong number
2. List Armstrong numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 0
Enter the ending number: 100
Armstrong numbers within the range (0, 100):
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

1. Check if a number is an Armstrong number
2. List Armstrong numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```