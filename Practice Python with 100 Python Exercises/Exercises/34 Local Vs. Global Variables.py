# Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).

# Expected output: 1

# def foo(): 
#     c = 1 
#     return c 
# foo() 
# print(c)          #problem: you can't print c outside its scope


# my Sol'n:
def foo(): 
    c = 1 
    return c 
print(foo())    #1      #my sol'n


def foo():
    global c        #answer key added the global keyword
    c = 1 
    return c 
foo() 
print(c)        #1      #answer key



