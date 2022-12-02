# 1) What would your total score be if everything goes exactly according to your strategy guide?
from functools import reduce

outcome_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def shape_score(game):
    match game:
        case ['A', 'Y'] | ['B', 'X'] | ['C', 'Z']:
            return 1
        case ['A', 'Z'] | ['B', 'Y'] | ['C', 'X']:
            return 2
        case ['A', 'X'] | ['B', 'Z'] | ['C', 'Y']:
            return 3


def read_input():
    with open('input') as f:
        lines = f.read().split("\n")
        return list(map(lambda x: x.split(" "), lines))


def compute_score(game):
    return shape_score(game) + outcome_score[game[1]]


if __name__ == "__main__":
    strategy_guide = read_input()
    scores = list(map(compute_score, strategy_guide))
    print(scores)
    final_score = reduce(lambda x, y: x + y, scores)
    print(final_score)
