import sys

args = sys.argv

p1 = 0
p2 = 0

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "V": (1, 0)
}

turn_right = {
    ">": "V",
    "V": "<",
    "<": "^",
    "^": ">"
}


def get_new_coordinates(pos, dir):
    x, y = pos
    dx, dy = dir
    x += dx
    y += dy
    return x, y


def walk_guard(guard: tuple[str, int], lines):
    # simulate guard walking in the grid,
    # if guard would hit '#' turn right
    # if guard leaves the grid, remove him from list
    # mark all visited cells with X

    # copy lines, and guards
    nlines = [line.copy() for line in lines]
    h, w = len(nlines), len(nlines[0])
    p1 = 0
    visited = set()

    (x, y), dir = guard

    while True:
        # Check if we've been in this state before
        state = (x, y, dir)
        if state in visited:
            return False, None, None  # Cycle detected
        visited.add(state)

        # Compute next position
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy

        # Out of bounds
        if not (0 <= nx < h and 0 <= ny < w):
            break
        if nlines[nx][ny] == "#":
            dir = turn_right[dir]
            nx, ny = x, y
        elif nlines[nx][ny] != "X":
            nlines[nx][ny] = "X"
            p1 += 1
        x, y = nx, ny

    return True, nlines, p1


guards = []

p2 = 0

with open(sys.argv[1]) as f:
    lines = list(map(str.strip, f.readlines()))
    # unwrap each line linto list of characted
    # get position of guards marked as <, > or ^, V
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "<" or c == ">" or c == "^" or c == "V":
                g = ((i, j), c)
                guards.append(g)

lines = list(map(list, lines))

succ, marked, p1 = walk_guard(
    ((guards[0][0][0], guards[0][0][1]), guards[0][1]), lines)

print(p1)

for i in range(len(marked)):
    for j in range(len(marked[i])):
        if marked[i][j] == "X":
            lines[i][j] = "#"
            succ, _, _ = walk_guard(
                ((guards[0][0][0], guards[0][0][1]), guards[0][1]), lines)
            if not succ:
                p2 += 1
            lines[i][j] = "."
print(p2)
