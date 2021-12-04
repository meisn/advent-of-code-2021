from collections import Counter


def get_bits(inputlist):
    maxlen = max(len(i) for i in inputlist)
    minlen = min(len(i) for i in inputlist)
    if maxlen == minlen:
        res = dict()
        res['data'] = dict()
        gamma = ''
        epsilon = ''
        for i in range(maxlen):
            cnter = Counter(nr[i] for nr in inputlist)
            maxbit = cnter.most_common()[0][0]
            minbit = cnter.most_common()[1][0]
            gamma += maxbit
            epsilon += minbit
            res['data'].update({i: dict(maxbit=maxbit, minbit=minbit)})
        res.update(gamma=gamma, epsilon=epsilon, gammadec=int(
            gamma, 2), epsilondec=int(epsilon, 2))
    return res


def reduce_list(inputlist, searchpattern, searchposition):
    return [nr for nr in inputlist if nr[searchposition] == searchpattern]


def search_bits(inputlist, search):
    idx = 0 if search == "max" else 1
    haystack = inputlist[:]
    for i in range(12):
        cnter = Counter(nr[i] for nr in haystack)
        most_common = cnter.most_common()
        nrmax, nrmin = [v for k, v in most_common]
        if nrmax == nrmin:
            searchbit = "1" if search == "max" else "0"
        else:
            searchbit = most_common[idx][0]
        lst = reduce_list(haystack, searchbit, i)
        haystack = lst
        if len(lst) >= 2:
            continue
        else:
            return lst[0], int(lst[0], 2)


if __name__=='__main__':
    with open("2021_puzzle3.txt") as f:
        raw = [line.strip() for line in f]

    res = get_bits(raw)
    print(f"Answer Part1: {res['gammadec'] * res['epsilondec']}")

    oxygenbin, oxygendec = search_bits(raw, "max")
    nitrogenbin, nitrogendec = search_bits(raw, "min")

    print(f"Answer Part2: {oxygendec * nitrogendec}")
