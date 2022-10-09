# Question: Create a function that takes any string as input and returns the number of words for that string.

def count_words(string):
    string_list = string.split()
    return len(string_list)

print(count_words("Hey there it's me"))

# Explanation:

# We're using split  here which is a string method that splits a string into several strings given a separator passed inside the brackets. When you don't pass a separator, split  will split a string at white spaces. This will output a list of strings..Applying len  to that list returns the number of list items, so the number of words.

#did not solve