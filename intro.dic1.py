list1=["ten","twenty","thirty"]
list2=[10,20,30]
marks={}
for i in range(0,len(list1)):
    marks[list1[i]]=list2[i]



print(marks)



marks={"english":20,"maths":35,"science":30}
sum=1


for i in marks.values():
    sum=sum*i
print(sum)
