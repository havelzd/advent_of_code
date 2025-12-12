import sys

args = sys.argv


def part_1(ranges):
    p1 = 0
    for r in ranges:
        start, end = int(r[0]), int(r[1])

        for i in range(start, end + 1):
            if i % 2 != 0:
                continue
            s = str(i)
            if s[:len(s)//2] == s[len(s)//2:]:
                p1 += i
    return p1


def part_2(ranges):
    p2 = 0
    for r in ranges:
        start, end = int(r[0]), int(r[1])

        for i in range(start, end + 1):
            s = str(i)
            ls = len(s)
            for j in range(1, ls//2 + 1):
                if ls % j != 0:
                    continue
                if s[:j] * (ls // j) == s:
                    p2 += i
                    break

    return p2


with open(sys.argv[1]) as f:
    content = f.read()
    ranges = list(map(lambda x: x.split("-"), content.strip().split(",")))
    print(part_1(ranges))
    print(part_2(ranges))
