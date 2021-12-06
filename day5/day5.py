def read_input(file):
    with open(file) as f:
        raw = [line.strip() for line in f]
        result = []
        for line in raw:
            first, second = line.split(" -> ")
            x1, y1 = [int(i) for i in first.split(",")]
            x2, y2 = [int(i) for i in second.split(",")]
            result.append(((x1, y1), (x2, y2)))
        return result
            

def get_points(points:tuple):
    (x1, y1), (x2, y2) = points
    return x1, y1, x2, y2


def process_lines(inplist:list, zeroes:bool):
    pts = set()
    cross = set()
    for line in inplist:
        x1, y1, x2, y2 = get_points(line)
        delta = (x2-x1, y2-y1)
        if 0 in delta or zeroes:
            if 0 in delta:
                irange = range(x1,x2+1) if delta[0] > 0 else range(x2,x1+1)
                jrange = range(y1,y2+1) if delta[1] > 0 else range(y2,y1+1)
                for i in irange:
                    for j in jrange:
                        leng = len(pts)
                        pts.add((i,j))
                        if leng == len(pts):
                            cross.add((i,j))
            else:
                slope = delta[1]//delta[0]
                for i in range(abs(delta[0])+1):
                    leng = len(pts)
                    pt = (x2+i,y2+slope*i) if delta[0] < 0 else (x1+i,y1+slope*i)
                    pts.add(pt)
                    if leng == len(pts):
                        cross.add(pt)


    return len(cross)


if __name__ == "__main__":
    inp = read_input("2021_puzzle5.txt")
    answer1 = process_lines(inp, False)
    answer2 = process_lines(inp, True)
    print(f"Answer 1: {answer1}")
    print(f"Answer 2: {answer2}")
