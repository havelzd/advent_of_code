import sys

args = sys.argv

p1 = 0
p2 = 0

DIRECTIONS = [
    ((0, 1), 'c'),
    ((0, -1), 'c'),
    ((1, 0), 'r'),
    ((-1, 0), 'r'),
]


def get_num_lines(tuples: set[tuple[int, int]], c):
    # group tuples by first element and count number of consecutive groups
    grouped = {}
    for x, y in tuples:
        if x in grouped:
            grouped[x].append(y)
        else:
            grouped[x] = [y]

    group_counts = {}

    for x, ys in grouped.items():
        ys.sort()  # Sort y values
        groups = 0
        for i in range(len(ys)):
            if i == 0 or ys[i] != ys[i - 1] + 1:  # Start of a new group
                groups += 1
        group_counts[x] = groups
    if c == 'I':
        print(group_counts)
    return sum(group_counts.values())


def mark_garden(grid, x, y):
    # calculate the perimeter and area of a garden for p1 "width"
    # of the sides and area as number of cells
    visited = set()
    queue = [(x, y)]
    garden_type = grid[x][y]
    perimeter, area = 0, 0
    rows, cols = set(), set()

    while queue:
        x, y = queue.pop(0)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        area += 1

        for dir in DIRECTIONS:
            (dx, dy), d = dir
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])\
                    and grid[new_x][new_y] == garden_type:
                queue.append((new_x, new_y))
            else:
                if garden_type == 'I':
                    print(f"({new_x}, {new_y}), {d}")
                perimeter += 1
                if d == 'r':
                    rows.add((new_x, new_y))
                else:
                    cols.add((new_y, new_x))
    if garden_type == 'I':
        print(f"rows: {rows}")
        print(f"cols: {cols}")
    num_lines = get_num_lines(rows, garden_type) + \
        get_num_lines(cols, garden_type)
    return perimeter, area, visited, num_lines


def find_gardens(grid):
    marked = set()
    result_p1 = 0
    result_p2 = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in marked:
                continue
            print(f"Garden [{grid[i][j]}]")
            p, a, v, lines = mark_garden(grid, i, j)
            result_p1 += a * p
            result_p2 += a * lines
            print(f"area: {a}, perimeter: {lines}")
            marked.update(v)
    print(result_p1)
    print(result_p2)


with open(sys.argv[1]) as f:
    lines = f.readlines()
    map = []
    for line in lines:
        map.append(list(line.strip()))
    find_gardens(map)
