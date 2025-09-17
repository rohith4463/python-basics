x="rohithandCODE" #count how many uppercase and lowercase
lower_count = 0
upper_count = 0

for i in x:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count+=1
print(upper_count)
print(lower_count)

x=input("enter a string = ") #count the alpha letters
count = 0
for i in x:
    if i.isalpha():
        count +=1
print(count)
    
