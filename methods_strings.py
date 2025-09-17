"""my_string="EDDDY" # upper case to lower case
result="" 
for i in my_string:
    ascii = ord(i)
    if ascii >= 65 and ascii <= 90:
        new_ascii=ascii+32
        char=chr(new_ascii)
        result += char
    else:
        result = result + i
print(result)"""

my_string="koushik" #lower case to upper
result="" 
for i in my_string:
    ascii = ord(i)
    if ascii >= 97 and ascii <= 122:
        new_ascii=ascii-32
        char=chr(new_ascii)
        result += char
    else:
        result = result + i
print(result)
