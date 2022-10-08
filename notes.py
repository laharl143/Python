from distutils.command.build_scripts import first_line_re
from distutils.log import info
from doctest import script_from_examples
import math
from msilib.schema import File
from re import A, X
from sqlite3 import OperationalError
from tkinter import BOTH

from parser import tuple2st


Open IDLE

Open new File

F5 to run and it will open in IDLE






################################################################
#The secrets of a Top Programmers:
How to ask great questions

Use the community!


The Python Bible “How to ask an
Excellent Question” Checklist
Hi There! Use the following checklist to ask an excellent question in the course forums when you have a problem related to python programming. Either myself or someone else will be there to help you as quick as a flash!

1) Make a great question title ☐
a. I have added the [Help] Tag at the start of my title ☐
b. My Question title is Clear and descriptive and it is obvious what the problem is ☐

2) My Question has a complete description ☐
a. I have written down the observed behaviour (What has happened) ☐
b. I have written down the expected behaviour (What was supposed to happen) ☐
c. I have added a link to my code using gist.github.com ☐
d. I have mentioned what I think the problem might be and the location. ☐
e. I have provided a list of at least 3 things that I have tried to solve the problem ☐
f. My Description uses full sentences with correct grammar and punctuation ☐

3) I have included other relevant information
a. Error messages in full ☐
b. Version of python used ☐
c. Screen shots where necessary ☐


################################################################
How to ask Question in a Community Example:

Title:

    [Help] Answer not being shown on screen when running Python script

Description:

    1) Observed Behaviour -
    Script runs successfully but answer doesnt show up

    2) Expected Behaviour -
    I expected the answer 2 to show up when I ran the script.

    3) Link to Code: #(Use gist.github) -
    https://gist.github.com/laharl143/2b3072c1ebc8245a182800355fcc3955

    4) Where I think the problem is-
    There must be something different between script and the shell
    It worked in the shell...lines 1-2 hold the issue
    Is something missing?

    5) What I have tried -
    I tried running the script with different numbers. No difference.

    6) Errors and Warnings
    None

    7) Version info
    3.5.2

    8) Screenshots
    N/A


################################################################
Variables:

>>> number = 1  #this is used to store value to variable


Type Function:  #this is used to know the type of any variable

>>> type(number)
<class 'int'>


################################################################
HOW TO NAME VARIABLES:

-lower case
-separate with underscore(_)

example:
    first_number   (good example)
    second_number  (good example)

    FirstNumber    (bad example) #camel case is used in javascript


################################################################
2 DIFFERENT TYPE OF NUMBERS IN PYTHON:

>>> type(2)
<class 'int'>  #integer

>>> type(0.5)
<class 'float'> #float


rare type:

>>> 5 % 3   #modulo gives the remainder
2

>>> 10 % 2
0


################################################################
ORDERING OPERATIONS:

B Brackets
O Order     #^ ,square root, etc
D Division
M Multiplication
A Addition
S Subtraction





Writing Variables:

!!!It's Important to write variables in python with no spaces.!!!




################################################################
Math Module:   (import math)

>>>round(2.1)
2
>>>round(1.5)
2
>>>math.floor(1.5)
1
>>>math.ceil(2.1)
3

>>>math.pi(2.1)
3.141592653589793
>>>math.e(2.1)
2.718281828459045

>>>math.sin(math.pi / 2)
1.0
>>>math.sin(math.pi)
1.2246467991473532e-16
>>>math.floor(math.sin(math.pi))
0
>>>math.cos(0)
1.0
>>>math.asin(0)    #inverse function of sine
0.0
>>>math.acos(0)    #inverse function of cosine
1.5707963267948966

>>>math.hypot(3,4) #get hypotenuse with (a,b)
5.0

>>>math.pow(2,3)  #2 to the power of 3
8.0
>>>2 ** 3   #2 to the power of 3
8

>>>math.exp(2)  #E^2
7.38905609893065

>>>math.log(math.e)
1.0
>>>math.log10(1000)  #10^3 = 1000 ; logarithmic
3

################################################################
##Adding or multiplying strings

>>> A = "part one"
>>> B = "part two"
>>> A + B
"part onepart two"

>>> A * 3
"part onepart onepart one"
>>> "=" * 20
"===================="

