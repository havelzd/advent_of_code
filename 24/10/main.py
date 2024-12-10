import sys

args = sys.argv

p1 = 0
p2 = 0

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve_p1(grid):
    p1 = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                p1 += spt((i, j), grid)
    print(p1)


def spt(start, grid):
    q = [start]
    # visited = set()
    p1 = 0
    while len(q):
        current = q.pop(0)
        x, y = current
        current_value = grid[x][y]

        # if current in visited:
        #     continue

        if current_value == 9:
            # visited.add(current)
            p1 += 1
            continue

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                next_value = grid[nx][ny]
                if current_value + 1 == next_value:
                    q.append((nx, ny))

    return p1


with open(sys.argv[1]) as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append([int(c) for c in line.strip()])
# print(grid)
solve_p1(grid)
