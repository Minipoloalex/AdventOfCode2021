
def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().split("\n")
        input_list.pop()
    
    diagram = get_diagram(input_list)
    count = count_2plus(diagram)
    
    print(f"Count of 2+ Hydrothermal vents: {count} (only considering horizontal/vertical vents")
    return

def get_diagram(input_list):
    diagram = [ [0 for _ in range(1000)] for __ in range(1000) ]

    for point in input_list:
        point_list = point.split(" -> ")    # 2 points to connect
        
        point1 = point_list[0].split(",")   # [x, y]
        point2 = point_list[1].split(",")   # [x, y]

        
        x1 = int(point1[0])
        y1 = int(point1[1])
        x2 = int(point2[0])
        y2 = int(point2[1])
        if x1 == x2:         # vertical lines
            if y1 < y2:
                for y in range(y1, y2 + 1):     ## include y2
                    diagram[y][x1] += 1
            else:
                for y in range(y2, y1 + 1):     ## include y1
                    diagram[y][x1] += 1

        elif y1 == y2:        # horizontal lines
            if x1 < x2:
                for x in range(x1, x2 + 1):     ## include x2
                    diagram[y1][x] += 1
            else:
                for x in range(x2, x1 + 1):     ## include x1
                    diagram[y1][x] += 1

    return diagram


def count_2plus(diagram):
    count = 0
    for line in diagram:
        for value in line:
            if value >= 2:
                count += 1
    return count


if __name__ == "__main__":
    main()


