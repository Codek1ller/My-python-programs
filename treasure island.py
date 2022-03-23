print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("This is a treasure game.")
b = input('Your at a cross road where do you want to go? type "left" to go left or "right" to go right.')

if b == "right":
    print("You died, Game over.")

elif b == "left":
    lake = input('You come to a lake. there is an island in the middle of the lake. type'
                ' "wait" to wait for a b''oat or type "swim" to swim to the island ')

    if lake == "swim":
        print("Game over you died from drowning.") or print("Game over.You were eaten alive by piranhas. ")
    if lake == "wait":
        doors = input('You arrive at the island unharmed theres a house\n'
                      ' with 3 doors one red one yellow and one blue door.\n type "red" to go'
                      ' into the red one type "yellow" to go into the yellow one and type "blue"'
                      ' to go into the blue door. ')

        if doors == "red" or "Red":
            print("game over you were Burned bu fire")
        elif doors == "Blue" or "blue":
            print("you walk into a room full of beasts.Game over")
        if doors == "yellow":
            print("Congrats you won !")
