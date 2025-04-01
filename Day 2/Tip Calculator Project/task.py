print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill ?"))
percentage_tip=float(input("How much tip would you like to give ? 10, 12, or 15?"))
tip=(total_bill*percentage_tip)/100
nr_people=float(input("How many people to split the bill"))
sum=(total_bill+tip)/nr_people
print(f"Each person should pay {round(sum,2)}")


