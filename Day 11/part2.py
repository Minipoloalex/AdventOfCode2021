def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")
    input_list = [ [int(value) for value in line ] for line in input_list ]

    step_all_flash = all_flash(input_list)
    print(f"First step when all dumbo octopuses flash: {step_all_flash}")

    return


def all_flash(input_list):
    steps = 1
    while True:
        for i, line in enumerate(input_list):
            for j, value in enumerate(line):
                input_list[i][j] += 1
        to_zero = set()
        for i, line in enumerate(input_list):
            for j, value in enumerate(line):
                if value > 9:
                    input_list[i][j] = 0
                    to_zero.add( (i, j) )

                    adjacent = get_adjacent(input_list, i, j)
                    bonus_flashes(input_list, adjacent, to_zero)
        if len(to_zero) == len(input_list) * len(input_list[0]):
            return steps
        steps += 1
    return


def get_adjacent(input_list, i, j):
    adjacent = []
    # i - 1
    if i > 0:
        adjacent.append((i - 1, j))
        if j > 0:
            adjacent.append((i - 1, j - 1))
        if j < len(input_list[0]) - 1:
            adjacent.append((i - 1, j + 1))
    # i + 1
    if i < len(input_list) - 1:
        adjacent.append((i + 1, j))
        if j > 0:
            adjacent.append((i + 1, j - 1))
        if j < len(input_list[0]) - 1:
            adjacent.append((i + 1, j + 1)) 
    # i
    if j > 0:
        adjacent.append((i, j - 1))
    if j < len(input_list[0]) - 1:
        adjacent.append((i, j + 1))

    return adjacent


def bonus_flashes(input_list, to_check, to_zero):
    for position in to_check:
        if position not in to_zero:
            i, j = position
            input_list[i][j] += 1
            if input_list[i][j] > 9:
                input_list[i][j] = 0
                to_zero.add(position)

                adjacent = get_adjacent(input_list, i, j)
                bonus_flashes(input_list, adjacent, to_zero)
    return None


if __name__ == "__main__":
    main()

