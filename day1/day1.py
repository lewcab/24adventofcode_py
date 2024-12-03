def main():
    with open('input.txt') as f:
        lines = f.readlines()

    list_l = []
    list_r = []
    for line in lines:
        n, m = line.strip().split()
        list_l.append(int(n))
        list_r.append(int(m))

    print(f"Part 1: {part1(list_l, list_r)}")
    print(f"Part 2: {part2(list_l, list_r)}")


def part1(list_l: list, list_r: list) -> int:
    sorted_l = sorted(list_l)
    sorted_r = sorted(list_r)
    n = len(sorted_l)

    total = 0
    for i in range(n):
        total += abs(sorted_l[i] - sorted_r[i])

    return total


def part2(list_l: list, list_r: list) -> int:
    freq_map = {}
    for x in list_r:
        if x not in freq_map:
            freq_map[x] = 1
        else:
            freq_map[x] += 1

    total = 0
    for y in list_l:
        if y in freq_map:
            total += y * freq_map[y]

    return total


if __name__ == '__main__':
    main()
