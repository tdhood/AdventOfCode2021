counts_by_column = [
    [0, 0], # In the first column, 0 "0"s, and 0 "1"s
    [0, 0], # In the second column, 0 "0"s, and 0 1"s...
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0], # In the 12th column, 0 "0"s, and 0 "1"s...
]



with open(r'/home/kestrel/Documents/CodingProjects/Advent2021/3/day3data.py') as f:
    lines = f.readlines()
    for line in lines:
        for column, bit in enumerate(line):
            if bit == '0':
                counts_by_column[column][0] += 1
            if bit == '1':
                counts_by_column[column][1] += 1

gamma = ""
epsilon = ""

for counts in counts_by_column:
    num_zeroes = counts[0]
    num_ones = counts[1]
    if num_zeroes > num_ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(gamma, epsilon, f'\nAnswer: {int(gamma, 2) * int(epsilon, 2)}')
