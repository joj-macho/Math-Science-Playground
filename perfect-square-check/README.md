# Perfect Square Check

## Description

The "Perfect Squares Program" is a Python program that allows the user to check if a number is a perfect square and list all the perfect squares within a given limit.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly display a menu of options and handle the user's choice. The user's input is obtained using the `input` function and stored in the `choice` variable.

- The program provides three options to the user: Check if a number is a perfect square, List perfect squares within a limit, Quit the program. If the user selects option 1, the program calls the `check_perfect_square` function. If the user selects option 2, the program calls the `list_perfect_squares` function. If the user selects option 3 or enters 'q', the program displays "Bye." and breaks out of the loop, terminating the program.

- The `check_perfect_square` function prompts the user to enter a number and checks if it is a perfect square. It calls the `is_perfect_square` function, passing the entered number as an argument. If the result is `True`, it indicates that the number is a perfect square. If not, it indicates that the number is not a perfect square.

- The `list_perfect_squares` function prompts the user to enter a limit and lists all the perfect squares within that limit. It iterates over numbers from 1 to the limit (inclusive) and calls the `is_perfect_square` function for each number. If a number is a perfect square, it is added to the `squares` list. After checking or listing perfect squares, the program displays the results to the user.

- The `is_perfect_square` function takes a number as an argument and checks if it is a perfect square. It calculates the square root of the number using the expression `int(n ** 0.5)`. It then checks if the square of the calculated square root is equal to the original number. If the condition is satisfied, it returns `True`, indicating that the number is a perfect square. Otherwise, it returns `False`.


## Program Input & Output

When you run the program, `perfect_square.py`, the output will look like this;

```

Perfect Squares Program

1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the limit: 100
Perfect squares within the limit (100):
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Enter (q)uit to exit program
Enter your choice:
> 2
Enter the limit: 3
Perfect squares within the limit (3):
[1].

1. Check if a number is a perfect square
2. List perfect squares within a limit
3. Enter (q)uit to exit program
Enter your choice:
> 3
Bye.
```