age = input("What is your current age: ")
age_as_int = int(age)
years = 90

years_remaining = years - age_as_int
days_remaining = round(years_remaining) * 364
weeks_remaining = round(years_remaining) * 52
months_remaining = round(years_remaining) * 12
b = f"You have {days_remaining}days, {weeks_remaining}weeks, and {months_remaining}months left to live"
print(b)
