"""list1= [20,0,45,87,0,20]
list2= [78,98,78,65,23,0]

a=set(list1)
b=set(list2)

print(a.intersection(b))"""

list1=[3,5,1,2,2,6,4,"Rohith"]
list2=[3,8,7,2,1,5,9,"pooja"]
list3=[8,9,5,2,1,7,4,"virat"]

print(set(list1) & set(list2) & set(list3)) # this  a one line method (intersection)

print(set(list1) | set(list2) | set(list3)) # this  a one line method (union)

"""s=set(list1)
c=set(list2)
v=set(list3)

x=s.intersection(c)
result=x.intersection(v)
print(result)"""
