""" There are three numeric types in python :
    1) int
    2) float
    3) complex """

x=10
y=10.6
z=1j

print(type(x))
print(type(y))
print(type(z))

""" Output:
<class 'int'>
<class 'float'>
<class 'complex'> """

""" Random number : "random" module in python is used to generate random numbers """

import random
print(random.randrange(1,100))