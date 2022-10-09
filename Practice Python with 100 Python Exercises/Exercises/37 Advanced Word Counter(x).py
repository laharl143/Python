# Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.

def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("words1.txt"))

# Explanation 1:

# This solution is like the previous exercise's solution with the difference that before splitting, we are replacing all commas with a space that will let the split method count the number of words.

#did not solve this