# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:18:53 2022

@author: User
"""
def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split()
        input_list = map(int, input_list)
    print(count_window_increases(input_list))
    return

def count_window_increases(input_list):
    '''considers 3 measurements'''
    N_MEASURES = 3

    count = 0
    last_sum = None
    current_vals = [0 for _ in range(N_MEASURES)] 

    for i, value in enumerate(input_list):
        current_vals[i % N_MEASURES] = value
        if i < N_MEASURES - 1:          # wait for N_MEASURES measurements to calculate sums
            continue
        current_sum = sum(current_vals)
        if last_sum != None and current_sum > last_sum:
            count += 1

        last_sum = current_sum

    return count

    
if __name__ == "__main__":
    main()
