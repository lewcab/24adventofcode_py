def main():
    with open('input.txt') as f:
        lines = f.readlines()

    mat = []
    for line in lines:
        row = line.strip().split()
        row = [int(x) for x in row]
        mat.append(row)

    print(f"Part 1: {part1(mat)}")


def part1(mat: list) -> int:
    total_safe = 0
    for report in mat:
        if is_safe(report):
            total_safe += 1

    return total_safe


def is_safe(report: list) -> bool:
    increasing = report[0] < report[-1]

    prev = report[0]
    for i in range(1, len(report)):
        if increasing:
            if report[i] < prev:
                return False
            diff = abs(report[i] - prev)
            if not (1 <= diff <= 3):
                return False

        else:
            if report[i] > prev:
                return False
            diff = abs(report[i] - prev)
            if not (1 <= diff <= 3):
                return False

        prev = report[i]

    return True


if __name__ == '__main__':
    main()
