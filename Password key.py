
print("This is a password guessing Game !!!")
password1 = ("password")
password_question = input("You are given these letters sspaowrd "
                          "and you have to put them in the right order and find the password !: ")
bank = 0

if password_question == password1:
    print(" ")
    bank += 100
    print(f"You now have £{bank} from working as a hacker")
else:
    print("Wrong password !")

q2_extra = input('would you like to carry on to question 2 ? "Y" or "N" : ')
print(" ")
if q2_extra == "Y":
    password2 = 'number'
    q2 = input('the passwords muddled up un muddle it and write it down: "mubren" : ')
    if q2 == password2:
        bank += 1000
        print(" ")
        print(f'Well done you now got £{bank} working as a hacker')
    else:
        print("Wrong password!")
print(" ")
q3_extra = input('would you like to carry on to question 3 ? "Y" or "N" : ')
print(" ")
if q3_extra == "Y":
    password3 = 'apple'
    q3 = input('the passwords muddled up un muddle it and write it down: "ppale" : ')
    if q3 == password3:
        bank += 1500
        print(" ")
        print(f'Well done you now got £{bank} working as a hacker')
    else:
        print("wrong answer !")

