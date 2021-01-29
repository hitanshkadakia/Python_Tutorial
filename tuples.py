# Create a tuple
tup=("python","java","C++")
print(tup)

# access the tuples items
tup=("python","java","C++")
print(tup[1])

# Negative indexing
tup=("python","java","C++")
print(tup[-1])

# Range of indexes
tup=("python","java","C++","kotlin")
print(tup[1:3])

# Change Item Value
tup=("python","java","C++")
x=list(tup)
x[1]="Flutter"
tup=tuple(x)
print(tup)

# tuple Length
tup=("python","java","C++")
print(len(tup))

# Remove Tuple
tup=("python","java","C++")
del tup

# join two tuples
tup1=("python","java","C++")
tup2=("kotlin","dart","javascript")
tup3=tup1+tup2
print(tup3)