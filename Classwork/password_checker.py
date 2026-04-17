"""
take input 
check the length of user password
if the length of user password is less than 8 
print very weak
if the length of user password is equal to 8 
print weak
if the length of user password is between 8 and 16 
print strong
if the length of user password is greater than 16
print very strong
"""

user_password = input("Enter your password")
lengthofpass = len(user_password)
print(lengthofpass)
if lengthofpass < 8:
    print ("very weak")
elif lengthofpass ==8:
    print("weak")
elif user_password >8 and user_password <16:
    print("Strong")
elif lengthofpass >=16:
    print("Strong")
