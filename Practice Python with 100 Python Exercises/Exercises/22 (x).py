#Create a dictionary of keys a, b, b where each key has a value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out

x = {'a': [x for x in range(11)]}
x['b'] = [x + 10 for x in range(21)]
x['c'] = [x + 20 for x in range(31)]
print(x)    #{'a': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 'c': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]}    #my sol'n

from pprint import pprint
 
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)   #{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            #'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            #'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}     #the answer key


#didn't solved