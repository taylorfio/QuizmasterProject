f = open("demofile.txt", "r")
# r (Read), w (Write), a (Append), r+ (Read/Write)
print(f.read())  # -reads the whole file
print(f.read(5))  # -reads the first 5 characters
print(f.readline())  # -reads a whole line
print(f.readlines())  # -reads every line


f = open("demofile.txt", "a") #append to the end
f.write("\nNow the file has one more line!")

f = open("demofile.txt", "w") #write to the file
f.write("Woops! I have deleted the content!")

f = open("myfile.txt", "x") #creates the file


file = open("demofile.txt", "r")#read
file = open("demofile.txt", "w")#write
file = open("demofile.txt", "r+")#read/write
file = open("demofile.txt", "a")#append
file = open("demofile.txt", "x")#create
file.close()


try:
   f = open("samplefile.txt", "a")
   print(f.read())
except:
   print("What happened")

try:
   f = open("samplefile.txt", "a")
   print(f.read())
except IOError:
   print("What happened")

try:
   f = open("samplefile.txt", "a")
   print(f.read())
except IOError:
   print("What happened to my file")
except ArithmeticError:
   print("Don’t even try to divide by zero")

try:
   f = open("samplefile.txt", "a")
   print(f.read())
except IOError:
   print("What happened to my file")
except ArithmeticError:
   print("Don’t even try to divide by zero")
else:
   print("Success!")



import os

os.remove("demofile.txt")
os.rename("samplefile.txt", "demofile.txt")

# We can use .mkdir() to make a new directory
os.mkdir("FileIOFolder")
# We can use .rmdir() to remove an EMPTY folder
os.rmdir("FileIOFolder")
# We can use .chdir() to change the folder
os.chdir("FileIOFolder")
# We can use .getcwd() to get the current working directory
os.getcwd()

try:
   f = open("samplefile.csv", "r")
   print(f.read())
except:
   print("ERROR")


1976, Chevrolet, Impala
2002, Mini, Cooper
1981, Ford, Bronco




