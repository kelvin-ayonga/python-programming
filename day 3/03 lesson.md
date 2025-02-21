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


