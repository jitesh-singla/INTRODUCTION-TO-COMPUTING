################### Question 1 #####################

print('################### Question 1 #####################')
print('\n')

input_string=input('enter a string :')  # taking input from user
string_lower=input_string.lower()
if ' ' in string_lower :
    list1=string_lower.split() 
else :
    list1=list(string_lower)
count={}       # specifing empty dictionary to count the no. of occurance
for i in list1 :         
    if i not in count :
        count[i]=1
    else :         
        count[i]=count[i]+1
#### printing the occurance of the  each word or character
for i in count :
    print(i,count[i])

print('\n')

################## Question 2 #####################

print('################### Question 2 #####################')
print('\n')
day=int(input('provide a date (1-31):'))   # Taking input 
month=int(input('enter the month (1-12):'))
year=int(input('enter the year (1800-2025):'))

# checking if the input is of correct format : 

if day<1 or day >31 or month <1 or month >12 or year <1800 or year >2025 or (month==2 and ((year%4==0 and day>29)or(year%4!=0 and day>28)) or ((month in [4,6,9,11]) and day>30)) :
        print('Invalid input')

###### Printing the next date if the input is in right format

else :
      #### condition for leap and non leap year dates

    if month==2: 
        if year%4==0 :
            if day<29:
                day=day+1
                print('next date is :',day,'/',month,'/',year)
            else :
               print('the next date is : 01 /03 /',year)
        elif day <28 :
            day=day+1
            print('next date is :',day,'/',month,'/',year)
        elif day==28 :
            print('the next date is : 01 / 03 /',year)
    
    ###### for months having 30 days 

    elif month in [4,6,9,11] :     
        if day <30 :
            day=day+1
            print('next date is :',day,'/',month,'/',year)
        else :
            month=month+1
            print('the next date is : 01 /',month,'/',year)

    ###### for months having 31 days expect december 

    elif month in [1,3,5,7,8,10] :
        if day<31 :
            day=day+1
            print('the next date is :',day,'/',month,'/',year)
        else :
            month=month+1
            print('the next date is : 01  /',month,'/',year)

    ##### for december (last month of year)

    else :
        if day <31:
            day=day+1
            print('the next date is :',day,'/',month,'/',year)
        else :
            year=year+1
            print('the next date is : 01 / 01 /',year)
print('\n')

################## Question 3 #####################

print('################### Question 3 #####################')
print('\n')
list1=[]    #creating 2 empty list one for holding no. and second for its square
list2=[]
print('Enter the input numbers (enter 0 to stop input process) :') 
s=int(input())        # taking input via loop with terminating condition input==0
while s!=0 :
    list1.append(s)       # adding to the list 
    list2.append(s**2)
    s=int(input())
output_list=list(zip(list1,list2))   # creating the list of tupils pairs 
print('Output list is :',output_list)
print('\n')

################## Question 4 #####################

print('################### Question 4 #####################')
print('\n')
grade_point=int(input('Enter the grade point [integer between (4,10)]: '))
if grade_point<4 or grade_point>10 :
    print('invalid input')
else :        ## Specifiing dictionaries each for grade and performance having grade_point as theirs keys:
    grade={4:'D',5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
    performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',10:'Outstanding'}
      ## printing the required for a input given 
    print('Your grade is',grade[grade_point],'and',performance[grade_point],'performance')
print('\n')

################### Question 5 #####################

print('################### Question 5 #####################')
print('\n')

string='abcdefghijk'
list1=list(string.upper())    # crreating list of upper case letter

for i in range(1,7) :         # loop to print the required pattern
    for j in range(1,i):
        print(' ',end='')
    for  j in list1:
        print(j,end='')
    del list1[-2:]
    print('')

print('\n')   
    
################### Question 6 #####################

print('################### Question 6 #####################')
print('\n')
register=dict()     # creating an empty dictionary
ch='y'
while(ch=='y') :     # taking input and adding it tp the dictionary 
    sid=int(input('Enter the SID of the student :'))
    name=input('Enter the name of the student :')
    register[sid]=name
    ch=input('Due of want to give another response?[y/n]')

# Part a ---------------
print('\n###### Part a ######\n')    
for i in register :       ## printing values in dictionary
    print(i,register[i])

# Part b ---------------
print('\n###### Part b ######\n') 
student_name=list(register.values())  ## Making list of student names
student_name.sort()        ## Sorting the student names
sorted_register={}
for i in student_name:
    for key in register:      
        if i==register[key]:
            sorted_register[key]=i         ## Creating new sorted dictionary with student names 
print('the sorted dictionary is:')
for i in sorted_register :       ## printing values in dictionary
    print(i,sorted_register[i])

# Part c ---------------
print('\n###### Part c ######\n')    
list1=[]
for i in register:      ## Making list of SID 
    list1.append(i)
list1.sort()             ## Sorting the SID 
sorted_register=dict()
for i in list1:              ## Creating new sorted dictionary with SID               
    sorted_register[i]=register[i]
print('the sorted dictionary is:')
for i in sorted_register:
    print(i,sorted_register[i])

# Part d ---------------
print('\n###### Part d ######\n')           
search_sid=int(input('Enter the sid :'))     
print('Name of student with SID',search_sid,'is :',register[search_sid])
print('\n')

################### Question 7 #####################

print('################### Question 7 #####################')
print('\n')
no_of_term=int(input('Enter the no. of term of fibonacci series u want :'))    #Taking input
if no_of_term<=0:
    print('Invalid input')
else:
    a=0
    b=1  #specifing the default values of fibonahi series

    for i in range(1,no_of_term+1) :  #printing and calculating the sum of the series :
        if i==1 :
            print(a,end=" ")
            sum=0
        elif i==2 :
            print(b,end=" ")
            sum=1
        else :
            c=a+b
            print(c,end=" ")
            a=b
            b=c
            sum=sum+c
    ## Calculating the average:
    average=sum/no_of_term
    print('\nAverage of the terms is :',average)

print('\n')

################## Question 8 #####################

print('################### Question 8 #####################')

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

# Part a)------------
print('\n###### Part a ######\n')

new_set=set1^set2
print('The new set is :',new_set)

# Part b)------------ 
print('\n###### Part b ######\n')

set0=set1^set2    # creating a set having element that are in st1 and 2 but not both 
new_set=set0^set3 
print('New set is :',new_set)

# Part c)------------
print('\n###### Part c ######\n')

inter_set_123=(set1&set2&set3)   # Set of interaction of the 3 sets 
new_set=((set1&set2)|(set2&set3)|(set3&set1))-inter_set_123      # calculating the required sets 
print('Required set is :',new_set)

# Part d)------------ 
print('\n###### Part d ######\n')

list1=[]    # creating an empty list to get the elements
for i in range(1,11) :
    if i not in set1:
        list1.append(i)
new_set=set(list1)     # converting list into set 
print('Required set is :',new_set)

# Part e)------------
print('\n###### Part e ######\n')

list2=[]          # creating an empty list to get the elements
for i in range(1,11) :
    if (i not in set1) and (i not in set2) and (i not in set3):
        list2.append(i)
new_set=set(list2)         # converting list into set 
print('New set is :',new_set)




