# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"

# and store it in the answer variable....

# answer = word[7:20:1] 

answer = word[word.index("establishment"):word.index("arianism")]

print(answer)