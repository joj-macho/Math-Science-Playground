# Amicable Number Checker

## Description

Amicable numbers are pairs of positive integers ($a$ and $b$) where each number is the sum of the proper divisors of the other number. In other words, the sum of the proper divisors of one number equals the other number, and vice versa.
For a pair of numbers ($a, b$), we have:
$$s(a) = b \quad \text{and} \quad s(b) = a$$
where $s(n)$ denotes the sum of the proper divisors of $n$.

For example, consider the pair of numbers ($220, 284$), we have that 
- For $a = 220$:
    - Proper divisors of $220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, \ \text{and} \ 110$
    - $s(220) = \sum{\{1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110} \} \\ s(220)= 284$
- For $b = 284$:
    - Proper divisors of $284: 1, 2, 4, 71, \ \text{and} \ 142$
    - $s(284) = \sum{\{1, 2, 4, 71, 142} \} \\ s(284)= 220$

Hence $(220, 284)$ is an amicable parit because $s(220) = 284$ and $s(284) = 220$, satisfying the definition of amicable numbers.

You can read more about amicable numbers on [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers) and [Wolfram MathWorld](https://mathworld.wolfram.com/AmicablePair.html)

This program, Amicable Number Checker, is a Python program that allows users to check if a pair of numbers is amicable or find amicable numbers within a given range.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: check if a number is amicable, list amicable pairs within a range, or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `find_amicable_pair` function is called. If the user chooses option 2, the `generate_amicable_pairs` function is called. If the user chooses option 3, the loop breaks and the program ends.

- To check if a number is part of an amicable pair, the program calls the `find_amicable_pair(n)` function. The `find_amicable_pair(n)` function finds an amicable pair for a given number, `n`. It calculates the sum of the proper divisors for the number and for that sum. If the input number is not equal to the sum of the proper divisors for the number and is equal to the sum of the proper divisors for that sum, the function considers it an amicable pair and returns the pair as $(a, b)$.

- - The `get_divisors(n)` function takes a number `n` as input and calculates its proper divisors. It iterates from 1 to `n-1` and checks if `n` is divisible by each number. If it is, the number is a proper divisor and is added to the list of divisors. The list of divisors is returned.

- When the user chooses to list amicable pairs within a range, the program calls the `generate_amicable_pairs(start, end)` function. This function iterates through a range, `start` to `end`, of numbers, finds amicable pairs for each number (using the `find_amicable_pair` function), and stores them in a list (`amicable_pairs`) while ensuring that only unique pairs are added by using a set (`found_pairs`) to track previously found pairs. The set helps prevent the addition of duplicate pairs, and the reversed form of each pair is also added to the set to ensure uniqueness.



## Program Input & Output

When you run the program, `amicable_numbers.py`, the output will look like this;

```

Amicable Number Checker and Generator

Choose an option:
1. Check if a number is part of an amicable pair
2. Generate amicable pairs within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is an amicable number: 280
280 is not part of an amicable pair.

Choose an option:
1. Check if a number is part of an amicable pair
2. Generate amicable pairs within a range
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is an amicable number: 284
The amicable pair for 284 is: (284, 220)

Choose an option:
1. Check if a number is part of an amicable pair
2. Generate amicable pairs within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 0
Enter an upper limit: 200
No amicable pairs within the range (0, 200).

Choose an option:
1. Check if a number is part of an amicable pair
2. Generate amicable pairs within a range
3. Exit program
Enter your choice: 2
Enter the lower limit: 200
Enter an upper limit: 6000
Amicable pairs within the range (200, 6000):
[(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)]

Choose an option:
1. Check if a number is part of an amicable pair
2. Generate amicable pairs within a range
3. Exit program
Enter your choice: 3
Bye.
```