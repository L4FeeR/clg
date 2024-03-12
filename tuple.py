#!/usr/bin/python3
import os
l=list()
while True:
    print("1.createlist\n2.Insert element\n3.Append element\n4.Delete matching item\n5.Delete with indx\n6.Enter list\n7.Max value\n8.Min value\n9.Show list\n10.exit")
    ch=int(input("[+]Enter choice : "))
    print("\n\t\t",l)
    if ch==1:
        l=eval(input("[+]Enter list : "))
        print(l)
    elif ch==2:
        ins=int(input("[+]Enter element to insert : "))
        imp=int(input("[+]Enter index : "))
        l.insert(imp, ins)
        print(l)
    elif ch==3:
        inp=int(input("[+]Enter element to append : "))
        l.append(inp)
    elif ch==4:
        inp=int(input("[+]Enter element to delete : "))
        l.remove(inp)
    elif ch==5:
        inp=int(input("[+]Enter index to delete : "))
        l.pop(inp)
    elif ch==6:
        i=eval(input("[+]Enter list to extend : "))
        l.extend(i)
    elif ch==7:
        print("Max Value : ",max(l))
    elif ch==8:
        print("Min value : ",min(l))
    elif ch==9:
        print("List : ",l)
    elif ch==10:
        exit(0)

