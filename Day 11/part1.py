def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")
    input_list = [ [int(value) for value in line ] for line in input_list ]
    
    STEPS = 100
    flashes = total_flashes(input_list, STEPS)
    print(f"Total flashes: {flashes}")
    return

def total_flashes(input_list, steps):
    n_flashes = 0

    while steps > 0:
        for i, line in enumerate(input_list):
            for j, value in enumerate(line):
                input_list[i][j] += 1
        to_zero = []
        for i, line in enumerate(input_list):
            for j, value in enumerate(line):
                if value > 9:
                    n_flashes += 1
                    input_list[i][j] = 0
                    to_zero.append( (i, j) )

                    adjacent = get_adjacent(input_list, i, j)
                    n_flashes += bonus_flashes(input_list, adjacent, to_zero)
        steps -= 1
    return n_flashes


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
    n_flashes = 0
    for position in to_check:
        if position not in to_zero:
            i, j = position
            input_list[i][j] += 1
            if input_list[i][j] > 9:
                n_flashes += 1
                input_list[i][j] = 0
                to_zero.append(position)

                adjacent = get_adjacent(input_list, i, j)
                n_flashes += bonus_flashes(input_list, adjacent, to_zero)

    return n_flashes


if __name__ == "__main__":
    main()

