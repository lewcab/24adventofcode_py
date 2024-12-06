def main():
    with open("input.txt") as f:
        data = f.readlines()

    data = [ln.strip() for ln in data]

    rules, updates = parse_data(data)

    print(f"Part 1: {part1(rules, updates)}")


def part1(rules: dict, updates: list) -> int:
    total = 0

    for u in updates:
        broken = False
        for i in range(1, len(u)):
            curr_page = u[i]
            page_rules = rules[curr_page]

            for j in range(i):
                # Check all previous pages if rules are broken
                prev_page = u[j]
                if prev_page in page_rules:
                    broken = True
                    break

            if broken:
                break

        if not broken:
            total += u[len(u)//2]

    return total


def parse_data(data: list) -> tuple:
    rules = {}
    updates = []

    i = 0
    while data[i] != "":
        before, after = data[i].split("|")
        before = int(before)
        after = int(after)

        if before not in rules:
            rules[before] = {after}
        else:
            rules[before].add(after)
        i += 1

    i += 1
    while i < len(data):
        page = data[i].split(",")
        page = [int(p) for p in page]
        updates.append(page)
        i += 1

    return rules, updates


if __name__ == '__main__':
    main()
