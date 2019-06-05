# Python code to convert string to list 
  
def convert(string): 
    li = list(string.split("'")) 
    return li 
  
# Driver code     
str1 = "[('lucas',), ('lucas',), ('lucas',), ('cartaxo',), ('samuel1',), ('samuel1',), ('samuel1',), ('adriel1',), ('maycon1',), ('maycon1',), ('teste',), ('teste',), ('stardeath',), ('test',), ('lskd',)]"
b="'[(,)]"

for i in range(0,len(b)):
    str1 = str1.replace(b[i],"")
print (str1)
print (str1.split(" "))