def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")     ## list of strings -> all strings have same length
    low_point_sum = get_sum_low_points(input_list)
    print(f"Low point risk level sum: {low_point_sum}")

    return


def get_sum_low_points(input_list):
    total_risk_level = 0
    for i, height_string in enumerate(input_list):
        for k, height in enumerate(height_string):
            height = int(height)
            left = right = up = down = 10       # always bigger than height -> corners/sides will only depend on valid ones
            if k > 0:
                left = int(height_string[k - 1])
            if k < len(height_string) - 1:
                right = int(height_string[k + 1])
            if i > 0:
                up = int(input_list[i - 1][k])
            if i < len(input_list) - 1:
                down = int(input_list[i + 1][k])
            
            if right > height and left > height and up > height and down > height:
                total_risk_level += 1 + height
    
    return total_risk_level

if __name__ == "__main__":
    main()