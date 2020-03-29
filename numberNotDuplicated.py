import numpy as np


n = 100
consult_array = np.zeros(100, dtype = int)

array = []
with open('array.txt') as file:
    for line in file:
        for elem in line.split(","):
            elem = int(elem)
            array.append(elem)
            consult_array[elem] += 1

i=0
while consult_array[array[i]] != 1:
    i+=1

print("o numero é =",array[i])


