# Lucas Number Generator

## Description

Lucas numbers are a sequence of integers that start with $2$ and $1$, and each subsequent number is the sum of the previous two numbers. Lucas numbers form a sequence of integers defined by the recurrence relation:
$$L_n = L_{n-1} + L_{n-2}$$

with initial conditions:
$$L_0 = 2, \quad L_1 = 1$$

where $L_{n}$ is the nth Lucas number, $L_{n-1}$ is the (n-1)th Lucas number, and $L_{n-2}$ is the (n-2)th Lucas number. 


The values of $L_n$ for $n=1, 2, \ldots$ are $2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, \ldots$


You can read more about Lucas numbers on [Wikipedia](https://en.wikipedia.org/wiki/Lucas_number) and [Wolfram MathWorld](https://mathworld.wolfram.com/LucasNumber.html)

This program, Lucas Number Generator, is a Python program that allows users to generate Lucas numbers and Lucas sequences.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: generate the nth Lucas number, generate the Lucas sequence up to the nth term, or quit the program. The user's choice is obtained using the `get_valid_input(message)` function and stored in the `choice` variable.

- The `get_valid_input(message)` function is called to obtain a valid input from the user. This function validates the input, ensuring that the entered value is a positive integer greater than 0. If the input is not valid, appropriate error messages are displayed, and the user is prompted to re-enter the value.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `get_nth_lucas_number` function is called. If the user chooses option 2, the `generate_lucas_sequence` function is called. If the user chooses option 3 the program terminates.

- To generate the nth Lucas number, the program calls the `get_nth_lucas_number(n)` function. The function checks for the base cases where the function directly returns the 0th and 1st Lucas numbers.  For `n` greater than 1, it initializes the first two Lucas numbers, $L_0$ and $L_1$. Then using a loop, it calculate subsequent Lucas numbers based on the Lucas sequence formula: $L(n) = L(n-1) + L(n-2)$. In each iteration, the values of `a` and `b` are updated according to the formula. Then finally it returns the nth Lucas number, which is stored in `b` after the loop completes.


- To generate the Lucas sequence up to the nth term, the program calls the `generate_lucas_sequence(n)` function. This function returns a list containing the Lucas sequence up to the nth term. It iterates from 0 to `n` and calls the `get_nth_lucas_number` function for each term, adding the result to the sequence list.


## Program Input & Output

When you run the program, `lucus_sequence.py`, the output will look like this;

```

Lucas Number Generator

Choose an option:
1. Generate nth Lucas number
2. Generate Lucas sequence up to nth term
3. Exit program
Enter your choice: 1
Enter a positive integer: 15
The 15th Lucas number is: 1364

Choose an option:
1. Generate nth Lucas number
2. Generate Lucas sequence up to nth term
3. Exit program
Enter your choice: 2
Enter a positive integer: 10
The Lucas sequence up to the 10th term is:
[2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123].

Choose an option:
1. Generate nth Lucas number
2. Generate Lucas sequence up to nth term
3. Exit program
Enter your choice: 3
Bye.
```