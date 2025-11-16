#subscripting in Python


"""
Demonstrates string subscripting and slicing operations in Python.

This module shows how to:
- Access individual characters by index (positive and negative indexing)
- Extract substrings using slice notation [start:end]
- Use step values in slices to skip characters

Examples:
    Positive indexing accesses characters from the start (0-based).
    Negative indexing accesses characters from the end (-1 is last character).
    Slicing with [start:end] extracts characters from start up to (but not including) end.
    Slicing with [start:end:step] extracts every nth character.
"""
print("Hello World"[0])  # Output: H
print("Hello World"[4])  # Output: o            
print("Hello World"[-1]) # Output: d
print("Hello World"[-3]) # Output: r    
print("Hello World"[0:5]) # Output: Hello
print("Hello World"[6:11]) # Output: World                  
print("Hello World"[::2]) # Output: HloWrd
print("Hello World"[1:9:3]) # Output: el ol
print("Hello World"[::-1]) # Output: dlroW olleH    

#large number representation
# underscores can be used to make large numbers more readable
print(123_456_789) # Output: 123456789
print(1_000_000_000) # Output: 1000000000

#Datatypes in Python
""" 
This section demonstrates the basic data types in Python.   

Data Types Covered:
- Integer (int): Whole numbers, positive or negative, without decimals.
- Float (float): Numbers with decimal points or in exponential form.        
- String (str): Sequence of characters enclosed in single or double quotes.
- Boolean (bool): Represents one of two values: True or False.
"""
#integer
a = 123           # Integer
print(a)        # Output: 123
print(type(a))     # Output: <class 'int'>
#float
b = 123.456       # Float
print(b)    # Output: 123.456
print(type(b))     # Output: <class 'float'>
#string
c = "Hello, Python!"  # String
print(c)  # Output: Hello, Python!
print(type(c))     # Output: <class 'str'>
#boolean
d = True          # Boolean
print(d)       # Output: True
print(type(d))     # Output: <class 'bool'>

#Type Conversion in Python
"""         

This section demonstrates type conversion in Python, showing how to convert between different data types.   
Type Conversions Covered:
- int(): Converts a value to an integer.
- float(): Converts a value to a float.
- str(): Converts a value to a string.
- bool(): Converts a value to a boolean.
"""
#int conversion
x = "100"
y = int(x)  # Convert string to integer
print(y)        # Output: 100
print(type(y))     # Output: <class 'int'>

#float conversion
z = "123.45"
w = float(z)  # Convert string to float
print(w)      # Output: 123.45

print(type(w))     # Output: <class 'float'>
#string conversion
m = 456
n = str(m)  # Convert integer to string
print(n)      # Output: '456'
print(type(n))     # Output: <class 'str'>  

#boolean conversion
p = 0
q = bool(p)  # Convert integer to boolean
print(q)      # Output: False
print(type(q))     # Output: <class 'bool'>

#math operations in Python
""" 
This section demonstrates basic mathematical operations in Python, including addition, subtraction, multiplication, division, exponentiation, and modulus.  
Mathematical Operations Covered:
- Addition (+): Adds two numbers.
- Subtraction (-): Subtracts the second number from the first.
- Multiplication (*): Multiplies two numbers.
- Division (/): Divides the first number by the second, resulting in a float.
- Floor Division (//): Divides the first number by the second, resulting in an integer by discarding the decimal part.   
- Exponentiation (**): Raises the first number to the power of the second.  
- Modulus (%): Returns the remainder of the division of the first number by the second.

PEMDAS/BODMAS rules apply for operator precedence.  
Examples:
    5 + 3 = 8
    10 - 4 = 6
    6 * 7 = 42
    20 / 4 = 5.0
    20 // 3 = 6
    2 ** 3 = 8
    10 % 3 = 1
"""
#Addition
add = 5 + 3
print(add)  # Output: 8     
#Subtraction
sub = 10 - 4
print(sub)  # Output: 6
#Multiplication
mul = 6 * 7
print(mul)  # Output: 42
#Division
div = 20 / 4
print(div)  # Output: 5.0
#Floor Division
floor_div = 20 // 3
print(floor_div)  # Output: 6
#Exponentiation
exp = 2 ** 3
print(exp)  # Output: 8
#Modulus
mod = 10 % 3
print(mod)  # Output: 1
#Operator Precedence
result = 5 + 3 * 2  # Multiplication first, then addition
print(result)  # Output: 11
result2 = (5 + 3) * 2  # Parentheses first
print(result2)  # Output: 16
print(3*3+3/3-3)  # Output: 7.0


#___________________________________________________________

#f-strings in Python
"""     
This section demonstrates the use of f-strings (formatted string literals) in Python for embedding expressions inside string literals.
F-strings allow for easy and readable string formatting by prefixing the string with 'f' or 'F' and using curly braces {} to include variables or expressions directly within the string.

Examples:
    name = "Alice"
    age = 30
    print(f"Hello, my name is {name} and I am {age} years old.")
    Output: Hello, my name is Alice and I am 30 years old.
"""
name = "Alice"
age = 30            
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.
#Using expressions inside f-strings
calculation = f"In five years, I will be {age + 5} years old."
print(calculation)  # Output: In five years, I will be 35 years old.
#Formatting numbers in f-strings    
pi = 3.14159265
formatted_pi = f"The value of pi is approximately {pi:.2f}."
print(formatted_pi)  # Output: The value of pi is approximately 3.14.
print(f"Hello, my name is {name} and I am {age} years old.")
    



