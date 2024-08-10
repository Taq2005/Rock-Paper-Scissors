import random
user_score=0
computer_score=0
options=["rock", "paper", "scissors"]
x=input("Do you want to play Rock Paper Scissors!!")
print("The game will automatically end when your score reaches 3")

if(x.lower()=="yes"):
    print("Let's start the game")
    while True:
        if(user_score==3):
            break
        user_choice=input("Choose between rock/paper/scissors:\n")
        

        if user_choice.lower() not in options:
                print("Invalid option")
                continue
        computer_choice=options[random.randint(0,2)]
        print("The computer chose", computer_choice)
        if(user_choice.lower()=="rock" and computer_choice=="scissors"):
            print("You won")
            user_score=user_score+1
        elif(user_choice.lower()=="paper" and computer_choice=="rock"):
            print("You won")
            user_score=user_score+1
        elif (user_choice.lower()=="scissors" and computer_choice=="paper"):
            print("You won")
            user_score=user_score+1
        elif(user_choice.lower()==computer_choice):
            print("Try again")
        
        
        
        else:
            print("You lost!")
            computer_score=computer_score+1
        

else:
        
    print("Sad to see you go")
    
       
print("You have won", user_score,"times")
print("The computer has won", computer_score,"times")  
