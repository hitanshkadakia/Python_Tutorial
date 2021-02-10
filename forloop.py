#For loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String

for x in "happy_coding01":
  print(x)

#break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range() function

for x in range(6):
  print(x)

#start parameter

for x in range(2, 6):
  print(x)

#Increment the sequence

for x in range(2, 30, 3):
  print(x)

#Nested loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)