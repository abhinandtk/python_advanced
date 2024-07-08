mydict={"name":"Max","age":28,"city":"New York"}
print(mydict)
mydict2=dict(name="Mary",age=28,city="Boston")
value=mydict["name"]
print(value)
mydict["email"]="max@xyz.com"
print(mydict)
del mydict["name"]
print(mydict)
mydict.pop("age")
print(mydict)
mydict.popitem()
print(mydict)
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("error")

for value in mydict.values():
    print(value)

for key in mydict.keys():
    print(key)
for key,value in mydict.items():
    print(key,value)

mydict.update(mydict2)
print(mydict)

mydict3={3:2,4:5,6:7}
print(mydict3[3])
