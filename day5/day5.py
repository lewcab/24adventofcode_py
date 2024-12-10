def main():
    with open("input.txt") as f:
        data = f.readlines()

    data = [ln.strip() for ln in data]

    rules, updates = parse_data(data)

    print(f"Part 1: {part1(rules, updates)}")
    print(f"Part 2: {part2(rules, updates)}")


def part1(rules: dict, updates: list) -> int:
    total = 0

    for u in updates:
        if is_update_correct(rules, u):
            total += u[len(u)//2]

    return total


def part2(rules: dict, updates: list) -> int:
    total = 0

    for u in updates:
        if not is_update_correct(rules, u):
            new_update = fix_update(rules, u)
            if is_update_correct(rules, new_update):
                total += new_update[len(new_update)//2]
            else:
                print(f"Failed to fix update: {u}")

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


def is_update_correct(rules: dict, update: list) -> bool:
    for i in range(1, len(update)):
        curr_page = update[i]
        page_rules = rules[curr_page]

        for j in range(i):
            # Check all previous pages if rules are broken
            prev_page = update[j]
            if prev_page in page_rules:
                return False

    return True


def fix_update(rules: dict, update: list) -> list:
    # Cheese solution, but it works. Basically sorts the list by the number of effective rules
    effective_rules = {}
    update_set = set(update)
    for u in update:
        effective_rules[u] = rules[u].intersection(update_set)

    new_update = [0 for _ in range(len(update))]
    for u in update:
        i = len(update) - len(effective_rules[u]) - 1
        new_update[i] = u

    return new_update


if __name__ == '__main__':
    main()
