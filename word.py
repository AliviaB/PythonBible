word ="supercalifragalistic"
print(word[:7:])

name="alivia banerjee"
print(name[-3])# reverse index prints j from end

#print(name[name.index("B"):name.index("j")])# error.. case need to be matched

def myfunc(n):  return lambda a : a * n
mydoubler = myfunc(3)
print(mydoubler(5))
