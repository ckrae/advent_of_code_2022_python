# In how many assignment pairs do the ranges overlap?
from part1 import read_input


def overlaps(b):
    if int(b[2]) <= int(b[1]) and not int(b[3]) < int(b[0]):
        return True
    if int(b[0]) <= int(b[3]) and not int(b[1]) < int(b[2]):
        return True
    return False


def compute_solution(pairs):
    bounds = [p.replace('-', ',').split(',') for p in pairs]
    containing = [int(overlaps(b)) for b in bounds]
    return sum(containing)


if __name__ == "__main__":
    solution = compute_solution(read_input())
    print(solution)
