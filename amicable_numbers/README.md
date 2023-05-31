# Amicable Number Checker

## Description

Amicable numbers are pairs of positive integers where each number is the sum of the proper divisors of the other number. In other words, the sum of the proper divisors of one number equals the other number, and vice versa. For example, the pair of numbers (220, 284) is amicable because the sum of the proper divisors of 220 is 284, and the sum of the proper divisors of 284 is 220. That is, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110, with a sum of 284. The proper divisors of 284 are 1, 2, 4, 71, and 142, with a sum of 220. Since the sums of the proper divisors for each number match, the pair (220, 284) is considered amicable.

This program, Amicable Number Checker, is a Python program that allows users to check if a pair of numbers is amicable or find amicable numbers within a given range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is amicable, list amicable numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_amicable_number` function is called. If the user chooses option 2, the `list_amicable_numbers` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To check if a number is amicable, the program calls the `check_amicable_number` function. This function prompts the user to enter a number and validates the input. The program then utilizes the `is_amicable` function to determine if the number is amicable and displays the result accordingly.

- When the user chooses to list amicable numbers within a range, the program calls the `list_amicable_numbers` function. This function prompts the user to enter a starting and ending number, validates the input, and iterates over each number in the range. For each number, the program checks if it is amicable using the `is_amicable` function. If it is, the number is added to a list of amicable numbers. Finally, the program displays the list of amicable numbers found within the specified range.

- The `is_amicable` function checks if a number `n` is amicable. It calls the `get_divisors` function to calculate the sum of the proper divisors of `n`, which is stored in `sum_divisors_a`. Then it calculates the sum of the proper divisors of `sum_divisors_a`, stored in `sum_divisors_b`. If `n` is not equal to `sum_divisors_a` and `n` is equal to `sum_divisors_b`, the number is considered amicable, and the function returns `True`. Otherwise, it returns `False`.

- The `get_divisors` function takes a number `n` as input and calculates its proper divisors. It iterates from 1 to `n-1` and checks if `n` is divisible by each number. If it is, the number is a proper divisor and is added to the list of divisors. The list of divisors is returned.

## Program Input & Output

When you run the program, `amicable_numbers.py`, the output will look like this;

```

Amicable Number Checker

1. Check if a number is amicable
2. List amicable numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 0
Enter the ending number: 5000
Amicable numbers within the range (0, 5000):
[220, 284, 1184, 1210, 2620, 2924]

1. Check if a number is amicable
2. List amicable numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 
Invalid input. Please enter a valid integer.
Enter a number: 284
284 is an amicable number.

1. Check if a number is amicable
2. List amicable numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 35
Invalid choice. Please enter a valid option.
1. Check if a number is amicable
2. List amicable numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```