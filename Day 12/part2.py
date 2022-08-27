def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n")
        input_list = [ cave_connection.split("-") for cave_connection in input_list]
    
    number_of_paths = possible_paths(input_list)
    print(f"Number of paths with those restrictions: {number_of_paths}")

    return


def possible_paths(input_list):
    '''
    finds number of distinct paths that start at start, 
    end at end, and don't visit small caves more than once
    "start" and "end" also only appear in the start and end
    '''
    from_start = from_paths(input_list, "start")
    paths_cache = generate_cache(input_list)
    
    number_paths = calculate_path_number(input_list, from_start, {}, "start", True, paths_cache)

    return number_paths



def generate_single_caves(input_list):
    caves = set()
    for cave_connection in input_list:
        for cave in cave_connection:
            caves.add(cave)
    return caves

def generate_cache(input_list):
    cache = {}
    single_caves = generate_single_caves(input_list)
    for cave in single_caves:
        cache[cave] = from_paths(input_list, cave)
    return cache

def from_paths(input_list, cave_name):
    possible_next = []
    for cave_connection in input_list:
        if cave_name in cave_connection:
            index = not( cave_connection.index(cave_name) )
            value = cave_connection[index]
            if value != "start":
                possible_next.append(value)
    return possible_next

def is_small_cave(cave_name):
    return cave_name.islower()


def calculate_path_number(input_list: list, from_before: list, count: dict, current: str, double_cave: bool, paths_cache: dict):
    n = 0
    new_count = count.copy()
    # print(new_count)
    # print(current, from_before)
    for next_cave in from_before:
        # print(next_cave)
        if next_cave == "end":
           n += 1
           continue
        new_count[next_cave] = new_count.get(next_cave, 0) + 1
        times_visited = new_count[next_cave]
        if not(is_small_cave(next_cave)) or times_visited == 1:
            n += calculate_path_number( input_list, paths_cache[next_cave], new_count, next_cave, double_cave, paths_cache )

        elif times_visited == 2 and double_cave:
            n += calculate_path_number( input_list, paths_cache[next_cave], new_count, next_cave, False, paths_cache )


        new_count[next_cave] -= 1

    return n



if __name__ == "__main__":
    main()


