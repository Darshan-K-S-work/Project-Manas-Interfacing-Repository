import time
import random

from mymodule import snakes, ladders, bite, climb, board, dice, play

chance = 0
p1pos = 0
p2pos = 0
arr = []
num = []
d = 0

k = list(snakes.keys())
l = list(ladders.keys())


def welcome():  # Welcome screen, player names and the toss
    global p1
    global p2
    input("\n\t\t\t...SNAKES AND LADDERS...\n\t\t\t\t\t\t-Darshan K S\n\n\t\t\t\tPress Any Key\n")
    time.sleep(1)
    msg = """\a
    Welcome to Snake and Ladder Game.
    Rules-
    \t1. Both players start at Box 0.
    \t2. Hit ENTER to Roll the Dice.
    \t3. The first one to reach Box 100 wins.\n
    """
    print(msg)
    time.sleep(2)
    # Input player names
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")

    print("\t\tMatch between "+p1+" and "+p2+"!")
    # Toss
    c = random.randint(1, 2)

    if (c == 1):
        print("\nPlayer "+p1+" won the Toss.\n")
        return 1
    elif (c == 2):
        print("\nPlayer "+p2+" won the Toss\n")
        return 2


chance = welcome()
time.sleep(2)
board(arr, num, k, l)
time.sleep(2)
play(chance, p1, p2, p1pos, p2pos, d, k, l, bite, climb)
time.sleep(7)
