# Perfect Square Check

## Description

A perfect square is a non-negative integer that can be expressed as the square of an integer. That is, a number $N$ is a perfect square if it satisfies the following condition:
$$N = m^2$$
where $m$ is an integer, representing the square root of $N$

A perfect square is the result of multiplying an integer by itself. For instance, $4$, $9$, and $25$ are perfect squares since they can be written as $2^2$, $3^2$, and $5^2$ respectively. Some examples of perfect square numbers include $0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, \ldots$

The, Perfect Squares Program, is a Python program that allows the user to check if a number is a perfect square and generates perfect squares within a specified range.


## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle the user's choice. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program provides three options to the user: Check if a number is a perfect square, generate perfect squares within a range, Quit the program. If the user selects option 1, the program calls the `is_perfect_square` function. If the user selects option 2, the program calls the `generate_perfect_squares` function. If the user selects option 3 the program breaks out of the loop, terminating the program.

- The `is_perfect_square` function checks if a number is a perfect square. The `is_perfect_square(n)` function takes a number as an argument and checks if it is a perfect square. It calculates the square root of the number using the expression `int(n ** 0.5)`. It then checks if the square of the calculated square root is equal to the original number. If the condition is satisfied, it returns `True`, indicating that the number is a perfect square. Otherwise, it returns `False`.

- The `generate_perfect_squares` function iterates over numbers in a range and calls the `is_perfect_square` function for each number. If a number is a perfect square, it is added to the `squares` list. After checking or listing perfect squares, the program displays the results to the user.


## Program Input & Output

When you run the program, `perfect_square.py`, the output will look like this;

```

Perfect Squares Program

Choose an option:
1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Perfect Square: 42
42 is not a perfect square.

Choose an option:
1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Exit program
Enter your choice: 1
Enter a positive integer to check if it is a Perfect Square: 36
36 is a perfect square.

Choose an option:
1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Exit program
Enter your choice: 2
Enter the lower limit: 1
Enter an upper limit: 1000
Perfect squares within the range [1, 1000]: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961].

Choose an option:
1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Exit program
Enter your choice: 3
Bye.
```