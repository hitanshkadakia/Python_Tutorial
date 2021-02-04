#If statement

a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#One line if statement:

if a > b: print("a is greater than b")

#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#pass statement
#if statements cannot be empty
#but if you for some reason have an if statement with no content
#put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass