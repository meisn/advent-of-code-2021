from collections import defaultdict
from itertools import product


def read_input(file) -> list:
    with open(file) as f:
        return [int(i) for i in f.read().strip().split(",")]


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


class Delta:
    """Cache/Stack to reduce the calculation time by looking up already calculated values.
    
    Stores tuple of delta, exponentialdelta per check/deltanumber
    """
    def __init__(self) -> None:
        self.cache = dict()

    def __call__(self, minuend, subtrahend) -> tuple:
        delta = abs(minuend - subtrahend)
        if delta in self.cache:
            return self.cache[delta]
        self.cache[delta] = delta, sum(range(delta+1))
        return self.cache[delta]


def calc_delta_optimized(inputlist: list, exponential=False) -> dict:
    """Refined solution for both answers. Surely not the most efficient..."""
    retval = defaultdict(int)
    checks = set(inputlist)
    deltacalc = Delta()
    for checknumber, number in product(checks, inputlist):
        deltaval = deltacalc(checknumber, number)
        delta = deltaval[0]
        if exponential:
            delta = deltaval[1]
        retval[checknumber] += delta
    return retval


if __name__ == "__main__":
    inp = read_input("2021_puzzle7.txt")
    #inp = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14] #test
    answer = calc_delta_optimized(inp)
    answer1 = min(answer.items(), key=lambda x: x[1])
    print(f"Answer1 (pos, cost): {answer1}")
    answer = calc_delta_optimized(inp, True)
    answer2 = min(answer.items(), key=lambda x: x[1])
    print(f"Answer2 (pos, cost): {answer2}")
