import random
NoOfGames = 1;
YourWins = 0;
def Game(YourWins,NoOfGames):
    ComputerChoice = random.choice(["Rock","Paper","Scissors"]);
    print("#### Rock Paper Scissors Game ####");
    print("1. Rock");
    print("2. Paper");
    print("3. Scissors");
    MyChoice = input("Enter Your Choice : ");
    if(MyChoice=='1'):
        YourChoice = "Rock"
        if(ComputerChoice=="Rock"):
            print("Its a Draw")
        elif(ComputerChoice=="Paper"):
            print("You Loose");
        else:
            print("You win")
            YourWins = YourWins + 1;
    elif(MyChoice=='2'):
        YourChoice = "Paper"
        if(ComputerChoice=="Paper"):
            print("Its a Draw")
        elif(ComputerChoice=="Scissors"):
            print("You Loose");
        else:
            print("You win")
            YourWins = YourWins + 1;
    elif(MyChoice=='3'):
        YourChoice = "Scissors"
        if(ComputerChoice=="Scissors"):
            print("Its a Draw")
        elif(ComputerChoice=="Rock"):
            print("You Loose");
        else:
            print("You win")
            YourWins = YourWins + 1;
    else:
        print("Invalid Input")
    print(f"Your Choice : {YourChoice}")
    print(f"Computer Choice : {ComputerChoice}")
    print(f"You win {YourWins} Matches out of {NoOfGames}");
    again = input("Want to Play Again (y/n) : ")
    if(again=='y'):
        NoOfGames = NoOfGames + 1;
        Game(YourWins,NoOfGames);
    else:
        return 0;
Game(YourWins,NoOfGames);