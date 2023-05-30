# Monty Hall Problem

## Description

This program is an implementation of the Monty Hall problem, a probability puzzle that highlights the counter-intuitive nature of probability. The program allows the user to play the Monty Hall game, where they can pick one of three doors in an attempt to win a car. The program simulates multiple rounds of the game and keeps track of the user's wins and losses.

## How it Works

- In this program, the user is asked to pick one of three doors, one of which contains a car, while the other two contain goats. Before the selected door is opened, one of the two remaining doors is opened to reveal a goat. The user is then given the option to swap their choice to the other unopened door or stick with their initial choice. The program runs multiple iterations of the game, allowing the user to see whether switching or sticking with their initial choice leads to more wins.

- The game is implemented through a while loop, which runs indefinitely until the user chooses to quit the game. Within each iteration of the loop, a random door is assigned the car, and the user is prompted to select a door. A different door with a goat behind it is then opened to show the user. The user is then asked whether they would like to swap doors or stick with their initial choice, and the program determines whether the user has won or lost based on their selection. The results of each game are recorded, and the number of wins and losses for switching and sticking with the initial choice are displayed at the end of the program.

## Program Input & Output

When you run the program `montyhall.py`, the output will look like this;

```

```
