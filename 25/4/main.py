import sys

args = sys.argv


DIRS = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
    (1, 1),  # down-right
    (1, -1),  # down-left
    (-1, 1),  # up-right
    (-1, -1)  # up-left
]


def solve_p2(grid):
    p2 = 0
    while True:
        rolls = solve_p1(grid)
        if len(rolls) == 0:
            return p2
        p2 += len(rolls)
        for (i, j) in rolls:
            grid[i] = grid[i][:j] + '.' + grid[i][j+1:]

    return p2


def solve_p1(grid):
    rolls = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '@':
                continue
            num_rolls = 0
            for direction in DIRS:
                xd, yd = direction
                x, y = i + xd, j + yd
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '@':
                    num_rolls += 1
                    if num_rolls >= 4:
                        break
            if num_rolls < 4:
                rolls.append((i, j))

    return rolls


with open(sys.argv[1]) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    print(len(solve_p1(grid)))
    print(solve_p2(grid))
