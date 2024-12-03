import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    memory = [ln.strip() for ln in lines]

    print(f"Number of lines: {len(memory)}")

    print(f"Part 1: {part1(memory)}")
    print(f"Part 2: {part2(memory)}")


def part1(memory: list) -> int:
    total = 0

    for line in memory:
        mult_list = re.findall(r'mul\(\d+,\d+\)', line)
        for mult_str in mult_list:
            total += get_mult(mult_str)

    return total


def part2(memory: list) -> int:
    total = 0

    enabled = True
    for line in memory:
        mult_matches = list(re.finditer(r'mul\(\d+,\d+\)', line))
        cond_matches = list(re.finditer(r'(do\(\))|(don\'t\(\))', line))

        mult_i = 0
        cond_i = 0

        while mult_i < len(mult_matches):
            curr_mult = mult_matches[mult_i]
            if cond_i < len(cond_matches):
                curr_cond = cond_matches[cond_i]
                curr_cond_start = curr_cond.start()
            else:
                curr_cond = cond_matches[-1]
                curr_cond_start = len(line) + 1

            if curr_mult.start() < curr_cond_start:
                if enabled:
                    total += get_mult(curr_mult.group())
                mult_i += 1

            else:
                if curr_cond.group() == "don't()":
                    enabled = False
                else:
                    enabled = True
                cond_i += 1

    return total


def get_mult(mult_str: str) -> int:
    nums = re.findall(r'\d+', mult_str)
    if len(nums) != 2:
        raise ValueError(f"Invalid input: {mult_str}")
    return int(nums[0]) * int(nums[1])


if __name__ == '__main__':
    main()
