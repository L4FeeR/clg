#!/usr/bin/python3
import os, sys
n=eval(input("[+]Enter tuple: "))
print(n)
p=tuple(n)
k=list(n)
n=tuple(k)
while True:
    print("\n\n\t\t",n)
    print("1.Slice at index\n2.Add tuple\n3.Length of tuple\n4.count element\n5.find element at index\n6.Sort\n7.Max\n8.Min\n9.Compare\n10.Exit")
    a=int(input("[+]Enter choice : "))

    if a==1:
        x=int(input("[+]Enter index to slice : "))
        print("After slice : ",p[x:])
    elif a==3:
        print("Length : ",len(n))
    elif a==2:
        t=eval(input("[+]Enter another tuple : "))
        print("After adding : ",p+t)
    elif a==4:
        s=int(input("Enter element to count : "))
        print("Counts : ",k.count(s))
    elif a==5:
        d=int(input("[+]Enter element : "))
        print("Index of given element : ",p.index(d))
    elif a==6:
        k.sort()
        print("After sorted : ",k)
    elif a==7:
        print("Max : ",max(k))
    elif a==8:
        print("Min : ",min(n))
    elif a==9:
        f=eval(input("[+]Enter tuple : "))
        if n==f:
            print("Same")
        else:
            print("not equal")
    elif a==10:
        exit(0)
  
