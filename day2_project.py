# tip calculator project

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $\n"))
tip = float(input("how much tip would you like to give?\n"))
persons =  int(input("how many people to split the bill?\n"))
tip_as_percent = tip/100
total_tip = bill*tip_as_percent
toal_bill = bill+total_tip
bill_per_person = toal_bill/persons
print(f"Each person sould pay ${bill_per_person:.2f}")