#get user email

email =input("Whats is your Email:").strip()

#slice out user name
username = email[:email.index("@")]

#slice out domain name
domain = email[email.index("@")+1:]
#format message
out = "your user name is {} and your domain name is {}".format(username,domain)
#display message
print(out)