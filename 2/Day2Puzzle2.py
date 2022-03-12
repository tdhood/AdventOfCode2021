'''
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X
'''
with open (r"C:\Users\taylo\Documents\Coding\Advent2021\2\data.py") as file:
    data = file.readlines()

lines = []

for i in data:
    lines.append(i.rstrip('\n'))
    
aim = x = y = 0

for i in lines:
    direction, distance = i.split(' ')
    distance = int(distance)
    if direction == "down":
        aim += distance
    if direction == "up":
        aim -= distance
    if direction == "forward":
        x += distance
        y += aim * distance
    
print(x * y)


