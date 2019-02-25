## STEPS TO ACHIEVE "tic-tac-toe" like game

### 1 - Determine objectives

Do a "tic-tac-toe" like game playable by 2 gamers on a computer

### 2 - Understand what we are doing

Understand rules of the game.

game system :
- put a chip in a square
- we have 9 chips 
- we have two type of chips (cross and round, same number of chips for each type)

Winning:
- have a column with 3 following chips horizontally
- have a column with 3 following chips vertically
- have a column with 3 following chips in diagonals

### 3 -  Model the game

#### - Model the board

See [GameBoard](GameBoard.py)


Take a matrix (or 2d list in our case)

```python
[
    [0, 0, 0],
    [1, 0, 0],
    [-1, 0, 0],
]
```

corresponds to [tic-tac-toe_board_example](images/tic-tac-toe_board_example.png)

caption:

- 0 empty box
- 1 yellow chip
- -1 red chip

#### - Model the turn system 

- modulo 2 is good to determine the player

#### - Model the wining rules (by summing following box values):

- 1+1+1= **3 yellow win** 
- -1-1-1 = **-3 red win**

This addition work in all possibles directions (vertical, horizontal, diagonals)

### 4 - Manage UX 

See [GameView](GameView.py)

### 5 - Link all

See [Game](Game.py)
