print("Welcome to the tip calculator")

bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give?  10, 12, or 15?\n"))
numOfPeople = int(input("How many people to split the bill?\n"))


billAfterTip = (bill * tip) / 100

amoutPerPerson = round((bill + billAfterTip) / numOfPeople, 2)
print(f"Each person should pay: ${amoutPerPerson}")
