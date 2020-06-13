#!/usr/bin/env python
input_list=[[2, 5, 9, 12, 13, 15, 16, 17, 18, 19], [2, 4, 5, 6, 7, 9, 13, 16], [1, 2, 5, 9, 10, 11, 12, 13, 15]]
C = set(input_list[0])
F = set(input_list[1])
H = set(input_list[2])

#Students play all three sports
c = C & F & H 
print(sorted(c))


#Students play both cricket and football but don't play hockey
cf = (C & F ) - H
print(sorted(cf))

#Students who play exactly two of the sports
cfh = (((C - F)&H) - ((C - H) & F ) | ((F - H)&C))
print(sorted(cfh))

# Students who dont play any of the three sports
lazy={}
ch=list()
for i in range(1,21):
    lazy[str(i)] = 0
    
for i in C:
    lazy[str(i)] +=1
 
for i in H:
    lazy[str(i)] +=1  

for i in F:
    lazy[str(i)] +=1

for i in lazy.keys():
    if lazy[str(i)] == 0:
        ch.append(int(i))
print(ch)
