import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#print(rock)
continue_game=1
while continue_game==1:
    user_choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    user_choice_int= int(user_choice)
    #print(f"User choice {user_choice_int}")
    if user_choice_int==0:
      print(rock)
    elif user_choice_int==1:
      print(paper)
    elif user_choice_int==2:
      print(scissors)
  
    computer_choose=random.randint(0,2)
    print(f"Computer chose {computer_choose}")
    if user_choice_int==0:
      if computer_choose==0:
        print(rock)
        print("Draw")
      elif computer_choose==1:
        print(paper)
        print("You lose")
      elif computer_choose==2:
        print(scissors)
        print("You win!")
      else:
        print("Wrong input, you lose")
    elif user_choice_int==1:
      if computer_choose==1:
        print(paper)
        print("Draw")
      elif computer_choose==0:
        print(rock)
        print("You win")
      elif computer_choose==2:
        print(scissors)
        print("You lose")
      else:
        print("Wrong input, You lose")
    elif user_choice_int==2:
      if computer_choose==2:
        print(scissors)
        print("Draw")
      elif computer_choose==0:
        print(rock)
        print("You lose")
      elif computer_choose==1:
        print(paper)
        print("You win!")
      else:
        print("Wrong input, you lose")
    else:
      print("Wrong choice, you lose")
    ask_continue=input("Do you want to continue the game?(Type 'y' to continue or 'n' to exit)")
    if ask_continue=="y" or ask_continue=="Y":
        continue_game=1
    else:
        continue_game=0
print("The game has ended. Hope you have enjoyed the game. Good Bye, Have a nice day!")