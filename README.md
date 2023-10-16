# MinMax-ABPrune

## Intro
This repository contains Python code for playing a game similar to Connect 4, called Connect383, with various artificial intelligence agents to play against. The game board is represented by a height and length that is user defined, where two players take turns dropping their pieces into the columns. The goal is to connect four of your own pieces horizontally, vertically, or diagonally before your opponent does.

## How to Play
To play Connect383, run the connect383.py script with the following command:

python connect383.py [player1] [player2] [board]

player1: Type of the first player, options: random, human, mini, lookN, prune, altN
player2: Type of the second player, options: random, human, mini, lookN, prune, altN
board: Initial game board, options: test_1, test_2, writeup_1, writeup_2, tournament, your_test, your_tester, your_testest or specify the board size as RxS where R is the number of rows and S is the number of columns.

## Player Types
random: Random moves; a basic player that makes random legal moves.
human: Allows a human player to input moves manually.
mini: Minimax agent; an AI player that uses minimax algorithm to make optimal moves.
lookN: Minimax with depth-limited search; an AI player that uses minimax with a limited depth of search.
prune: Minimax with alpha-beta pruning; an optimized AI player that uses minimax with alpha-beta pruning.
altN: Alternative heuristic AI player used for testing purposes.

## Sample Usage
python connect383.py look2 look3 writeup_1
In this example, player 1 (look2) plays against player 2 (look3) on the writeup_1 board.

## Game Rules
Players take turns dropping their pieces into any of the seven columns.
The first player to connect four of their pieces in a row wins.
The game ends in a draw if the board is full and no player has won.

## Additional Information
The code includes various game state evaluation methods, search algorithms, and heuristics to determine optimal moves.
The agents use different strategies to find the best moves, providing a variety of gameplay experiences.
Feel free to explore and modify the code to create your own Connect Four AI strategies!
