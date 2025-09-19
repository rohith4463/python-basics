my_string = "python is good" # write a program that accepts a string and 

#capitalizes the first letter of each word 

words=my_string.split()

result=" ".join(i.title() for i in words)

print(result)


my_string = "python is good"

words=my_string.split() #revese the words

result=" ".join(i[::-1] for i in words)
print(result)
