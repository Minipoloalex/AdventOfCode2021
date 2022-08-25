score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}

def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")
    score = get_syntax_errors_score(input_list)
    print(f"Syntax errors score: {score}")
    
    return

def get_syntax_errors_score(input_list):
    score = 0
    for chunk_str in input_list:
        character = get_illegal_character(chunk_str, [])
        score += score_dict.get(character, 0)
    return score

def get_illegal_character(string, seen = []):
    if len(string) == 0:
        return 0

    if string[0] == "[" or string[0] == "(" or string[0] == "{" or string[0] == "<":
        seen.append(string[0])
        return get_illegal_character(string[1:], seen)

    elif string[0] == "]":
        if len(seen) == 0:
            return "]"
        corresponding = seen.pop()
        if corresponding != "[":
            return "]"
   
    elif string[0] == ")":
        if len(seen) == 0:
            return ")"
        corresponding = seen.pop()
        if corresponding != "(":
            return ")"
   
    elif string[0] == "}":
        if len(seen) == 0:
            return "}"
        corresponding = seen.pop()
        if corresponding != "{":
            return "}"

    elif string[0] == ">":
        if len(seen) == 0:
            return ">"
        corresponding = seen.pop()
        if corresponding != "<":
            return ">"

    return get_illegal_character(string[1:], seen)


if __name__ == "__main__":
    main()


