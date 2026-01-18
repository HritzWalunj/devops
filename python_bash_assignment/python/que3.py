"""Write a program to create a text file and write some content to it.

Using file functions like write and open.
"""

#open file in read write mode
file = open("demo.txt", "r+")

#write into file
file.write("Hey...\n")
file.write("How are you?")

#close file
file.close()
