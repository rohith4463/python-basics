"""my_string="hello world"

words=my_string.split() # reverse the string

words=words[::-1]

result=" ".join(i for i in words)

print(result)"""

my_string = "python is good" # write a program that accepts a string and 

#capitalizes the first letter of each word 

words=my_string.split()

result=" ".join(i.title() for i in words)

print(result)
