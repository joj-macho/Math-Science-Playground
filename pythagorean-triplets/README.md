# Pythagorean Triplets

## Description

The Pythagorean Triplets program is a Python program that generates Pythagorean triplets within a specified range. Pythagorean triplets are sets of three positive integers (a, b, and c) that satisfy the Pythagorean theorem, which states that the square of the hypotenuse (c) is equal to the sum of the squares of the other two sides (a and b). For example, the triplet (3, 4, 5) is a Pythagorean triplet because $3^2 + 4^2 = 5^2$ ($9 + 16 = 25$). 

## How it Works

- The program begins by defining a <code>main</code> function. Inside the <code>main</code> function, a while loop is used to repeatedly display a menu of options and handle user input. The user is prompted to choose an option: generate Pythagorean triplets within a range or quit the program. The user's choice is obtained using the <code>input</code> function and stored in the <code>choice</code> variable.

- The program uses an if-elif-else statement to execute the corresponding functions based on the user's choice. If the user chooses option 1, the <code>generate_triplets</code> function is called. If the user chooses option 2 or enters "q" to quit, the program terminates.

- To generate Pythagorean triplets within a range, the program calls the <code>generate_triplets</code> function. This function prompts the user to enter a starting and ending number, validates the input, and calls the <code>find_triplets</code> function to calculate the Pythagorean triplets. The function then displays the generated triplets.

- The <code>find_triplets</code> function takes a starting number <code>start</code> and an ending number <code>end</code> as input and returns a list of Pythagorean triplets within that range. It iterates over all possible combinations of values for <code>a</code> and <code>b</code> within the range and calculates the value of <code>c</code> using the Pythagorean theorem. If <code>c</code> is an integer and within the range, the triplet <code>(a, b, c)</code> is added to the list of triplets.


## Program Input & Output

When you run the program, `pythagorean_triplets.py`, the output will look like this;

```

Pythagorean Triplets

1. Generate Pythagorean triplets within a range
2. Enter (q)uit to exit program
Enter your choice:
> 1
Enter the starting number: 5
Enter the ending number: 9
No Pythagorean triplets found within the range (5, 9).

1. Generate Pythagorean triplets within a range
2. Enter (q)uit to exit program
Enter your choice:
> 1
Enter the starting number: 1
Enter the ending number: 15
Pythagorean triplets within the range (1, 15):
3 4 5
5 12 13
6 8 10
9 12 15

1. Generate Pythagorean triplets within a range
2. Enter (q)uit to exit program
Enter your choice:
> 2
Bye.
```