import sys


def part_1(content, start=50):
    password = 0
    for line in content.splitlines():
        dir, num = line[0], int(line[1:])
        num *= 1 if dir == 'R' else -1

        start += num
        start %= 100

        if start == 0:
            password += 1

    return password


def part_2(content, start=50):
    password = 0

    for line in content.splitlines():
        dir, num = line[0], int(line[1:])
        clicks = abs(num) // 100
        password += clicks

        num %= 100

        if dir == 'R':
            if start + num > 99:
                password += 1
            start = (start + num) % 100
        if dir == 'L':
            if start and start - num <= 0:
                password += 1
            start = (start - num) % 100

    return password


with open(sys.argv[1], 'r') as file:
    content = file.read()
    print(part_1(content))
    print(part_2(content))
