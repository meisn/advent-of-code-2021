from typing import Callable

def accum1(direction: str, val: int, horizontal: int, depth: int, aim: int = 0) -> tuple:
    """
    Logic of part1, 'aim' not relevant
    """
    if direction == 'forward':
        horizontal += val
    elif direction == 'up':
        depth -= val
    else:
        depth += val
    
    return direction, val, horizontal, depth, aim


def accum2(direction: str, val: int, horizontal: int, depth: int, aim: int) -> tuple:
    """
    Logic of part2, 'aim' used for 'depth' calculation
    """
    if direction == 'forward':
        horizontal += val
        depth += aim*val
    elif direction == 'up':
        aim -= val
    else:
        aim += val
    
    return direction, val, horizontal, depth, aim


def calc_position(inplist: list, accumulator: Callable) -> dict:
    """Returns a dict for each step on the input."""
    horizontal = 0
    aim = 0
    depth = 0
    res = []
    for item in inplist:
        direction, val = item
        direction, val, horizontal, depth, aim = accumulator(
            direction, val, horizontal, depth, aim)
        res.append(dict(direction=direction, val=val, horizontal=horizontal,
                   aim=aim, depth=depth, product=horizontal*depth))
    return res


if __name__=='__main__':

    with open("2021_puzzle2.txt") as f:
        raw = []
        for line in f:
            direction, val = line.strip().split(" ")
            raw.append((direction, int(val)))

    part1 = calc_position(raw, accumulator=accum1)[-1]
    print(f"Part1 answer: {part1['product']}")

    part2 = calc_position(raw, accumulator=accum2)[-1]
    print(f"Part1 answer: {part2['product']}")
