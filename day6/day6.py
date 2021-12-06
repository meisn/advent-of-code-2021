from collections import Counter, defaultdict


def read_input(file) -> dict[int, int]:
    with open(file) as f:
        return Counter(int(i) for i in f.read().strip().split(","))


def produce_fish(inpdict: dict, days: int) -> int:

    for _ in range(days):
        new_freq = defaultdict(int)
        for key in inpdict:
            if key == 0:
                new_freq[6] += inpdict[key]
                new_freq[8] = inpdict[key]
            else:
                new_freq[key - 1] += inpdict[key]
        inpdict = new_freq

    return sum(new_freq.values())


if __name__ == "__main__":
    inp = read_input("2021_puzzle6.txt")
    answer1 = produce_fish(inp, 80)
    answer2 = produce_fish(inp, 256)
    print(f"Answer1: {answer1}")
    print(f"Answer2: {answer2}")
