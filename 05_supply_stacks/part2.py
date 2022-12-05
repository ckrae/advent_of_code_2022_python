# After the rearrangement procedure completes, what crate ends up on top of each stack?
from part1 import read_input
from part1 import read_stacks
from part1 import read_move


def apply_moves(stacks: dict, moves: list):
    for move in moves:
        apply_move(stacks, int(move[0]), move[1], move[2])
    return stacks


def apply_move(stacks: dict[str, list], number: int, source, target):
    for i in range(0, number):
        item_index = len(stacks[source]) - number + i
        item = stacks[source][item_index]
        stacks[target].append(item)
    stacks[source] = stacks[source][:-number]


def compute_solution(data):
    stacks = read_stacks(data[0])
    moves = [read_move(m) for m in data[1].split('\n')]
    result_stacks = apply_moves(stacks, moves)
    return ''.join([s.pop() for s in result_stacks.values()])


if __name__ == "__main__":
    solution = compute_solution(read_input())
    print(solution)