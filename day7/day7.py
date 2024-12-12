def main():
    with open("input.txt") as f:
        data = f.readlines()

    equations = process_data(data)

    print("Part 1:", part1(equations))
    print("Part 2:", part2(equations))


def part1(equations: list) -> int:
    total = 0

    for target, nums in equations:
        if equation_valid(target, nums):
            total += target

    return total


def part2(equations: list) -> int:
    total = 0

    for target, nums in equations:
        if equation_valid_alt(target, nums):
            total += target

    return total


def equation_valid(target: int, nums: list) -> bool:
    # Base case
    if len(nums) == 1:
        return target == nums[0]

    # Checking addition
    if equation_valid(target, [nums[0] + nums[1]] + nums[2:]):
        return True

    # Checking multiplication
    if equation_valid(target, [nums[0] * nums[1]] + nums[2:]):
        return True

    return False


def equation_valid_alt(target: int, nums: list) -> bool:
    # Base case
    if len(nums) == 1:
        return target == nums[0]

    # Checking addition
    if equation_valid_alt(target, [nums[0]+nums[1]] + nums[2:]):
        return True

    # Checking multiplication
    if equation_valid_alt(target, [nums[0]*nums[1]] + nums[2:]):
        return True

    # Checking concatenation
    if equation_valid_alt(target, [int(str(nums[0])+str(nums[1]))] + nums[2:]):
        return True

    return False


def process_data(data: list):
    equations = []
    for line in data:
        target, nums = line.strip().split(":")
        nums = nums.strip().split(" ")

        target = int(target)
        nums = [int(x) for x in nums]

        equations.append((target, nums))

    return equations


if __name__ == '__main__':
    main()
