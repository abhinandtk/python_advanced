myTuple=("Max",28,"Boston") #parenthesis are optional
print(type(myTuple))
myTuple2="Max",28,"Boston" #This is also a tuple
print(myTuple2)
myTuple3=tuple(["Abhi",22,"kerala"]) #Create tuple from a list
print(myTuple3)
item=myTuple[0]
print(item)

tuple1=["a","b","c","a","c"]
print(tuple1.count("a"))
mylist=list(tuple1)
print(tuple1)
print(tuple1[2:4])
tuple2=[1,2,3,4,5,6,7,8,9,0]
print(tuple2[::1])
print(tuple2[::2])
print(tuple2[::-1])