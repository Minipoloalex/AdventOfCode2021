# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:02:32 2022

@author: User
"""
def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split()
        input_list = map(int, input_list)
    n_increases = count_increases(input_list)
    print(n_increases)
    return

def count_increases(input_list):
    '''input_list is an iterable of numbers'''
    count = 0
    before_value = None

    for value in input_list:
        if before_value != None and value > before_value:
            count += 1
        before_value = value
        
    return count

if __name__ == "__main__":
    main()
