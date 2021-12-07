from collections import Counter
from more_itertools import windowed

with open("2021_puzzle1.txt") as f:
    inp = [int(line.strip()) for line in f]


def part1(inplist: list) -> list:
    res = []
    increment = None
    cmp = 0
    for i, nr in enumerate(inplist):

        if nr < cmp:
            increment = '-'
        elif nr > cmp:
            increment = '+'
        else:
            increment = None
        res.append(dict(nr=nr, cmp=cmp, increment=(
            increment if i > 0 else None)))
        cmp = nr
    return res


cnter: Counter = Counter(d['increment'] for d in part1(inp))
print(f"Day1-Part1 - Answer: {cnter['+']}")


def part2(inplist: list) -> list:
    res = []
    windows = windowed(inplist, 3)
    for window in windows:
        res.append(sum(window))
    return res


cnter2: Counter = Counter(d['increment'] for d in part1(part2(inp)))
print(f"Day1-Part2 - Answer: {cnter2['+']}")
