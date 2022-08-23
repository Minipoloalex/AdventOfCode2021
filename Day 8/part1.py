
def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split("\n")
    input_processed = []
    for input_value in input_list:
        if input_value == "":
            continue
        a = input_value.split("|")
        b = [ c.split(" ") for c in a ]
        input_processed.append(b)           ## input_processed has "" -> ignore these
    
    count_1_4_7_8 = count_unique_segments(input_processed)
    print(count_1_4_7_8)
    print(f"Digits 1, 4, 7, 8 appear: {sum(count_1_4_7_8)} times")

    return


def count_unique_segments(input_list):
    count = [0, 0, 0, 0]            # count = [1s, 4s, 7s, 8s]
    for display in input_list:      ## display = [ [y, y, y, y, y, y, y, y, y, y], [x, x, x, x] ]
        print(display)
        for number_str in display[1]:          ## count numbers from display[1]
            if number_str == "":
                continue
            if len(number_str) == 2:
                count[0] += 1
            elif len(number_str) == 4:
                count[1] += 1
            elif len(number_str) == 3:
                count[2] += 1
            elif len(number_str) == 7:
                count[3] += 1
    return count


if __name__ == "__main__":
    main()


