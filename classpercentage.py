classes_held = int(input("enter total class ="))
classes_attended = int(input("enter total classes attended = "))

class_per = (classes_attended/classes_held)*100

print(f"percentage of class attended = {class_per :}%")

if class_per>=75:
    print("allowed to exam")
else:
    print("not allowed to exam")
