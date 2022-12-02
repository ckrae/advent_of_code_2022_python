# 1) What would your total score be if everything goes exactly according to your strategy guide?
from functools import reduce

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def outcome_score(game):
    match game:
        case ['A', 'Z'] | ['B', 'X'] | ['C', 'Y']:
            return 0
        case ['A', 'X'] | ['B', 'Y'] | ['C', 'Z']:
            return 3
        case ['A', 'Y'] | ['B', 'Z'] | ['C', 'X']:
            return 6


def read_input():
    with open('input') as f:
        lines = f.read().split("\n")
        return list(map(lambda x: x.split(" "), lines))


def compute_score(game):
    return shape_score[game[1]] + outcome_score(game)


if __name__ == "__main__":
    strategy_guide = read_input()
    scores = list(map(compute_score, strategy_guide))
    print(scores)
    final_score = reduce(lambda x, y: x + y, scores)
    print(final_score)
