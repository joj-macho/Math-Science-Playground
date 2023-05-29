import copy
import random
import sys
import time
import bext

# Set up the constants:
SCREEN_WIDTH, SCREEN_HEIGHT = bext.size()
SCREEN_WIDTH -= 1
SCREEN_HEIGHT -= 1

NUMBER_OF_ANTS = 10
PAUSE_AMOUNT = 0.1

ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    '''This is the main function that runs the ant simulation.'''

    bext.fg(ANT_COLOR)  # The ants' color is the foreground color.
    bext.bg(WHITE_TILE)  # Set the background to white to start.
    bext.clear()

    # Create a new board data structure:
    board = create_board()

    # Create ant data structures:
    ants = create_ants()

    while True:  # Main program loop.
        display_board(board, ants)

        # next_board is what the board will look like on the next step in the simulation.
        next_board = update_board(board, ants)

        board = next_board


def create_board():
    '''This function creates the initial board data structure.'''

    return {'width': SCREEN_WIDTH, 'height': SCREEN_HEIGHT}


def create_ants():
    '''This function creates the initial ant data structures.'''

    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, SCREEN_WIDTH - 1),
            'y': random.randint(0, SCREEN_HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)
    return ants


def update_board(board, ants):
    '''This function updates the board and ants for the next step in the simulation.'''

    next_board = copy.copy(board)

    for ant in ants:
        if board.get((ant['x'], ant['y']), False):
            next_board[(ant['x'], ant['y'])] = False
            ant['direction'] = turn_clockwise(ant['direction'])
        else:
            next_board[(ant['x'], ant['y'])] = True
            ant['direction'] = turn_counter_clockwise(ant['direction'])

        move_ant_forward(ant)

        ant['x'] = ant['x'] % SCREEN_WIDTH
        ant['y'] = ant['y'] % SCREEN_HEIGHT

    return next_board


def turn_clockwise(direction):
    '''This function turns the ant's direction clockwise.'''

    clockwise_turn = {
        NORTH: EAST,
        EAST: SOUTH,
        SOUTH: WEST,
        WEST: NORTH,
    }
    return clockwise_turn[direction]


def turn_counter_clockwise(direction):
    '''This function turns the ant's direction counter-clockwise.'''

    counter_clockwise_turn = {
        NORTH: WEST,
        WEST: SOUTH,
        SOUTH: EAST,
        EAST: NORTH,
    }
    return counter_clockwise_turn[direction]


def move_ant_forward(ant):
    '''This function moves the ant forward in its current direction.'''

    if ant['direction'] == NORTH:
        ant['y'] -= 1
    elif ant['direction'] == SOUTH:
        ant['y'] += 1
    elif ant['direction'] == WEST:
        ant['x'] -= 1
    elif ant['direction'] == EAST:
        ant['x'] += 1


def display_board(board, ants):
    '''This function displays the board and ants on the screen.'''

    bext.clear()

    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            if board.get((x, y), False):
                bext.goto(x, y)
                bext.bg(BLACK_TILE)
                print(' ', end='')

    for ant in ants:
        bext.goto(ant['x'], ant['y'])
        if ant['direction'] == NORTH:
            print(ANT_UP, end='')
        elif ant['direction'] == SOUTH:
            print(ANT_DOWN, end='')
        elif ant['direction'] == EAST:
            print(ANT_LEFT, end='')
        elif ant['direction'] == WEST:
            print(ANT_RIGHT, end='')

    # Display the quit message at the bottom of the screen:
    bext.goto(0, SCREEN_HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()
    time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
