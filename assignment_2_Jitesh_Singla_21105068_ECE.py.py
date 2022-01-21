##########-----------------Question 1-----------------##########  

print("Question 1")

#### Storing the given input ####
input_string="Python is a case sensitive language"

# 1.a) Finding the length of string #
print("Part 1.a)")
length=len(input_string)
print(length)

# 1.b) Reverse the order of the string #
print("Part 1.b)")
reverse_string=input_string[::-1]
print(reverse_string)

# 1.c) Slicing and printing new string #
print("Part 1.c)")
sub_input_string=input_string[10:26]
print("The new string :",sub_input_string)

# 1.d) Replacing and printing #
print("Part 1.d)")
replace_string=input_string.replace("a case sensitive","object oriented")
print(replace_string)

# 1.e) Priting the index of "a" #
print("Part 1.e)")
print(input_string.index("a"))

# 1.f) Removing the white spaces #
print("Part 1.f)")
print(input_string.replace(" ", ""))

print("\n")

##########-----------------Question 2-----------------##########  

print("Question 2")

# specifing variables # 
Name="Jitesh Singla"
SID=21105068
Department="ECE"
CGPA=9.8

# pritning the statement #
print("Hey, %s Here ! \nMy sid is %d \nI am from %s department and my CGPA is %f"%(Name,SID,Department,CGPA))

print("\n")

##########-----------------Question 3-----------------##########  

print("Question 3")


a=56
b=10

print("a&b :",a & b)
print("a|b :",a | b)
print("a^b :",a ^ b)

# Left shift by 2 bits #
print("a<<2 :",a<<2,"\tb<<2 :",b<<2)
# Right shift a by 2 bits and b by 4 bits #
print("a>>2 :",a>>2,"\tb>>4 : ",b>>4)

print("\n")

##########-----------------Question 4-----------------##########

print("Question 4")

# Taking input #
a=int(input("enter the first no. :"))
b=int(input("enter the second no. :"))
c=int(input("enter the third no. :"))

# Finding and printing the highest no. #
if a>b:
    if a>c:
        print("Highest no. is :",a)
    else:
        print("Highest no. is :",c)

if b>a:
    if b>c:
        print("Highest no. is :",b)
    else:
        print("Highest no. is :",c)

print("\n")

##########-----------------Question 4-----------------##########

print("Question 5")

# Taking input #
input_string=input("Enter a string :")

if "name" in input_string :
    print("Yes")
else :
    print("No")

print("\n")

##########-----------------Question 5-----------------##########

print("Question 6")

# Taking input #
a=int(input("Enter 1st length :"))
b=int(input("Enter 2nd length :"))
c=int(input("Enter 3rd length :"))

if a+b>c & a+c>b & b+c>a :
   print("Yes")
else :
    print("No")



##########--------------------------------------------##########
