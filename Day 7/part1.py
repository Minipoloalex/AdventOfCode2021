
def main():
    with open("input.txt", "r") as input_file:
        input_string = input_file.read().rstrip("\n")
        input_list = input_string.split(",")
    input_list = [ int(value) for value in input_list ]
    optimal_pos, fuel_spent = binary_test_fuel(input_list)
    print(f"The optimal position is {optimal_pos} and fuel wasted is {fuel_spent}")
    
def binary_test_fuel(input_list):
    # REGION OF INTEREST (lower and upper bounds)
    lb = min(input_list)
    ub = max(input_list)
    while True:
        test = (ub + lb)//2
        print(f"ROI: {lb}-{ub}")
        before = calculate_fuel(test - 1, input_list)
        current = calculate_fuel(test, input_list)
        after = calculate_fuel(test + 1, input_list)

        if before > current and after > current:        # minimum value (base case)
            return test, current
        if before > current and after < current:
            lb = test + 1
        if before < current and after > current:
            ub = test - 1
    return


def calculate_fuel(final_pos, input_list):
    fuel_wasted = 0
    for value in input_list:
        fuel_wasted += abs(value - final_pos)
    return fuel_wasted


# def calculate_mean(input_list):
#     val_sum = 0
#     for value in input_list:
#         val_sum += int(value)
#     return val_sum/len(input_list)


if __name__ == "__main__":
    main()

