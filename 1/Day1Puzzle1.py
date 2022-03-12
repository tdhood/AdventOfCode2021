with open(r"C:\Users\taylo\Documents\Coding\Advent2021\Day1Puzzle1\1\DepthList.txt") as file:
    data = file.readlines()

import pprint

depths = []

for i in data:
    depths.append(i.rstrip('\n'))

for i in range(0, len(depths)):
    depths[i] = int(depths[i])


from math import inf


def solve(depths):
    prev = depths[0]
    count = 0
    for depth in depths[1:]:
        if depth > prev:
            count += 1
        prev = depth
    return count



print(solve(depths))


'''
Start:
    depths = [333, 234, 451, ...]
    
First Loop Through: 
    prev == 1,000,000,000
    count == 0
    depth == 333

Second Loop Through:
    prev == 333
    count == 0
    depth == 234

'''
