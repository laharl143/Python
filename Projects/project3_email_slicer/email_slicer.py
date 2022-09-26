#get user email address
email = input("What is your email address?: ").strip()
#slice out username
username = email[:email.index("@")]
#slice domain name
domain_name = email[email.index("@") + 1 :]  # +1 is used to not include the @
#format message
string = "Your username is {} and your domain name is {}"
output = string.format(username,domain_name)
#display output message
print(output)

