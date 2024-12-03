def main():
    with open('input.txt') as f:
        lines = f.readlines()

    mat = []
    for line in lines:
        row = line.strip().split()
        row = [int(x) for x in row]
        mat.append(row)

    print(f"{len(mat)} Reports to check ...")
    print(f"Part 1: {part1(mat)}")
    print(f"Part 2: {part2(mat)}")


def part1(mat: list) -> int:
    total_safe = 0
    for report in mat:
        if is_safe(report):
            total_safe += 1

    return total_safe


def part2(mat: list) -> int:
    total_safe = 0
    for report in mat:
        if any([is_safe(remove_index(report, i)) for i in range(len(report))]):
            total_safe += 1

    return total_safe


def is_safe(report: list) -> bool:
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    increasing = diffs[0] > 0
    for d in diffs:
        if increasing and d < 0:
            return False
        if not increasing and d > 0:
            return False
        if not (1 <= abs(d) <= 3):
            return False

    return True


def remove_index(arr: list, index: int) -> list:
    return arr[:index] + arr[index + 1:]


if __name__ == '__main__':
    main()
