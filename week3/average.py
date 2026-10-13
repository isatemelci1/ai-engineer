import random
import statistics

totals = []

for i in range(10):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    totals.append(total)
    print(f"Roll {i + 1}: {total}")

average = statistics.mean(totals)
print("Average:", average)