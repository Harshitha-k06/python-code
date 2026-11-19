#conditional statement                                                       
"""s = eval(input("enter a tuple: "))
if type(s) == tuple:
    print("input is tuple")
else:
    print("input is not tuple")         

     #digit 
num=int(input("enter digit:")) 
if 10<=num<=99:
  print("two digit number")
else:
   print("not a two digit number")       

   


    
# convert string to upper case
s=input("enter a string: ")
print(s.upper())



# exam1                                                          #exa2
s=(input("enter a string: "))                                   ch=(input("enter a character: ")) 
if s.isupper()==True:                                               if 'A'<=ch<='Z':
    print("string is in upper case")                                    perint("string is in upper case")
elif s.islower()==True:                                          elif 'a'<=ch<='z':
    print("string is in lower case")                                    print("string is in lower case")
elif s.isdigit()==True:                                           elif '0'<=ch<='9':
    print("string is digit")                                            print("string is digit")
else:                                                               else:
    print("input is  special character")                          print("input is  special character")


list1=[1,2,3,4,5]
if len(list1)%2==0:
    print("list has even ")
else:
    print("list has odd ")



#while statement
i=1
while i<=5:
    print("hello")
    i+=1 


list1=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list1):
    print(list1[i])
    i+=


n=int(input("enter :"))
rev=0
while  n>0:
    Id=n%10
    n=n/10
    rev=rev*10+Id
print(rev)


s=input("enter : ")
output=""
for i in s:
    if 'a'<=i<='z':
        output=output+chr(ord(i)-32)
    else:
        output+=i
print("output is:",output)


s=[12,10,'hello','Good',5j,'Bye']
output={}
for i in s:
    if type(i)==str:
        output[i]=i[0]+i[-1]
print("output is:",output)



for i in range(1,6):
    for j in range(1,6):
        print('a',end=' ')
    print()


def convert():
    s = input("enter a string: ")
    output = ""
    for i in s:
        if 'a' <= i <= 'z':
            output = output + chr(ord(i) - 32)
        else:
            output += i
    print("output is:", output)
convert()"""

def convert():
    s = input("enter a string: ")
    output = ""
    for i in s:
        if 'A' <= i <= 'Z':
            output = output + chr(ord(i) + 32)
        else:
            output += i
    print("output is:", output)
convert()