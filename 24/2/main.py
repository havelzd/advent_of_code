import sys

args = sys.argv

p1 = 0
p2 = 0


def __is_safe(level):
    ps = []
    for i in range(len(level)-1):
        ps.append((level[i] - level[i+1]))
    tone = 1 if all(i > 0 for i in ps) else - \
        1 if all(i < 0 for i in ps) else 0
    diff = all(abs(i) > 0 and abs(i) <= 3 for i in ps)
    is_correct_tone = tone == 1 or tone == -1
    return tone, is_correct_tone, diff


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        level = list(map(int, line.split()))

        tone, is_correct_tone, diff = __is_safe(level)

        if is_correct_tone and diff:
            p1 = p1 + 1
            p2 = p2 + 1
        # part 2
        else:
            for i in range(len(level)):
                # take one number out and measure again
                level_subset = level[:i] + level[i+1:]
                tone, is_correct_tone, diff = __is_safe(level_subset)
                if is_correct_tone and diff:
                    p2 = p2 + 1
                    break


print(p1)
print(p2)
