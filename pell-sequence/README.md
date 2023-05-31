# Pell Sequence

## Description

Pell numbers form a sequence of integers that can be calculated using a recursive formula. The sequence starts with 0 and 1, and each subsequent number is twice the previous number plus the number before that. For example, the Pell sequence starts as 0, 1, 2, 5, 12, 29, 70, ...

This program, Pell Sequence, is a Python program that allows users to calculate and generate a Pell sequence.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: generate Pell numbers or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `generate_pell_numbers` function is called. If the user chooses option 2 or enters 'q', the program terminates.

- To generate Pell numbers, the program calls the `generate_pell_numbers` function. This function prompts the user to enter the number of Pell numbers to generate and validates the input. The program then generates the Pell numbers using a loop.

- The `pell_numbers` list is initialized with the first two Pell numbers: 0 and 1.

- If the requested number of Pell numbers is less than or equal to 2, the program prints the generated Pell numbers and returns.

- If the requested number of Pell numbers is greater than 2, the program enters a loop starting from index 2 up to the specified number of Pell numbers minus one. In each iteration, it calculates the current Pell number using the formula 2 * pell_numbers[i - 1] + pell_numbers[i - 2] and appends it to the `pell_numbers` list.

- After generating the Pell numbers, the program displays them to the user.

## Program Input & Output

When you run the program, `pell_sequence.py`, the output will look like this;

```

Pell Number Generator

1. Generate Pell numbers
2. Enter (q)uit to exit program
Enter your choice:
> 1
Enter the number of Pell numbers to generate: 20
Generated Pell numbers:
[0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782, 195025, 470832, 1136689, 2744210, 6625109].

1. Generate Pell numbers
2. Enter (q)uit to exit program
Enter your choice:
> 3
Invalid choice. Please enter a valid option.
1. Generate Pell numbers
2. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```