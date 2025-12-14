# The following code demonstrates the use of the print function in Python.
# The print() function outputs text or other data to the console.
# Text to be printed must be enclosed in quotation marks (" " for strings).
# For example, print("Hello, World!") will display Hello, World! on the screen.
# Quotation marks tell Python that the enclosed value is a string literal.
# You can use single (' ') or double (" ") quotation marks for strings.
print("1 Hello, World!") 
#\n is next line, dont leave space before \n-> causes space in necxt line
print("2 Hello, World!\nHello, World!")
#String concatination
print("3 " + "Hello, " + "World!")
#input function allows user to input data
#this would take the input and return it to the program
#this can be used with concatination as well

input("Ask what needs to be inputted: ")
#Example of input function with print and concatination
print("Hello " + input("Enter your name: ") + "!")

#You can also store the input in a variable for later use
name = input("Enter your name: ")   
print("Hello " + name + "!")
#finding string length
name_length = len(name)
#in python, the variable declaration is dynamic -> auto detects the datatypes
print(name_length)
print(len(name))
#if printing with concatinated string, we need to maintain the data types
#len() function returns the length of the string -> int
#str() function converts the integer to a string
#print() can only concatinate same data types
print("Length of your name is: " + str(len(name)))






