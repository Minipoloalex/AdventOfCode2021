def main():
    with open("input.txt") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n\n")
        polymer = input_list[0]
        insertion_rules = input_list[1].split("\n")
    insertion_rules = [ rule.split(" -> ") for rule in insertion_rules ]
    final_polymer_count = apply_rules(polymer, insertion_rules, 40)
    print(final_polymer_count)

    most, least = get_common_chars(final_polymer_count)
    print(f"The quantity of the most common element subtracted by the quantity of the least common element is: {most - least}")
    return


def apply_rules(polymer, insertion_rules, steps):
    count = {}
    for character in polymer:
        count[character] = count.get(character, 0) + 1
    pair_dict = get_initial_pairs(polymer)
    while steps > 0:
        new_pair_dict = pair_dict.copy()
        for pair, n in pair_dict.items():
            first = pair[0]
            second = pair[1]
            to_add = get_rule(pair, insertion_rules)
            new_pair_dict[pair] -= n        # do not set to 0 since it's the new dictionary

            pair_one = first + to_add
            pair_two = to_add + second
            new_pair_dict[pair_one] = new_pair_dict.get(pair_one, 0) + n
            new_pair_dict[pair_two] = new_pair_dict.get(pair_two, 0) + n
            count[to_add] = count.get(to_add, 0) + n

        pair_dict = new_pair_dict
        steps -= 1

    return count


def get_initial_pairs(polymer):
    pair_dict = {}
    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i + 1]
        pair_dict[pair] = pair_dict.get(pair, 0) + 1
    return pair_dict

def get_rule(pair, insertion_rules):
    for rule in insertion_rules:
        if rule[0] == pair:
            return rule[1]
    raise ValueError(pair)

def get_common_chars(count):
    most_common = max(count.values())
    least_common = min(count.values())
    return most_common, least_common


if __name__ == "__main__":
    main()

