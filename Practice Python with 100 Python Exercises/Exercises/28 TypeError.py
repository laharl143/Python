# Question:  Why is there an error in the code, and how would you fix it?

def foo(a, b):
    x = (a + b)
    return x

print(foo(2, 3) * 10)   #50     #my sol'n


def foo(a, b):
    return a + b
x = foo(2, 3) * 10
print(x)    #50     # answer key

