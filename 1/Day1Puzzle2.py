with open(r"C:\Users\taylo\Documents\Coding\Advent2021\Day1Puzzle1\DepthList.txt") as file:
    data = file.readlines()

import pprint

depths = []

for i in data:
    depths.append(i.rstrip('\n'))

for i in range(0, len(depths)):
    depths[i] = int(depths[i])

def solve(depths):
    prev3 = depths[0]
    prev2 = depths[1]
    prev1 = depths[2]
    count = 0
    for depth in depths[3:]:
        if depth + prev2 + prev1 > prev3 + prev2 + prev1:
            count += 1
        prev3 = prev2
        prev2 = prev1
        prev1 = depth
    return count

print(solve(depths))
