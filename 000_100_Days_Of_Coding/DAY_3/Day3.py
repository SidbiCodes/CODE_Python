#control flow with if-else statements in python
""" 
If-else statements allow you to execute different blocks of code based on certain conditions.
The syntax for if-else statements in Python is as follows:

Indentation is crucial in Python as it defines the scope of code blocks.

 if condition:
      code to execute if condition is true        
 else:
      code to execute if condition is false
"""
# Example of if-else statement

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))
if height >= 120:
    print("You are eligible to ride the rollercoaster!")
else:
    print("Sorry, you need to be at least 120 cm tall to ride the rollercoaster.")

#Comparison operators in python
# ==  : equal to
# !=  : not equal to
# >   : greater than    
# <   : less than
# >=  : greater than or equal to
# <=  : less than or equal to

#Nested if-else statements
if height >= 120:
    print("You are eligible to ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your ticket price is $5.")
    #elif is used to check multiple conditions -> else if
    elif age <= 18:
        print("Your ticket price is $7.")
    else:
        print("Your ticket price is $12.")
else:
    print("Sorry, you need to be at least 120 cm tall to ride the rollercoaster.")  


#Python pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")    
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : S")
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2   
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3   
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3   
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}")


