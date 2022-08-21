# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:42:40 2022

@author: User
"""
def main():   
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split()

    oxygen_rating = int(get_rating(input_list, "oxygen"), 2)
    co2_rating = int(get_rating(input_list, "co2"), 2)
    print(f"Oxygen generator rating: {oxygen_rating}")
    print(f"CO2 scrubber rating: {co2_rating}")
    print(f"Life support rating: {oxygen_rating * co2_rating}")
    return

def get_count_index(input_list, index):
    count = [0, 0]
    for bin_str in input_list:
        count[ int(bin_str[index]) ] += 1
    return count


def get_rating(input_list, rating_type):
    new_list = input_list.copy()
    
    assert rating_type == "oxygen" or rating_type == "co2"
    function = oxygen_condition if rating_type == "oxygen" else co2_condition

    i = 0
    while True:
        if len(new_list) == 1:
            return new_list[0]
        else:
            count = get_count_index(new_list, i)
            new_list = [ bin_str for bin_str in new_list if function(bin_str, count, i) ]
            i += 1


def oxygen_condition(bin_str, count, i):
    if bin_str[i] == '1' and count[1] >= count[0]:
        return True
    if bin_str[i] == '0' and count[0] > count[1]:
        return True
    return False


def co2_condition(bin_str, count, i):
    if bin_str[i] == '1' and count[1] < count[0]:
        return True
    if bin_str[i] == '0' and count[0] <= count[1]:
        return True
    return False


if __name__ == "__main__":
    main()


