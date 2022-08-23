from functools import reduce
from operator import mul

def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")     ## list of strings -> all strings have same length
    
    largest_basins = get_largest_basins(input_list)
    print(f"Size of three largest basins: {largest_basins}")
    print(f"Result: {reduce(mul, largest_basins)}")

    return


def get_largest_basins(input_list):
    largest_basins = [0, 0, 0]
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
            
            if right > height and left > height and up > height and down > height:      # low point
                basin_size = find_basin(input_list, i, k, [])
                print(basin_size)
                min_basin = min(largest_basins)
                for index, basin in enumerate(largest_basins):
                    if basin == min_basin and basin_size > basin:
                        largest_basins[index] = basin_size
                        break
    return largest_basins


def find_basin(input_list, i, k, visited):     ## finds basin size
    if (i, k) not in visited and input_list[i][k] != '9':
        visited.append( (i, k) )
    else: return 0
    # possible_places
    if i > 0:
        find_basin(input_list, i - 1, k, visited)
    if i < len(input_list) - 1:
        find_basin(input_list, i + 1, k, visited)
    if k > 0:
        find_basin(input_list, i, k - 1, visited)
    if k < len(input_list[i]) - 1:
        find_basin(input_list, i, k + 1, visited)

    return len(visited)


# def get_sum_low_points(input_list):
#     total_risk_level = 0
#     for i, height_string in enumerate(input_list):
#         for k, height in enumerate(height_string):
#             height = int(height)
#             left = right = up = down = 10       # always bigger than height -> corners/sides will only depend on valid ones
#             if k > 0:
#                 left = int(height_string[k - 1])
#             if k < len(height_string) - 1:
#                 right = int(height_string[k + 1])
#             if i > 0:
#                 up = int(input_list[i - 1][k])
#             if i < len(input_list) - 1:
#                 down = int(input_list[i + 1][k])
            
#             if right > height and left > height and up > height and down > height:
#                 total_risk_level += 1 + height
    
#     return total_risk_level

if __name__ == "__main__":
    main()