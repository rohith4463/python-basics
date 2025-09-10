marks1 = int(input("enter marks1 = "))
marks2 = int(input("enter marks2 = "))
marks3 = int(input("enter marks3 = "))
marks4 = int(input("enter marks4 = "))
marks5 = int(input("enter marks5 = "))


total_percentage = ((marks1+marks2+marks3+marks4+marks5)/500)*100

print(f"total_percentage is {total_percentage}%")

if total_percentage>=91 and total_percentage<100:
    print("A grade")
elif total_percentage>=81 and total_percentage<=90:
    print("B grade")
elif total_percentage>=71 and total_percentage<=80:
    print("C grade")
elif total_percentage>=60 and total_percentage<=70:
    print("D grade")
elif total_percentage>=0 and total_percentage<=59:
    print("fail")
else :
    print("Invaild")
