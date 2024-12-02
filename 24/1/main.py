import sys

args = sys.argv

counts = {}

with open(sys.argv[1]) as f:
    lines = f.readlines()
    l, r = [], []
    for line in lines:
        a, b = map(int, line.split())
        l.append(a)
        r.append(b)
        counts[b] = 1 if b not in counts else counts[b] + 1

# sort arrays
l = sorted(l)
r = sorted(r)

p1 = 0
p2 = 0
for i in range(len(l)):
    p1 = p1 + abs(l[i] - r[i])
    p2 = p2 + (l[i] * (counts[l[i]] if l[i] in counts else 0))

print(p1)
print(p2)
