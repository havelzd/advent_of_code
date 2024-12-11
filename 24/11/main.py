import sys

args = sys.argv

p1 = 0
p2 = 0

stones = {}
BLINKS = 75


def get_new_stones(num):
    snum = str(num)
    snum_len = len(snum)

    if num == 0:
        return [1]
    if snum_len % 2 == 0:
        return [int(snum[:snum_len//2]), int(snum[snum_len//2:])]
    else:
        return [num * 2024]


def solve(stones):
    for i in range(0, BLINKS):
        new_stones = {}
        for j, k in stones.items():
            new_stone = get_new_stones(j)
            for ns in new_stone:
                if ns in new_stones:
                    new_stones[ns] += k
                else:
                    new_stones[ns] = k
        stones = new_stones

    print(sum(stones.values()))
    pass


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        line = [int(x) for x in line.split()]
        for s in line:
            if s in stones:
                stones[s] += 1
            else:
                stones[s] = 1
solve(stones)
