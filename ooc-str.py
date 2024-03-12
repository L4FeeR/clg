#!/usr/bin/python3
l=eval(input("[+]Enter List Of String : "))
s=set(l)
o=[(l.count(x),x) for x in s]
print(o)
