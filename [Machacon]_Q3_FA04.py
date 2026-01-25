names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []

for s in steps:
    totals.append(sum(s))

for i in range(len(names)):
    print(names[i], "total steps:", totals[i])

highest = max(totals)
lowest = min(totals)

index = totals.index(highest)
print("\nHighest total steps:", names[index], "with", highest)

difference = highest - lowest
print("Difference between highest and lowest:", difference)
