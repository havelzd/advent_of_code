import sys
import ast

args = sys.argv


def bfs(start, end, states, joltage=None):
    queue = [(start, 0, None if joltage else 0)]
    visited = set()

    while queue:
        current, depth = queue.pop(0)
        if (not joltage and current == end) or (joltage and current == joltage):
            return depth
        if not joltage and current in visited:
            continue
        visited.add(current)
        for button, next in states[current]:
            if next not in visited:
                queue.append((next, depth + 1))
    return -1


def next_state(current, button):
    next = list(current)
    for pos in button:
        next[pos] = "#" if current[pos] == "." else "."
    return "".join(next)


def create_automaton(switches, buttons):
    start = "." * len(switches)

    states = {}

    new_states = [start]

    while new_states:
        current = new_states.pop()
        transitions = []
        for b in buttons:
            next = next_state(current, b)
            transitions.append((b, next))
            if next not in states:
                new_states.append(next)
        states[current] = transitions

    return states


def solve_p1(diagrams):
    p1 = 0
    for line in diagrams:
        switches = line[0]
        buttons = line[1]
        automaton = create_automaton(switches, buttons)
        start = "." * len(switches)
        p1 += bfs(switches, start, automaton, joltage)
    return p1


def solve_p2(diagrams):
    p2 = 0
    for line in diagrams:
        switches = line[0]
        buttons = line[1]
        joltage = line[2]
        automaton = create_automaton(switches, buttons)
        start = "." * len(switches)
        p2 += bfs(switches, start, automaton, joltage)
    return p2


with open(sys.argv[1]) as f:
    lines = f.readlines()

    diagrams = []
    for line in lines:
        tokens = line.strip().split()
        switches = tokens[0].replace("[", "").replace("]", "")
        buttons = [ast.literal_eval(t) for t in tokens[1:-1]]
        buttons = [x if isinstance(x, tuple) else (x,) for x in buttons]
        print(buttons)
        joltage = tokens[-1]

        diagrams.append((switches, buttons, joltage))
    print(solve_p1(diagrams))
