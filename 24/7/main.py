import sys
import itertools as it

args = sys.argv

p2 = 0


op_per_len = {}


def evaluate(eq):
    # evaluate equation left to right
    res = eq[0]
    for i in range(1, len(eq), 2):
        if eq[i] == "+":
            res += eq[i + 1]
        elif eq[i] == "*":
            res *= eq[i + 1]
        elif eq[i] == "||":
            # concat numbers
            res = int(str(res) + str(eq[i + 1]))
    return res


def prepare_equation(equation, operators):
    result, numbers = equation
    for op in operators:
        # merge numbers with operators into a single list
        eq = zip(numbers, [*op, ''])
        # flatten the tuple into a single list excluding ''
        eq = [x for y in eq for x in y if x != '']
        res = evaluate(eq)
        if res == result:
            return res

    return False


def solve_p1(equations):
    # for each equation find possible operators (addition, multiplication)
    # joining numbers, evaluated left to right for which the equation holds
    p1 = 0
    for equation in equations:
        eq_ops = op_per_len[len(equation[1])]
        res = prepare_equation(equation, eq_ops)
        if res:
            p1 += res

    print("Part 1: ", p1)


with open(sys.argv[1]) as f:
    lines = f.readlines()
    equations = []
    for line in lines:
        result, numbers = line.split(":")
        result, numbers = int(result), list(map(int, numbers.split()))
        equations.append((result, numbers))
        n = len(numbers)
        if n not in op_per_len:
            eq_ops = list(it.product(["*", "+", "||"], repeat=n-1))
            op_per_len[n] = eq_ops
    solve_p1(equations)
    pass
