import sys

args = sys.argv


def solve_p1(lines):
    # find all occurences of 'XMAS' horizontally, vertically, and diagonally in both directions
    p1 = 0
    # horizontal
    for line in lines:
        p1 += line.count('XMAS')
        p1 += line.count('SAMX')

    # vertical
    for i in range(len(lines[0])):
        col = ''.join([line[i] for line in lines])
        p1 += col.count('XMAS')
        p1 += col.count('SAMX')

    # diagonal
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if i + 3 < len(lines) and j + 3 < len(lines[0]):
                diag = ''.join([lines[i + k][j + k] for k in range(4)])
                p1 += diag.count('XMAS')
                p1 += diag.count('SAMX')
            if i - 3 >= 0 and j + 3 < len(lines[0]):
                diag = ''.join([lines[i - k][j + k] for k in range(4)])
                p1 += diag.count('XMAS')
                p1 += diag.count('SAMX')
    print(p1)
    pass


def solve_p2(lines):
    p2 = 0

    for i in range(len(lines) - 2):
        line1 = lines[i]
        line2 = lines[i + 1]
        line3 = lines[i + 2]

        # Ensure lines have enough length for the pattern
        for j in range(1, len(line2) - 1):
            # Check Diagonal 1 (top-left to bottom-right)
            diag1_mas = (line1[j - 1] == 'M' and line2[j]
                         == 'A' and line3[j + 1] == 'S')
            diag1_sam = (line1[j - 1] == 'S' and line2[j]
                         == 'A' and line3[j + 1] == 'M')

            # Check Diagonal 2 (top-right to bottom-left)
            diag2_mas = (line1[j + 1] == 'M' and line2[j]
                         == 'A' and line3[j - 1] == 'S')
            diag2_sam = (line1[j + 1] == 'S' and line2[j]
                         == 'A' and line3[j - 1] == 'M')

            # Ensure that both diagonals contain 'MAS' or 'SAM'
            if (diag1_mas or diag1_sam) and (diag2_mas or diag2_sam):
                p2 += 1

    print(p2)
    pass


with open(sys.argv[1]) as f:
    lines = f.readlines()
    solve_p2(lines)
