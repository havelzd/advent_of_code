import sys

args = sys.argv
DIRECTIONS = [
    ((0, 1), 'c'),
    ((0, -1), 'c'),
    ((1, 0), 'r'),
    ((-1, 0), 'r'),
]


def split_into_consecutive_sequences(sequence: list[int]):
    result = []
    used = [False] * len(sequence)

    for i in range(len(sequence)):
        if not used[i]:
            current_group = [sequence[i]]
            used[i] = True

            for j in range(i + 1, len(sequence)):
                if not used[j] and sequence[j] == current_group[-1] + 1:
                    current_group.append(sequence[j])
                    used[j] = True

            result.append(current_group)

    return len(result)


def count_lines(tuples: list[tuple[int, int]]):
    result = 0
    grouped = {}
    for x, y in tuples:
        if x in grouped:
            grouped[x].append(y)
        else:
            grouped[x] = [y]

    for x, ys in grouped.items():
        ys.sort()  # Sort y values
        result += split_into_consecutive_sequences(ys)
    return result


def mark_garden(grid: list[list[chr]], x: int, y: int):
    visited = set()
    queue = [(x, y)]
    garden_type = grid[x][y]
    perimeter, area = 0, 0
    rows, cols = [], []

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
                perimeter += 1
                if d == 'r':
                    rows.append((new_x, new_y))
                else:
                    cols.append((new_y, new_x))
    num_lines = count_lines(rows) + \
        count_lines(cols)
    return perimeter, area, visited, num_lines


def find_gardens(grid: list[list[chr]]):
    marked = set()
    result_p1 = 0
    result_p2 = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in marked:
                continue
            p, a, v, lines = mark_garden(grid, i, j)
            result_p1 += a * p
            result_p2 += a * lines
            marked.update(v)
    print(result_p1)
    print(result_p2)


with open(sys.argv[1]) as f:
    lines = f.readlines()
    map = []
    for line in lines:
        map.append(list(line.strip()))
    find_gardens(map)
