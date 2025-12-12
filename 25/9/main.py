import sys

args = sys.argv


def solve_p1(tiles):
    p1 = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] == tiles[j]:
                continue
            # Calculate area of rectangle formed by tiles[i] and tiles[i+1]
            width = abs(tiles[j][0] - tiles[i][0]) + 1
            height = abs(tiles[j][1] - tiles[i][1]) + 1
            p1 = max(width * height, p1)
    return p1


def solve_p2():
    p2 = 0
    return p2


with open(sys.argv[1]) as f:
    tiles = [tuple(map(int, line.strip().split(",")))
             for line in f.readlines()]
    print(tiles)
    print("Part 1:", solve_p1(tiles))
