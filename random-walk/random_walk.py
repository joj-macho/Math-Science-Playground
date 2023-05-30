import random

def main():
    '''This function generates random walks and displays it as a grid.'''

    print('\nRandom Walk in 2-Dimensions.\n')
    # variables
    N = 1000  # number of steps
    step_length = 1
    x, y = 0, 0  # initial position

    # Generate random walk
    walk = simulate_random_walk(N, step_length, x, y)

    # Display results
    display_random_walk(walk, x, y)


def simulate_random_walk(N, d, x, y):
    '''This function generates a random walk in 2D.'''

    walk = []
    for _ in range(N):
        random_number = random.random()
        if 0 <= random_number < 0.25:
            y += d
        elif 0.25 <= random_number < 0.5:
            x += d
        elif 0.5 <= random_number < 0.75:
            y -= d
        else:
            x -= d
        walk.append((x, y))

    return walk


def display_random_walk(walk, start_x, start_y):
    '''This function displays the random walk as a grid-like output.'''

    # Determine the boundaries of the grid
    min_x = min(walk, key=lambda coord: coord[0])[0]
    max_x = max(walk, key=lambda coord: coord[0])[0]
    min_y = min(walk, key=lambda coord: coord[1])[1]
    max_y = max(walk, key=lambda coord: coord[1])[1]

    # Create the grid
    grid = [['  ' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    # Update the grid with the walk path
    for x, y in walk:
        grid[y - min_y][x - min_x] = '██'

    # Print the grid
    for row in grid:
        print(' '.join(row))

    # Print starting and ending positions
    print(f'\nStarting Position: ({start_x}, {start_y})')
    print(f'Ending Position: ({walk[-1][0]}, {walk[-1][1]})\n')


if __name__ == '__main__':
    main()