#Ask user for name
name = input("What is your name?: ")

#Ask user for their age
age = input("What is your age?: ")

#Ask user for city
city = input("What city do you live in?: ")

#Ask user what they enjoy
hobby = input("What do you enjoy the most?: ")


#Create output text

string = "Hi {}! So, you are {} years old? Great job levelling up! So, you live in {}? That's a great place to live! Oh you love {} too? Me too!".format(name,age,city,hobby) 

print(string)

#Print output to screen



