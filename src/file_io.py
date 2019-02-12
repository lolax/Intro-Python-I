"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open("foo.txt") as f:
    read = f.read()
    print(read)
f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

with open("bar.txt","w+") as f:
    f.write("'The day after the wedding, a Monday, was rainy. \n The rain began to fall just after midnight and continued without a stop till dawn. \n A soft, gentle rain that darkly dampened the spring earth and quietly stirred up the nameless creatures living in it.' Murakami (Sputnik Sweetheart)")
f.closed