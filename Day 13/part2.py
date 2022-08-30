import turtle

def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n\n")
    dot_list = input_list[0].split("\n")
    instr_list = input_list[1].split("\n")

    dot_set = { tuple(dot.split(",")) for dot in dot_list }
    instr_list = [ instr.lstrip("fold along ") for instr in instr_list ]
    print(instr_list)
    for instr in instr_list:
        if instr.startswith("x="):
            dot_set = fold_x(dot_set, instr)
        elif instr.startswith("y="):
            dot_set = fold_y(dot_set, instr)
        else:
            print("Wrong", instr)
    print(dot_set)

    screen = turtle.Screen()
    screen.setup(1000, 500)
    my_turtle = turtle.Turtle()
    my_turtle.shape("circle")
    my_turtle.shapesize(0.5)
    my_turtle.penup()
    for dot in dot_set:
        dot = ( int(dot[0]) * 10 - 250 , 100 - int(dot[1]) * 10)     ## 100 - y_value -> (turtle y grows upwards, opposite to this problem)
        my_turtle.setpos(dot)
        my_turtle.stamp()

    screen.mainloop()
    turtle.bye()

    return


def fold_y(dot_set, instr_y):
    fold_y = int(instr_y.lstrip("y="))
    new_dot_set = dot_set.copy()
    for dot in dot_set:
        y_value = int(dot[1])
        if y_value > fold_y:
            new_y = fold_y - (y_value - fold_y)
            x = dot[0]
            new_dot_set.remove(dot)
            new_dot_set.add( (x, str(new_y)) )
    return new_dot_set


def fold_x(dot_set, instr_x):
    fold_x = int(instr_x.lstrip("x="))
    new_dot_set = dot_set.copy()
    for dot in dot_set:
        x_value = int(dot[0])
        if x_value > fold_x:
            new_x = fold_x - (x_value - fold_x)
            y = dot[1]
            new_dot_set.remove(dot)
            new_dot_set.add( (str(new_x), y) )
    return new_dot_set


if __name__ == "__main__":
    main()

