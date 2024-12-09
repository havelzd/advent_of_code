import sys

args = sys.argv

p1 = 0
p2 = 0

antennas = {}
h, w = 0, 0


def is_in_bounds(x, y, h, w):
    return x >= 0 and x < h and y >= 0 and y < w


def solve_p1(antennas, lines, h, w):
    p1 = 0
    for k, v in antennas.items():
        for i in range(0, len(v)):
            for j in range(i + 1, len(v)):
                diff = (v[i][0] - v[j][0], v[i][1] - v[j][1])
                x, y = v[i][0], v[i][1]
                while True:
                    x, y = x + diff[0], y + diff[1]
                # print(v[i], v[j], diff)
                # check if in bounds
                # print(x, y)
                    if is_in_bounds(x, y, h, w):
                        if lines[x][y] != '#':
                            lines[x][y] = '#'
                            p1 += 1
                    else:
                        break
                x, y = v[j][0], v[j][1]
                while True:
                    # generate new pos against v[i]
                    x, y = x - diff[0], y - diff[1]

                # print(x, y)
                    if is_in_bounds(x, y, h, w):
                        if lines[x][y] != '#':
                            lines[x][y] = '#'
                            p1 += 1
                    else:
                        break
    for line in lines:
        for c in line:
            if c != '.' and c != '#':
                p1 += 1
    print()
    for line in lines:
        print(''.join(line))
    print()
    print(p1)


with open(sys.argv[1]) as f:
    lines = [c for c in map(str.strip, f.readlines())]
    # lines to list of lists of chars
    lines = [list(c) for c in lines]
    h = len(lines)
    w = len(lines[0])

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            c = lines[i][j]
            pos = (i, j)
            if c != '.':
                if c in antennas:
                    antennas[c].append(pos)
                else:
                    antennas[c] = [pos]
solve_p1(antennas, lines, h, w)
