# Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

# Expected output: 

# {'a': 1, 'c': 3, 'b': 2} 


d = {"a": 1, "c":3, "b": 2}
print(d)    #{'a': 1, 'c': 3, 'b': 2}   #my solution

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)    #{'a': 1, 'b': 2, 'c': 3}   #their solution
