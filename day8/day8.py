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
            outset = [set(s) for s in outraw.split() if s]
            retval.append(dict(inraw=inraw, inset=inset,
                          outraw=outraw, outset=outset))
        return tuple(retval)


if __name__ == "__main__":
    inp = read_input("2021_puzzle8.txt")