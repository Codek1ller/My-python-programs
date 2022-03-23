print("Welcome to the tip calculator. ")
bill_total = input("What is the total bill: ")
percentage = input("What percentage of the tip would you like to pay 10, 12 or 15 ? ")
people = input("How many people would you like to split the bill with ? ")
if percentage == "10":
    percentage9 = (int(bill_total)-int(bill_total)/100*int(percentage))/int(people)
    print(round(int(percentage9), 2))
if percentage == "12":
    percentage9 = (int(bill_total)-int(bill_total)/100*int(percentage))/int(people)
    print(round(int(percentage9), 2))

if percentage == "15":
    percentage9 = (int(bill_total)-int(bill_total)/100*int(percentage))/int(people)
    print("everyone should pay: ", round(int(percentage9), 2))