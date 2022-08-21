# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:15:17 2022

@author: User
"""

def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split()
    final_hor, final_depth = calculate_pos(input_list)
    print(f"Final horizontal position: {final_hor}")
    print(f"Final depth: {final_depth}")
    print(f"Result: {final_hor * final_depth}")
    return

def calculate_pos(input_list):
    hor_pos = 0
    depth = 0
    for i in range(0, len(input_list), 2):
        command = input_list[i]
        value = int(input_list[i + 1])
        if command == "forward":
            hor_pos += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value
        else:
            raise ValueError(f"Command: {command}")
    return hor_pos, depth

if __name__ == "__main__":
    main()
