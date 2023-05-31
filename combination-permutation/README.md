# Combination and Permutation Calculator

## Description

The Combination and Permutation Calculator is a Python program that performs calculations related to combinations and permutations. Combinations and permutations are mathematical concepts used to count the number of possible arrangements or selections from a given set of items. The program provides options to calculate combinations (nCr) and permutations (nPr) based on user input values for n and r. It utilizes the factorial function to compute the necessary factorials and applies the formulas for combinations and permutations to produce the desired results.


## How it Works

- The program starts by defining a <code>main</code> function. Inside the <code>main</code> function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: calculate combination (nCr), calculate permutation (nPr), or quit the program. The user's choice is obtained using the <code>input</code> function and stored in the <code>choice</code> variable.

- The program uses an if-elif-else statement to execute the corresponding functions based on the user's choice. If the user chooses option 1, the <code>calculate_combination</code> function is called. If the user chooses option 2, the <code>calculate_permutation</code> function is called. If the user chooses option 3 or enters "q" to quit, the program terminates.

- To calculate the combination, the program calls the <code>calculate_combination</code> function. This function prompts the user to enter the values of n and r (where n is the total number of objects and r is the number of objects to choose). The input is validated, and if the input is valid (n &gt;= r &gt;= 0), the program calculates the combination using the formula <code>factorial(n) // (factorial(r) * factorial(n - r))</code>. The result is then displayed.

- To calculate the permutation, the program calls the <code>calculate_permutation</code> function. This function prompts the user to enter the values of n and r (where n is the total number of objects and r is the number of objects to arrange). The input is validated, and if the input is valid (n &gt;= r &gt;= 0), the program calculates the permutation using the formula <code>factorial(n) // factorial(n - r)</code>. The result is then displayed.

- The <code>factorial</code> function is used to calculate the factorial of a given number. It is a recursive function that returns the factorial of <code>n</code>. If <code>n</code> is 0, the function returns 1. Otherwise, it multiplies <code>n</code> by the factorial of <code>n - 1</code> to compute the factorial.


## Program Input & Output

When you run the program, `combination_permutation.py`, the output will look like this;

```

Combination and Permutation Calculator

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 1
Enter the value of n: 2
Enter the value of r: 5
Invalid values. Make sure n >= r >= 0.

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 1
Enter the value of n: 5
Enter the value of r: 2
The combination of 5 choose 2 is 10.

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 2
Enter the value of n: 5
Enter the value of r: 2
The permutation of 5P2 is 20.

1. Calculate Combination (nCr)
2. Calculate Permutation (nPr)
3. Enter (q)uit to exit program
Enter your choice: 3
Bye.
```