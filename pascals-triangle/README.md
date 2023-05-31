# Pascal's Triangle

## Description

The Pascal's Triangle program is a Python program that displays Pascal's Triangle based on the number of rows specified by the user. Pascal's Triangle is a triangular arrangement of numbers where each number is the sum of the two numbers directly above it. The program utilizes the concept of binomial coefficients and factorial calculations to generate and display Pascal's Triangle.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to prompt the user to enter the number of rows for Pascal's Triangle. The input is validated to ensure it is a valid integer. The number of rows is stored in the `rows` variable.

- The program then calls the `display_pascals_triangle` function and passes the number of rows as an argument. The `display_pascals_triangle` function is responsible for generating and displaying Pascal's Triangle. It uses two nested loops to iterate over the rows and columns of the triangle. The outer loop iterates from 0 to the number of rows specified, and the inner loop iterates from 0 to the current row index.

- Inside the inner loop, the function calls the `binomial_coefficient` function to calculate the binomial coefficient for the current row and column. The binomial coefficient is calculated using the formula $\frac{n!}{k! \times (n-k)!} $, where n is the row index and k is the column index.

- The `binomial_coefficient` function calculates the binomial coefficient by calling the `factorial` function. The `factorial` function is a recursive function that calculates the factorial of a given number. It returns 1 if the input is 0 and recursively multiplies the number with the factorial of (n - 1) for other positive integers.

- Finally, the program prints the calculated binomial coefficient for each position in Pascal's Triangle, separated by spaces. After printing all the numbers in a row, it moves to the next line to start a new row.


## Program Input & Output

When you run the program, `pascals_triangle.py`, the output will look like this;

```

Pascal's Triangle

Enter the number of rows: 5
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 

Pascal's Triangle

Enter the number of rows: 15
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1 
1 8 28 56 70 56 28 8 1 
1 9 36 84 126 126 84 36 9 1 
1 10 45 120 210 252 210 120 45 10 1 
1 11 55 165 330 462 462 330 165 55 11 1 
1 12 66 220 495 792 924 792 495 220 66 12 1 
1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1 
1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1 
```