################################################################
##Adding string and integer

>>> A = "part"
>>> B = 1
>>> A + B
TypeError: Can't convert 'int' object to str implicitly

#This is the fix
>>> A + str(B)   #you need to convert the int to str first
'part1'

################################################################
##Python format function
>>>"{} - {}".format(A,B)   #this is used to put variables to a placeholder
'part - 1'
>>>"{1} - {0}".format(A,B) #this is used to reverse their position
'1 - part'


#String methods:    #important note: strings are immutable;
>>> string.method()

# .count()
>>> text = "happy birthday"
>>> text.count("a")    #this counts how many letter "a" in the string
2

>>> text.count("day")
1
################################################################
# .lower(), .upper(), .capitalize(), .title()
>>> x = "Happy Birthday"
>>> x.lower()           #this makes the string all lower case
"happy birthday"
>>> x.upper()           #this makes the string all upper case
"HAPPY BIRTHDAY"
>>> x                   #if you call again the string, it will go back to its original
"Happy Birthday"

>>> x = x.lower()       #this registers the x to lower case
"happy birthday"
>>> x                   #if you call x, its now in lower care
"happy birthday"
>>> x.capitalize()      #capitalize method() is used to capitalize the first letter of the sentence
"Happy birthday"
>>> x.title()           #title method() is used to capitalize the first letter of each word in a sentence
"Happy Birthday"

# .islower(), .isupper(), x.istitle()
>>> x.islower()         # .is<method>() is used to check the current case the x is
False
>>> x.isupper()
False
>>> x.istitle()         #here its True, so the x is currently a title case
True

################################################################
# .index(), .find(), .strip()
>>> x = "happy birthday"
>>> x.index("birthday")     #this counts the first letter of "birthday"; 0=H, 1=A, 2=P, 3=P, 4=Y, 5=*space* 6=Birthday
6
>>> x.find("birthday")
6
>>> y = "0000000000000happybirthday00000000000000"
>>> y.strip("0")            #this is used to strip out the "0" in the string
"happybirthday"
>>> y.lstrip("0")           #strips only the left side
"happybirthday00000000000000"
>>> y.rstrip("0")           #strips only the right side
"0000000000000happybirthday"
>>> y.strip()               #if you use strip without input, it will only strip the spaces
"happybirthday"

################################################################
#Slice

>>> word = "supercalifragilisticexpialidocious"
>>> word[0]     #count start at 0
's'
>>> word[2]
'p'
>>> word[0:5:1]     #[start:end:step] format
'super'
>>> word[0:5:2]     #2 step
'spr'               #the output is 0,2,4
>>> word[5:9:1]     #the start is 5
'cali'
>>> word[5:]        #the start is 5 all the way to the end
'califragilisticexpialidocious'
>>> word[5::2]      #start 5, step 2
'clfaiitcxildcos'
>>> word[:7]        #from start to the desired end[7]
'superca'
>>> word[:8]
'supercal'
>>> word[::-1]      #this is used to invert word
'suoicodilaipxecitsiligarfilacrepus'

>>> word = "supercalifragilisticexpialidocious"
>>> word[-1]        #used to count from the last letter of word. !!note the last is -1 not -0
's'
>>> word[-5]
'c'
>>> word[-2]
'u'
>>> word.index("cali")      #used to know the number of the first letter of input
'5'
>>> word.index("fragi")
'9'
>>> word[word.index("cali"):word.index("fragi")]    #used to get the word from first:second
'cali'
>>> word[word.index("docious")]     #used to get the word from first:second
'docious'
>>> word[word.index("fragilistic"):word.index("exp")]   #used to get the word from first:second
'fragilistic'
>>> word[word.index("fragilistic"):word.index("e")]    #there is an error here since the second input is only "e"
'' 

################################################################
Boolean
if
elif
else


################################################################
Logical Operators

>>> not True
False
>>> not False
True
>>> not 2 < 3
False
>>> not 3 > 1
False
>>> not 4 == 3
True
>>> not True
False
>>> not True
False

################################################################
Conditional Operators

==  // equal
!=  //not equal
<=  //less than or equal
>=  //greater than or equal
<   //less than
>   //greater than

################################################################
Chained Conditionals

or  //if either is true, the condition is true
not //its the opposite 
and //all of the value should be true, for the condition to be true

