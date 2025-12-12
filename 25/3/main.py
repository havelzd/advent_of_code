import sys
from collections import Counter

args = sys.argv

p1 = 0


def solve_p1(lines):
    p1 = 0

    for line in lines:
        ll = len(line)
        x1, x2 = 0, 0
        for i in range(ll):
            num = int(line[i])

            if i < (ll - 1) and num > x1:
                x1 = num
                x2 = 0
            elif num > x2:
                x2 = num
        p1 += int(str(x1) + str(x2))

    return p1


def solve_p2(lines, num_digits):
    p2 = 0
    for line in lines:
        digits = []
        idx = 0
        for i in range(num_digits, 0, -1):
            sub_arr = line[idx:len(line) - i + 1]
            m = max(map(int, sub_arr))
            ms = str(m)
            digits.append(ms)
            idx += sub_arr.index(ms) + 1
        p2 += int(''.join(digits))

    return p2


with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = list(filter(lambda x: x, map(str.strip, lines)))
    print(solve_p1(lines))
    print(solve_p2(lines, 12))
