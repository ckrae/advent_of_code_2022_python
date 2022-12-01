# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
with open('input') as f:
    maxCalories = 0
    currentCalories = 0
    for line in f:
        if len(line.strip()) == 0:
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
        else:
            currentCalories = currentCalories + int(line)
    print(maxCalories)