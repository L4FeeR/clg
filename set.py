#!/usr/bin/python3
import os, sys
s=eval(input("[+]Enter set : "))
while True:

    print("""      1.Add element
      2.update set
      3.copy set
      4.pop an element
      5.remove element
      6.discard element
      7.clear a set
      8.find union of another set
      9.find intersection of another set
      10.exit""")
    a=int(input("[+]Enter choice : "))
    if a==1:
        k=int(input("[+]Enter element : "))
        s.add(k)
        print(s)
    if a==2:
        k1=eval(input("[+]Enter element to update : "))
        s.update(k1)
    if a==3:
        s1=s.copy()
        print("copied to s1 : ",s1)
    if a==4:
        print("After Popping : ",s.pop())
    if a==5:
        k2=input("[+]Enter element to remove : ")
        if k2 in s:
            s.remove(k2)
            print("after remove : ",s)
        else:
            print("key not found")
    if a==6:
        k3=input("[+]Enter element to remove : ")
        s.discard(k3)
        print("After discard : ",s.discard(k3))
    if a==7:
        s.clear()
        print(s)
    if a==8:
        s2=eval(input("[+]Enter another set : "))
        print("After union : ",s.union(s2))
    if a==9:
        s2=eval(input("[+]Enter another set : "))
        print("After intersection : ",s.intersection(s2))
    if a==10:
        exit(0)


