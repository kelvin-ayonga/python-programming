len("12345")

#type Error, Checking & Conversion
print(type("Hello")) # <class 'str'>
print(type(1234)) # <class 'int'>
print(type(34.98)) # <class 'float'>
print(type(True)) # <class 'bool'>

# Type conversion
print(int("123") + int(345))

# int()
# float()
# str()

print("Number of letters in your name: " + str(len(input("Enter your name"))))