# Prime Factorization

## Description

The Prime Factorization Program is a Python program that performs prime factorization on a given number. Prime factorization involves breaking down a composite number into a product of its prime factors. Prime factors are the prime numbers that divide the given number without leaving a remainder. For instance, the prime factorization of 24 is $2 × 2 × 2 × 3$, as 2 and 3 are the prime factors of 24.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle the user's choice. The user's input is obtained using the `input` function and stored in the `choice` variable.

- The program provides two options to the user: Perform prime factorization of a number. Quit the program. If the user selects option 1, the program calls the `perform_prime_factorization` function. If the user selects option 2 or enters 'q', the program displays "Bye." and breaks out of the loop, terminating the program.

- The `perform_prime_factorization` function prompts the user to enter a number and performs prime factorization on that number. It calls the `prime_factorization` function, passing the entered number as an argument. The function receives a dictionary containing the prime factors as keys and their counts as values.

- The `prime_factorization` function takes a number `n` as an argument and returns a dictionary with prime factors and their counts. It initializes an empty dictionary `factors` to store the prime factors. It starts with the smallest prime factor, which is 2, and repeatedly divides the number by the factor until it is no longer divisible by the factor. If the factor divides the number, it increments its count in the `factors` dictionary. If the factor is not a divisor, it is incremented by 2 if it is already greater than 2, or by 1 if it is 2 (to consider the next odd number). This process continues until the square of the current factor is greater than the number.

- After performing prime factorization, the program prints the prime factors and their counts to the user.


## Program Input & Output

When you run the program, `prime_factors.py`, the output will look like this;

```

Prime Factorization Program

1. Perform prime factorization of a number
2. Enter (q)uit to exit program
Enter your choice: 1
Enter a number: 25
Prime factors of 25:
5^2

1. Perform prime factorization of a number
2. Enter (q)uit to exit program
Enter your choice: 1
Enter a number: 258998
Prime factors of 258998:
2^1
129499^1

1. Perform prime factorization of a number
2. Enter (q)uit to exit program
Enter your choice: 3696
Invalid choice. Please enter a valid option.
1. Perform prime factorization of a number
2. Enter (q)uit to exit program
Enter your choice: 1
Enter a number: 3696
Prime factors of 3696:
2^4
3^1
7^1
11^1

1. Perform prime factorization of a number
2. Enter (q)uit to exit program
Enter your choice: q
Bye.
```