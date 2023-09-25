import random #importing needed variables
import time
p1score=0 #sets game score to 0 for both players
p2score=0
tiebreaker_p1=0
tiebreaker_p2=0
Winnerscore=0
p1_login=False #sets login to false as the 2 players are not yet logged in
p2_login=False

while p1_login==False:
    username=input(" What is your username player1?")
    password=input("What is your password player1?")
    if username == "player1": #username for player1 is player1
        if password == "password": #password for player1 is password
            print("Access Granted, Welcome Player1.")
            p1_login=True #this breaks the while loop as the user has been authenticated
            username1=(username) #makes it easier to mention the user later
        else:
            print("Incorrect Username or Password.")

while p2_login==False:
    username=input(" What is your username player2?")
    password=input("What is your password player2?")
    if username == "player2": #username for player2 is player2
        if password == "password": #password for player2 is password
            print("Access Granted, Welcome Player2.")
            p2_login=True #this breaks the while loop as the user has been authenticated
            username2=(username) #makes it easier to mention the user later
        else:
            print("Incorrect Username or Password.")


def roll(): #this subroutine rolls the dice for the player and calculates a score
    score=0
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dicetotal=(dice1+dice2) #adds the score from both dices and puts it into 1 variable
    score=(score+dicetotal)

    if dicetotal == 2 or 4 or 6 or 8 or 10 or 12: #this adds 10 to the score if its an even number 
        score=(score+10)

    if dicetotal == 1 or 3 or 5 or 7 or 9 or 11: #takes away 5 if its an odd number
        score=(score-5)

    return(score)

for i in range(1,5): #rolls dice 5times
    p1score=roll()
    print("After the current round",username1,"'s score is now",p1score) #displays score
    time.sleep(2) #adds break between each roll
    p2score=roll()
    print("After the current round",username2,"'s score is now",p2score) #displays score
    time.sleep(2)


if p1score == p2score:
    while tiebreaker_p1==tiebreaker_p2:
        tiebreaker_p1=random.randint(1,6)
        tiebreaker_p2=random.randint(1,6)

    if tiebreaker_p1 > tiebreaker_p2:    #this rolls a 3rd dice to determine a winner between the 2 players
        p2score=0
    elif tiebreaker_p2 > tiebreaker_p1:
        p1score=0

#calculates the winner and saves it into a variable 

if p1score>p2score:
    winnerscore=(p1score)
    winner_player=(username1)
    winner=(winnerscore, username1)
elif p2score>p1score:
    winnerscore=(p2score)
    winner_player=(username2)
    winner=(winnerscore, username2)
#####################

print("The final winner is", winner_player," with a total score of",winnerscore) #displays winner

winner=(winnerscore,",",winner_player)


#I forgot how to do file read/write etc
    


    
    


            

            
        
