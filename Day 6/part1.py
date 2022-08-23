def main():
    with open("input.txt", "r") as input_file:
        input_string = input_file.read()
        input_string = input_string.rstrip("\n")
    input_list = input_string.split(",")
    n_lanternfish = lanternfish_reproduce(input_list)
    print(f"Number of lanternfish after 80 days: {n_lanternfish}")
    return

def lanternfish_reproduce(input_list):
    days = 80
    updated_list = [ int(fish) for fish in input_list ]

    while days > 0:
        to_add = []
        for i, fish in enumerate(updated_list):     ## fish are represented by numbers (days to reproduce)
            if fish == 0:
                updated_list[i] = 6
                to_add.append(8)        ## do not updated these added fish in the current day
            else:
                updated_list[i] -= 1
        updated_list += to_add
        days -= 1

    return len(updated_list)


if __name__ == "__main__":
    main()


