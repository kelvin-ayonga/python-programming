# Control flow and logical operators

if/else statements
Examples
``` python
x = 13
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than 10")

```

## Comparison operators
- `>` greater than
- `<` less than
- `>=` greater than or equal to 
- `<=` less than or equal to
- `==` equal to equality check  NB not the difference with assigning `=`
- `!=` not equal to

## Modulo operator

10 % 5 == 0 it gives the remainder

## nested if/else

``` python

x = 1
if(x > 10):
    print("x is greater than 10")
    if y < 10:
        print("y is less than 10")
    else:
        print("y is greater than 10")
else:
    print("x is less than 10")
```

## elif
``` python

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("Your ticket is $7")
    else:
        print("Your ticket is $12")
else:
    print("Sorry you have to grow taller before you can ride.")
    
```

# Logical operators
 - and
 - or
 - not

 ``` python
 print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    if age >= 45 and age <= 55:   # shorter format 45 >= age >= 55
        bill = 0
        print("Everything is free, you will be Okay")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

 ```


