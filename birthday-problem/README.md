# The Birthday Problem

## Description

This program is a simulation of the birthday paradox. The birthday paradox states that in a group of randomly selected people, there is a higher probability than expected that at least two people share the same birthday.

The program aims to determine the percentage of people sharing the same birthday for various group sizes by performing multiple _Monte Carlo_ Experiments.

## How it Works

- The program begins by importing the `datetime` and `random` modules for generating random birthdays and working with dates.

- The `main()` function begins by displaying an introduction to the birthday paradox and prompts the user to enter the number of birthdays they want to generate.

- The program starts by printing an introduction message that explains the birthday paradox and the purpose of the program. It then prompts the user to enter the number of birthdays they want to generate, with a limit of 100. The program validates the user's input and ensures it is a valid number between 1 and 100. If the user enters 'q', the program exits.

- The `generate_birthdays()` function is called with the user's input as the argument. This function generates a list of random birthdays for the specified number of people. Birthdays are represented as `datetime.date` objects.

- The `display_birthdays()` function is called to display the generated birthdays. It formats the birthdays and prints them to the console.

- The `find_birthday_match()` function is called to check if any birthdays in the list occur more than once. If a match is found, it returns the first matching birthday; otherwise, it returns None.

- The program checks the return value of `find_birthday_match()` and prints whether there are multiple people sharing the same birthday or not.

- The program proceeds to perform simulations to determine the percentage of people sharing the same birthday. It sets `num_simulations` to 100,000 and initializes a counter variable, matches, to keep track of the number of simulations with matching birthdays.

- The program enters a loop and generates a new set of birthdays for each simulation using the `generate_birthdays()` function. It checks if there is a birthday match using the `find_birthday_match()` function. If a match is found, it increments the matches counter. Every 10,000 simulations, the program prints the number of simulations completed so far.

- After all the simulations are completed, the program calculates the probability of two people sharing a birthday by dividing the number of matches by the total number of simulations. It then multiplies the result by 100 to get a percentage.

- The program prints the result, including the number of matching birthdays found in the simulations and the probability of having the same birthday in the group of people.


## Program Input & Output

When you run `birthdayParadox.py`, the output will look like this:

```

The Birthday Paradox!
In a set of n-randomly selected people, what is the probability that at least two people share the same birthday? What is the smallest value of n where the probability is at least 50% or 99%?

This program performs multiple simulations to determine the percentage of people sharing the same birthday for various group sizes.
    
How many birthdays (max = 100) do you want to generate?
Enter (q)uit to exit the program.
> 23

23 Birthdays Randomly Generated:
13 March, 25 August, 5 October, 25 July, 4 April, 16 July, 15 March, 9 November, 28 December, 22 December, 9 January, 12 April, 24 February, 5 June, 6 January, 29 November, 29 August, 6 February, 16 December, 22 December, 18 December, 5 August, 21 July

In this group of 23 people ... Multiple people share the birthday 22 December

Performing 100000 simulations with 23 birthdays...
0 Simulations Completed...
10000 Simulations Completed...
20000 Simulations Completed...
30000 Simulations Completed...
40000 Simulations Completed...
50000 Simulations Completed...
60000 Simulations Completed...
70000 Simulations Completed...
80000 Simulations Completed...
90000 Simulations Completed...

In the 100000 simulations of 23 people/birthdays:
There are 50782 matching birthdays in the group after 100000 simulations.
That is, 23 people have a 50.782% chance of having the same birthday in their group.

.
.
.

The Birthday Paradox!
In a set of n-randomly selected people, what is the probability that at least two people share the same birthday? What is the smallest value of n where the probability is at least 50% or 99%?

This program performs multiple simulations to determine the percentage of people sharing the same birthday for various group sizes.
    
How many birthdays (max = 100) do you want to generate?
Enter (q)uit to exit the program.
> 75

75 Birthdays Randomly Generated:
13 February, 26 July, 4 February, 28 May, 9 July, 30 September, 19 August, 16 October, 18 July, 18 February, 13 August, 29 December, 13 October, 15 February, 22 October, 13 April, 15 May, 12 November, 23 June, 7 December, 22 December, 23 April, 29 May, 3 October, 27 October, 20 December, 31 January, 29 July, 30 March, 31 January, 6 May, 29 August, 29 July, 13 December, 30 July, 17 June, 1 February, 3 April, 21 June, 3 May, 14 January, 2 November, 11 April, 26 March, 23 April, 13 December, 19 March, 5 November, 20 May, 24 July, 14 December, 18 April, 31 October, 12 July, 19 September, 3 May, 22 April, 3 July, 4 October, 4 September, 7 August, 20 March, 28 May, 14 February, 20 February, 24 November, 19 September, 12 February, 21 May, 24 May, 12 July, 26 April, 12 November, 3 September, 30 November

In this group of 75 people ... Multiple people share the birthday 28 May

Performing 100000 simulations with 75 birthdays...
0 Simulations Completed...
10000 Simulations Completed...
20000 Simulations Completed...
30000 Simulations Completed...
40000 Simulations Completed...
50000 Simulations Completed...
60000 Simulations Completed...
70000 Simulations Completed...
80000 Simulations Completed...
90000 Simulations Completed...

In the 100000 simulations of 75 people/birthdays:
There are 99974 matching birthdays in the group after 100000 simulations.
That is, 75 people have a 99.974% chance of having the same birthday in their group.
```

- Running the program with `number_of_birthdays` = 23 and 100 000 simulations, the returned probability value is always $\approx 0.5$ indicating about $50\%$ of the time across 100 000 trials, at least two birthdays shared a date in a group of 23 people.

- Running the program with `number_of_birthdays` = 75 and 100 000 simulations, the returned probability value is always $\approx 0.999$ indicating about $99.9\%$ of the time across 100 000 trials, at least two birthdays shared a date in a group of 75 people.
