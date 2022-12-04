# In how many assignment pairs does one range fully contain the other?
def read_input():
    with open('input') as f:
        return f.read().split("\n")


def fully_contains(bounds):
    if int(bounds[0]) <= int(bounds[2]) and int(bounds[1]) >= int(bounds[3]):
        return True
    if int(bounds[0]) >= int(bounds[2]) and int(bounds[1]) <= int(bounds[3]):
        return True
    return False


def compute_solution(pairs):
    bounds = [p.replace('-', ',').split(',') for p in pairs]
    containing = [int(fully_contains(b)) for b in bounds]
    return sum(containing)


if __name__ == "__main__":
    solution = compute_solution(read_input())
    print(solution)
