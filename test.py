def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(**{'x': 2, 'y':5}) #1 2
                            #3 4