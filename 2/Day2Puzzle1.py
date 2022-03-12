with open (r"C:\Users\taylo\Documents\Coding\Advent2021\2\data.py") as file:
    data = file.readlines()

direction = []

for i in data:
    direction.append(i.rstrip('\n'))



up = []
down = []
forward = []

# i = "forward 6", or "down 2"
for i in direction:
    if "down" in i:
        down.append(int(i.split()[1]))
    if "up" in i:
        up.append(int(i.split()[1]))
    if "forward" in i:
        forward.append(int(i.split()[1]))

UpSum = 0
for i in up:
    UpSum += i

DownSum = 0
for i in down:
    DownSum += i
    
ForwardSum = 0
for i in forward:
    ForwardSum += i

aim = DownSum - UpSum

answer = (aim * ForwardSum) * (DownSum - UpSum)


print(ForwardSum)
print(DownSum)
print(UpSum)

print(answer)

