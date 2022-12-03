# What is the sum of the priorities of those item types?
def read_input():
    with open('input') as f:
        return f.read().split("\n")


def priority_upper(char):
    return ord(char) - 38


def priority_lower(char):
    return ord(char) - 96


def priority(char):
    if char.isupper():
        return priority_upper(char)
    else:
        return priority_lower(char)


def half_size(string):
    return int(len(string) / 2)


def find_overlapping(compartments):
    for item_type in compartments[0]:
        if item_type in compartments[1]:
            return item_type


if __name__ == "__main__":
    rucksacks = read_input()
    rucksack_compartments = [[r[:half_size(r)], r[half_size(r):]] for r in rucksacks]
    overlapping_item_types = [find_overlapping(r) for r in rucksack_compartments]
    priorities = [priority(i) for i in overlapping_item_types]
    priorities_sum = sum(priorities)
    print(priorities_sum)
