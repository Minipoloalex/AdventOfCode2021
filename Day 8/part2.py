
def main():
    with open("input.txt", "r") as input_file:
        input_string = input_file.read().rstrip("\n")
        input_list = input_string.split("\n")
    input_processed = []
    for input_value in input_list:
        if input_value == "":
            continue
        a = input_value.split("|")
        b = [ c.split(" ") for c in a ]
        d = [ [ set(el0) for el0 in b[0] if el0 ] , [ set(el1) for el1 in b[1] if el1 ] ]
        input_processed.append(d)

    decipher_list = get_patterns(input_processed)
    result = 0
    for display, decipher in zip(input_processed, decipher_list):
        digit_list = display[1]
        number = 0
        for digit_set in digit_list:
            digit = obtain_digit(digit_set, decipher)
            number *= 10
            number += digit
        result += number

    print(result)
    return


def get_patterns(input_processed):
    '''
    - Start by going for the easy numbers: 1, 4, 7 (8 doesn't do anything here)
    - "Discover" 0 by using subset
    - Finish using 5 (also using subset) to get everything else
    '''
    decipher_list = []
    for display in input_processed:     ## display[1] won't be used (only display[0])
        pattern_result = [ 0 for _ in range(7) ]        ## seven-segment displays
        # pattern_result = [ top, topLeft, topRight, middle, bottomLeft, bottomRight, bottom ]
        right = 0
        topLeft_middle = 0
        bottomLeft_bottom = 0
        for digit_set in display[0]:
            if len(digit_set) == 2:         # digit 1
                right = digit_set.copy()
        
        for digit_set in display[0]:
            if len(digit_set) == 3:         # digit 7
                top = digit_set - right
                pattern_result[0] = top.copy().pop()
            elif len(digit_set) == 4:       # digit 4
                topLeft_middle = digit_set - right
        
        bottomLeft_bottom = {"a", "b", "c", "d", "e", "f", "g"} - right - topLeft_middle - set(top)

        for digit_set in display[0]:
            if len(digit_set) == 6 and digit_set.issuperset(bottomLeft_bottom | right | top):  # digit 0
                topLeft = digit_set - (bottomLeft_bottom | right | top)
                middle = topLeft_middle - topLeft
                pattern_result[1] = topLeft.copy().pop()
                pattern_result[3] = middle.copy().pop()
        
        for digit_set in display[0]:
            if len(digit_set) == 5 and digit_set.issuperset(top | topLeft | middle):    # digit 5
                for character in (digit_set - top - topLeft - middle):
                    if character in right:
                        pattern_result[5] = character                                   # bottomRight
                        pattern_result[2] = (right - set(character)).pop()              # topRight
                    elif character in bottomLeft_bottom:
                        pattern_result[6] = character                                   # bottom
                        pattern_result[4] = (bottomLeft_bottom - set(character)).pop()  # bottomLeft
        decipher_list.append(pattern_result)
    return decipher_list

def obtain_digit(digit_set, decipher):
    n = len(digit_set)
    if n == 2:
        return 1
    if n == 3:
        return 7
    if n == 4:
        return 4
    if n == 7:
        return 8
    [ top, topLeft, topRight, middle, bottomLeft, bottomRight, bottom ] = decipher
    if n == 5:
        if digit_set == { top,  topRight, middle, bottomLeft, bottom }:
            return 2
        if digit_set == { top, topRight, middle, bottomRight, bottom }:
            return 3
        if digit_set == { top, topLeft, middle, bottomRight, bottom }:
            return 5
            
    elif n == 6:
        if digit_set == { top, topLeft, topRight, bottomLeft, bottomRight, bottom }:
            return 0
        if digit_set == { top, topLeft, middle, bottomLeft, bottomRight, bottom }:
            return 6
        if digit_set == { top, topLeft, topRight, middle, bottomRight, bottom }:
            return 9
    return None

if __name__ == "__main__":
    main()