x={"name":"rohith","age":66,"gender":"male"}

print(x,type(x)) 


"ask subject name and marks from the user and keep adding it to dic "

marks={}

subject_count=int(input("enter how many subjects = "))
for _ in range(0,subject_count):
    subject_name=input("enter a subject name = ")
    subject_marks=input("enter a marks = ")
    marks[subject_name]=subject_marks

print(marks)
