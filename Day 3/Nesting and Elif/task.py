print("Welcome to the rollercoaster ")

number =int(input("Give me your hight in cm \n"))
bill=0
if number > 120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age \n"))
    if age > 18  :
        bill=12
        print("You have to pay $12 \n")
    else :
        if  18 > age >= 12 :
            bill=7
            print("You have to pay $7 \n")
        else:
            bill=5
            print("You have to pay $5 \n")
    photo=input("Do you want a photo in your bill?")
    if photo=="yes":
        bill+=3
    print(f"Your bill is {bill} ")
else:
    print("You have to grow taller to ride a rollercoaster")