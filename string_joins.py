#joins

#convert a list to string

my_list=["abcd","xyxy","hello","rohith",33]

my_string="-".join(str(i) for i in my_list)
print(my_string,type(my_string))

"""my_string="hello world"

words=my_string.split() # reverse the string

words=words[::-1]

result=" ".join(i for i in words)

print(result)"""
