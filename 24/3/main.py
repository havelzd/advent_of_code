import sys
import re

args = sys.argv

p1 = 0
p2 = 0


def solve_p1(lines):
    """
    Parse mul(int,int) instructions with two 1-3 digit numbers and multiply them
    """
    p1 = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in lines:
        matches = re.findall(regex, line)
        for match in matches:
            p1 += int(match[0]) * int(match[1])

    print(p1)
    pass


def solve_p2(lines):
    """
    Parse do() and don't() instructions working as a switch to enable or disable the multiplication
    Parse mul(int,int) instructions with two 1-3 digit numbers and multiply them
    """
    p2 = 0
    skip = False
    regex_mul_do_dont = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    for line in lines:
        matches = re.findall(regex_mul_do_dont, line)
        for match in matches:
            if 'mul' in match[0] and not skip:
                p2 += int(match[1]) * int(match[2])
            elif match[0] == 'do()':
                skip = False
            elif match[0] == "don't()":
                skip = True

    print(p2)


with open(sys.argv[1]) as f:
    lines = f.readlines()
    solve_p1(lines)
    solve_p2(lines)
