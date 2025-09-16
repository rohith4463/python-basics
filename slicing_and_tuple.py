# list Slicing

a=[23,3,45,67,8,90,11,23]

b=a[0:3]
print(b)


# tuple Immutable

# in tuple there is only index and count and we cannt add any value to 
# tuple

"""my_tuple = (56,43,44,78,99)

x=my_tuple.index(99)
y=my_tuple.count(99)

print(x,y)"""


my_tuple=(10,23,55,65,78,12)

my_list = list(my_tuple)

my_list.append(200)

my_tuple = tuple(my_list)

print(my_tuple)

