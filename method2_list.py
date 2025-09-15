my_list=[12,11,34,57,88,97,21,23,44,46]
even=[]
odd=[]
for i in my_list:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
