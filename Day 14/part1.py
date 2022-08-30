def main():
    with open("input.txt") as input_file:
        input_list = input_file.read().rstrip("\n").split("\n\n")
        polymer = input_list[0]
        insertion_rules = input_list[1].split("\n")
    insertion_rules = [ rule.split(" -> ") for rule in insertion_rules ]
    final_polymer = apply_rules(polymer, insertion_rules, 10)
    print(final_polymer)
    most, least = get_common_chars(final_polymer)
    print(f"The quantity of the most common element subtracted by the quantity of the least common element is: {most - least}")

    return

def apply_rules(polymer, insertion_rules, steps):
    while steps > 0:
        new_polymer = polymer
        j = 0
        for i in range(len(polymer) - 1):
            first = polymer[i]
            second = polymer[i + 1]
            to_add = get_rule(first + second, insertion_rules)
            new_polymer = new_polymer[ : i + 1 + j] + to_add + new_polymer[i + 1 + j : ]
            j += 1
        polymer = new_polymer
        steps -= 1

    return polymer


def get_rule(pair, insertion_rules):
    for rule in insertion_rules:
        if rule[0] == pair:
            return rule[1]
    raise ValueError(pair)

def get_common_chars(polymer):
    count = {}
    for character in polymer:
        count[character] = count.get(character, 0) + 1
    most_common = max(count.values())
    least_common = min(count.values())
    return most_common, least_common


if __name__ == "__main__":
    main()

