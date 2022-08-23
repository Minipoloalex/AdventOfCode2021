# input_list = [0, 1, 5, 7, 8]

# def calculate_fuel(final_pos, input_list):
#     fuel_wasted = 0
#     for value in input_list:
#         fuel_wasted += abs(int(value) - final_pos)
#     return fuel_wasted

# for i in range(9):
#     print(f"Fuel for {i}: {calculate_fuel(i, input_list)}")


def calculate_fuel_crab_engineering(final_pos, input_list):
    fuel_wasted = 0
    for value in input_list:
        if value <= final_pos:
            step = 1
        else:
            step = -1
        i = 1
        for _ in range(value, final_pos, step):
            fuel_wasted += i
            i += 1
    return fuel_wasted

input_list = [16,1,2,0,4,2,7,1,2,14]

for i in range(17):
    print(f"Fuel for {i}: {calculate_fuel_crab_engineering(i, input_list)}")

