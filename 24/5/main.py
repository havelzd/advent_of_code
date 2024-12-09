import sys
from functools import cmp_to_key

args = sys.argv


def parse_precedence(rules):
    preceedence = {}
    prec2 = {}
    rules = rules.split("\n")
    for rule in rules:
        a, b = rule.split("|")
        a, b = int(a), int(b)
        lta = preceedence.get(a, [])
        gta = prec2.get(b, [])
        lta.append(b)
        gta.append(a)
        preceedence[a] = lta
        prec2[b] = gta
    return preceedence, prec2


def solve(rules, update):
    """
        Parse rules given as a|b\n meaning a preceeds b
        Update is a list of sequences, for each sequence verify if its
        in correct based on given rules
    """
    p1 = 0
    p2 = 0
    rules, prec2 = parse_precedence(rules)

    update = update.split("\n")
    for seq in update:
        if seq == "":
            break
        seq = list(map(int, seq.split(",")))
        s = set()
        is_valid = True
        for i in seq:
            if i in s:
                is_valid = False
                break
            gta = prec2.get(i, [])
            for g in gta:
                s.add(g)
        if is_valid:
            p1 += seq[int(len(seq) / 2)]
        else:
            # sort the sequence in correct order based on preceedence
            seq = sorted(seq, key=cmp_to_key(lambda x,
                         y: 1 if x in prec2.get(y, []) else -1))
            p2 += seq[int(len(seq) / 2)]

    print("P1:", p1)
    print("P2:", p2)
    pass


with open(sys.argv[1]) as f:
    all = f.read()
    rules, update = all.split("\n\n")
solve(rules, update)
