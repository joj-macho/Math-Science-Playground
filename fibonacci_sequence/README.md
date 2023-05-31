# Fibonacci Number Generator

## Description

The Fibonacci Number Generator is a Python program that generates the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. It starts with 0 and 1, and the subsequent numbers are calculated by adding the previous two numbers. For example, the Fibonacci sequence begins as 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. 


## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: generate the Fibonacci sequence or quit the program. The user's choice is obtained using the `input` function and stored in the `choice` variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the `generate_fibonacci_sequence` function is called. If the user chooses option 2, the program terminates.

- To generate the Fibonacci sequence, the program calls the `generate_fibonacci_sequence` function. This function prompts the user to enter the number of terms they want in the sequence and validates the input. The program then generates the Fibonacci sequence using a while loop.

- Inside the while loop, the program checks if the number of terms requested is valid (greater than 0). If not, an error message is displayed. If the number of terms is 1 or 2, the program prints the Fibonacci sequence accordingly. Otherwise, the program initializes the Fibonacci sequence list with the first two numbers (0 and 1) and continues to generate the subsequent numbers by summing the last two numbers in the sequence.

- Once the Fibonacci sequence is generated, the program displays it to the user, indicating the number of terms requested.

## Program Input & Output
When you run `fibonacci_sequence.py`, the output will look like this;

```

Fibonacci Number Generator

1. Generate Fibonacci sequence
2. Quit Program
Enter your choice:
> 1
Enter the number of terms: 1
Fibonacci sequence for n = 1: [0]

1. Generate Fibonacci sequence
2. Quit Program
Enter your choice:
> 1
Enter the number of terms: 2
Fibonacci sequence for n = 2: [0, 1]

1. Generate Fibonacci sequence
2. Quit Program
Enter your choice:
> 1
Enter the number of terms: 50
Fibonacci sequence for n = 50: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

1. Generate Fibonacci sequence
2. Quit Program
Enter your choice:
> 2
Bye.

```
