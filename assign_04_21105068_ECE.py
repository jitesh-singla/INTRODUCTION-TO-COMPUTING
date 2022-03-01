############################### Question 1 ###############################



print('############################### Question 1 ###############################')
print()
## defining the function :
def tower_of_harnoi(n,source,destination,auxillary): 
    if n==1 :
        print('Move disk 1 from source',source,'to destination',destination)
        return 
    tower_of_harnoi(n-1,source,auxillary,destination) 
    print('move disk',n,'from source',source,'to destination',destination)
    tower_of_harnoi(n-1,auxillary,destination,source)

## calling function for 3 discs :

tower_of_harnoi(3,'S','D','A')   

print()

############################### Question 2 ###############################

print('############################### Question 2 ###############################')
print()

## defining factorial recursive function          
def pascal_triangle(n):
    def factorial(n) :
        if n==0 :
           return 1
        else :
           return n*factorial(n-1)
    for i in range(n+1):
        c=int(factorial(n)/(factorial(i)*factorial(n-i)))
        print(c,end=' ')


        
## Printing pascal triangle with factorial recursion :
no_rows=int(input(('enter the no. of rows for passcal triangle :')))
print('with recursion \n')
if no_rows>0 :
    for i in range(no_rows) :  
        for c in range(i,no_rows-1):
            print(' ',end='')
        pascal_triangle(i)
        print()
    print()
## Printing without recursion 
    print('Without recursion \n')

    for i in range(no_rows) :  
            for c in range(i,no_rows-1):
                print(' ',end='')
            for j in range(i+1):
                a,b,d=1,1,1
                for k in range(i+1):
                    if k>0:       ## calculating the factorials by help of for loops 
                        a=a*k
                        if k<=j:
                            b=b*k
                        if k<=i-j:
                            d=d*k
                print(int(a/(b*d)),end=' ')
            print()
      
else :
    print('invalid input')

############################### Question 3 ###############################

print('############################### Question 3 ###############################')
print()
a=int(input('enter first no. :'))  ## taking input 
b=int(input('enter secod no. :'))
if b==0 :
    print('Denominator cant be 0 , error')
else :
    result=divmod(a,b)    ## calling divmod function
    print(result)
    print('\nPart a)')
    print(callable(divmod))   ## using callable function to check calability

    print('\nPart b)')
    if result[0] == 0 :   ## checking weather the values are non zeros 
        if result[1] == 0 :
            print('both values are zero ')
    else :
       if result[1] == 0 :
            print('one value is zero')
       else :
            print('both values are non zero')    
    
    print('\nPart c)')
    lis=[result[0],result[1],4,5,6]   ##adding (4,5,6) to values and finding out values greater than 4 
    print(lis)
    set1=set()
    for i in lis :
        if i > 4 :
            print(i,end=' ')
            set1.add(i)   ## making set of the values
    print()


    print('\nPart d)')
    print(set1)

    print('\nPart e)')
    fr_set=frozenset(set1)  ## making set immutable
    print('the immutable set is :',fr_set)

    print('\nPart f)')
    b=max(set1)
    print('max value :',b)    ### calculating max value and its hash value
    print('Hash value :',hash(b))


print()

############################### Question 4 ###############################

print('############################### Question 4 ###############################')
print()

class Student :   ### defining class with its constuctor and destructor
    def __init__(self,name,roll_no) :
        self.name=name           
        self.roll_no=roll_no

    def __del__(self) :
        print('Record of ',self.name,' destroyed')


obj1=Student('Jitesh Singla',21105068)      ## creating the object and assigning the value 
print(obj1.name) 
print(obj1.roll_no)
del obj1      ### deleting the object 
print()   
############################### Question 5 ###############################

print('############################### Question 5 ###############################')
print()

class Employee :      ##  creating the class 
    def __init__ (self,name,salary) :
        self.name=name 
        self.salary=salary  

      

empolye1=Employee('Mehak',40000)    ## creating the objects 
empolye2=Employee('Ashok',50000)
empolye3=Employee('Viren',60000)

print('name :',empolye1.name,'salary :',empolye1.salary)   ## printing the details.
print('name :',empolye2.name,'salary :',empolye2.salary)
print('name :',empolye3.name,'salary :',empolye3.salary)
print ('\nPart a')
empolye1.salary=70000    ## updating the salary 
print('updated salary of',empolye1.name,'is',empolye1.salary)

print ('\nPart b')
del empolye3    ### deleting the record of Viren 
print('Record of viren is deleted')

############################### Question 6 ###############################

print('############################### Question 6 ###############################')
print()

def anagram(s):  ## Defining the anagram function 
    if s=='' :
        return [s]
    else :
        word=[]
        for i in anagram(s[1:]) :
            for p in range(len(i)+1) :
                word.append(i[:p]+s[0]+i[p:])
        return word
### Taling input from the users 
word1=input('Give a word to test your friendship :')
wordl1=word1.lower()
word2=input('Give a meaningfull word containing same letter of the word given by your friend :')
wordl2=word2.lower()
## checking if the word contains same letter as the first word i.e its in its anagram or not
if wordl2 in anagram(wordl1) :  
    c=input('does the word entered by 2nd friend seems meaningfull ? (y/n) :')
    if c == 'y' :   ### checing if the word is meaningfull or not 
        print('Test passed , friendship is true')
    else :
        print('Test failed , friendship is false ')
else :
    print('word doesnt have the same letters , test failed friendship is false ')


        


                              