print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    bill = 0
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill  = 12
        print("Adult ticket is $12")

    with_photo = input("Do you want a photo included? Y or N \n")

    if with_photo == "y":
        bill += 3

    print(f"Please pay ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
