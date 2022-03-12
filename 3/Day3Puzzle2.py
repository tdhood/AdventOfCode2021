'''
Oxygen Generator Rating = Most bit values
CO2 Scrubber rating = Least bit values
'''

with open(r'C:\Users\taylo\Documents\Coding\Advent2021\3\day3data.py') as f:
    lines = f.readlines()


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

ox = []
co = []
lines_ox = lines
lines_co = lines
        
for line in lines:
    for column, bit in enumerate(line):
        if bit == '0':
            counts_by_column[column][0] += 1
        if bit == '1':
            counts_by_column[column][1] += 1

print(counts_by_column)            
##for i, count in enumerate(counts_by_column):
##    if count[0] > count[1]:
##        while (len(lines_ox)) > 1:
##            for line in lines_ox:
##                if line[i] == '1':
##                    lines_ox.remove(line)
##    if count[0] < count[1]:
##        while (len(lines_ox)) > 1:
##            for line in lines_ox:
##                if line[i] == '0':
##                    lines_ox.remove(line)
                    
##        for line in lines:
##            if line[0] == '0':
##                ox.append(line)
##            else:
##                co.append(line)
                
 

