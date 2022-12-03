from functools import reduce

from part1 import read_input
from part1 import priority


def group_teams(elfs):
    teams = []
    for i in range(0, len(elfs) - 2, 3):
        team = [elfs[i], elfs[i + 1], elfs[i + 2]]
        teams.append(team)
    return teams


def find_overlapping_item_types(elf_1, elf_2):
    result = set()
    for item_type in elf_1:
        if item_type in elf_2:
            result.add(item_type)
    return list(result)


def compute_solution(elfs):
    teams = group_teams(elfs)
    overlapping_item_types = [reduce(find_overlapping_item_types, team)[0] for team in teams]
    priorities = [priority(it) for it in overlapping_item_types]
    return sum(priorities)


if __name__ == "__main__":
    solution = compute_solution(read_input())
    print(solution)
