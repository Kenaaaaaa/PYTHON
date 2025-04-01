print("Python Pizza")

# Prices for different sizes
small_price1 = 15
medium_price1 = 20
large_price1 = 25

# User input for size
size = input("What size of pizza do you want? S, M, or L? \n")

# Small size
if size == "S":
    pepperoni = input("Do you want pepperoni on top of the pizza? Y or N \n")
    if pepperoni == "Y":
        small_price1 += 2  # Add pepperoni price for small size

    extra_cheese = input("Do you want extra cheese? Y or N \n")
    if extra_cheese == "Y":
        small_price1 += 1  # Add cheese price

    print(f"Your bill is {small_price1} ")

# Medium size
elif size == "M":
    pepperoni = input("Do you want pepperoni on top of the pizza? Y or N \n")
    if pepperoni == "Y":
        medium_price1 += 3  # Add pepperoni price for medium size

    extra_cheese = input("Do you want extra cheese? Y or N \n")
    if extra_cheese == "Y":
        medium_price1 += 1  # Add cheese price

    print(f"Your bill is {medium_price1} ")

# Large size
elif size == "L":
    pepperoni = input("Do you want pepperoni on top of the pizza? Y or N \n")
    if pepperoni == "Y":
        large_price1 += 3  # Add pepperoni price for large size

    extra_cheese = input("Do you want extra cheese? Y or N \n")
    if extra_cheese == "Y":
        large_price1 += 1  # Add cheese price

    print(f"Your bill is {large_price1} ")

# Invalid input case
else:
    print("Invalid size selection. Please choose S, M, or L.")








