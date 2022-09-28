dict= {"name":"Kelly","age":25,"salary":8000,"city":"New york"}

#key to remove keys = ["name", "salary"]
#Expected output:{'city': 'New york', 'age': 25}
key=["name","salary"]
for item in key:
     dict.pop(item)


print(dict)
