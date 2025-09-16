start = int(input("enter a number = "))
end = int(input("enter a number =  "))

list1 = [i for i in range(start,end) if  i % 2 == 0 and i % 3 ==0]
print(list1)
