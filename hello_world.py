message = """hello john "ohh fine!!" """
hello = "hello world !"
print(message)
# Hello You
# ask user Questions

name = input("what is your name? : ")
age = input("What is your age? : ")
city = input("Where do you stay?: ")
love = input(" What do you love to do ?: ")



# create out put and print
#print(name + " is "+ age +" years old, "+"stays at "+city+" and loves to"+love)
answer = "My name is {} and I am {} years old, I stay at {} and Love to {}"
output = answer.format(name, age, city, love)
print(output)
a = "Part"

b = 1
c = "{1} {0}".format(a, b)
print(c)
# word[start:end:step]
