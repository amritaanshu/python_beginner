# -*- coding: utf-8 -*-
"""python_beginner.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yg5sNe3Ua9dcxZxd9ZX-Vaj77H3vJbPg
"""

age = input("what is your age? ")
print("your age is " + age )

dogs = ["Roger", 1, "Syd", True]

dogs[2] = "Beau"
dogs.extend(["Judah", 5])
dogs.remove("Judah")
print(dogs)

items = ["Roger", 1, "Syd", True, "Quincy", 7]

items.insert(2, "Test")
print(items)

items = ["Roger", "bob", "Beau", "Quincy"]

print(sorted(items, key=str.lower))
print(items)

#Tuples
names = ("Roger", "Syd")

names[-1]
names.index("Roger")

len(names)

print("Roger" in names)
print(sorted(names))
newTuple = names + ("tina", "Quincy")

#Dictionaries

dog = {"name": "Roger", "age": 8, "color": "green"}

dog["name"] = "Syd"
dog["favorite food"] = "Meat"
del dog['color']
print(dog)
print(dog.get("color", "brown"))
print(dog.pop("name"))