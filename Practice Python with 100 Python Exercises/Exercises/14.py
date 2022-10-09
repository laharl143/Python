# Question: Complete the script so that it removes duplicate items from the list a .

# Expected output: 
#   ['1', 2, 1] 

a = ["1", 1, "1", 2]

print(set(a))   #{1, 2, '1'}

#answer explanation: sets can't contain duplicates. so the easiest way is to convert the list to set