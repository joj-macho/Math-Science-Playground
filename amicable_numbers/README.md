# Amicable Number Checker

## Description

Amicable numbers are pairs of positive integers where each number is the sum of the proper divisors of the other number. In other words, the sum of the proper divisors of one number equals the other number, and vice versa. For example, the pair of numbers (220, 284) is amicable because the sum of the proper divisors of 220 is 284, and the sum of the proper divisors of 284 is 220. That is, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110, with a sum of 284. The proper divisors of 284 are 1, 2, 4, 71, and 142, with a sum of 220. Since the sums of the proper divisors for each number match, the pair (220, 284) is considered amicable. You can readme more about amicable numbers on [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers)

This program, Amicable Number Checker, is a Python program that allows users to check if a pair of numbers is amicable or find amicable numbers within a given range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is amicable, list amicable pairs within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_amicable_pair` function is called. If the user chooses option 2, the `list_amicable_pairs` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To check if a number is part of an amicable pair, the program calls the `check_amicable_pair` function. This function prompts the user to enter a number and validates the input. The program then utilizes the `find_amicable_pair` function to determine if the number is part of an amicable pair and displays the result accordingly.

- When the user chooses to list amicable pairs within a range, the program calls the `list_amicable_pairs` function. This function prompts the user to enter a starting and ending number, validates the input, and iterates over each number in the range. For each number, the program checks if it is part of an amicable pair using the `find_amicable_pair` function. If it is, the pair is added to a list of amicable pairs. Finally, the program displays the list of amicable pairs found within the specified range.

- The `find_amicable_pair` function finds an amicable pair for a given number. It calculates the sum of the proper divisors for the number and for that sum. If the input number is not equal to the sum of the proper divisors for the number and is equal to the sum of the proper divisors for that sum, the function considers it an amicable pair and returns the pair as (a, b).

- The `get_divisors` function takes a number `n` as input and calculates its proper divisors. It iterates from 1 to `n-1` and checks if `n` is divisible by each number. If it is, the number is a proper divisor and is added to the list of divisors. The list of divisors is returned.

## Program Input & Output

When you run the program, `amicable_numbers.py`, the output will look like this;

```

Amicable Number Checker

1. Check if a number is part of an amicable pair
2. List amicable pairs within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 200
200 is not part of an amicable pair.

1. Check if a number is part of an amicable pair
2. List amicable pairs within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 10744
The amicable pair for 10744 is: (10744, 10856)

1. Check if a number is part of an amicable pair
2. List amicable pairs within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 200
Enter the ending number: 6000
Amicable pairs within the range (200, 6000):
[(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)]

1. Check if a number is part of an amicable pair
2. List amicable pairs within a range
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```