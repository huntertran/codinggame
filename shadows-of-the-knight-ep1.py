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

    if bomb_dir == "U":
        max_y = y
        jump_x = 0
        jump_y = 0 - get_reversed_middle_pos(min_y, y)
    
    if bomb_dir == "UR":
        min_x = x
        max_y = y
        jump_x = get_middle_pos(max_x, x)
        jump_y = 0 - get_reversed_middle_pos(min_y, y)

    if bomb_dir == "R":
        min_x = x
        jump_x = get_middle_pos(max_x, x)
        jump_y = 0

    if bomb_dir == "DR":
        min_x = x
        min_y = y
        jump_x = get_middle_pos(max_x, x)
        jump_y = get_middle_pos(max_y, y)

    if bomb_dir == "D":
        min_y = y
        jump_x = 0
        jump_y = get_middle_pos(max_y, y)


    if bomb_dir == "DL":
        max_x = x
        min_y = y
        jump_x = 0 - get_reversed_middle_pos(min_x, x)
        jump_y = get_middle_pos(max_y, y)


    if bomb_dir == "L":
        max_x = x
        jump_x = 0 - get_reversed_middle_pos(min_x, x)
        jump_y = 0


    if bomb_dir == "UL":
        max_x = x
        max_y = y
        jump_x = 0 - get_reversed_middle_pos(min_x, x)
        jump_y = 0 - get_reversed_middle_pos(min_y, y)


    x = x + jump_x
    y = y + jump_y

    print("min X Y: " + str(min_x) + " " + str(min_y), file=sys.stderr, flush=True)
    print("max X Y: " + str(max_x) + " " + str(max_y), file=sys.stderr, flush=True)

    # the location of the next window Batman should jump to.
    print(str(x) + " " + str(y))
