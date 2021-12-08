from collections import defaultdict

SEGMENTS = {0: set('abcefg'),
            1: set('cf'),
            2: set('acdeg'),
            3: set('acdfg'),
            4: set('bcdf'),
            5: set('abdfg'),
            6: set('abdefg'),
            7: set('acf'),
            8: set('abcdefg'),
            9: set('abcdfg'),
            }


def read_input(file):
    with open(file) as f:
        retval = []
        for line in f:
            inraw, outraw = line.strip().split(" | ")
            inset = [set(s) for s in inraw.split() if s]
            inlen = [len(s) for s in inraw.split() if s]
            outset = [set(s) for s in outraw.split() if s]
            outlen = [len(s) for s in outraw.split() if s]
            retval.append(dict(inraw=inraw, inset=inset, inlen=inlen,
                          outraw=outraw, outset=outset, outlen=outlen))
        return tuple(retval)


def answer1(inputlist, searchlist):
    res = defaultdict(int)
    for lst in inputlist:
        for nr in lst:
            if nr in searchlist:
                res[nr]+=1
    return res


if __name__ == "__main__":
    inp = read_input("2021_puzzle8.txt")
    len1 = [i['outlen'] for i in inp]
    ans1 = answer1(len1, [2,3,4,7])
    print(f"Answer1: {sum(ans1.values())}")