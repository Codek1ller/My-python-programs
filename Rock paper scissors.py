import random
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = input("Type 0 for rock type 1 for paper and type 2 for scissors: ")

if option == "0":
    print(rock)
    list_1 = [rock, paper, scissors]
    computer_choice = ("The computer Chose:")
    print(computer_choice)
    v = (random.choice(list_1))
    print(v)
    if v == list_1[1]:
        print('you lost paper covers rock.')
    if v == list_1[2]:
        print("you win rock smashes scissors !")
    if v == list_1[0]:
        print("Its a draw !")
if option == "1":
    print('You chose Paper: ')
    print(paper)
    list_2 = [paper, rock, scissors]
    computer_choice2 = ("The computer Chose:")
    rando = random.choice(list_2)
    print(computer_choice2)
    print(rando)
    if rando == list_2[1]:
        print("you win paper covers rock")
    if rando == list_2[2]:
        print("You lost scissors cuts paper")
    if rando == list_2[0]:
        print("Its a draw !")

if option == "2":
    print("You chose: ")
    print(scissors)
    list_3 = [rock, paper]
    computer_choice3 = ("The computer chose: ")
    rand = random.choice(list_3)
    print(computer_choice3)
    print(rand)
    if rand == list_3[1]:
        print("rock breaks scissors you lost")
    if rand == list_3[2]:
        print("You win scissors cuts rock")
    if rand == list_3[0]:
        print("Its a draw !")