Order of operation:
not //first to operate
and //second to operate
or //last to operate

x = 1
y = 2 
z = 4

result = ((x + y) > z) or ((x + y) < z)
print(result) #True

result = ((x + y) > z) and ((x + y) < z)
print(result) #False

result = not((x + y) > z) and ((x + y) < z)
print(result) #True

################################################################
If/Else/Elif

x = input('Name: ')

if x == 'Tim':
    print('You are great!')
elif x == 'Joe':
    print('Hello Joe')
elif x == 'Jhanna':
    print('Hi langga!')
else:
    print('No')

################################################################
List/Tuples

List
-list use a [] square brackets
-is an ordered collection
-list is mutable; it means it is changeable

Tuple 
-tuples use a () round brackets
-cannot move and cannot change elements
-tuple is an immutable list

List:
x = [4, True, 'hi']   #list
print(len(x))  #3

x = [4, True, 'hi']   
x.append('hello')  #append adds a single data to the end of the list
print(x)  #[4, True, 'hi', 'hello'] 

x = [4, True, 'hi']   
x.extend([4,5,5,5,5])  #extend adds lists to a list
print(x)  #[4, True, 'hi', 4,5,5,5,5] 

x = [4, True, 'hi']   
print(x.pop())  #'hi'       #pop removes the last data in the list
print(x)        # [4, True]

x = [4, True, 'hi']   
print(x.pop(0))  #'4       #you can put an argument inside pop and it will remove that element
print(x)        # [True, 'hi']

x = [4, True, 'hi']   
print(x[1])     #True     # this is used access an element inside a list

x = [4, True, 'hi']   
x[0] = 'hello'  # this is used to change an element inside a list
print(x)     #['hello', True, 'hi']

Tuple:
x = (0,0,2,2)
print(x[0])     # 0

x = (0,0,2,2)
x[0] = 5
print(x[0])     # error ; tuple is immutable!

x = (0,0,2,2)
x.append(3)
print(x[0])     # error ; tuple is immutable!

################################################################
For Loops:   #(start,stop,step)

for i in range(5):     #(stop)   #default start is 0
    print(i)  #0
              #1
              #2
              #3
              #4

for i in range(1,5):     #(start,stop)
    print(i)  #1
              #2
              #3
              #4
              #5

for i in range(1,5,2):     #(start,stop,step)   #step is increment    #you can put a negative number in step
    print(i)  #1
              #3
              #5
              #7
              #9

for i in range(5,-1,-1):     #(start,stop,step)   #you can put a negative number in step
    print(i)  #5
              #4
              #3
              #2
              #1
              #0

for i in [3,4,42,3,69]:    #you can also use for loop in list
    print(i)  #3
              #4
              #42
              #3
              #69

x = [3,4,42,3,69]
for i, element in enumerate(x):    #you can also use for loop in list
    print(i,element)  #0  3
                      #1  4
                      #2  42
                      #3  3
                      #4  69
            
################################################################
While Loops

i = 0
while i < 5:
    print('run')
    i += 1  #run
            #run
            #run 
            #run
            #run 

################################################################
Slice Operators   #[start:stop:step]

x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"

sliced = x[0:4:2]       #[start:stop:step]
print(sliced)  #[0, 2]   #start from 0, stop at 4, increment by 2   #important note! the argument in stop is not included in the printed slice

sliced = x[0:5:2]
print(sliced)  #[0, 2, 4]   #start from 0, stop at 5, increment by 2

sliced = x[:5]   #[:stop]
print(sliced)  #[0, 1, 2, 3, 4]

sliced = x[2:]   #[start:]
print(sliced)  #[2, 3, 4, 5, 6, 7, 8]

sliced = x[4:2:-1]    #[start:stop:step]
print(sliced)  #[4, 3]

sliced = x[::-1]    #[::step]    #this is used to print the list in backwards
print(sliced)  #[8, 7, 6, 5, 4, 3, 2, 1, 0]

sliced = s[::-1]    #[::step]    #this is used to print the list in backwards
print(sliced)  #olleh

################################################################
Sets    #is a collection which is unordered, unchangeable*, and unindexed.

s = {4,32,2,2}   #this is called a set literal
print(s)    #{32, 2, 4}     # the duplicate 2 were removed

