# Lucas Number Generator

## Description

Lucas numbers are a sequence of integers that start with 2 and 1, and each subsequent number is the sum of the previous two numbers. For example, the Lucas sequence starts as 2, 1, 3, 4, 7, 11, 18, ...

The "Lucas Number Generator" is a Python program that allows users to generate Lucas numbers and Lucas sequences.

## How it Works

- The program starts with a <code>main</code> function. Inside this function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: generate the nth Lucas number, generate the Lucas sequence up to the nth term, or quit the program. The user's choice is obtained using the <code>input</code> function and stored in the <code>choice</code> variable.

- The program uses if-elif-else statements to execute the corresponding functions based on the user's choice. If the user chooses option 1, the <code>generate_nth_lucas_number</code> function is called. If the user chooses option 2, the <code>generate_lucas_sequence</code> function is called. If the user chooses option 3 or enters 'q', the program terminates.

- To generate the nth Lucas number, the program calls the <code>generate_nth_lucas_number</code> function. This function prompts the user to enter the value of n and validates the input. The program then calculates the nth Lucas number using the <code>get_nth_lucas_number</code> function.

- The <code>get_nth_lucas_number</code> function returns the nth Lucas number. If n is 0, it returns 2. If n is 1, it returns 1. For n greater than 1, it uses a loop to calculate the nth Lucas number based on the Lucas number formula: $L(n) = L(n-1) + L(n-2)$, where $L(0) = 2$ and $L(1) = 1$. After calculating the nth Lucas number, the program displays it to the user.

- To generate the Lucas sequence up to the nth term, the program calls the <code>generate_lucas_sequence</code> function. This function prompts the user to enter the value of n and validates the input. The program then generates the Lucas sequence up to the nth term using the <code>get_lucas_sequence</code> function.

- The <code>get_lucas_sequence</code> function returns a list containing the Lucas sequence up to the nth term. It iterates from 0 to n and calls the <code>get_nth_lucas_number</code> function for each term, adding the result to the sequence list. After generating the Lucas sequence, the program displays it to the user.


## Program Input & Output

When you run the program, `lucus_sequence.py`, the output will look like this;

```

Lucas Number Generator

1. Generate nth Lucas number
2. Generate Lucas sequence up to nth term
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the value of n: 10
The Lucas sequence up to the 10th term is:
[2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123].

1. Generate nth Lucas number
2. Generate Lucas sequence up to nth term
3. Enter (q)uit to exit program
Enter your choice:
> 1
Enter the value of n: 11
The 11th Lucas number is: 199

1. Generate nth Lucas number
2. Generate Lucas sequence up to nth term
3. Enter (q)uit to exit program
Enter your choice:
> q
Bye.
```