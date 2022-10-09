# Question: Access the third value of key b  from the dictionary.
# Expected output: 13  

from pprint import pprint
from stringprep import b1_set
 
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))  # {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}

print(d['b'][2])    #13