s = {4,32,2,2}   
s.add(5)
print(s)    #{32, 2, 4, 5}

s = {4,32,2,2}   
s.remove(2)
print(s)    #{32, 4}

s = {4,32,2,2}   
print(4 in s)    #True

s = {4,32,2,2}   
print(33 in s)    #False

s = {4,32,2,2}  
s2 = {3,4,22,1}  
print(s.union(s2))  #{32, 1, 2, 3, 4, 22}

s = {4,32,2,2}  
s2 = {3,4,22,1}  
print(s.difference(s2))   #{32, 2}  #it removes the elements that are common

s = {4,32,2,2}  
s2 = {3,4,22,1}  
print(s.intersection(s2)) #{4}

################################################################
Dictionaries    #Dictionaries are used to store data values in key:value pairs.

x = {'key': 4}
print(x['key'])  #4

x = {'key': 4}
x['key2'] = 5
print(x)  #{'key': 4, 'key2': 5}

x = {'key': 4}
x['key2'] = 5
x[2] = 8
print(x)  #{'key': 4, 'key2': 5, 2: 8}

x = {'key': 4}
x['key2'] = 5
x[2] = [2,2,1,1]
print(x)  #{'key': 4, 'key2': 5, 2: [2, 2, 1, 1]}

x = {'key': 4}
print('key' in x)   #True

x = {'key': 4}
print(x.values())   #dict_values([4])

x = {'key': 4}
print(list(x.values()))   #[4]

x = {'key': 4}
print(list(x.keys()))   #['key']

x = {'key': 4}
del x['key']
print(x)  #{}

x = {'key': 4}
for key, value in x.items():
    print(key, value)   #key 4

################################################################
Comprehensions  #provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.)

x = [x for x in range(5)]
print(x)    #[0, 1, 2, 3, 4]

x = [x + 5 for x in range(5)]
print(x)    #[5, 6, 7, 8, 9]

x = [0 for x in range(5)]
print(x)    #[0, 0, 0, 0, 0]

x = [0 for x in range(30) for x in range(5)]
print(x)    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = [i for i in range(100) if i % 5 == 0]    #modulus is used in divisibility   #this is the multiples of 5 up to 100 but not including 100
print(x)    #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

x = {i for i in range(100) if i % 5 == 0}    #can also be used in sets
print(x)    #{0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95}

x = {0:i for i in range(100) if i % 5 == 0}    #can also be used in a dictionary
print(x)    #{0: 0, 5: 0, 10: 0, 15: 0, 20: 0, 25: 0, 30: 0, 35: 0, 40: 0, 45: 0, 50: 0, 55: 0, 60: 0, 65: 0, 70: 0, 75: 0, 80: 0, 85: 0, 90: 0, 95: 0}

################################################################
Functions   #function is a block of code which only runs when it is called

def func():
    print('Run')
func()  #Run

def func(x, y):     #(parameter, parameter)
    print('Run', x, y)
func(5, 6)  #Run 5 6      #(argument, argument)

def func(x, y):     
    print('Run', x, y)
    return x * y
print(func(5, 6))   #Run 5 6  
                    #30

def func(x, y):     
    print('Run', x, y)
    return x * y, x / y
print(func(5, 6))   #Run 5 6
                    #(30, 0.8333333333333334)

def func(x, y):     
    print('Run', x, y)
    return x * y, x / y
r1, r2 = func(5, 6)
print(r1, r2)   #Run 5 6
                #30 0.8333333333333334               
                #     
################################################################
*Args & **Kwargs
#   *args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed
#   **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.

def func (*args, **kwargs):
    pass
x = [1, 23, 236363, 2727]
print(*x)   #1 23 236363 2727

def func (*args, **kwargs):
    pass
x = [1, 23, 236363, 2727]
print(x)
print(*x)   #[1, 23, 236363, 2727]
            #1 23 236363 2727

def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair) #1 2                    #single asterisk is used for a tuple or list
                #3 4

def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(**{'x': 2, 'y':5}) #2 5        #double asterisk is used for dictionaries
                            #2 5


################################################################
Scope & Globals


################################################################
Exceptions

################################################################
Handling Exceptions

################################################################
Lambda

################################################################
Map & Filter

################################################################
F Strings

################################################################






