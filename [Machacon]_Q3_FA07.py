steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

names = ["Me", "Lia", "Jake"]

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    print(names[i], "steps:", steps[i])
    print("Total:", total)
    print("Average:", average)
    print()

max_value = steps[0][0]
for row in steps:
    for value in row:
        if value > max_value:
            max_value = value

print("Highest step count in the dataset:", max_value)
