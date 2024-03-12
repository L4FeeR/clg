#!/usr/bin/python3
t=((1,2,3),(4,5,6),(7,8,9))
rs=[0 for i in range(0, 3)]
cs=[0 for i in range(0, 3)]
for i in range(len(t)):
    for j in range(len(t[i])):
        rs[i]+=t[i][j]
        cs[j]+=t[i][j]
for i in range(len(t)):
    for j in range(len(t[i])):
        print(t[i][j], end="")
        print(rs[i])
        print(*cs)
