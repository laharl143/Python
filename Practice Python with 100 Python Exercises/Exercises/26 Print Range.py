# Question: Make a script that prints out numbers from 1 to 10

# Expected output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

number = list(range(1, 11))
print(*number, sep='\n')    #1         #my sol'n
                            #2
                            #3
                            #4
                            #5
                            #6
                            #7
                            #8
                            #9
                            #10

for i in range(1,11):
    print(i)    #1         #answer key
                #2
                #3
                #4
                #5
                #6
                #7
                #8
                #9
                #10