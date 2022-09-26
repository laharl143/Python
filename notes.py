from distutils.log import info
from doctest import script_from_examples
import math
from msilib.schema import File
from re import A, X
from sqlite3 import OperationalError
from tkinter import BOTH


Open IDLE 

Open new File

F5 to run and it will open in IDLE







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



###################Variables:

>>> number = 1  #this is used to store value to variable


Type Function:  #this is used to know the type of any variable
    
>>> type(number)
<class 'int'>



HOW TO NAME VARIABLES:
    
-lower case
-separate with underscore(_)

example:
    first_number   (good example)
    second_number  (good example)
    
    FirstNumber    (bad example) #camel case is used in javascript
    
    

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



ORDERING OPERATIONS:
    
B Brackets
O Order     #^ ,square root, etc
D Division
M Multiplication
A Addition
S Subtraction





Writing Variables:
    
!!!It's Important to right variables in python with no spaces.!!!





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


##Adding or multiplying strings

>>> A = "part one"
>>> B = "part two"
>>> A + B
"part onepart two"

>>> A * 3
"part onepart onepart one"
>>> "=" * 20
"===================="


##Adding string and integer

>>> A = "part"
>>> B = 1
>>> A + B
TypeError: Can't convert 'int' object to str implicitly

#This is the fix
>>> A + str(B)   #you need to convert the int to str first
'part1'

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