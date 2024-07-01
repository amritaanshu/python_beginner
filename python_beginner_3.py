# -*- coding: utf-8 -*-
"""python_beginner_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pFM-z_DDbq26LEtY79z7H84Ee7diTAf5
"""

#map(), #filter(), #reduce()

numbers = [1, 2, 3]

def isEven(n):
  return n % 2 == 0

result = filter(isEven, numbers)

print(list(result))

#Recursion

def factorial(n):
  if n ==1: return 1
  return n * factorial(n-1)

  print(factorial(3))
  print(factorial(4))
  print(factorial(5))

#Decorators

def logtime(func):
  def wrapper():
    print("before")
    val = func()
    print("after")
    return val
  return wrapper
@logtime
def hello():
  print("hello")

hello()

from os import name
#Docstrings
"""Dog module

This module does ... bla bla bla and provides the following classes:

- Dog

...
"""

class Dog:
  """ A class representing a dog"""
  def __init__(self, nam, age):
    """initialize a new dog"""
    self.name = name
    self.age = age
    """Let the dog bark"""
    print('WOF!')

print(help(Dog))

#Annotations

def increment(n: int) -> int:
  return n + 1

count: int = 0

#Execption

try:
  result = 2 / 0
except ZeroDivisionError:
 print('Cannot divide by Zero!')
finally:
  result = 1

  print(result) #1

try:
  raise Exception('An error!')
except Exception as error:
  print(error)

class DogNotFoundException(Exception):
  pass

try:
  raise DogNotFoundException()
except DogNotFoundException:
  print('Dog not found!')

#List Compressions

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

numbers_power_2 = []
for n in numbers:
 numbers_power_2.append(n**2)

numbers_power_2 = list(map(lambda n : n**2, numbers))

#Polymorphis

class Dog:
  def eat(self):
    print('Eating dog food')

class Cat:
  def eat(self):
   print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

#Operator Overloding

class Dog:
  #the Dog class
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __gt__(self, other):
    return True if self.age > other.age else False

roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

print(roger > syd)