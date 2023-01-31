print(1+9)
print(2-4)
print(5*2)
print(4/2)
print(4//2)
print(4%2)
#Strings in python
this_is_a_string_name= "My Name is Ezekiel"
print(this_is_a_string_name)
#there various types of comments, single line and multiple line comment
#Singline Comment  #
'''
Docstring
Comment
'''
array01=[0,12,3,4,5]
print('my array is', array01)
'''
for i in range (2):
    print('Enter Your Age')
    numb= input(int)
print('you are',numb,'years old')
print('Enter Your name')
namess=input(str)
print('Your name is', namess)
'''
a= [2,3,4,6,7,8,9]
print('the array has',len(a),'integers')
names="James Omabti"
print('your name has',len(names),'letters')
#Typecastin variables
var= 123
print(str(var))
flo=123
print(float(flo))
var1=3.5
print(int(var1))
'''print("you for loop range values are:")
for i in range(2, 20, 5):
    print( i)
print("Your while loop values are:")
count=5
while count>0:
    print(count)
    count -=1'''
#the break Statement
print("the break Statement")
for i in range (6):
    print(i)
    if i==1:
        break
#the continue statement
print("the continue statement")
for i in range(8):
    if i==3:
        continue
    print(i)
#the pass statement
print("the pass statement")
for i in range(9):
    if i %2==0:
        pass
    else:
        print(i)
#Return Statement
print("Return Statement")
def func(x):
    if x=="Hello":
        x=input()
        print("your x is:", x)
        return  True
    else:
        return True
#Functions in Python
print("Functions in Python")
def sum_of_two(a, b):
    return  a+b
print(sum_of_two(8,4))
#Importing Python modules
import  math
print(math.pi)
print("Try,except and Finally Blocks")
def divide(a, denominator):
    try:
        return a/denominator
    except ZeroDivisionError as e:
        print("Zero division error")
    finally:
        print("Division Complete")
print (divide(9, 0))
#Lists in Python
print("Lists in Python")
list1=["Samsung","Nokia","Tecno","IPhone","Itel"]
print(list1)
#ccessing ellements in a list
print("Accessing elements in a list")
print(list1[-2])
#Slicing Elements
print("Slicing Elements")
print(list1[0:3])
print(list1[-2:])
#Changing list values
print("Changing list values")
list1[4]='PhantomX'
print(list1)
#lists concatenation
print("lists concatenation")
list2=["Hp", "Lenovo", "Apple","ASUS","Razer","Microsoft","MacbookAir","Acer"]
final_list=list1+list2
print(final_list)
print(final_list[5:13])
#List Replication
'''print("Repricating Lists")
list1=list1*2
print(list1)'''
#Deleting List values
print("Deleting List values")
del list2[1]
print(list2)
#Looping Through List elements
print("Looping through List Elements")
for li in list2:
    print(li)
#in and Not Keywords
print("In and NOT keyword")
print("ASUS" in list2)
print("Nokia" not in list2)
print("asus" in list2)
#Adding Values into List
print("Adding Values into List")
list1.insert(3, 'RealMe')
print(list1)
#Appending list
print("Addingi elemenet at the back of the list")
list1.append('Motorora')
print(list1)
#Sorting List elements
print("Sorting Lists elements in ascending order")
list1.sort()
print(list1)
print("Sorting Lists elements in descending order")
list1.sort(reverse=True)
print(list1)
print("Sorting Lists elements in ascending order")
numbr=[2,4,5,1,7,3]
numbr.sort()
print(numbr)
print("Sorting Lists elements in descending order")
numbr.sort(reverse=True)
print(numbr)
#TUPLES
print("tubles")
tup=("Python","Java","Kotlin","C#","C++","Flutter","C")
print(tup)
print(tup[2:5])
#Python Dictionaries
print("Python Dictionaries")
dict1={'FirstName':'Ezekiel', 'SecondName': 'Mose', 'ThirdName': 'Ogeto'}
print(dict1)
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
#Updating Key Values in Dictionary
print('Updated Key Values')
dict1['FourthName']='James'
print(dict1)
#adding value to the dictionary
print("adding value/key to the dictionary")
dict1['FirstName']='Ezekiah'
print(dict1)
print("Deleting the value/key from a dictionary")
del dict1['ThirdName']
print(dict1)
print("Merging two dictionares")
dict2={1:200, 2:800, 3:500, 4:963}
print(dict2)
dict1.update(dict2)
print(dict1)
#Sets in Python
#a set authomatically remove a duplicate value from the set
print("Sets in Pyton")
set1={1,2,5,7,3,2,2,22,5,7,2,7,7,4}
print(set1)
print("Inserting Elements into a set")
set1.add(90)
print(set1)
print("Inserting Multiple elements into a set")
set1.update([70,88,92,44])
print(set1)
print("Deleting Elements From a Set")
set1.remove(92)
print(set1)
set1.discard(44)
print(set1)
#Operators in Sets
print("Operators in Sets")
set2={1,3,444,7,666,70}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)
#Comprehensions in Python
#This is a shorter syntax to create a new list using the values of an existing list
print("Comprehensions in Python")
a=[0,1,2,3,4,5,6,7]
b=[i+4 for i in a]
print(b)
#Set Comprehensions
print("Set Comprehensions")
#It is a shoter syntax to create a new set using values of an existing set
se={3,4,5,6,7,8,1}
se1={i+2 for i in se}
print(se1)
#Dict Comprehension
print("Dict Comprehension")
di={'name':'John', 'Age':22, 'Gender':'Male'}
di1={val:k for k ,val in di.items()}
print(di1)
#Strings Manipulation
print("Strings Manipulation")
#Escape Sequence
print("Escape Sequence")
# \\    Backslash
# \n    next line
# \t    tab space
# \'    Single Quote
#Strings Indexing
print("Strings Indexing")
stri="Dictionary"
print(stri)
print(stri[2], stri[5], stri[0])
#Case Conversions
print("Case Conversions")
#Upper_Case and Lower_Case Conversion
print(stri)
print(stri.upper())
print(stri.lower())
print(stri.isupper())
print(stri.islower())
print(stri.isalnum())
print(stri.isalpha())
print(stri.istitle())
#join ans split functions
print(list1)
joinlist=','.join(list1)
print(joinlist)
splitlist=joinlist.split(',')
print(splitlist)
'''
print("String Formatting")
first="First"
second="Second"
str2= "I was the {} candidate  my class  Clinton was the {} candidate".format ()
print(str2)
'''


