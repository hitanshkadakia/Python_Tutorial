# Create a Set
Set={"python","java","C++"}
print(Set)

# access the Sets items
Set={"python","java","C++"}
for x in Set:
    print(x)

# Add Items
Set={"python","java","C++"}
Set.add("kotlin")
print(Set)

# Remove items
Set={"python","java","C++","kotlin"}
Set.remove("java")
print(Set)

# empty the set
Set={"python","java","C++"}
Set.clear()
print(Set)

# delete the set
Set={"python","java","C++"}
del Set

# join two Sets
Set1={"python","java","C++"}
Set2={"kotlin","dart","javascript"}
Set3=Set1.union(Set2)
print(Set3)

# Constructor
a=set(("python","java","C++"))
print(a)
