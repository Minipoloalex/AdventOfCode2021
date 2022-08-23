def main():
    DAYS = 256
    with open("input.txt", "r") as input_file:
        input_string = input_file.read()
        input_string = input_string.rstrip("\n")
    input_list = input_string.split(",")
    n_lanternfish = lanternfish_reproduce(input_list, DAYS)
    print(f"Number of lanternfish after {DAYS} days: {n_lanternfish}")
    return

def lanternfish_reproduce(input_list, days):              ## Only difference to part1 is the days
    fish_dict = [ 0 for _ in range(9) ]         ## works like a dictionary
    for fish in input_list:
        fish_dict[int(fish)] += 1

    while days > 0:
        new_fish_dict = [ 0 for _ in range(9) ]
        to_add = 0
        for fish_days, fish_number in enumerate(fish_dict):     ## fish are represented by numbers (days to reproduce)
            if fish_days == 0:
                new_fish_dict[6] += fish_number
                to_add = fish_number       ## do not updated these added fish in the current day
            else:
                new_fish_dict[fish_days - 1] += fish_number
        new_fish_dict[8] = to_add
        fish_dict = new_fish_dict
        days -= 1

    return sum(fish_dict)

if __name__ == "__main__":
    main()


