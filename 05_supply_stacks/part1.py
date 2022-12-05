# After the rearrangement procedure completes, what crate ends up on top of each stack?
def read_input():
    with open('input.txt') as f:
        return f.read().split("\n\n")


def read_stacks(data: str):
    lines = list(reversed(data.split('\n')))
    stacks = dict()
    for char in lines[0]:
        if char.isnumeric():
            i = lines[0].index(char)
            stacks[char] = [l[i] for l in lines[1:] if l[i].isalpha()]
    return stacks


def read_move(move: str):
    return move.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')


def apply_moves(stacks: dict, moves: list):
    for move in moves:
        apply_move(stacks, move)
    return stacks


def apply_move(stacks: dict, move: list):
    for i in range(0, int(move[0])):
        apply_move_step(stacks, move[1], move[2])


def apply_move_step(stacks: dict[str, list], source, target):
    stacks[target].append(stacks[source].pop())


def compute_solution(data):
    stacks = read_stacks(data[0])
    moves = [read_move(m) for m in data[1].split('\n')]
    result_stacks = apply_moves(stacks, moves)
    return ''.join([s.pop() for s in result_stacks.values()])


if __name__ == "__main__":
    solution = compute_solution(read_input())
    print(solution)
