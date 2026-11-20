====================================================
SNAKES AND LADDERS PLUS
====================================================

Author: Huy
Language: Python
Version: Classic / Plus Edition

----------------------------------------------------
DESCRIPTION
----------------------------------------------------

This project is a text-based implementation of the
classic Snakes and Ladders board game.

The game supports two game modes:

1. Classic
   - Traditional Snakes and Ladders gameplay.
   - Players roll a die and race to tile 100.
   - Snakes move players backwards.
   - Ladders move players forwards.

2. Plus
   - Includes all Classic mode features.
   - Adds reward tiles.
   - Adds collectible items.
   - Adds temporary buffs.

----------------------------------------------------
FEATURES
----------------------------------------------------

1-4 Players

Visual board representation using tabulate

Classic snakes and ladders

Exact landing required to reach tile 100

Extra turn when rolling a 6

Replay option after game ends

PLUS MODE FEATURES

Reward tiles

Reward tiles:
7, 28, 35, 42, 70, 77, 91

Landing on a reward tile grants a random reward.

----------------------------------------------------
ITEMS
----------------------------------------------------

Items can be stored and used before rolling.
Once you have an item in your inventory, you will not have a second same item even when you get it from reward tiles unless you used the first one.
Items do not stack effects.
You can use only 1 item each turn.

ROLL TWICE
- Roll the die twice and add the results.

2X MULTIPLIER
- Roll the die and double the result.

CUSTOM DIE
- Choose the die value manually
  (between 1 and 6).

----------------------------------------------------
BUFFS
----------------------------------------------------

ADVANCE
- Move an additional 1 to 3 tiles.

SHIELD
- Ignore the next snake encountered.
- You can only have 1 shield at a time.

EXTRA TURN
- Immediately gain an additional turn.

JACKPOT
- Instantly move to tile 99.

----------------------------------------------------
BOARD ELEMENTS
----------------------------------------------------

SNAKES

23 -> 8
34 -> 12
43 -> 17
54 -> 21
61 -> 39
73 -> 45
84 -> 51
92 -> 67

LADDERS

5  -> 33
11 -> 36
14 -> 63
25 -> 56
31 -> 49
40 -> 78
52 -> 89
68 -> 97

----------------------------------------------------
REQUIREMENTS
----------------------------------------------------

Python 3.x

Required package:

tabulate

Install with:

pip install tabulate

----------------------------------------------------
RUNNING THE GAME
----------------------------------------------------

Run:

python snakes_and_ladders.py

Gameplay flow:

1. Enter number of players.
2. Enter player names.
3. Select Classic or Plus mode.
4. Take turns rolling the die.
5. Reach tile 100 first to win.

----------------------------------------------------
FUTURE IDEAS
----------------------------------------------------

- Trick tiles
- Debuff system
- GUI version using Tkinter
- Pygame version
- Online multiplayer
- Save/load system
- AI opponents

----------------------------------------------------
KNOWN LIMITATIONS
----------------------------------------------------

- Terminal-based interface.
- No save system.
- No graphical board.
- No multiplayer networking.

----------------------------------------------------
LICENSE
----------------------------------------------------

Personal learning project.

Feel free to modify and expand the game.