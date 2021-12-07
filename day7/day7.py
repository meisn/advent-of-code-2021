from collections import Counter, defaultdict
from itertools import product


def read_input(file) -> list:
    with open(file) as f:
        return [int(i) for i in f.read().strip().split(",")]


def calc_delta_answer1(inputlist: list) -> dict:
    retval = defaultdict(int)
    checks = set(inputlist)
    for checknumber, number in product(checks, inputlist):
        delta = abs(checknumber - number)
        retval[checknumber] += delta
    return retval


def calc_delta(inputlist: list, exponential=False) -> dict:
    """Refined solution for both answers. Surely not the most efficient..."""
    retval = defaultdict(int)
    checks = set(inputlist)
    for checknumber, number in product(checks, inputlist):
        delta = abs(checknumber - number)
        if exponential:
            delta = sum(range(delta+1))
        retval[checknumber] += delta
    return retval


if __name__ == "__main__":
    inp = read_input("2021_puzzle7.txt")
    #inp = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14] #test
    answer = calc_delta(inp)
    answer1 = min(answer.items(), key=lambda x: x[1])
    print(f"Answer1 (pos, cost): {answer1}")
    answer = calc_delta(inp, True)
    answer2 = min(answer.items(), key=lambda x: x[1])
    print(f"Answer2 (pos, cost): {answer2}")
