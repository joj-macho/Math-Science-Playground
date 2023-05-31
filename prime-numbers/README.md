# Prime Number Checker

## Description

Prime numbers are positive integers greater than 1 that have no divisors other than 1 and themselves. In other words, prime numbers are only divisible by 1 and the number itself. For example, the number 7 is a prime number because its only divisors are 1 and 7.

This program, Prime Number Checker, is a Python program that allows users to check if a number is prime and list prime numbers within a range.

## How it Works

- The program begins by defining a `main` function. Inside the `main` function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is prime, list prime numbers within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses a series of if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `check_prime_number` function is called. If the user chooses option 2, the `list_prime_numbers` function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To check if a number is prime, the program calls the `check_prime_number` function. This function prompts the user to enter a number and validates the input. The program then utilizes the `is_prime` function to determine if the number is prime and displays the result accordingly.

- When the user chooses to list prime numbers within a range, the program calls the `list_prime_numbers` function. This function prompts the user to enter a starting and ending number, validates the input, and iterates over each number in the range. For each number, the program checks if it is prime using the `is_prime` function. If it is, the number is added to a list of prime numbers. Finally, the program displays the list of prime numbers found within the specified range.

- The `is_prime` function takes a number `n` as input and checks if it is prime. The function first checks if the number is less than 2, in which case it returns `False` since prime numbers must be greater than 1. Then, it iterates from 2 to the square root of `n` and checks if `n` is divisible by any of these numbers. If a divisor is found, the function immediately returns `False`. If no divisors are found, the function returns `True`, indicating that the number is prime.



## Program Input & Output

When you run the program, `prime_numbers.py`, the output will look like this;

```

Prime Number Generator

1. Check if a number is prime
2. List prime numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 2
2 is a prime number.

1. Check if a number is prime
2. List prime numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter a number: 99
99 is not a prime number.

1. Check if a number is prime
2. List prime numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the starting number: 1
Enter the ending number: 100
Prime numbers within the range (1, 100):
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].

1. Check if a number is prime
2. List prime numbers within a range
3. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```