import copy
import random
import sys
import time

# Constants
# Width and height of the cell grid
WIDTH = 79
HEIGHT = 20
# Dead and live cells
ALIVE = 'O'
DEAD = ' '

def main():
    '''Main function to run Conway's Game of Life.'''

    print('\nConway\'s Game of Life: Cellular Automata\n')

    next_cells = {}
    # Initialize cells randomly
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if random.randint(0, 1) == 0:
                next_cells[(i, j)] = ALIVE
            else:
                next_cells[(i, j)] = DEAD

    try:
        while True:
            display_cells(next_cells)
            cells = copy.deepcopy(next_cells)
            update_cells(cells, next_cells)
            print("Press Ctrl-C to quit.")
            time.sleep(1)

    except KeyboardInterrupt:
        sys.exit()


def display_cells(cells):
    '''This function displays the current state of the cells.'''

    print('\n' * 50)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(cells[(j, i)], end='')
        print()


def update_cells(cells, next_cells):
    '''This function updates the state of the cells based on Conway's Game of Life rules.'''
    
    for i in range(WIDTH):
        for j in range(HEIGHT):
            # Get the neighboring coordinates of (x, y)
            left = (i - 1) % WIDTH
            right = (i + 1) % WIDTH
            above = (j - 1) % HEIGHT
            below = (j + 1) % HEIGHT

            # Count the number of living neighbors:
            number_of_cell_neighbors = 0
            if cells[(left, above)] == ALIVE:
                number_of_cell_neighbors += 1  # Top-left neighbor is alive.
            if cells[(i, above)] == ALIVE:
                number_of_cell_neighbors += 1  # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                number_of_cell_neighbors += 1  # Top-right neighbor is alive.
            if cells[(left, j)] == ALIVE:
                number_of_cell_neighbors += 1  # Left neighbor is alive.
            if cells[(right, j)] == ALIVE:
                number_of_cell_neighbors += 1  # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                number_of_cell_neighbors += 1  # Bottom-left neighbor is alive.
            if cells[(i, below)] == ALIVE:
                number_of_cell_neighbors += 1  # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                number_of_cell_neighbors += 1  # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if cells[(i, j)] == ALIVE and (number_of_cell_neighbors == 2 or number_of_cell_neighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[(i, j)] = ALIVE
            elif cells[(i, j)] == DEAD and number_of_cell_neighbors == 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[(i, j)] = ALIVE
            else:
                # Everything else dies or stays dead:
                next_cells[(i, j)] = DEAD


if __name__ == "__main__":
    main()
