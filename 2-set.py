#!/usr/bin/python3
s1=set(eval(input("[+]Enter first set : ")))
s2=set(eval(input("[+]Enter second set : ")))
print("Missing element from s1 : ",s2.difference(s1))
print("Additional element in s1 : ",s1.difference(s2))
