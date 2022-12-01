# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
def is_empty(string):
    return len(string.strip()) == 0


calories = []
with open('input') as f:
    elf_weight = 0
    for line in f:
        if is_empty(line):
            calories.append(elf_weight)
            elf_weight = 0
        else:
            elf_weight = elf_weight + int(line)

calories.sort(reverse=True)
top_three = calories[0] + calories[1] + calories[2]
print(top_three)
