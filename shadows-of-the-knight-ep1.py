# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

def get_middle_pos(max, current):
    return int(abs((max-current) / 2))

def get_reversed_middle_pos(min, current):
    result = int(abs((min-current) / 2))
    if result == 0:
        result = 1
    return result

x = x0
y = y0

print("W: " + str(w), file=sys.stderr, flush=True)
print("H: " + str(h), file=sys.stderr, flush=True)

min_x = 0
min_y = 0

max_x = w
max_y = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    jump_x = 0
    jump_y = 0

    if "U" in bomb_dir:
        max_y = y
        jump_y = 0 - get_reversed_middle_pos(min_y, y)
    
    if "D" in bomb_dir:
        min_y = y
        jump_y = get_middle_pos(max_y, y)

    if "L" in bomb_dir:
        max_x = x
        jump_x = 0 - get_reversed_middle_pos(min_x, x)

    if "R" in bomb_dir:
        min_x = x
        jump_x = get_middle_pos(max_x, x)


    x = x + jump_x
    y = y + jump_y

    # the location of the next window Batman should jump to.
    print(str(x) + " " + str(y))
