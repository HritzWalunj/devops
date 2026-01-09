""" Read from a File """

file = open("demo.txt","r")
data = file.read()
print(data)
file.close()