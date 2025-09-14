"""my_list=[23,4,566,78,12,2]

# reverse the list
for i in range(len(my_list)-1,-1,-1):
    print(my_list[i],end=" ")"""

"""my_list=[4,5,89.0,23.4]
# print even numbers
for i in range(0,len(my_list)):
    if my_list[i] % 2 == 0:
        print(my_list[i])"""

"""my_list=[23,45,66,87,98.3]
# print odd numbers
for i in range(0,len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i],end= " ")"""

"""my_list=[23,12,33,45,65,34]

for i in range(0,len(my_list)):
    if i % 2 == 0:
        print(my_list[i])"""

"""my_list=[23,43,44.12,90,33]
summ =0

#print sum of elements
for i in my_list:
    summ = summ + i
   
print(summ)"""

"""my_list=[23,44,54,67,98]
#counr the even numbers in the list
count= 0
for i in my_list:
    if i % 2 ==0:
        count = count+ 1
print(count)"""

"""my_list=[45,23,10,98,33,22,48]
# count the number which is divisble by 2 and 5
count = 0
for i in my_list:
    if i % 2 ==0 or i % 5 == 0 :
        count +=1
print(count)"""

"""my_list=[22,46,77,98.22,14]
# do the sum of even numbers
total = 0

for i in my_list:
    if i % 2 == 0:
        total += i
print(total)"""

my_list=[43,123,55,687,990]

largest = 0

for i in my_list:
    if i>largest:
        largest = i
print(largest)

