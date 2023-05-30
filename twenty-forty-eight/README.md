# Twenty-Forty-Eight (2048) Game

## Description

This program is a basic implementation of the game "2048" in Python. It uses a text-based interface to allow the player to slide tiles on a 4x4 board in four directions: up, down, left, and right. The goal of the game is to combine tiles with the same number to create a tile with the value of 2048.

## How it Works

- `main()`: The main function that orchestrates the game and controls the flow.
- `generate_new_board()`: Generates a new game board with two initial tiles (2 or 4) placed randomly.
- `draw_board(board)`: Displays the current state of the game board on the console.
- `get_score(board)`: Calculates and returns the score based on the values of the tiles on the board.
- `combine_tiles_in_column(column)`: Combines the tiles in a column if they have the same value and returns the updated column.
- `make_move(board, move)`: Performs the requested move (up, down, left, right) on the board and returns the updated board.
- `add_new_tile(board)`: Adds a new tile (2 or 4) to a random empty space on the board.
- `is_board_full(board)`: Checks if the board is full and returns True or False.
- `ask_for_player_move()`: Prompts the player for a move (W, A, S, D) and returns the valid move entered by the player.

## Program Input & Output

When you run the program `twenty_48.py`, the output will look like this;

```

```
