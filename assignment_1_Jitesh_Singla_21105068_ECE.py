#Question  1
print('Question  1')

# Taking input from user and storing it .....
Number_1=int(input('Please enter the first  no.-   '))
Number_2=int(input('Please enter the second no.-   '))
Number_3=int(input('Please enter the third  no.-   '))

#calculating the average......
average=(Number_1+Number_2+Number_3)/3

#printing the average........
print(average)
print('\n')

############################################
#Question  2
print('Question  2')

#Taking input.......
gross_income=float(input('Enter your gross income - $'))
Num_Dependent=int(input('Total no. of Dependents - '))

#Rounding of to nearset pennies....
gross_income=round(gross_income,2)

#Defining variable with constant values.......
std_deduction=10000
per_dep_deduction=3000

#Calculating the taxable income ......
taxable_income=gross_income-std_deduction-(per_dep_deduction*Num_Dependent)

#Checking wheather the taxable income is greater than 0 or not.....
if taxable_income>0:
    tax=0.20*taxable_income
else :
    tax=0

#Printing the calculated tax.........
print('Your tax = $',tax)
print('\n')


############################################
#Question  3
print('Question  3')

#Taking input from user.......
SID=int(input('SID-'))
Name=input('Name-')
Gender=input('Gender(F,M or U)-')
Course_name=input('Course Name-')
Course_name=Course_name.upper()
CGPA=float(input('CGPA-'))

#Storing all the data into a list..... 
Student=[SID,Name,Gender,Course_name,CGPA]

#Printing collected data....... 
print(Student)
print('\n')


############################################
#Question  4
print('Question  4')

#Taking input........
student=[]
print('Plz give marks of the students \n')
for i in range(0,5):
    element=int(input())
    student.append(element)

#Sorting the marks.....
student.sort()

#Printing the marks.......
print('--------Output---------')
print(*student,sep='\n')
print('\n')


############################################
#Question  5
print('Question 5')

#Making list of colors as given....
Color=['Red','Green','White','Black','Pink','Yellow']

#Part a -Removing 4th element and printing new lst ....
print('Part a')
Color.pop(3)

print(Color)

#Part b -Removing 'Black' and 'Pink' from the list and replacing them....
print('Part b')
Color=['Red','Green','White','Black','Pink','Yellow']
del Color[3:5]
Color.insert(3,'Purple')
print(Color)


############################################
