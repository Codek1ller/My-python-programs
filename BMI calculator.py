height = input("Enter you're height in meters here:")
weight = input("Enter you're weight in kg here:")

BMI = (float(weight) / float(height) ** 2)
BMI_int = int(BMI)

print("Your BMI is ", round(BMI, 2))
if BMI < 18.5:
    print("You're under weight.")
if 18.5 < BMI < 25:
    print("You're normal weight")
elif BMI > 25:
    print("You're overweight.")
if BMI > 30:
    print("You're obese.")
