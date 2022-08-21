# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 08:28:11 2022

@author: User
"""
def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split()
    gamma_rate, epsilon_rate = get_power_consumption(input_list)
    print(f"Gamma rate: {gamma_rate}")
    print(f"Epsilon rate: {epsilon_rate}")
    print(f"Power consumption: {gamma_rate * epsilon_rate}")
    return

def get_power_consumption(input_list):
    count = [[0, 0] for _ in range(len(input_list[0]))]
    for bin_str in input_list:
        for i, digit in enumerate(bin_str):
            count[i][int(digit)] += 1
    gamma_rate = 0
    epsilon_rate = 0
    for c in count:
        if c[0] > c[1]:
            gamma_rate = gamma_rate * 2  + 0        # 0 most common
            epsilon_rate = epsilon_rate * 2 + 1
        else:
            gamma_rate = gamma_rate * 2 + 1         # 1 most common
            epsilon_rate = epsilon_rate * 2 + 0

    return (gamma_rate, epsilon_rate)

if __name__ == "__main__":
    main()
    