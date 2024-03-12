
#!/usr/bin/python3
import os
a=[]
lis=eval(input("[+]Enter List : "))
f=int(input("[+]Enter frequency : "))

for i in lis:
    if lis.count(i) >= f:
        if i not in a:
            a.append(i)

print("Elements having given frequency : ",a)

