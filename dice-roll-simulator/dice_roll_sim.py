import random
import time


def main():
    '''This function runs the Dice Roll Simulator program. The program generates simulations of rolling n dice and gives you the percentage of the dice total.'''

    print('\nDice Roll Simulator.\nThis program generates simulations of rolling n dice and gives you the percentage of the dice total.\n')

    try:
        num_of_dice = int(input('Enter the number of Dice:\n> '))
        if num_of_dice <= 0:
            raise ValueError("Number of dice must be a positive integer.")
    except ValueError as e:
        print("Invalid input:", e)
        return

    # Store dice roll results
    results = {}
    for i in range(num_of_dice, (num_of_dice * 6) + 1):
        results[i] = 0

    # Dice Roll Simulation
    print(f'Simulating 1,000,000 rolls of {num_of_dice} dice.')
    last_print = time.time()
    for i in range(1000000):
        if time.time() > last_print + 1:
            progress = round(i / 10000, 1)
            print('{0}% done ...'.format(progress))
            last_print = time.time()

        total = sum(random.randint(1, 6) for _ in range(num_of_dice))
        results[total] += 1

    # Show results
    print('--' * 15)
    print('Total - Rolls - Percentage')
    print('--' * 15)

    for i in range(num_of_dice, (num_of_dice * 6) + 1):
        roll = results[i]
        percentage = round(results[i] / 10000, 1)
        print(f'  {i} - {roll} rolls - {percentage}%')


if __name__ == '__main__':
    main()
