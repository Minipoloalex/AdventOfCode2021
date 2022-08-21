# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:36:41 2022

@author: User
"""
def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split("\n")
    
    drawn_nums, boards = get_lists(input_list)
   
    # print(drawn_nums)
    # print("\n")
    # print(boards)
    
    final_value, unmarked_sum = get_winner_board(drawn_nums, boards)
    
    print(f"Final value: {final_value}")
    print(f"Unmarked sum: {unmarked_sum}")
    print(f"Final score: {final_value * unmarked_sum}")
    
    return


def get_lists(input_list):
    boards = []
    
    new_board = True
    
    for i, string in enumerate(input_list):
        if i == 0:
            drawn_nums = input_list[0].split(",")
        elif string == "":
            new_board = True
            continue
        else:
            if new_board:
                this_board = [ string.split() ]
                new_board = False
                count_lines = 1
            else:
                this_board.append(string.split())
                count_lines += 1
                if count_lines == 5:
                    boards.append(this_board)
                    count_lines = 0
    return drawn_nums, boards


def get_winner_board(drawn_nums, boards):
    for number_str in drawn_nums:
        for board in boards:
            for l, line in enumerate(board):
                for c, value in enumerate(line):
                    if value == number_str:
                        board[l][c] = "-1"
                        if check_win(board):
                            unmarked_sum = get_sum(board)
                            final_value = int(value)   
                            
                            return final_value, unmarked_sum



def check_win(board):
    ''' Checked numbers are represented by "-1" '''
    for line in board:
        if line_win(line):
            return True
    for i in range(len(board[0])):
        if col_win(i, board):
            return True
    return False


def line_win(line):                 # check for line win
    for value in line:
        if value != "-1":
            return False
    return True

def col_win(i, board):              # check for column win
    for j in range( len(board) ):   # line j , column i
        if board[j][i] != "-1":
            return False
    return True


def get_sum(board):
    unmarked_sum = 0
    for line in board:
        for value in line:
            if value != "-1":
                unmarked_sum += int(value)
    return unmarked_sum


if __name__ == "__main__":
    main()



