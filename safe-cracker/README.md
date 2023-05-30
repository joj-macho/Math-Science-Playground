# Safe Cracker

## Description

This program is a lock combination cracker that uses two different methods: hill climbing and brute force. It prompts the user to enter a lock combination and then cracks it using either the hill climbing method or the brute force method.

## How it Works

- The program starts by importing the necessary modules: `time`, `randint` and `randrange` from the `random` module, and `product` from the `itertools` module.

- The `main()` function is defined. It prompts the user to enter a lock combination, starts the timer, and then calls the appropriate method to crack the combination: `hill_climbing_cracker()` or `brute_force_cracker()`.

- The `hill_climbing_cracker()` function applies the hill climbing algorithm to crack the lock combination. It starts by converting the combination string to a list of integers. Then, it initializes the `best_attempt` list as a sequence of zeros and calculates its initial fitness grade. The function enters a loop where it generates a new attempt by copying the `best_attempt` list and randomly changing one digit at a time. If the fitness grade of the new attempt is higher than the current best attempt, it becomes the new best attempt. The loop continues until the best attempt matches the combination. Finally, the function prints the cracked combination and the number of tries it took.
    - The `fitness()` function compares two lists, `combo` and `attempt`, and counts the number of matching elements. It is used by the hill climbing method to evaluate the quality of each attempt.

- The `brute_force_cracker()` function uses a brute force approach to crack the lock combination. It iterates through all possible permutations of digits (from 0 to 9) with a length equal to the combination. For each permutation, it checks if it matches the combination. If a match is found, it prints the cracked combination and breaks out of the loop.

## Program Input & Output

When you run the program `safe_cracker.py`, the output will look like this;

```

Safe Cracker.

Enter the lock combination to crack:
> 2569879
Cracking Combination: 2569879
Combination Cracked! [2, 5, 6, 9, 8, 7, 9]
Cracked in 144 tries.

Runtime for this program was 0.00175 seconds.
sh-5.1$ /usr/bin/python3 ".../safe-cracker/safe_cracker.py"

Safe Cracker.

Enter the lock combination to crack:
> 5698741235
Cracking Combination: 5698741235
Combination Cracked! [5, 6, 9, 8, 7, 4, 1, 2, 3, 5]
Cracked in 306 tries.

Runtime for this program was 0.00226 seconds.
```