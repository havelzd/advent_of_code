import sys

args = sys.argv

p1 = 0
p2 = 0

door_pad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]
robot_pad = [
    [None, '^', 'A',],
    ['<', 'v', '>']]


def make_dict(pad):
    pad_dict = {}
    for i, line in enumerate(pad):
        for j, value in enumerate(line):
            if not value:
                continue
            pad_dict[(i, j)] = value
            pad_dict[value] = (i, j)
    return pad_dict


door_pad_dict = make_dict(door_pad)
robot_pad_dict = make_dict(robot_pad)


def move(start, end, pad):
    (sy, sx), (ey, ex) = start, end
    dy, dx = ey - sy, ex - sx
    h = ("v" if dy > 0 else "^" if dy < 0 else "") * \
        abs(dy)
    w = (">" if dx > 0 else "<" if dx < 0 else "") * \
        abs(dx)
    if dx > 0 and (ey, sx) in pad:
        return h+w
    if (sy, ex) in pad:
        return w+h
    return h+w


def find_path_counts(seq, pad):
    counts = {}
    nseq = ['A', *seq]
    for i in range(len(nseq)-1):
        curr, next = nseq[i], nseq[i+1]
        partial_new_seq = move(pad[curr], pad[next], pad) + 'A'
        counts[partial_new_seq] = counts.get(partial_new_seq, 0) + 1
    return counts


def find_final_seq(code, reps):
    door_seq = {code: 1}
    for i in range(reps):
        new_seq_counts = {}
        for seq, count in door_seq.items():
            sub_seq_counts = find_path_counts(
                seq, robot_pad_dict if i > 0 else door_pad_dict)
            for k, v in sub_seq_counts.items():
                new_seq_counts[k] = new_seq_counts.get(
                    k, 0) + sub_seq_counts.get(k, 0) * count
        door_seq = new_seq_counts
    return door_seq


with open(sys.argv[1]) as f:
    codes = [code.strip() for code in f.readlines()]
    # part1
    for code in codes:
        final_seq = find_final_seq(code, 3)
        p1 += sum([len(k) * v for k, v in final_seq.items()]) * int(code[:-1])

    # part2
    for code in codes:
        final_seq = find_final_seq(code, 26)
        p2 += sum([len(k) * v for k, v in final_seq.items()]) * int(code[:-1])

print(p1)
print(p2)
