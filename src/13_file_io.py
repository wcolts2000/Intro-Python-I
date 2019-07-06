import os
"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
dirname = os.path.dirname(os.path.abspath(__file__))
fileToOpen = 'foo.txt'
fileNameToOpenWithPath = os.path.join(dirname, fileToOpen)


# using only open, you need to append the close() if you want it to immediately close upon completion, else, memleak!!!
fileRead = open(fileNameToOpenWithPath, 'r')
print(fileRead.read())
fileRead.close()

# using with will automatically close after the printout is complete
with open(fileNameToOpenWithPath, 'r') as fileRead:
    print(fileRead.read())


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newDirname = os.path.dirname(os.path.abspath(__file__))
newFileToOpen = 'bar.txt'
newFileNameToOpenWithPath = os.path.join(newDirname, newFileToOpen)
with open(newFileNameToOpenWithPath, 'w+') as f:
    string1 = "some stuff here \n"
    string2 = "some more stuff here \n"
    string3 = "yet again, some more stuff here"
    f.write(string1)
    f.write(string2)
    f.write(string3)

f = open('bar.txt', 'r')
print(f.read())
f.close()

filenameBar = 'bar.txt'
filenameBarWithPath = os.path.join(dirname, filenameBar)
with open(filenameBarWithPath, 'w+') as f:
    for i in range(1, 4):  # lines 1-3
        f.write("This is line %d\n" % (i))
with open(filenameBarWithPath, 'a+') as f:
    for i in range(4, 7):  # lines 4-6
        f.write("This is line %d (appended)\n" % (i))
with open(filenameBarWithPath, 'r') as f:
    print(f.read())

# print(f.closed)
