# Question: Please complete the script so that it prints out the expected output.

# Expected output: 
# b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from pprint import pprint

# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))  #{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}
# pprint(d)   #{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             #'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#             #'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}


d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for key, value in d.items():
    print(key, "has value", value)  #a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                    #b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                                    #c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]       #answer key

#i didnt solve this
