NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def main():
    with open("input.txt") as f:
        data = f.readlines()

    obst_map, visited, start_pos = parse_data(data)

    print("Part 1:", part1(obst_map, visited, start_pos))


def part1(obst_map: list, visited: list, start_pos: tuple) -> int:
    facing = NORTH

    m = len(obst_map)
    n = len(obst_map[0])

    i = start_pos[0]
    j = start_pos[1]

    while 0 <= i < m and 0 <= j < n:
        visited[i][j] = True

        if obstacle_in_front(obst_map, (i, j), facing):
            facing = turn_right(facing)

        i, j = move_forward((i, j), facing)

    return sum([sum(x) for x in visited])


def obstacle_in_front(obst_map: list, pos: tuple, facing: int) -> bool:
    try:
        if facing == NORTH:
            return obst_map[pos[0] - 1][pos[1]]
        elif facing == EAST:
            return obst_map[pos[0]][pos[1] + 1]
        elif facing == SOUTH:
            return obst_map[pos[0] + 1][pos[1]]
        elif facing == WEST:
            return obst_map[pos[0]][pos[1] - 1]
    except IndexError:
        return False


def move_forward(pos: tuple, facing: int) -> tuple:
    if facing == NORTH:
        return pos[0] - 1, pos[1]
    elif facing == EAST:
        return pos[0], pos[1] + 1
    elif facing == SOUTH:
        return pos[0] + 1, pos[1]
    elif facing == WEST:
        return pos[0], pos[1] - 1


def turn_right(facing: int) -> int:
    return (facing + 1) % 4


def parse_data(data: list) -> tuple:
    data = [x.strip() for x in data]

    m = len(data)
    n = len(data[0])

    obst_map = [[False for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    pos = None

    for i in range(m):
        for j in range(n):
            if data[i][j] == "#":
                obst_map[i][j] = True
            elif data[i][j] == "^":
                pos = (i, j)

    return obst_map, visited, pos


if __name__ == '__main__':
    main()
