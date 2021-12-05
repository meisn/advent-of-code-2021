def read_puzzle(file) -> tuple[list, list]:

    with open(file) as f:

        raw = [line.strip() for line in f if line.strip()]
        numbers, *rest = raw
        numbers = [int(n) for n in numbers.split(",")]
        boards = []
        while rest:
            board, rest = rest[:5], rest[5:]
            boards.append(board)
        return numbers, boards


def prepare_grids(inp: list) -> list:

    lines = []
    for l in inp:
        res = [int(n) for n in l.split()]
        lines.append(res)
    return lines


def is_winner(grid:list, row:int, col:int) -> bool:

    grid[row][col] = -1
    if sum(grid[row]) == -5:
        return True
    if sum([row[col] for row in grid]) == -5:
        return True
    return False


def answer1(grids:list, grid_indexes:dict, number:int) -> int:
    

    for gridix, rowix, colix in grid_indexes:
        grid = grids[gridix]
        if is_winner(grid, rowix, colix):
            lst = []
            for i in range(5):
                for j in range(5):
                    lst.append(0 if grid[i][j] == -1 else grid[i][j])
            return sum(lst) * number
    return None


def answer2(grids:list, grid_indexes:dict, number:int, winners:list) -> int:

    for gridix, rowix, colix in grid_indexes:
        if gridix in winners:
            continue

        grid = grids[gridix]
        if is_winner(grid, rowix, colix):
            winners.append(gridix)

            if len(winners) == len(grids):
                lst = []
                for i in range(5):
                    for j in range(5):
                        lst.append(0 if grid[i][j] == -1 else grid[i][j])
                return sum(lst) * number
    return None


if __name__ == "__main__":
    #prepare
    numbers, rawboards = read_puzzle("2021_puzzle4.txt")
    boards = [prepare_grids(board) for board in rawboards]
    
    winnerboards = {}
    for num in numbers:
        winnerboards[num] = []
    for gridix, grid in enumerate(boards):
        for rowix, row in enumerate(grid):
            for colix, num in enumerate(row):
                if num in winnerboards:
                    winnerboards[num].append((gridix, rowix, colix))
    #part1

    ans = 0
    for num in numbers:
        ans = answer1(boards, winnerboards[num], num)
        if ans is not None:
            break

    print(f"Answer1: {ans}")

    #part2
    winners = []
    ans = None

    for num in numbers:
        ans = answer2(boards, winnerboards[num], num, winners)
        if ans is not None:
            break
    print(f'Answer2: {ans}')
