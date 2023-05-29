# Dice Roller Simulator

## Description

This program simulates the rolling of a given number of dice, a specified number of times (one million times), and then calculates the percentage of each possible total outcome of the dice rolls.

The program allows the user to simulate rolling a specified number of dice, performs the simulation by generating random dice rolls, and provides a table showing the total, the number of rolls, and the percentage of rolls for each possible total.


## How it Works

- The program starts by importing the `random` and `time` modules to generate random numbers and to keep track of the time taken to simulate the dice rolls.

- The `main()` function is defined, the user is prompted to enter the number of dice they want to roll. The input is obtained using the `input()` function and converted to an integer using `int()`. An input validation check is performed to ensure that the number of dice is a positive integer. If the input is invalid, a `ValueError` is raised, and an error message is displayed. The program terminates if the input is invalid.

- A dictionary called `results` is then created to store the results of each dice roll, with the keys being the possible totals that can be obtained from rolling `num_of_dice` dice (i.e., values between `num_of_dice` and `num_of_dice*6`, inclusive), and the values being the number of times that each total is obtained. Initially, all values in the results dictionary are set to 0.

- The program starts simulating the dice rolls by displaying a message indicating the start of the simulation. It simulates 1,000,000 rolls of the specified number of dice. A loop runs 1,000,000 times and performs the following steps for each iteration:
  - If one second has passed since the last progress update, a progress message is displayed indicating the percentage of completion.
  - The total sum of the dice rolls is calculated by generating random numbers between 1 and 6 (inclusive) for each die and summing them using a generator expression.
  - The count for the calculated total in the `results` dictionary is incremented by 1.

- After completing the simulation, the program displays a separator line and a header for the results table.

- Another loop iterates over the possible totals from the number of dice to `num_of_dice * 6`. For each total, it retrieves the roll count from the results dictionary and calculates the percentage of rolls for that total.

- The program displays the total, the number of rolls for that total, and the percentage of rolls for each total in the results table. The program execution finishes.


## Program Input & Output

When you run the program `dice_roll_sim.py`, the output will look like this;

```

Dice Roll Simulator.
This program generates simulations of rolling n dice and gives you the percentage of the dice total.

Enter the number of Dice:
> 5
Simulating 1,000,000 rolls of 5 dice.
21.6% done ...
43.2% done ...
64.7% done ...
86.1% done ...
------------------------------
Total - Rolls - Percentage
------------------------------
  5 - 128 rolls - 0.0%
  6 - 613 rolls - 0.1%
  7 - 1936 rolls - 0.2%
  8 - 4461 rolls - 0.4%
  9 - 8949 rolls - 0.9%
  10 - 16187 rolls - 1.6%
  11 - 26338 rolls - 2.6%
  12 - 39193 rolls - 3.9%
  13 - 53807 rolls - 5.4%
  14 - 69601 rolls - 7.0%
  15 - 83995 rolls - 8.4%
  16 - 94492 rolls - 9.4%
  17 - 100286 rolls - 10.0%
  18 - 100351 rolls - 10.0%
  19 - 94569 rolls - 9.5%
  20 - 83525 rolls - 8.4%
  21 - 69454 rolls - 6.9%
  22 - 53832 rolls - 5.4%
  23 - 39452 rolls - 3.9%
  24 - 26353 rolls - 2.6%
  25 - 16189 rolls - 1.6%
  26 - 9081 rolls - 0.9%
  27 - 4534 rolls - 0.5%
  28 - 1899 rolls - 0.2%
  29 - 648 rolls - 0.1%
  30 - 127 rolls - 0.0%
```
