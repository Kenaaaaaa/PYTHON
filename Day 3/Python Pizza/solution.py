print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 350
elif size == "M":
    bill += 500
elif size == "L":
    bill += 700
else:
    print("You have chosen an invalid size.")

    # todo: work out how much to add to their bill based on their pepperoni choice.
    if pepperoni == "Y":
        if size == "S":
            bill += 5
        else:
            if size=="M":
                bill += 10
            else:
                bill+=15



    # todo: work out their final amount based on whether if they want extra cheese.
    if extra_cheese == "Y":
        bill += 7

    print(f"Your final bill is: ${bill}.")



