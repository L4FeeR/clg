#!/usr/bin/python3
import os
l=eval(input("[+]Enter Number : "))
o=[]
p=1
for i in l:
    if (i not in o):
        o.append(i)
        p*=i

print("Product : ",p)
