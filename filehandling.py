# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

#Syntax
#To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")

#The code above is the same as:

f = open("demofile.txt", "rt")
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.

#Open a File on the Server

f = open("demofile.txt", "r")
print(f.read())

#Python File Write

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#Python Delete File

import os
os.remove("demofile.txt")

#Check if File exist:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")