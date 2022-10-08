
'''
find the life support rating, with is Oxygen Generator Rating x CO2 Scrubber rating
Oxygen Generator Rating = Most bit values
CO2 Scrubber rating = Least bit values
'''
'''
1.count all the 0 and 1 in the first column.
2.find the most
3.remove the least
4.count all the 0 and 1 in second column.
5.repeat 2-3

'''        
with open('/home/kestrel/Documents/CodingProjects/AdventOfCode2021/3/day3data.py') as f:
    lines = f.readlines()
    

def filter_most(line_list, index):
    if len(line_list) == 1:
        print('02', line_list)
        return line_list

    counter_of_0 = 0
    counter_of_1 = 0
    
    for line in line_list:
        if line[index] == "0":
            counter_of_0 += 1
        if line[index] == "1":
            counter_of_1 += 1
    

    if counter_of_1 >= counter_of_0:
        filtered = [line for line in line_list if line[index]=="1"]
        
    else:
        filtered = [line for line in line_list if line[index]=="0"]
     

    return filter_most(filtered, index + 1)

def filter_least(line_list, index):
    if len(line_list) == 1:
       
        return line_list

    counter_of_0 = 0
    counter_of_1 = 0
    
    for line in line_list:
        if line[index] == "0":
            counter_of_0 += 1
        if line[index] == "1":
            counter_of_1 += 1
    

    if counter_of_0 <= counter_of_1:
        filtered = [line for line in line_list if line[index]=="0"]
        
    else:
        filtered = [line for line in line_list if line[index]=="1"]
        
    return filter_least(filtered, index + 1)
    

o2 = filter_most(lines, 0)
num_o2 = int(o2[0][:-1],2)


co2 = filter_least(lines, 0)
num_co2 = int(co2[0][:-1],2)


life_support_rating = num_o2 * num_co2



     


    