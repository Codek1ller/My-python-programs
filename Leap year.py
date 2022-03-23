year = input("which year do you want to check ? ")
year_int = int(year)
if (year_int % 4) == 0:
    step_2 = year_int % 100
    if step_2 == 0:
        step_3 = year_int % 400
        if step_3 == 0:
            print("Not a leap year")
if (year_int % 4) == 0:
    step_2 = year_int % 100
    if step_2 != 0:
        print("this is a leap year")

if (year_int % 4) != 0:
    print("Not a leap year")
