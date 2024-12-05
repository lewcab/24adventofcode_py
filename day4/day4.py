MATCH = "XMAS"
MATCH_LEN = len(MATCH)


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    data = [ln.strip() for ln in lines]
    m = len(data)
    n = len(data[0])

    print(f"Dimensions: {m} * {n}")

    print(f"Part 1: {part1(data, m, n)}")


def part1(data: list, m: int, n: int) -> int:
    total = 0
    for row in range(m):
        for col in range(n):
            if data[row][col] == MATCH[0]:
                total += match(data, row, col, m, n)

    return total


def match(data: list, row: int, col: int, m: int, n: int) -> int:
    # Brute force check for a match in all 8 directions
    matches = 0
    for i in range(8):
        comp = create_string(data, row, col, m, n, i)
        if comp == MATCH:
            matches += 1

    return matches


def create_string(data: list, row: int, col: int, m: int, n: int, dir: int) -> str:
    if dir == 0:
        # Right
        if col + MATCH_LEN > n:
            return ""
        else:
            return "".join([data[row][col + i] for i in range(MATCH_LEN)])

    elif dir == 1:
        # Left
        if col - MATCH_LEN + 1 < 0:
            return ""
        else:
            return "".join([data[row][col - i] for i in range(MATCH_LEN)])

    elif dir == 2:
        # Up
        if row + MATCH_LEN > m:
            return ""
        else:
            return "".join([data[row + i][col] for i in range(MATCH_LEN)])

    elif dir == 3:
        # Down
        if row - MATCH_LEN + 1 < 0:
            return ""
        else:
            return "".join([data[row - i][col] for i in range(MATCH_LEN)])

    elif dir == 4:
        # Up-Right
        if row + MATCH_LEN > m or col + MATCH_LEN > n:
            return ""
        else:
            return "".join([data[row + i][col + i] for i in range(MATCH_LEN)])

    elif dir == 5:
        # Up-Left
        if row + MATCH_LEN > m or col - MATCH_LEN + 1 < 0:
            return ""
        else:
            return "".join([data[row + i][col - i] for i in range(MATCH_LEN)])

    elif dir == 6:
        # Down-Right
        if row - MATCH_LEN + 1 < 0 or col + MATCH_LEN > n:
            return ""
        else:
            return "".join([data[row - i][col + i] for i in range(MATCH_LEN)])

    elif dir == 7:
        # Down-Left
        if row - MATCH_LEN + 1 < 0 or col - MATCH_LEN + 1 < 0:
            return ""
        else:
            return "".join([data[row - i][col - i] for i in range(MATCH_LEN)])

    return ""


if __name__ == '__main__':
    main()
