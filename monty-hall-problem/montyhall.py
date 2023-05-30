import random
import sys

# ASCII-art
ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""


def main():
    """The main function."""
    print('''
Welcome to the Monty Hall Problem!

In the Monty Hall game show, you are faced with three doors. Behind one of the doors, there is a brand new car, while the other two doors hide worthless goats:

{}
Imagine you have initially chosen Door #1.

Before revealing the contents of your chosen door, the host, Monty Hall, decides to add a twist. He opens another door that reveals a goat:

{}
Now, you are presented with a choice: stick with your original selection or switch to the remaining unopened door.

Surprisingly, your chances of winning significantly improve if you decide to switch doors! This program allows you to explore the Monty Hall problem through repeated experiments.
'''.format(ALL_CLOSED, THIRD_GOAT))

    input('Press Enter to start...')

    global swap_wins, swap_losses, stay_wins, stay_losses
    swap_wins = swap_losses = stay_wins = stay_losses = 0

    while True:
        print(ALL_CLOSED)
        door_with_car = random.randint(1, 3)
        door_pick = get_user_choice()
        goat_door = show_goat_door(door_pick, door_with_car)
        
        while True:
            swap = input('Do you want to swap? (y/n): ').lower()
            if swap in ['y', 'n']:
                break
        
        if swap == 'y':
            door_pick = swap_doors(door_pick, goat_door)
        
        if door_pick == 1:
            print(FIRST_CAR_OTHERS_GOAT)
        elif door_pick == 2:
            print(SECOND_CAR_OTHERS_GOAT)
        elif door_pick == 3:
            print(THIRD_CAR_OTHERS_GOAT)
        
        print_final_result(door_with_car, door_pick, swap == 'y')
        
        print_success_rates()
        input('Press Enter to play again or (q)uit...')

def get_user_choice():
    """Gets the user's choice of a door."""
    while True:
        response = input(
            'Pick A Door 1, 2, or 3. Enter (q)uit to exit.\n> ').lower()
        if response in ['q', 'quit']:
            print('Bye.')
            sys.exit()
        if response in ['1', '2', '3']:
            return int(response)

def show_goat_door(door_pick, door_with_car):
    """Shows the door with a goat behind it."""
    possible_doors = [1, 2, 3]
    possible_doors.remove(door_pick)
    if door_with_car in possible_doors:
        possible_doors.remove(door_with_car)
    goat_door = random.choice(possible_doors)
    
    if goat_door == 1:
        print(FIRST_GOAT)
    elif goat_door == 2:
        print(SECOND_GOAT)
    elif goat_door == 3:
        print(THIRD_GOAT)
    
    print(f'Door {goat_door} has a goat.')

    return goat_door

def swap_doors(door_pick, goat_door):
    """Swaps the user's door choice."""
    possible_doors = [1, 2, 3]
    possible_doors.remove(door_pick)
    possible_doors.remove(goat_door)
    return possible_doors[0]

def print_final_result(door_with_car, door_pick, swap):
    """Prints the final result of the game."""
    if door_pick == door_with_car:
        print('You won!')
        if swap:
            global swap_wins
            swap_wins += 1
        else:
            global stay_wins
            stay_wins += 1
    else:
        print('Sorry, you lost.')
        if swap:
            global swap_losses
            swap_losses += 1
        else:
            global stay_losses
            stay_losses += 1

def print_success_rates():
    """Prints the success rates of swapping and not swapping."""
    total_swaps = swap_wins + swap_losses
    if total_swaps != 0:
        swap_success = round(swap_wins / total_swaps * 100, 1)
    else:
        swap_success = 0.0

    total_stays = stay_wins + stay_losses
    if total_stays != 0:
        stay_success = round(stay_wins / total_stays * 100, 1)
    else:
        stay_success = 0.0

    print()
    print('Swapping:     ', end='')
    print('{} wins, {} losses, '.format(swap_wins, swap_losses), end='')
    print('success rate {}%'.format(swap_success))
    print('Not swapping: ', end='')
    print('{} wins, {} losses, '.format(stay_wins, stay_losses), end='')
    print('success rate {}%'.format(stay_success))
    print()



if __name__ == '__main__':
    main()