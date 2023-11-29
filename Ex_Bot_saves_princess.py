# First AI exercise
"""
Princess Peach is trapped in one of the four corners of a square grid.
You are in the center of the grid and can move one step at a time in any of the four directions.
Can you rescue the princess?

Input format:
    The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid.
    This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45).
    The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Output format:
    Print out the moves you will take to rescue the princess in one go.
    The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input:
    3
    ---
    -m-
    p--
Sample output:
    DOWN
    LEFT
"""

n = int(input())

for i in range(n):
    str = input()
    str = [*str]
    if 'm' in str:
        y_m = i
        x_m = str.index('m')
    if 'p' in str:
        y_p = i
        x_p = str.index('p')

if y_m > y_p:
    for i in range(y_m-y_p):
        print('UP')

if y_m < y_p:
    for i in range(y_p-y_m):
        print('DOWN')

if x_m > x_p:
    for i in range(x_m-x_p):
        print('LEFT')

if x_m < x_p:
    for i in range(x_p-x_m):
        print('RIGHT')
