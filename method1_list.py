my_list=[25,43,67,12,10,35]
a=int(input("enter a number"))
result=[]

for i in my_list:
    if i % a != 0:
        result.append(i)

print(result)
