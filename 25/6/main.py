import sys

args = sys.argv


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p


def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


def solve_p1(nums, ops):
    p1 = 0

    for i in range(len(nums)):
        op = ops[i]
        acc = sum(nums[i]) if op == '+' else prod(nums[i])
        p1 += acc
    return p1


def solve_p2(nums, ops):
    p2 = 0

    transformed = []
    for i in range(len(nums)):
        op = ops[i]
        nums_str = list(map(str, nums[i]))
        max_len = max(map(len, nums_str))
        r = []
        for l in range(max_len):
            col = ""
            for n in nums_str:
                if l < len(n):
                    col += n[l]
            r.append(int(col))
        print(r)
        transformed.append(r)
    return solve_p1(transformed, ops)


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
    nums, ops = lines[:-1], lines[-1]
    nums = [[int(y) for y in x] for x in nums]
    print(solve_p1(transpose(nums), ops))
    print(solve_p2(transpose(nums), ops))
