import sys

args = sys.argv


def solve_p1(ranges, ids):
    p1 = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                p1 += 1
                break
    return p1


def solve_p2(ranges):
    p2 = 0
    ranges = sorted(ranges)
    merged = [ranges[0]]
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    for r in merged:
        p2 += r[1] - r[0] + 1
    return p2


with open(sys.argv[1]) as f:
    lines = f.read()
    ranges, ids = lines.split("\n\n")
    ranges = [[int(x[0]), int(x[1])]
              for x in (map(lambda x: x.split('-'), ranges.splitlines()))]
    ids = [int(x) for x in ids.splitlines()]
    print(solve_p1(ranges, ids))
    print(solve_p2(ranges))
