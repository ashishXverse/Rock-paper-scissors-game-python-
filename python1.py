import random
item_list=["Rock","Paper", "Scissors"]

user_choice= input('Enter your choice = ')
comp_choice= random.choice(item_list)

print(f"user_choice= {user_choice}, Computer choice={comp_choice}")
if user_choice== comp_choice:
    print("both chose same= Match tie")

elif user_choice == "Rock":
    if comp_choice== "Paper":
        print('Paper cover Rocks= Computer  win')
    else:
       print("Rock smashes scissors= You win")

elif user_choice== "Paper":
    if comp_choice== "Scisoors":
        print("Scissors cuts paper = Computer  win")
    else:
        print("Paper covers rock = You  win")

elif user_choice== "Scissors":
    if comp_choice== "Paper":
        print("Scissors cut paper = You win")
    else:
        print("Rock smashes Scissors = Compuer wins")

        

