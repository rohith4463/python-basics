# make a list of your own.and remove all the 
# duplicates elemnts for the list

my_list=[2,1,2,2,3,56,66,56,"rohith",1,"rohith"]

result=[]

for i in my_list:
    if i not in result:
        result.append(i)
print(result)


# make a list, then ask a number from user. If number exists in that list the print the position of the element else print -1

my_list=[23,12,34,56,76,22,99]
num=int(input("enter a number"))

if num in my_list:
        index=my_list.index(num)
        print(index)
else:
    print(-1)



