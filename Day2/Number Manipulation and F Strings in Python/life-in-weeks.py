age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remianing = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remianing} months left")