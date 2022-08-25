def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")
    score = get_incomplete_score(input_list)
    score.sort()
    print(score)
    print(f"Middle score (winner): {score[len(score)//2]}")
    
    return


def get_incomplete_score(input_list):
    score = []
    for chunk_str in input_list:
        chunk_score = get_string_score(chunk_str, [])
        if chunk_score != 0:
            score.append(chunk_score)
    return score


def get_string_score(string, seen = []):
    if len(string) == 0:
        return score_incomplete_string(seen)      # incomplete line

    if string[0] == "[" or string[0] == "(" or string[0] == "{" or string[0] == "<":
        seen.append(string[0])
        return get_string_score(string[1:], seen)

    elif string[0] == "]":              # corrupted checks
        if len(seen) == 0:
            return 0
        corresponding = seen.pop()
        if corresponding != "[":
            return 0
   
    elif string[0] == ")":
        if len(seen) == 0:
            return 0
        corresponding = seen.pop()
        if corresponding != "(":
            return 0

    elif string[0] == "}":
        if len(seen) == 0:
            return 0
        corresponding = seen.pop()
        if corresponding != "{":
            return 0

    elif string[0] == ">":
        if len(seen) == 0:
            return 0
        corresponding = seen.pop()
        if corresponding != "<":
            return 0

    return get_string_score(string[1:], seen)


score_dict = {"(": 1, "[": 2, "{": 3, "<": 4}
def score_incomplete_string(to_complete):
    print(len(to_complete))
    string_score = 0
    for character in reversed(to_complete):
        string_score *= 5
        string_score += score_dict[character]
    return string_score


if __name__ == "__main__":
    main()