def func(num_list):
    num_list.sort()
    return [num_list[-i] + num_list[-i]
            for i in range (len(num_list))]
print(func([4,3,2,1]))

print((b_val:=True)or(b_val==False))

#FORMATING DATES IN PYTHON
print("FORMATING DATES IN PYTHON")
#We use datetime module to handle date and time

import  datetime
tm=datetime.time(1,30,11,22)
print(tm)

date=datetime.date(2023, 1, 26)
print("Date is",date.day ,"day of", date.month,"of month the year", date.year)

print("Cnverting time from date")
from  datetime import datetime
print(datetime.strptime('26/1/2023','%d/%m/%Y'))

from  time import gmtime, strftime
s=strftime("%a, %d %b %Y %H:%M:%S", gmtime())
print(s)

#Python RegEx
print("#Python RegEx")
import re
landline= re.compile(r'(\d\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
num=landline.search("Landline Number is: 2233-3212-4444")
print("Landline Number is: {}".format(num.group()))
print(num.group(1))

#Debbugging in python
print("Debbugging in Python")
#Traceback as a String
import traceback
try:
    raise Exception("Error Occurred")
except:
    with open('error.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())
    print("The traceback info was writen to error.txt")

#Assert Statements in Python
'''Assertions are widely used in debugging programs and checking if the code is performing some operations that is 
obviously wrong according to teh logic of the program'''
#Components of an assertion statement
'''
assert keyword
condition resulting to a boolean value
a dispay message for when an assertion fails
a comma separating the condition and the display message
'''
print("Assertion Statement")
#sum=4
#assert sum==5, 'Addition Error'

print("Logging in Python")

import logging
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s')
logg=logging.getLogger()
logg.setLevel(logging.DEBUG)

logging.debug("Debug Message")
logging.warning("its a warning")
logging.info("Just an information")

#Lambda Function in Python
print("Lambda functions in Python")
print("Lambda is a small anpnymous functions in python")
print("Normal Function")
def mul (a,b):
    return a*b
print(mul(3,5))

print("Equivalent Lambda Function")
mul=lambda a,b: a*b
print(mul(3,5))



























