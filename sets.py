myset={1,2,3}
print(myset)
myset2=set("Hello")
print(myset2)
myset.add(4)
myset.add(5)
myset.add(6)
myset.remove(6) #error occures when no element
myset.discard(6) #no error occures when no element
print(myset)
print(myset.pop())
print(myset.clear())